# 🤖 OpenAI Skills API — Python Project

A complete Python demo of the **OpenAI Skills API**.

This project demonstrates the complete workflow:

* Create a skill
* List skills
* Use a skill with the Responses API
* Delete a skill
* Automatically clean up duplicate skills
* Organize code using a production-style structure

---

# 📁 Project Structure

```text
openai-skills/
├── main.py
├── requirements.txt
├── .env
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
└── README.md
```

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

Windows (PowerShell):

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

## 5. Run the Project

```bash
python main.py
```

---

# 🔄 Workflow

| Step | Action                                      |
| ---- | ------------------------------------------- |
| 1    | Delete previously uploaded duplicate skills |
| 2    | Upload a fresh custom skill                 |
| 3    | Wait for skill propagation                  |
| 4    | Retrieve and verify the uploaded skill      |
| 5    | List available skills                       |
| 6    | Use the skill with GPT-5.2 + Shell Tool     |
| 7    | Delete the uploaded skill                   |
| 8    | Verify cleanup                              |

---

# 📦 Upload a Skill

```python
with open("my_skill/SKILL.md", "rb") as f:
    skill = client.skills.create(
        files=[
            (
                "my_skill/SKILL.md",
                f,
                "text/markdown",
            )
        ]
    )
```

---

# ⚡ Use the Skill with Responses API

```python
response = client.responses.create(
    model="gpt-5.2",
    input="Analyze this sales data...",
    tools=[
        {
            "type": "shell",
            "environment": {
                "type": "container_auto",
                "skills": [
                    {
                        "type": "skill_reference",
                        "skill_id": skill_id,
                    }
                ],
            },
        }
    ],
)
```

---

# 🗑️ Delete a Skill

```python
client.skills.delete(skill_id)
```

---

# 📌 Key Features

* Uses the official OpenAI Python SDK
* Demonstrates the complete OpenAI Skills API workflow
* Uses GPT-5.2 with the Shell Tool
* Supports reusable `SKILL.md` definitions
* Automatic duplicate skill cleanup
* Modular service-based architecture
* Environment variable management with `python-dotenv`
* Production-style project structure
* Easy to extend for FastAPI and AI Agent projects

---

# 📦 requirements.txt

```txt
openai>=2.0.0
python-dotenv>=1.0.0
```

---

# 🔑 Get an OpenAI API Key

https://platform.openai.com/api-keys
