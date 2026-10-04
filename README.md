# Document Q&A Chatbot

An AI-powered chatbot that answers questions using only the content of an uploaded document — built using Python and Meta's Llama 3 model running locally via Ollama.

## What It Does
- Reads a text document
- Answers user questions based strictly on that document's content
- Runs entirely locally — no external API costs, full data privacy

## Tech Stack
- **Python** — core logic
- **Ollama** — runs Llama 3 locally
- **Flask** — REST API for serving the chatbot
- **Git/GitHub** — version control

## Project Files
- `my_chatbot.py` — command-line version: ask a question, get an answer
- `my_api.py` — REST API version: POST a question to `/ask` and get a JSON response
- `mydocument.txt` — sample document used for testing

## How It Works
1. Loads the document text from a file
2. Combines the document and the user's question into a prompt
3. Sends the prompt to Llama 3 (via Ollama), instructing it to answer **only** from the document
4. Returns the answer

## Running Locally

**Command-line version:**
\`\`\`bash
python my_chatbot.py
\`\`\`

**API version:**
\`\`\`bash
python my_api.py
\`\`\`
Then send a request:
\`\`\`bash
curl -X POST http://127.0.0.1:5050/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "your question here"}'
\`\`\`

## Why I Built This
This project demonstrates practical skills in Python, REST API development, local LLM integration (RAG-style document grounding), and Git/GitHub workflow — built as part of my hands-on learning toward a career in AI/cloud engineering.

## Author
Dhanalakshmi — [GitHub](https://github.com/Dhanalakshmi85)
