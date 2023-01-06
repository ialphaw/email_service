from fastapi import APIRouter
from fastapi.responses import JSONResponse

from mail.schemas import SendMail
from mail.tasks import mail_request
from utils import get_task_info


router = APIRouter()


@router.post("/send_email", name="email:send_email")
def send_email(send_email_body: SendMail):
    """This endpoint will trigger the send mails"""

    task = mail_request.delay(send_email_body.to_email, body="Hello World")
    return {"task_id": task.id}


@router.get("/{task_id}/get_status")
def get_status(task_id):
    """This endpoint will get the datils of the related task"""

    result = get_task_info(task_id)
    return JSONResponse(result)
