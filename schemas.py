from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Message(BaseModel):
    text: str
    user_id: str
    timestamp: datetime
    thread_timestamp: Optional[datetime] = None
    channel_id: str


class RequestModel(BaseModel):
    question: str
