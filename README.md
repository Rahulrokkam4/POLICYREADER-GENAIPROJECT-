# POLICYREADER-GENAIPROJECT-
Policy Reader is an intelligent, interactive question-answering app built using LangChain, Groq’s LLaMA3-70B, and FAISS. It allows users to input a URL (e.g., a government policy or legal document), processes the content, and enables natural language querying over the document using advanced LLM reasoning.

#  Tech Stack
**LangChain** – for chaining retrieval + LLMs
**Groq Cloud API (LLaMA3 70B)** – lightning-fast inference with low latency
**HuggingFace Embeddings (BAAI/bge-base-en-v1.5)** – document embedding for semantic search
**FAISS** – vector store for fast document retrieval
**Streamlit** – interactive frontend for user input and output
**UnstructuredURLLoader** – to load data directly from URLs
**.env + Python-dotenv** – secure API key management

# Example Use Case
You paste a URL to a public policy document about privacy regulations. The app loads it, semantically indexes it, and you can ask:
"What does this policy say about third-party data sharing?"
It will return a concise, sourced answer.
