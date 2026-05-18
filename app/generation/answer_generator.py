from openai import OpenAI

import os

from dotenv import load_dotenv


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def build_context(documents):

    context = ""

    for i, doc in enumerate(documents):

        source = doc.metadata["source_file"]

        page = doc.metadata["page"]

        content = doc.page_content

        context += f"""
        DOCUMENT {i+1}

        SOURCE: {source}
        PAGE: {page}

        CONTENT:
        {content}

        --------------------------------------------------
        """

    return context


def generate_answer(user_query, context):

    prompt = f"""
    You are ResearchMind AI,
    an advanced AI research assistant.

    Answer the user's question ONLY using the provided context.

    RULES:
    - Do not hallucinate
    - Do not invent information
    - Cite sources where possible
    - Be technically detailed
    - Explain clearly

    USER QUESTION:
    {user_query}

    CONTEXT:
    {context}
    """

    response = client.chat.completions.create(

        model="gpt-4.1",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.2
    )

    return response.choices[0].message.content