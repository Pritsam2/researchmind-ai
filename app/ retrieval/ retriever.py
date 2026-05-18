def retrieve_documents(vectorstore, query_list, k=3):

    all_docs = []

    for query in query_list:

        results = vectorstore.similarity_search(
            query,
            k=k
        )

        all_docs.extend(results)

    return all_docs


def deduplicate_documents(documents):

    unique_docs = []

    seen_contents = set()

    for doc in documents:

        content = doc.page_content

        if content not in seen_contents:

            seen_contents.add(content)

            unique_docs.append(doc)

    return unique_docs