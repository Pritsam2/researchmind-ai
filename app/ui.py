import gradio as gr

from app.main import run_researchmind_ai


def ask_question(user_query):

    result = run_researchmind_ai(user_query)

    queries = "\n".join(result["generated_queries"])

    answer = result["answer"]

    return queries, answer


interface = gr.Interface(

    fn=ask_question,

    inputs=gr.Textbox(
        label="Ask ResearchMind AI",
        placeholder="Enter your research question..."
    ),

    outputs=[

        gr.Textbox(
            label="Generated Multi-Queries"
        ),

        gr.Textbox(
            label="ResearchMind AI Answer"
        )
    ],

    title="ResearchMind AI",

    description="""
    Advanced Multi-Query Retrieval-Augmented Generation (RAG) System
    for Research Paper Understanding
    """
)


interface.launch()