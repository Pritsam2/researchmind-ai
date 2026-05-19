from openai import OpenAI

import os

from dotenv import load_dotenv


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_multiple_queries(user_query):

    prompt = f"""
    You are an AI research assistant specialized in retrieval optimization.

    Generate 4 semantic variations of the user's question.

    Each variation should:
    - preserve meaning
    - use different technical wording
    - improve retrieval coverage
    - be concise

    Original Question:
    {user_query}

    Return ONLY the queries.
    """

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.7
    )

    output = response.choices[0].message.content

    queries = []

    for line in output.split("\n"):

        line = line.strip()

        if line:

            line = line.split(".", 1)[-1].strip()

            queries.append(line)

    return queries