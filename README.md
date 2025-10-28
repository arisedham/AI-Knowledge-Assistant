# AI-Knowledge-Assistant
An intelligent chatbot using LangChain and OpenAI API, enabling document-based question answering.

# Problem Statement

In organizations, valuable knowledge is often scattered across documents, reports, and PDFs—making it difficult for teams to retrieve relevant information quickly. Traditional search methods rely on keyword matching, which fails to capture semantic meaning and context.

The AI Knowledge Assistant solves this problem by combining Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs) to enable natural language question answering over custom documents.
Users can upload PDFs or text files and interact with an intelligent chatbot that provides accurate, context-aware answers.

# Tech Stack

| Layer               | Tools / Frameworks                         |
| ------------------- | ------------------------------------------ |
| **Frontend**        | Streamlit (interactive chat UI)            |
| **Backend API**     | FastAPI (RESTful endpoints + Swagger docs) |
| **AI / NLP**        | LangChain, OpenAI GPT API                  |
| **Vector Database** | FAISS (semantic embedding search)          |
| **Deployment**      | Docker, AWS EC2                            |
| **Version Control** | Git + GitHub Actions (CI/CD)               |

# Features

📂 Document Upload: Upload PDFs or text files for ingestion.

🔍 Semantic Retrieval: Retrieve relevant document chunks using FAISS vector embeddings.

💬 Contextual Chat: Ask natural-language questions and receive answers grounded in your uploaded documents.

🧠 RAG Pipeline: Integrates retrieval with GPT-based generation for contextually accurate responses.

🧾 API Access: FastAPI backend exposes /upload and /query endpoints with Swagger documentation.

🐳 Dockerized Deployment: Fully containerized for easy deployment on any environment.

⚡ CI/CD Integration: Automated testing and deployment pipeline via GitHub Actions.

☁️ Scalable Hosting: Deployed on AWS EC2 instance with persistent storage.

# System Architecture

                ┌────────────────────────────┐
                │         User Query          │
                └──────────────┬──────────────┘
                               │
                      ┌────────▼────────┐
                      │    Streamlit     │
                      │  (Chat UI App)   │
                      └────────┬────────┘
                               │ REST API Call
                      ┌────────▼────────┐
                      │     FastAPI      │
                      │ (Backend Server) │
                      └────────┬────────┘
                               │
            ┌──────────────────▼──────────────────┐
            │     LangChain RAG Pipeline          │
            │  (Embedding + Retrieval + LLM)      │
            └──────────────────┬──────────────────┘
                               │
                      ┌────────▼────────┐
                      │     FAISS DB     │
                      │ (Vector Store)   │
                      └──────────────────┘


# Demo Screenshots

(To be add later)

| Interface      | Description                                      |
| -------------- | ------------------------------------------------ |
| Chat UI        | Upload documents and chat interactively          |
| Swagger Docs   | API documentation for upload and query endpoints |
| System Diagram | RAG workflow visualization                       |

# Setup and Installation

# Clone the repository
git clone https://github.com/<your-username>/AI-Knowledge-Assistant.git
cd AI-Knowledge-Assistant

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt

# Run FastAPI backend
uvicorn app.backend.main:app --reload

# Run Streamlit frontend
streamlit run app/frontend.py

# Docker Deployment

# Build and run using Docker Compose
docker-compose up --build

Access the app:

Streamlit UI → http://localhost:8501

FastAPI Docs → http://localhost:8000/docs

# Future Enhancements

🔐 Add authentication (JWT-based access).

📚 Support multiple file types (CSV, DOCX, HTML).

🌍 Integrate Hugging Face local models for offline inference.

🧩 Add analytics dashboard (chat history, query performance).

# 🤝 Contributing

Contributions are welcome! Please fork the repo and submit a pull request with detailed changes.



