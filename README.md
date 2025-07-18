# 🧠 BlogGenius – AI-Powered Iterative Blog Post Generator

BlogGenius is a full-stack application that generates high-quality blog posts using iterative feedback. Built with **FastAPI** (backend) and **React** (frontend), this tool lets you ideate, refine, and finalize blog content with the help of advanced language models.

---

## 🚀 Features

- ✍️ **Topic-based blog generation** – Enter a topic and receive AI-generated blog drafts.
- 🔁 **Iterative feedback system** – Refine drafts by providing feedback on:
  - Clarity of Thought (CoT)
  - Depth of Analysis (DoA)
  - Language and Style
- 💬 **Real-time Streaming Output** – Live content generation via Server-Sent Events (SSE).
- 🌐 **Full-stack App** – FastAPI (Python) for backend + React (Vite) for frontend.
- 🎯 **Clean, modular structure** – Easy to extend or modify.

---

## 🛠️ Tech Stack

### Frontend
- React (Vite)
- HTML/CSS + Tailwind (optional)
- Fetch API for SSE (streaming)
  
### Backend
- FastAPI
- LangGraph + LangChain
- OpenAI/Groq/HuggingFace LLMs (plug-and-play)
- Pydantic models
- CORS Middleware

---

## 🧪 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/bloggenius.git
cd bloggenius
````

---

### 2️⃣ Backend Setup (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs at: `http://localhost:8000`

---

### 3️⃣ Frontend Setup (React)

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at: `http://localhost:5173`

---

## 🧠 How It Works

1. **User inputs a blog topic**
2. **LLM generates an initial blog draft**
3. **User provides structured feedback (CoT, DoA, Language)**
4. **LLM iteratively refines the blog post**
5. **Final blog is streamed back and can be copied/saved**

---


## 🌐 API Endpoints

* `GET /stream?topic=your_topic` – Start blog generation (SSE)
* `POST /feedback` – Submit feedback

Example payload:

```json
{
  "feedback": "Improve clarity and expand on the second paragraph."
}
```

---

## 🧑‍💻 Author

* **Lakshay Goel**
  🔗 [LinkedIn](https://www.linkedin.com/in/your-profile)
  📧 [your.email@example.com](iamlakshaygoel5990@gmail.com)

---

## 📜 License

MIT License – Free to use, modify, and distribute.
