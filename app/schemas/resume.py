from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.enums import ExtractionStatus


class ResumeResponse(BaseModel):
    id: int
    user_id: int
    filename: str
    stored_path: str
    raw_text: str | None
    extraction_status: ExtractionStatus
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)