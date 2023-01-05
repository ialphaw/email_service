import json
from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


@patch("core.tasks.mail_request")
def test_send_email(client):
    response = client.post(
        "/api/mail/send_email",
        data=json.dumps(
            {
                "to_email": "test@test.com",
                "body": "Hello World",
                "subject": "Test",
            },
        ),
    )
    content = response.json()
    task_id = content["task_id"]
    assert task_id
