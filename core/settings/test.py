import logging

from pydantic import SecretStr

from core.settings.app import AppSettings


class TestAppSettings(AppSettings):
    debug: bool = True

    title: str = "Email Service Test"

    sendgrid_api_key: SecretStr = SecretStr("test_secret")

    max_connection_count: int = 5
    min_connection_count: int = 5

    logging_level: int = logging.DEBUG
