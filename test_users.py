import pytest
@pytest.mark.smoke
def test_get_single_post_status_code(base_url, api_session):
    response = api_session.get(f"{base_url}/posts/1")
    assert response.status_code == 200
@pytest.mark.smoke
def test_get_single_post_response_structure(base_url, api_session):
    response = api_session.get(f"{base_url}/posts/1")
    body = response.json()

    assert "id" in body
    assert body["id"] == 1
    assert "title" in body
    assert isinstance(body["title"], str)
@pytest.mark.regression
@pytest.mark.parametrize("post_id, expected_status", [
    (1, 200),
    (9999, 404),   # несуществующий id
    (2, 200),
])
def test_get_post_various_ids(base_url, api_session, post_id, expected_status):
    response = api_session.get(f"{base_url}/posts/{post_id}")
    assert response.status_code == expected_status


@pytest.mark.regression
def test_create_post(base_url, api_session, new_user_payload):
    response = api_session.post(f"{base_url}/posts", json=new_user_payload)
    body = response.json()

    assert response.status_code == 201
    assert body["title"] == new_user_payload["title"]
    assert body["body"] == new_user_payload["body"]
    assert "id" in body


@pytest.mark.regression
def test_create_post_empty_payload(base_url, api_session):
    response = api_session.post(f"{base_url}/posts", json={})
    assert response.status_code == 201