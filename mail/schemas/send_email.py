from pydantic import BaseModel


class SendMail(BaseModel):
    """This schema is for send_mail API request body"""
    
    to_email: str
    subject: str = ""
