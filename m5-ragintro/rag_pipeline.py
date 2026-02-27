from retriever import load_documents, retrieve_context
from llm_layer import generate_answer

def run_rag(question):

    documents = load_documents()
    context = retrieve_context(question, documents)

    print("\n--- Retrieved Context ---\n")
    print(context)

    print("\n--- AI Answer ---\n")
    answer = generate_answer(context, question)
    print(answer)
