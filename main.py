from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import get_app_settings
from core.routes import router as api_router
from utils import create_celery


def get_application() -> FastAPI:
    settings = get_app_settings()

    settings.configure_logging()

    application = FastAPI(**settings.fastapi_kwargs)

    application.celery_app = create_celery()

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(api_router, prefix="/api")

    return application


app = get_application()
celery = app.celery_app
