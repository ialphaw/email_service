from core.config import AppSettings

import requests


def mailgun_mail_request(to_email, body, subject):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox695eb9f7e9ec4b4394a9e9225d256176.mailgun.org/messages",
        auth=("api", AppSettings().mailgun_api_key.get_secret_value()),
        data={
            "from": "Mailgun Sandbox <postmaster@sandbox695eb9f7e9ec4b4394a9e9225d256176.mailgun.org>",
            "to": to_email,
            "subject": subject,
            "text": body,
        },
    )
