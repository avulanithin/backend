from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import emails, tasks, calendar, dashboard

app = FastAPI(
    title="AI Executive Secretary",
    version="0.1.0",
)

# =========================
# ✅ CORS CONFIG (REQUIRED)
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# HEALTH / ROOT
# =========================
@app.get("/")
def root():
    return {"status": "running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

# =========================
# ROUTERS
# =========================
app.include_router(emails.router, prefix="/emails", tags=["Emails"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
app.include_router(calendar.router, prefix="/calendar", tags=["Calendar"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])
