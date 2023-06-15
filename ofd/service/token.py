import httpx

from .. import schemas


def get_token(login: str, password: str) -> schemas.AuthToken:
    url = 'https://ofd.ru/api/Authorization/CreateAuthToken'
    data = {'login': login, 'password': password}
    with httpx.Client() as client:
        response = client.post(url, data=data)
        match response.status_code:
            case 200:
                response_json = response.json()
                return schemas.AuthToken.parse_obj(response_json)
            case 403:
                raise httpx.HTTPError('403 Forbidden. Incorrect login or password.')
            case 503:
                raise httpx.HTTPError('Server error')
