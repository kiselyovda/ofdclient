from ofd import schemas
from .kkt import request_list_kkt

__all__ = ['get_inn']


def get_inn(auth_token: schemas.AuthToken) -> str:
    kkt_list = request_list_kkt(auth_token)
    inn = kkt_list[0].inn
    return inn
