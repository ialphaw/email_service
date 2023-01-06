from core.settings.app import AppSettings

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def sendgrid_mail_request(
    to_email: str,
    body: str,
    subject: str = "",
):
    """This function will send a mail request to Sendgrid service"""

    settings = AppSettings()
    message = Mail(
        from_email=settings.sendgrid_from_mail,
        to_emails=to_email,
        subject=subject,
        html_content=body,
    )
    try:
        sg = SendGridAPIClient(settings.sendgrid_api_key.get_secret_value())
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        raise Exception(e)
