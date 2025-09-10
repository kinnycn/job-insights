import argparse
import csv
from datetime import datetime
from sqlmodel import Session, select
from ..database import engine, create_db_and_tables
from ..models import Job

def load_sample():
    with Session(engine) as session:
          if session.exec(select(Job)).first():
               print("Sample data appears already loaded.")
               return

          with open("data/sample_jobs.csv", "r", encoding="utf-8") as f:
               reader = csv.DictReader(f)
               rows = list(reader)
          for r in rows:
               job = Job(
                     title=r["title"],
                     company=r["company"],
                     city=r["city"],
                     salary_min=int(r["salary_min"]),
                     salary_max=int(r["salary_max"]),
                     experience=r["experience"],
                     posted_at=datetime.fromisoformat(r["posted_at"]).date(),
                     desc=r["desc"],
               )
               session.add(job)
          session.commit()
          print(f"Loaded {len(rows)} rows into database.")

def main():
          parser = argparse.ArgumentParser()
          parser.add_argument("--load-sample", action="store_true", help="Load sample CSV into DB")
          args = parser.parse_args()
          if args.load_sample:
               load_sample()

if __name__ == "__main__":
          main()

