from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def calendar_view():
    return {"message": "Calendar endpoint"}
