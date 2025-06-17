from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test1():
    res = client.post("/brackets/check/", json={"text": "(vdvsf)[vrsb]"})
    assert res.status_code == 200
    assert res.json() == {"norm": True}

def test2():
    res = client.post("/brackets/check/", json={"text": "("})
    assert res.status_code == 200
    assert res.json() == {"norm": False}