def test_read_homes_ids_correct(test_app):
    response = test_app.get(f"/homebird/homes-ids")
    assert response.status_code == 200


def test_read_home_by_id_incorrect(test_app):
    home_id = 10
    response = test_app.get(f"/homebird/homes/{home_id}")

    assert response.status_code == 404
    assert response.json()["detail"] == f"Home with id: {home_id} not found"
