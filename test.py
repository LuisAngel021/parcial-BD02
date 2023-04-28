import requests

def test_url_response():
    response = requests.get('https://ejemplo.com')
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'text/html; charset=UTF-8'
