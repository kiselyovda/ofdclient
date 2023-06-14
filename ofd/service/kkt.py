import httpx

from ofd import schemas

__all__ = ['request_list_kkt']


def request_list_kkt(auth_token: schemas.AuthToken) -> list[schemas.KktList]:
    url = 'https://ofd.ru/api/integration/v1/kkts'
    params = {'AuthToken': auth_token.auth_token}
    with httpx.Client() as client:
        response = client.get(url, params=params)
        match response.status_code:
            case 200:
                response_json = response.json()
                kkt_list = [schemas.KktList(**items) for items in response_json['Data']]
                return kkt_list
            case 403:
                raise httpx.HTTPError('403 Forbidden.')
            case 503:
                raise httpx.HTTPError('503. Server error')
