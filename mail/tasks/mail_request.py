from utils import sendgrid_mail_request, mailgun_mail_request

from celery import shared_task


@shared_task(
    name="mail:mail_request",
)
def mail_request(
    to_email: str,
    body: str,
    subject: str = "",
):
    """This function will send the request to the mail servers"""
    
    for t in range(6):
        try:
            sendgrid_mail_request(to_email, body, subject)
            return True
        except Exception as e:
            print(e)
    for t in range(6):
        try:
            mailgun_mail_request(to_email, body, subject)
        except Exception as e:
            print(e)
            return True

    return False
