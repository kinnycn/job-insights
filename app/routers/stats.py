
from typing import List, Dict
from fastapi import APIRouter, Depends
from sqlmodel import select, func
from ..database import get_session
from ..models import Job

router = APIRouter()

@router.get("/city", response_model=List[Dict])
def stats_by_city(session = Depends(get_session)):
    stmt = select(Job.city, func.count()).group_by(Job.city)
    rows = session.exec(stmt).all()
    return [{"city": c, "count": int(n)} for c, n in rows]

@router.get("/salary", response_model=List[Dict])
def stats_salary(session = Depends(get_session)):
    ranges = {}
    jobs = session.exec(select(Job)).all()
    for j in jobs:
        bucket = f"{(j.salary_min//5000)*5000}-{((j.salary_max//5000)+1)*5000}"
        ranges[bucket] = ranges.get(bucket, 0) + 1
    return [{"range": k, "count": v} for k, v in sorted(ranges.items())]
