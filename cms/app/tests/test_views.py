import pytest


@pytest.mark.django_db
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Test Title 12' in response.content
    assert b'2022-02-10' in response.content

    # test for pagination
    assert b'Test Title 01' not in response.content
    assert b'2019-01-01' not in response.content


@pytest.mark.django_db
def test_index_page2(client):
    response = client.get('/?page=2')
    assert response.status_code == 200
    assert b'Test Title 07' in response.content
    assert b'Test Title 08' not in response.content


@pytest.mark.django_db
def test_detail(client):
    response = client.get('/entry/1')
    assert response.status_code == 200
    assert b'Test Title 01' in response.content
    assert b'2019-01-01' in response.content
    assert b'This body is test.' in response.content


@pytest.mark.django_db
def test_detail_exists_required(client):
    response = client.get('/entry/100')
    assert response.status_code == 404
