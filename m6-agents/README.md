# Module 6: AI Agents & Automation Thinking

## 🤖 Mini Project: Resume Review AI Agent

This module demonstrates AI Agent concepts through a Resume Review Agent that follows structured, multi-step reasoning.

### Agent Workflow

```
User Input (Resume + JD)
        ↓
Step 1: Extract Skills (Tool)
        ↓
Step 2: Compare Skills (Tool)
        ↓
Step 3: Suggest Improvements (LLM)
        ↓
Step 4: Score Resume (LLM)
```

### 🧠 What You'll Learn

- What is an AI Agent
- Multi-step reasoning
- Task decomposition
- Tool simulation
- Structured workflow thinking

## Setup

1. Copy `.env.example` to `.env` and add your Groq API key.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run:
   ```bash
   python main.py
   ```

## Structure

- `tools.py` — Simulated tools for keyword extraction and skill comparison.
- `llm_layer.py` — LLM interaction via LiteLLM with agent system prompt.
- `agent_brain.py` — Core agent logic: orchestrates tools and LLM reasoning.
- `main.py` — CLI interface for inputting resume and job description.
