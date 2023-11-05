# Sense-U Baby Monitor Client

The `sense-u-client` package provides a Python interface to the Sense-U Baby monitor API. It allows for easy access and control over your Sense-U devices programmatically.

## Features

- Login to the Sense-U API and manage session tokens.
- List all devices associated with the account.
- Retrieve user information.
- Get base station details.
- Access children information linked to the user's account.

## Installation

To install the `sense-u-client`, you need to have Python 3.10 or higher and `poetry` for dependency management.

```bash
git clone https://github.com/apmechev/Sense-U-Client.git
cd sense-U-Client

poetry install
```

## Usage

To use the `sense-u-client`, you must first create an instance of the `SenseUClient` class. You can provide your Sense-U username and password during initialization or set them as environment variables `SENSE_U_USERNAME` and `SENSE_U_PASSWORD`.

```python
from sense_u_client.client import SenseUClient

client = SenseUClient(username='your_username', password='your_password')

client.login()

devices = client.list_devices()
print(devices)

user_info = client.get_user_info()
print(user_info)

```

## Development

### Running Tests

Tests are written using `pytest`. To run tests, you can use the following command:

```bash
poetry run pytest
```

### Contributing

Contributions to the `sense-u-client` are welcome! Please ensure that your code adheres to the project's coding standards and includes tests for new features or bug fixes.
