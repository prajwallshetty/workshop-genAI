# Module 5: Introduction to RAG (Retrieval-Augmented Generation)

This project demonstrates a simple RAG pipeline using keyword-based retrieval and LiteLLM for generation.

## Setup

1. Copy `.env.example` to `.env` and add your Groq API key.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Structure

- `knowledge_base/`: Contains text files used as the retrieval source.
- `retriever.py`: Logic for loading documents and simple keyword-based retrieval.
- `llm_layer.py`: Logic for interacting with the LLM via LiteLLM.
- `rag_pipeline.py`: Orchestrates the retrieval and generation phases.
- `main.py`: Interactive CLI for asking questions.
