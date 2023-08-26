from typing import List
from pydantic import BaseModel, validator

class ModelInputFeatures(BaseModel):
    """
    Validate model input features.

    Args:
        bank: Bank's name.
        week: Number representing the week of the month.
        day: Day of month.
        arrival_time: Time of arrival at the bank (minutes).
        time_spent: Total time spent at the bank until service (minutes).
        exit_time: Time the user left the bank (minutes).
        people_in_queue: People in line who are in front of the user.
    """
    bank: List[str]
    week: List[int]
    day: str
    arrival_time: float
    time_spent: float
    exit_time: float
    people_in_queue: int

    @validator("bank")
    def validate_banks(cls, value):
        allowed_tags = ["bank_1", "bank_2", "bank_3"]
        for tag in value:
            if tag not in allowed_tags:
                raise ValueError(f"Bank '{tag}' is not allowed")
        return value
    
    @validator("week")
    def validate_weeks(cls, value):
        allowed_tags = [1, 2, 3, 4]
        for tag in value:
            if tag not in allowed_tags:
                raise ValueError(f"Week '{tag}' is not allowed")
        return value