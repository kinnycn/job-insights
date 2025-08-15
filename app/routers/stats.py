from typing import List, Dict, Any
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from sqlalchemy import func
from ..session import get_session
from ..models import Job

router = APIRouter()

@router.get("/city")
def stats_by_city(session: Session = Depends(get_session)) -> List[Dict[str, Any]]:
    stmt = (
        select(Job.city, func.count().label("count"))
        .group_by(Job.city)
        .order_by(func.count().desc())
    )
    rows = session.exec(stmt).all()  # List[tuple[city, count]]
    return [{"city": city, "count": count} for city, count in rows]

@router.get("/salary")
def stats_salary(session: Session = Depends(get_session)) -> List[Dict[str, int | str]]:
    buckets: dict[str, int] = {}
    jobs = session.exec(select(Job)).all()
    for j in jobs:
        # 如果可能存在空值，先跳过/兜底
        if j.salary_min is None or j.salary_max is None:
            continue
        low = (j.salary_min // 5000) * 5000
        high = ((j.salary_max // 5000) + 1) * 5000
        key = f"{low}-{high}"
        buckets[key] = buckets.get(key, 0) + 1
    return [{"range": k, "count": v} for k, v in sorted(buckets.items())]
