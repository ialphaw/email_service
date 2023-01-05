from pydantic import BaseModel


class SendMail(BaseModel):
    to_email: str
    subject: str = ""
