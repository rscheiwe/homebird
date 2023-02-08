def test_ping(test_app):
    response = test_app.get("/heartbeat")
    assert response.status_code == 200
    assert response.json() == {"health_check": "health status OK!"}