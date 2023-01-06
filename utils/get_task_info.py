from celery.result import AsyncResult


def get_task_info(task_id):
    """This function will return info of the related task"""

    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result,
    }
    return result
