import os
from functools import lru_cache


class BaseConfig:
    CELERY_BROKER_URL: str = os.environ.get(
        "CELERY_BROKER_URL", "redis://localhost:6379"
    )
    CELERY_RESULT_BACKEND: str = os.environ.get(
        "CELERY_RESULT_BACKEND", "redis://localhost:6379"
    )


@lru_cache()
def get_settings():
    config_cls = BaseConfig
    return config_cls()


settings = get_settings()
