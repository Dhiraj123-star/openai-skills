from pydantic import BaseModel, Field

class AnalyzeRequest(BaseModel):
    sales_data: str = Field(
        ...,
        max_length=10000,
        description="Raw sales data to analyze (maximum 10,000 characters).",
    )

class AnalyzeResponse(BaseModel):
    result: str
    