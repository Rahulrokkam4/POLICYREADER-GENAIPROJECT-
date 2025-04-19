import os
import streamlit as st
import pickle
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from groq import Groq
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
load_dotenv()
# api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    base_url="https://api.groq.com/openai/v1",
    # paste here "your actual key" in place os.getenv("OPENAI_API_KEY") or dotenv
    api_key=os.getenv("OPENAI_API_KEY"),
    model_name="llama3-70b-8192",
    temperature=0.6
)


st.title("Policy Reader 👨‍🏫")
st.sidebar.title("Policy URl or File")
urls = []
url = st.sidebar.text_input("Paste here")
urls.append(url)

process_click = st.sidebar.button("Submit")
file_path = "faiss_store.pkl"
main_ph = st.empty()


if process_click:
    loader = UnstructuredURLLoader(urls=urls)
    data = loader.load()
    main_ph.text("Data Loading....😊")
    # split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n','\n','.',','],
        chunk_size=1000,
        chunk_overlap=100
    )
    docs = text_splitter.split_documents(data)
    main_ph.text("Data was Splitting...😁")
    # embedding
    main_ph.text("Embedding started...😄")
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-base-en-v1.5")
    # FAISS vector database
    main_ph.text("Vector index Building started...😀")
    Vectorstore = FAISS.from_documents(docs, embedding=embeddings)
    # save the FAISS index to a pickle
    with open(file_path, "wb") as f:
        pickle.dump(Vectorstore, f)

query = main_ph.text_input("Question :")
if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
            result = chain({"question": query}, return_only_outputs=True)
            st.header("Answer :")
            st.write(result["answer"])

            sources = result.get("sources", "")
            if sources:
                st.header("Sources :")
                # sources_list = sources.split("/n")
                # for source in sources:
                st.write(sources)
#how many certificate we need for death claim? what are they?