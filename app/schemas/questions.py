from pydantic import BaseModel, Field
from typing import Optional
from app.schemas.categories import CategorySchema


class QuestionCreate(BaseModel):
    text: str = Field(..., description="Text of the question", max_length=140)
    category_id: int = Field(..., description="Category of the question")


class QuestionDelete(BaseModel):
    question_id: int = Field(...)


class QuestionUpdate(QuestionCreate):
    pass


class QuestionSchema(BaseModel):
    id: int
    text: str
    category: Optional[CategorySchema] #Specifies that the category field can be either a CategorySchema object or None.

    class Config:
        from_attributes = True #Allows you to extract data directly from object attributes, not just from a dictionary


