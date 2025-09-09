
from fastapi import FastAPI
from .database import create_db_and_tables
from .routers import jobs, stats

app = FastAPI(title="Job Insights API", version="0.1.0")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
app.include_router(stats.router, prefix="/stats", tags=["stats"])

@app.get("/", tags=["root"])
def root():
    return {"message": "Job Insights API is running. See /docs for details."}
