# 🤖 OpenAI Skills API — Python Project

A complete Python demo of the **OpenAI Skills API**.

This project demonstrates the complete workflow:

* Create a skill
* List skills
* Use a skill with the Responses API
* Delete a skill

---

# 📁 Project Structure

```text id="pqk9ea"
openai-skills/
├── main.py              # Full workflow: create → list → use → delete skill
├── SKILL.md             # Custom skill definition
├── requirements.txt
├── README.md
└── venv/
```

---

# 🚀 How to Run

## 1. Create Virtual Environment

```bash id="j0l5l1"
python3 -m venv venv
```

## 2. Activate Virtual Environment

Linux/macOS:

```bash id="n7h2ul"
source venv/bin/activate
```

Windows (PowerShell):

```powershell id="grg85m"
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash id="i3n0uh"
pip install -r requirements.txt
```

---

## 4. Set Your OpenAI API Key

Linux/macOS:

```bash id="n9tw8o"
export OPENAI_API_KEY=sk-your-key-here
```

Windows (PowerShell):

```powershell id="t3b1h9"
setx OPENAI_API_KEY "sk-your-key-here"
```

---

## 5. Run the Project

```bash id="7h2o0u"
python main.py
```

---

# 🔄 What the Script Does

| Step | Action                                                      |
| ---- | ----------------------------------------------------------- |
| 1    | Uploads `SKILL.md` using the OpenAI Skills API              |
| 2    | Lists all available skills                                  |
| 3    | Uses the uploaded skill with the Responses API + shell tool |
| 4    | Deletes the uploaded skill for cleanup                      |

---

# 📦 Upload a Skill

```python id="u2k4lk"
from openai import OpenAI

client = OpenAI()

with open("SKILL.md", "rb") as f:
    skill = client.skills.create(
        files=[("SKILL.md", f, "text/markdown")]
    )

print(skill.id)
```

---

# ⚡ Use the Skill with Responses API

```python id="x6s7mg"
response = client.responses.create(
    model="gpt-4o",
    tools=[{
        "type": "shell",
        "environment": {
            "type": "container_auto",
            "skills": [
                {
                    "type": "skill_reference",
                    "id": skill_id
                }
            ]
        }
    }],
    input="Analyze this data..."
)

print(response.output_text)
```

---

# 🗑️ Delete the Skill

```python id="c8whs4"
client.skills.delete(skill_id)
```

---

# 📌 Key Features

* Uses the official OpenAI Python SDK
* Demonstrates OpenAI Skills API workflow
* Uses Responses API with shell tool execution
* Supports reusable `SKILL.md` definitions
* Minimal and beginner-friendly implementation
* Great starting point for AI agent workflows

---

# 📦 requirements.txt

```txt id="3npq2u"
openai>=1.0.0
```

---

# 🔑 Get an OpenAI API Key

[OpenAI Platform API Keys](https://platform.openai.com/api-keys?utm_source=chatgpt.com)
