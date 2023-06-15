from . import kkt
from .. import schemas


def get_inn(auth_token: schemas.AuthToken) -> str:
    kkt_list = kkt.request_list_kkt(auth_token)
    inn = kkt_list[0].inn
    return inn
