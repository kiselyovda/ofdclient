from .. import schemas, utils


def request_list_kkt(auth_token: schemas.AuthToken) -> list[schemas.KktList]:
    url = 'https://ofd.ru/api/integration/v1/kkts'
    params = {'AuthToken': auth_token.auth_token}
    kkt_list = utils.get_data_from_request(url, params, schemas.KktList)
    return kkt_list


def request_kkt_folders(auth_token: schemas.AuthToken, *,
                        group_id: str | None = None) -> list[schemas.Folder]:
    url = 'https://ofd.ru/api/integration/v1/kktgroup/list'
    params = {'AuthToken': auth_token.auth_token}
    if group_id:
        params.update({'groupId': group_id})
    folder = utils.get_data_from_request(url, params, schemas.Folder)
    return folder
