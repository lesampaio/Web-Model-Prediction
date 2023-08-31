from pydantic import BaseModel

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
    bank: str
    week: int
    day: str
    arrival_time: float
    time_spent: float
    exit_time: float
    people_in_queue: int