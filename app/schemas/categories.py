from pydantic import BaseModel, Field


class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)


class CategoryDelete(BaseModel):
    category_id: int = Field(...)


class CategoryUpdate(CategoryCreate):
    pass


class CategorySchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
