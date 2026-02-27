# Module 7: GenAI Industry Use Cases

## 🎯 Mini Project: Design & Pitch a Domain-Specific GenAI Product

This module helps students design and pitch an AI product for a real industry problem.

### Workflow

```
Choose Industry → Identify Problem → AI Designs Solution → Product Pitch
```

### 🏭 Industries to Choose From

- 🏥 Healthcare
- 💳 Finance
- 🎓 EdTech
- 📈 Marketing
- 🛍 E-Commerce
- 🏛 Government

### 🧠 What You'll Learn

- AI Product Thinking
- Problem-Solution Fit
- Industry Constraints
- Deployment Thinking
- Monetization Strategy

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

- `product_designer.py` — Structures the product idea into a design prompt.
- `pitch_generator.py` — Uses LLM to generate a full product pitch.
- `main.py` — CLI entry point for industry and problem input.
