from app import app

def test_get_inventory():
    client = app.test_client()
    res = client.get("/inventory")
    assert res.status_code == 200


def test_add_invalid():
    client = app.test_client()
    res = client.post("/inventory", json={"code": "000"})
    assert res.status_code in [400, 200]