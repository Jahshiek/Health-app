from pydantic import BaseModel


class StudySessionCreate(BaseModel):
    # The ID of the user who completed the study session.
    user_id: str

    # The subject the user studied.
    subject: str

    # Number of minutes spent studying.
    duration_minutes: int

    # Whether the study session was completed.
    # Defaults to True.
    completed: bool = True