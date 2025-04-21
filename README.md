# 🧠 POLICYREADER-GENAIPROJECT 📜  
**An LLM-powered interactive policy analyzer built with LangChain, LLaMA3-70B, and FAISS**

![LangChain](https://img.shields.io/badge/LangChain-%23FFDB58.svg?style=flat&logo=LangChain&logoColor=black)
![Groq LLaMA3](https://img.shields.io/badge/LLaMA3--70B-Groq-blueviolet)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)
![License](https://img.shields.io/github/license/yourusername/PolicyReader-GenAIProject)

---

## 🌟 Overview

**Policy Reader** is an intelligent, interactive **question-answering app** built using cutting-edge LLMs. Just paste a URL to a public policy, law, or document, and ask questions about it in plain English.

> ⚡️ Powered by Groq’s ultra-fast LLaMA3-70B and LangChain’s powerful chaining capabilities, it enables accurate, real-time insights over complex documents.

---

## 🧰 Tech Stack

| Tool                  | Purpose                                              |
|-----------------------|------------------------------------------------------|
| 🧠 **LangChain**        | Chains LLMs with retrievers for Q&A flow            |
| 🚀 **Groq Cloud API**   | Blazing-fast LLaMA3-70B inference                   |
| 🧬 **HuggingFace Embeddings** | `BAAI/bge-base-en-v1.5` for semantic search     |
| 📦 **FAISS**            | Efficient vector store for document retrieval       |
| 🌐 **Streamlit**        | Interactive UI for user input/output                |
| 🔗 **UnstructuredURLLoader** | Load data directly from a webpage/document URL |
| 🔐 **dotenv**           | API key and environment variable management         |

---

## 🎯 Example Use Case

Imagine you want to analyze a new public privacy policy from a government website:

1. 🔗 **Paste the URL** (e.g., `https://govsite.gov/privacy-policy`)
2. 📄 The app loads the document and **converts it into vector embeddings**
3. 🧠 You ask:  
   **_"What does this policy say about third-party data sharing?"_**
4. ✅ It returns a **concise, accurate answer with context** — thanks to advanced LLM reasoning.

---

## 📸 Demo Screenshot *(optional)*

> *(Add a screenshot or Streamlit gif here to showcase the app UI and output)*

---

## 🛠 Setup Instructions

```bash
git clone https://github.com/yourusername/PolicyReader-GenAIProject.git
cd PolicyReader-GenAIProject
pip install -r requirements.txt
