from unittest.mock import patch

from core.tasks import mail_request


@patch("utils.sendgrid_mail_request")
@patch("utils.mailgun_mail_request")
def test_mail_request_task(mock_sendgrid_mail_request, mock_mailgun_mail_request):
    mock_sendgrid_mail_request.side_effect = Exception("Server Down")
    res = mail_request.run("test@email.com", "Hello World", "Test")
    assert res
