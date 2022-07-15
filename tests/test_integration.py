import requests

URL = "http://127.0.0.1:8080"


def test_given_get_request_when_http_call_then_returns_200():
    response = requests.get(url=URL)
    response.raise_for_status()

    assert response.status_code == 200


def test_given_post_request_when_http_call_then_returns_200():
    response = requests.post(url=URL)
    response.raise_for_status()

    assert response.status_code == 200


def test_given_delete_request_when_http_call_then_returns_200():
    response = requests.delete(url=URL)
    response.raise_for_status()

    assert response.status_code == 200


def test_given_put_request_when_http_call_then_returns_200():
    response = requests.delete(url=URL)
    response.raise_for_status()

    assert response.status_code == 200


def test_given_post_with_json_body_when_http_call_then_returns_200():
    data = {
        "aaaa": "aaaa",
        "bbbb": "bbbb",
        "cccc": "cccc",
    }
    response = requests.post(url=URL, json=data)
    response.raise_for_status()

    assert response.status_code == 200
