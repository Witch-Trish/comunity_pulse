from pydantic import BaseModel, Field


class ResponseCreate(BaseModel):
    question_id: int = Field(..., description="ID of the question the response is for")
    is_agree: bool = Field(...)


class ResponseUpdate(ResponseCreate):
    pass


class ResponseDelete(BaseModel):
    response_id: int = Field(...)


class ResponseSchema(BaseModel):
    question_text: str = Field(...)
    is_agree: bool = Field(...)
    question_id: int = Field(...)
    id: int = Field(...)