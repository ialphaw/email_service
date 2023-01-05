from fastapi import APIRouter

from mail.views.routes import router as mail_routes

router = APIRouter()

router.include_router(mail_routes, tags=["mails"], prefix="")
