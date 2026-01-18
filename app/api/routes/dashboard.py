from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date

from app.api.dependencies import get_db
from app.models.email import Email
from app.models.task import Task
from app.models.calendar import CalendarEvent

router = APIRouter()


@router.get("/daily-summary")
def daily_executive_summary(db: Session = Depends(get_db)):
    today = date.today()

    emails_today = db.query(Email).all()

    pending_tasks = (
        db.query(Task)
        .filter(Task.status == "pending_approval")
        .all()
    )

    approved_tasks = (
        db.query(Task)
        .filter(Task.status == "approved")
        .all()
    )

    calendar_events = db.query(CalendarEvent).all()

    return {
        "date": today.isoformat(),
        "emails_today": [
            {
                "id": e.id,
                "sender": e.sender,
                "subject": e.subject,
                "received_at": e.received_at,
            }
            for e in emails_today
        ],
        "pending_tasks": [
            {
                "id": t.id,
                "title": t.title,
                "priority": t.priority,
            }
            for t in pending_tasks
        ],
        "approved_tasks": [
            {
                "id": t.id,
                "title": t.title,
                "priority": t.priority,
            }
            for t in approved_tasks
        ],
        "calendar_events": [
            {
                "id": c.id,
                "title": c.title,
                "start_time": c.start_time,
                "end_time": c.end_time,
            }
            for c in calendar_events
        ],
    }
