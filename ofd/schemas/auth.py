from datetime import datetime

from pydantic import BaseModel, Field

__all__ = ['Auth', 'AuthToken']


class Auth(BaseModel):
    login: str = Field(alias='Login')
    password: str = Field(alias='Password')

    class Config:
        allow_population_by_field_name = True


class AuthToken(BaseModel):
    auth_token: str = Field(alias='AuthToken', description='Authorization key')
    expiration_date_utc: datetime | None = Field(
        alias='ExpirationDateUtc',
        description='Date and time of validity of the authentication key'
    )

    class Config:
        allow_population_by_field_name = True
