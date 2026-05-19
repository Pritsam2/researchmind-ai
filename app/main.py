from app.ingestion.loader import load_documents

from app.ingestion.chunker import split_documents

from app.ingestion.embeddings import create_vectorstore


from app.retrieval.multi_query import generate_multiple_queries

from app.retrieval.retriever import (
    retrieve_documents,
    deduplicate_documents
)


from app.generation.answer_generator import (
    build_context,
    generate_answer
)


# -----------------------------
# LOAD DOCUMENTS
# -----------------------------

documents = load_documents("data")


# -----------------------------
# SPLIT DOCUMENTS
# -----------------------------

chunks = split_documents(documents)


# -----------------------------
# CREATE VECTORSTORE
# -----------------------------

vectorstore = create_vectorstore(chunks)


# -----------------------------
# MAIN PIPELINE
# -----------------------------

def run_researchmind_ai(user_query):

    # Generate Multiple Queries
    query_list = generate_multiple_queries(user_query)

    # Retrieve Documents
    retrieved_docs = retrieve_documents(
        vectorstore,
        query_list
    )

    # Remove Duplicates
    unique_docs = deduplicate_documents(
        retrieved_docs
    )

    # Build Context
    context = build_context(unique_docs)

    # Generate Final Answer
    final_answer = generate_answer(
        user_query,
        context
    )

    return {
        "generated_queries": query_list,
        "answer": final_answer
    }