import pytest


@pytest.mark.django_db
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Test Title 1' in response.content
    assert b'2019-01-01' in response.content
