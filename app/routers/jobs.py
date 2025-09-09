
from typing import Optional, List
from fastapi import APIRouter, Depends, Query
from sqlmodel import select
from ..database import get_session
from ..models import Job

router = APIRouter()

@router.get("", response_model=List[Job])
def list_jobs(
    q: Optional[str] = None,
    city: Optional[str] = None,
    skip: int = 0,
    limit: int = Query(20, le=100),
    session = Depends(get_session),
):
    stmt = select(Job)
    if q:
        q_like = f"%{q}%"
        stmt = stmt.where((Job.title.like(q_like)) | (Job.desc.like(q_like)) | (Job.company.like(q_like)))
    if city:
        stmt = stmt.where(Job.city == city)
    stmt = stmt.offset(skip).limit(limit)
    return session.exec(stmt).all()

@router.get("/recommend", response_model=List[Job])
def recommend_jobs(skill: str, limit: int = 10, session = Depends(get_session)):
    like = f"%{skill}%"
    stmt = select(Job).where((Job.title.like(like)) | (Job.desc.like(like))).limit(limit)
    return session.exec(stmt).all()
