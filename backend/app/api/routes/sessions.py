from fastapi import APIRouter, HTTPException

from app.models.session import StudySessionCreate
from app.services.supabase import supabase

# APIRouter allows grouping of all session-related
# endpoints inside this file.

router = APIRouter(
    prefix="/sessions",
    tags=["sessions"]
)

################################
#GET
################################
@router.get("")
async def health_check():
    return {
        "status": "healthy",
        "service": "nurseflow-api",
    }

################################
#POST
################################
@router.post("/")
def create_session(session: StudySessionCreate):
    """
    Save a completed study session into Supabase.
    """
    try:
        session_data = {
            "user_id": session.user_id,
            "subject": session.subject,
            "duration_minutes": session.duration_minutes,
            "completed": session.completed
        }
        # Insert the session into the study_sessions table.
        response = (
            supabase
            .table("study_sessions")
            .insert(session_data)
            .execute()
        )
        #return the inserted row back to the frontend.
        return response.data
    
    except Exception as error:
        # If something unexpected happens,
        # return an HTTP 500 error instead of crashing silently.
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )