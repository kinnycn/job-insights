<<<<<<< HEAD

from typing import List, Dict
from fastapi import APIRouter, Depends
from sqlmodel import select, func
from ..database import get_session
=======
from typing import List, Dict, Any
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from sqlalchemy import func
from ..session import get_session
>>>>>>> b6dcf812102d9e113c33dd71636d795e7a79c53d
from ..models import Job

router = APIRouter()

<<<<<<< HEAD
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
=======
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
>>>>>>> b6dcf812102d9e113c33dd71636d795e7a79c53d
