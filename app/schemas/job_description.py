from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class JobDescriptionCreate(BaseModel):
    title: str = Field(min_length=2, max_length=255)
    company: str | None = Field(default=None, max_length=255)
    description: str = Field(min_length=10)


class JobDescriptionResponse(BaseModel):
    id: int
    user_id: int
    title: str
    company: str | None
    description: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)