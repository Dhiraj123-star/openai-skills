# 🤖 OpenAI Skills API + FastAPI

A production-style Python project demonstrating the **OpenAI Skills API** integrated with **FastAPI**.

This project showcases:

* Create a custom skill
* Upload and manage skills
* Use skills with the Responses API
* Analyze data using GPT-5.2 + Shell Tool
* Automatically clean up duplicate skills
* FastAPI REST API integration
* Modular service-based architecture
* Environment-based configuration

---

# 📁 Project Structure

```text
openai-skills/
├── app/
│   ├── main.py
│   ├── schemas.py
│   └── dependencies.py
│
├── config/
│   └── settings.py
│
├── data/
│   └── sample_data.py
│
├── services/
│   ├── skill_service.py
│   └── response_service.py
│
├── utils/
│   └── logger.py
│
├── my_skill/
│   └── SKILL.md
│
├── .env
├── requirements.txt
└── README.md
```

---

# 🚀 Features

* OpenAI Skills API integration
* GPT-5.2 Shell Tool execution
* FastAPI REST endpoints
* Automatic skill lifecycle management
* Duplicate skill cleanup
* Modular service architecture
* Environment variable configuration
* Swagger UI documentation
* Easy extension for AI agent workflows

---

# 🚀 How to Run

## 1. Create Virtual Environment

```bash
python3 -m venv venv
```

## 2. Activate Virtual Environment

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```powershell
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create `.env`

```env
OPENAI_API_KEY=sk-your-openai-api-key
```

---

## 5. Start FastAPI

```bash
uvicorn app.main:app --reload
```

---

# 📖 API Documentation

Swagger UI:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

---

# 🔄 API Workflow

| Step | Action                     |
| ---- | -------------------------- |
| 1    | Receive sales data via API |
| 2    | Upload custom skill        |
| 3    | Wait for skill propagation |
| 4    | Execute GPT-5.2 analysis   |
| 5    | Return business insights   |
| 6    | Delete uploaded skill      |
| 7    | Return structured response |

---

# 📡 Endpoints

## Health Check

```http
GET /
```

Response:

```json
{
  "status": "healthy",
  "service": "OpenAI Skills API"
}
```

---

## Analyze Sales Data

```http
POST /analyze
```

Request:

```json
{
  "sales_data": "January: 1000\nFebruary: 2000\nMarch: 3000"
}
```

Response:

```json
{
  "result": "Sales increased steadily from January to March..."
}
```

---

# 📌 Key Technologies

* FastAPI
* OpenAI Python SDK
* OpenAI Skills API
* GPT-5.2
* Shell Tool
* Python Dotenv
* Pydantic

---

# 📦 requirements.txt

```txt
fastapi
uvicorn[standard]
openai>=2.0.0
python-dotenv>=1.0.0
pydantic
```

---

# 🔑 Get an OpenAI API Key

https://platform.openai.com/api-keys
