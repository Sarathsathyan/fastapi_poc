from pydantic import BaseModel, Field

class AuthorBase(BaseModel):
    name: str = Field(..., min_length=5,title="Author Name", description="Name of the author")

class AuthorCreate(AuthorBase):
    pass

class AuthorResponse(AuthorBase):
    id: int
    class Config:
        orm_mode = True