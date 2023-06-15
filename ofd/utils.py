import typing as tp

import httpx
import pydantic as pd

from . import schemas


def post_data_to_get_token(login: str, password: str, **kwargs) -> schemas.AuthToken:
    url = 'https://ofd.ru/api/Authorization/CreateAuthToken'
    data = {'login': login, 'password': password}
    with httpx.Client() as client:
        response = client.post(url, data=data, **kwargs)
        match response.status_code:
            case 200:
                response_json = response.json()
                return schemas.AuthToken.parse_obj(response_json)
            case 403:
                raise httpx.HTTPError('403 Forbidden. Incorrect login or password.')
            case 503:
                raise httpx.HTTPError('Server error')


def get_data_from_request(url: str, params: dict,
                          response_model: tp.Type[pd.BaseModel], **kwargs) -> list[tp.Any]:
    with httpx.Client() as client:
        response = client.get(url, params=params, **kwargs)
        match response.status_code:
            case 200:
                response_json: dict = response.json()
                model = [
                    response_model.parse_obj(items)
                    for items in response_json.get('Data')
                ]
                return model
            case 403:
                raise httpx.HTTPError('403 Forbidden.')
            case 503:
                raise httpx.HTTPError('503. Server error')
