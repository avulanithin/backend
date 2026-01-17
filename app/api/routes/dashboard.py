from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def dashboard_summary():
    return {"message": "Dashboard summary endpoint"}
