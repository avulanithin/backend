from fastapi import FastAPI

from app.api.routes import emails, tasks, calendar, dashboard

app = FastAPI(
    title="AI Executive Secretary",
    version="0.1.0"
)

# Root health check
@app.get("/")
def root():
    return {"status": "running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

# 🔹 REGISTER ROUTERS (THIS IS WHAT WAS MISSING)
app.include_router(emails.router, prefix="/emails", tags=["Emails"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
app.include_router(calendar.router, prefix="/calendar", tags=["Calendar"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])
