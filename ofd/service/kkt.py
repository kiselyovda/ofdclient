from typing import Type, Any

import httpx
import pydantic as pd

from .. import schemas


def _get_data_from_request(url: str, params: dict,
                           response_model: Type[pd.BaseModel]) -> list[Any]:
    with httpx.Client() as client:
        response = client.get(url, params=params)
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


def request_list_kkt(auth_token: schemas.AuthToken) -> list[schemas.KktList]:
    url = 'https://ofd.ru/api/integration/v1/kkts'
    params = {'AuthToken': auth_token.auth_token}
    kkt_list = _get_data_from_request(url, params, schemas.KktList)
    return kkt_list


def request_kkt_folders(auth_token: schemas.AuthToken, *,
                        group_id: str | None = None) -> list[schemas.Folder]:
    url = 'https://ofd.ru/api/integration/v1/kktgroup/list'
    params = {'AuthToken': auth_token.auth_token}
    if id:
        params.update({'groupId': group_id})
    folder = _get_data_from_request(url, params, schemas.Folder)
    return folder
