"""
LangChain + Ollama Project
Chat with a PDF using Llama3

No API key required
Runs locally
"""

# PDF Loader
from langchain_community.document_loaders import PyPDFLoader

# Text splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Vector DB
from langchain_community.vectorstores import FAISS

# Embeddings using Ollama
from langchain_ollama import OllamaEmbeddings

# LLM
from langchain_ollama import ChatOllama


# -------------------------
# STEP 1: Load PDF
# -------------------------

print("Loading PDF...")

loader = PyPDFLoader("genai_sample_document.pdf")
documents = loader.load()

print("PDF loaded")
print("Pages:", len(documents))


# -------------------------
# STEP 2: Split document
# -------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

docs = text_splitter.split_documents(documents)

print("Chunks created:", len(docs))


# -------------------------
# STEP 3: Create embeddings
# -------------------------

embeddings = OllamaEmbeddings(
    model="phi3"
)

print("Embeddings ready")


# -------------------------
# STEP 4: Store in vector DB
# -------------------------

vectorstore = FAISS.from_documents(
    docs,
    embeddings
)

print("Vector database ready")


# -------------------------
# STEP 5: Retriever
# -------------------------

retriever = vectorstore.as_retriever()


# -------------------------
# STEP 6: Load LLM
# -------------------------

llm = ChatOllama(
    model="phi3"
)

print("LLM ready")


# -------------------------
# STEP 7: Ask Questions
# -------------------------

print("\nChat with your PDF")
print("Type 'exit' to stop")

while True:

    query = input("\nAsk a question: ")

    if query.lower() == "exit":
        break

    # Retrieve relevant docs
    retrieved_docs = retriever.invoke(query)

    context = "\n".join([doc.page_content for doc in retrieved_docs])

    prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    print("\nAnswer:")
    print(response.content)