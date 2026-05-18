import os

from langchain_community.document_loaders import PyMuPDFLoader


def load_documents(data_path):

    documents = []

    for file in os.listdir(data_path):

        if file.endswith(".pdf"):

            pdf_path = os.path.join(data_path, file)

            loader = PyMuPDFLoader(pdf_path)

            docs = loader.load()

            # Add filename metadata
            for doc in docs:

                doc.metadata["source_file"] = file

            documents.extend(docs)

    return documents