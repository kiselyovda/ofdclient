from .. import schemas, utils


def get_token(login: str, password: str) -> schemas.AuthToken:
    return utils.post_data_to_get_token(login, password)
