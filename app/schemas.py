from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    sales_data:str

class AnalyzeResponse(BaseModel):
    result:str
    