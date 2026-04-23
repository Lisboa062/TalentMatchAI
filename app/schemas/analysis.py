from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.enums import AnalysisStatus


class AnalysisCreate(BaseModel):
    resume_id: int
    job_description_id: int


class AnalysisResponse(BaseModel):
    id: int
    user_id: int
    resume_id: int
    job_description_id: int
    status: AnalysisStatus
    score: float | None
    error_message: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)