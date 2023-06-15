from datetime import datetime

from pydantic import BaseModel, Field


class Auth(BaseModel):
    login: str = Field(alias='Login')
    password: str = Field(alias='Password')


class AuthToken(BaseModel):
    auth_token: str = Field(alias='AuthToken', description='Authorization key')
    expiration_date_utc: datetime | None = Field(
        alias='ExpirationDateUtc',
        description='Date and time of validity of the authentication key'
    )
