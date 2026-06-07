# 🤖 OpenAI Skills API + FastAPI

A production-style Python project demonstrating the **OpenAI Skills API** integrated with **FastAPI**.

This project showcases:

* Create and manage custom skills
* Use OpenAI Skills with the Responses API
* Analyze data using GPT-5.2 + Shell Tool
* FastAPI REST API integration
* Async OpenAI SDK support
* Structured logging
* Automatic retry handling
* Environment-based configuration
* Modular service architecture

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
* Async OpenAI SDK support
* Connection pooling with single reuse of `AsyncOpenAI` client
* Request timeout configuration
* Fail-fast startup validation for `OPENAI_API_KEY`
* Payload size security limiting on API inputs
* Structured logging
* Automatic retry handling with exponential backoff
* Skill lifecycle management
* Duplicate skill cleanup
* Environment variable configuration
* Swagger UI documentation
* Production-ready service architecture

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

## 🐳 Run with Docker (Alternative)

Ensure you have Docker and Docker Compose installed, and your `.env` file is set up with your `OPENAI_API_KEY`.

### Build and Start Containers

To build the image and run the application in the background:

```bash
docker compose up -d --build
```

The application will be running at `http://localhost`.

### View Logs

To stream the service logs:

```bash
docker compose logs -f
```

### Stop Containers

To shut down the running containers:

```bash
docker compose down
```

### 🔒 Adding Local SSL Certificates (HTTPS)

To run the Docker setup with local SSL certificates (enabling `https://localhost`), follow these steps:

1. **Generate Certificates**: Create a directory named `nginx/certs` and generate the certificate files.
   * Using `mkcert` (Recommended for browser trust):
     ```bash
     mkdir -p nginx/certs
     mkcert -key-file nginx/certs/localhost-key.pem -cert-file nginx/certs/localhost.pem localhost 127.0.0.1 ::1
     ```
   * Using `openssl` (Self-signed):
     ```bash
     mkdir -p nginx/certs
     openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
       -keyout nginx/certs/localhost-key.pem \
       -out nginx/certs/localhost.pem \
       -subj "/CN=localhost"
     ```

2. **Configure Nginx**: Update [nginx/default.conf](file:///home/dhiraj-kumar/Desktop/Projects/openai-skills/nginx/default.conf) to support SSL on port `443` and map the certificate files. For details, refer to the [local_ssl_guide.md](file:///home/dhiraj-kumar/.gemini/antigravity-cli/brain/b5839594-4352-45f3-9f09-ce4e940f67fa/local_ssl_guide.md).

3. **Configure Docker Compose**: Expose port `443` and map the certificate directory in [docker-compose.yml](file:///home/dhiraj-kumar/Desktop/Projects/openai-skills/docker-compose.yml):
   ```yaml
     nginx:
       ports:
         - "80:80"
         - "443:443"
       volumes:
         - ./nginx/default.conf:/etc/nginx/conf.d/default.conf:ro
         - ./nginx/certs:/etc/nginx/certs:ro
   ```

4. **Restart the Stack**:
   ```bash
   docker compose down
   docker compose up -d
   ```

---

# 📖 API Documentation

Swagger UI (Docker/Nginx):

```text
http://localhost/docs
```

Or when running locally without Docker:

```text
http://localhost:8000/docs
```

ReDoc (Docker/Nginx):

```text
http://localhost/redoc
```

Or when running locally without Docker:

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

# 🏗️ Production Features

## Performance & Connection Pooling

* Reuses a single `AsyncOpenAI` client instance across the application lifecycle to enable HTTP connection pooling.
* Enforces a 60-second request timeout on all OpenAI calls to prevent requests from hanging indefinitely.

## Fail-Fast Validation

* Validates the presence of `OPENAI_API_KEY` at startup time.
* Immediately raises a `ValueError` if the key is missing or empty, avoiding late-stage runtime failures during requests.

## Payload Security

* Restricts the `sales_data` string input length to a maximum of 10,000 characters.
* Mitigates potential resource exhaustion and payload abuse vectors.

## Async Support

* Uses `AsyncOpenAI`
* Async FastAPI endpoints
* Improved concurrency and throughput

## Structured Logging

* Centralized logging utility
* Consistent log formatting
* Better observability and debugging

## Retry Handling

* Powered by Tenacity
* Automatic retries for transient failures
* Exponential backoff strategy

---

# 📌 Key Technologies

* FastAPI
* OpenAI Python SDK
* OpenAI Skills API
* GPT-5.2
* Shell Tool
* Python Dotenv
* Pydantic
* Tenacity

---

# 📦 requirements.txt

```txt
fastapi
uvicorn[standard]
openai>=2.0.0
python-dotenv>=1.0.0
pydantic
tenacity
```

---

# 🔑 Get an OpenAI API Key

https://platform.openai.com/api-keys
