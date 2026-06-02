from config.settings import MODEL_NAME
from tenacity import retry
from tenacity import stop_after_attempt
from tenacity import wait_exponential

@retry(
    stop= stop_after_attempt(3),
    wait= wait_exponential(min=2,max=10)
)
async def analyze_data(client,
                skill_id:str,
                sales_data:str):
    
    response = await client.responses.create(
        model= MODEL_NAME,
        input = f"""
Analyze the following sales dataset
and provide useful business insights:

{sales_data}
""",
tools =[
    {
        "type": "shell",
        "environment":{
            "type":"container_auto",
            "skills": [
                {
                "type": "skill_reference",
                "skill_id": skill_id,
                }
            ]
        }
    }
]
    
    )

    return response.output_text