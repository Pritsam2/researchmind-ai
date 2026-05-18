from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import FAISS


def create_vectorstore(chunks):

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vectorstore