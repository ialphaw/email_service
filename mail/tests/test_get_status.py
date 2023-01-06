import json
from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


@patch("mail.tasks.mail_request")
def test_task_status(mock_mail_request):
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

    response = client.get(f"api/mail/{task_id}/get_status")
    content = response.json()
    assert content == {
        "task_id": task_id,
        "task_status": "PENDING",
        "task_result": None,
    }
