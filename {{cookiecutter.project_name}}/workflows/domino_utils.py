import os

def get_host(host = None):
    if host is not None:
        return host
    host = os.getenv("FLYTE_PLATFORM_CONSOLE_ENDPOINT")
    return host


def get_project(project = None):
    if project is not None:
        return project
    owner = os.getenv("DOMINO_PROJECT_OWNER")
    name = os.getenv("DOMINO_PROJECT_NAME")
    return f"{owner}/{name}"


# TODO: see if possible to programmatically fill in api key
# https://docs.dominodatalab.com/en/latest/api_guide/d982cc/get-api-key/
def get_api_key(api_key = None):
    if api_key is not None:
        return api_key
    raise Exception("Api key is missing. Follow instructions at https://docs.dominodatalab.com/en/latest/api_guide/d982cc/get-api-key/")
