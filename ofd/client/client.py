from datetime import datetime, timedelta

from ofd import schemas, service

__all__ = [
    'Client'
]


class Client:
    def __init__(self, auth_token: str | None = None, *, login: str | None = None, password: str | None = None):
        self.login = login
        self.password = password
        if auth_token:
            self.auth_token = schemas.AuthToken(auth_token=auth_token, expiration_date_utc=None)
        else:
            self.auth_token = service.get_token(login, password)

    @property
    def inn(self) -> str:
        return service.get_inn(self.auth_token)

    @property
    def kkt_list(self) -> list[schemas.KktList]:
        return service.request_list_kkt(self.auth_token)
