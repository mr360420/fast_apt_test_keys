from pydantic import BaseModel, condecimal
from datetime import datetime


class MLData(BaseModel):
    regno_recognize: str
    afts_regno_ai: str
    recognition_accuracy: condecimal(gt=0)
    afts_regno_ai_score: condecimal(gt=0)
    afts_regno_ai_char_scores: str
    afts_regno_ai_length_scores: str
    camera_type: str
    camera_class: str
    time_check: datetime
    direction: int


class MLDataResult(BaseModel):
    result: list[list[float]]


