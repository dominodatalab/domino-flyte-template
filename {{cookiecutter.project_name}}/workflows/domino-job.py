import time
import requests
from flytekit import task, workflow

def start_job(
    command: str,
    host = "https://pipe-research.train-sandbox.domino.tech",
    project: str = "integration-test/flyte-school",
    api_key: str = "192e5eb8d2858f468ae1e366aa3a63a26a8f65d5e8d0c1beecf7decb5c09e2ac",
) -> str:

    start_job_url = f"{host}/v1/projects/{project}/runs"

    request = {
        "command": [command],
        "title": "Flyte job",
        "isDirect": False,
    }

    request_session = requests.Session()
    auth = requests.auth.HTTPBasicAuth("", api_key)

    response = request_session.post(start_job_url, auth=auth, json=request).json()
    run_id = response["runId"]
    get_status_url = f"{host}/v1/projects/{project}/runs/{run_id}"

    poll_start = time.time()
    cur_retry_count = 0

    while True:
        try:
            response = request_session.get(get_status_url, auth=auth).json()
            run_status = response["status"]
            print(f"Status response: {run_status}")
            if run_status in ["Stopped", "Succeeded", "Failed", "Error"]:
                return run_status

        except Exception as e:
            if cur_retry_count > 5:
                raise e
            else:
                cur_retry_count += 1
                print(f"Request for run status failed (attempt {cur_retry_count}), retrying in 5 seconds")
                time.sleep(5)

        elapsed_time = time.time() - poll_start
        if elapsed_time > 3000:
            raise Exception("Run exceeded max time")

        time.sleep(5)


@task
def domino_job_task_http(command: str) -> str:
    return start_job(command=command)


@workflow
def domino_job_workflow(command: str) -> str:
    return domino_job_task_http(command=command)
    

if __name__ == "__main__":
    domino_job_workflow(command="mlflow-job.py")