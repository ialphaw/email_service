from fastapi import APIRouter
from fastapi.responses import JSONResponse

from mail.schemas import SendMail
from core.tasks import mail_request

from celery.result import AsyncResult


router = APIRouter()


@router.post("/send_email", name="email:send_email")
def send_email(send_email_body: SendMail):
    """This endpoint will trigger the send mails"""

    task = mail_request.delay(send_email_body.to_email, body="Hello World")
    return {"task_id": task.id}


@router.get("/{task_id}/get_status")
def get_status(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result,
    }
    return JSONResponse(result)
