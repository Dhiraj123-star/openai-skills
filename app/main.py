from fastapi import FastAPI, HTTPException

from app.schemas import (
    AnalyzeRequest,
    AnalyzeResponse
)
from app.dependencies import get_openai_client

from services.skill_service import (
    upload_skill,
    delete_skill,
)

from services.response_service import (
    analyze_data
)


app = FastAPI(
    title="OpenAI Skills API",
    version="1.0.0",
)

@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "service": "OpenAI Skills API",
    }

@app.post(
    "/analyze",
    response_model=AnalyzeResponse,
)
def analyze(
    request: AnalyzeRequest,
):
    client= get_openai_client()

    skill = None

    try:
        # upload skill
        skill = upload_skill(client)

        # Analyze data
        result = analyze_data(
            client = client,
            skill_id = skill.id,
            sales_data = request.sales_data,
        )

        return AnalyzeResponse(
            result=result,
        )
    except Exception as exc:
        raise HTTPException (
            status_code = 500,
            detail = str(exc),
        )
    
    finally:
        if skill:
            try:
                delete_skill(
                    client,
                    skill.id,
                )
            except Exception:
                pass