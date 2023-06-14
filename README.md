# OFD.RU Client

This is unofficial client for [OFD.RU](https://ofd.ru/) API ["Receipts and cash registers"](https://ofd.ru/razrabotchikam/cheki-i-kkt#авторизация_через_authtoken).

## Requirements

- Python 3.10+
- [httpx](https://github.com/encode/httpx) - HTTP client library for Python 3.
- [Pydantic](https://github.com/pydantic/pydantic) - data validation using Python type hints.

## Installation

```
$ git clone https://github.com/kiselyovda/ofdclient
$ cd ofdclient
$ pip install -r requirements.txt
```

## Example

```python
import os

from ofd import client


login = os.environ.get('LOGIN')
password = os.environ.get('PASSWORD')

client = client.Client(login=login, password=password)
```

Or if you have `AuthToken` from request `POST https://ofd.ru/api/Authorization/CreateAuthToken`

Request body
```json
{
  "Login": "12345",
  "Password": "56789"
}
```

An example of a successful response to a request:
```json
{
    "AuthToken": "f3accdfda7574736ba94a78d00e974f4",
    "ExpirationDateUtc": "2017-01-24T14:44:21"
}
```

```python
import os

from ofd import client


auth_token = os.environ.get('AUTH_TOKEN')

client = client.Client(auth_token)
```
After that you have access to the following points of [API interface](https://ofd.ru/razrabotchikam/cheki-i-kkt#авторизация_через_authtoken) using Python:


You have access to the following points:

### 2
*future releases*

### 3
1. *future releases*
2. **Request for a list of cash registers** ✅