from config.settings import MODEL_NAME

def analyze_data(client,
                skill_id:str,
                sales_data:str):
    
    response = client.responses.create(
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