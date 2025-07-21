# 🧠 Multi-Agent Python Code Generator (LangChain + FastAPI + LM Studio)

This project is a lightweight code generation API powered by a local language model (LM Studio), built using **LangChain agents**, **FastAPI**, and a custom-coded agent architecture.

## 🚀 Features

- 💬 `MessengerAgent` takes user prompts
- 👨‍💻 `CoderAgent` generates clean, commented Python code using local LLM
- ⚡ FastAPI backend with a `/generate_code` POST endpoint
- 🧠 Powered by LM Studio running `phi-3-mini-4k-instruct`
- 📦 Clean structure, modular design, and .env-based config loading

---

## 🛠 Tech Stack

- [LangChain](https://www.langchain.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [LM Studio (Local LLM)](https://lmstudio.ai/)
- Python 3.10+

---

## 📁 Folder Structure

aspire2/
├── agents.py # MessengerAgent and CoderAgent logic
├── app.py # FastAPI backend
├── .env # Environment variables (excluded from Git)
├── requirements.txt # Python dependencies
└── README.md # You're here!

##CLONE THE REPO

```bash
git clone https://github.com/GUNREDDY14/multiagent.git
cd multiagent

## CREATE A .env file 
OPENAI_API_KEY=lm-studio

##INSTALL REQ
pip install -r requirements.txt

## RUN FASTAPI
uvicorn app:app --reload
