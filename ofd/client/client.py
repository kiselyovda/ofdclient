from .. import schemas, service


class Client:
    def __init__(self, auth_token: str | None = None, *, login: str | None = None, password: str | None = None):
        self.login = login
        self.password = password
        if auth_token:
            self.auth_token = schemas.AuthToken(AuthToken=auth_token, ExpirationDateUtc=None)
        else:
            self.auth_token = service.get_token(login, password)

    @property
    def inn(self) -> str:
        return service.get_inn(self.auth_token)

    @property
    def kkt_list(self) -> list[schemas.KktList]:
        return service.request_list_kkt(self.auth_token)

    @property
    def kkt_folders(self) -> list[schemas.Folder]:
        return service.request_kkt_folders(self.auth_token)

    def kkt_folder(self, group_id: str) -> list[schemas.Folder]:
        return service.request_kkt_folders(self.auth_token, group_id=group_id)
