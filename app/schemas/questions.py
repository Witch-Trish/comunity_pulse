from pydantic import BaseModel, Field


class QuestionCreate(BaseModel):
    text: str = Field(..., description="Text of the question", max_length=140)


class QuestionDelete(BaseModel):
    question_id: int = Field(...)


class QuestionUpdate(QuestionCreate):
    pass


class QuestionSchema(BaseModel):
    id: int
    text: str


