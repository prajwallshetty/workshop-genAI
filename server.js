import express from "express";
import dotenv from "dotenv";
import cors from "cors";
import Groq from "groq-sdk";

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

const groq = new Groq({
  apiKey: process.env.GROQ_API_KEY,
});

const SYSTEM_PROMPT = `
Thou art a learned scholar who speaketh in the grand tongue of Shakespeare,
yet also a wild pirate of the seven seas.

Explain all concepts in a dramatic Shakespearean style,
mixed with pirate slang and sea metaphors.

Be theatrical, witty, and humorous.
Keep explanations clear but entertaining.
`;

app.post("/explain", async (req, res) => {
  try {
    const { topic } = req.body;

    const completion = await groq.chat.completions.create({
  model: "llama-3.1-8b-instant",
  messages: [
    { role: "system", content: SYSTEM_PROMPT },
    { role: "user", content: `Explain this concept deeply: ${topic}` },
  ],
  temperature: 0.9,
});

    res.json({
      response: completion.choices[0].message.content,
    });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Something went wrong" });
  }
});

app.listen(5000, () => {
  console.log("Server running on port 5000");
});