from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.api.dependencies import get_db
from app.models.email import Email
from app.schemas.email import EmailCreate, EmailRead
from app.services.email_service import ingest_mock_emails

router = APIRouter()

# CREATE email
@router.post("/", response_model=EmailRead)
def create_email(email: EmailCreate, db: Session = Depends(get_db)):
    db_email = Email(
        sender=email.sender,
        subject=email.subject,
        body=email.body
    )
    db.add(db_email)
    db.commit()
    db.refresh(db_email)
    return db_email


# READ all emails
@router.get("/", response_model=List[EmailRead])
def get_emails(db: Session = Depends(get_db)):
    return db.query(Email).order_by(Email.received_at.desc()).all()


# READ single email
@router.get("/{email_id}", response_model=EmailRead)
def get_email(email_id: int, db: Session = Depends(get_db)):
    email = db.query(Email).filter(Email.id == email_id).first()
    if not email:
        raise HTTPException(status_code=404, detail="Email not found")
    return email

@router.post("/mock-ingest")
def mock_ingest(db: Session = Depends(get_db)):
    emails = ingest_mock_emails(db)
    return {
        "inserted": len(emails),
        "message": "Mock emails ingested successfully"
    }
