
from fastapi.testclient import TestClient
from app.main import app
from app.utils.ingest import load_sample

client = TestClient(app)

def setup_module(module):
    load_sample()

def test_root():
    res = client.get("/")
    assert res.status_code == 200

def test_list_jobs():
    res = client.get("/jobs")
    assert res.status_code == 200
