from config.settings import MODEL_NAME

def analyze_sales_data(client,skill_id,sample_data):
    response = client.responses.create(
        model= MODEL_NAME,
        input = f"""
Analyze the following sales dataset
and provide useful business insights:

{sample_data}
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

    return response