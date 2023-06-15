from datetime import datetime

import pydantic as pd


class Auth(pd.BaseModel):
    login: str = pd.Field(alias='Login')
    password: str = pd.Field(alias='Password')


class AuthToken(pd.BaseModel):
    auth_token: str = pd.Field(alias='AuthToken', description='Authorization key')
    expiration_date_utc: datetime | None = pd.Field(
        alias='ExpirationDateUtc',
        description='Date and time of validity of the authentication key'
    )
