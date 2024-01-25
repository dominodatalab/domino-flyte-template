import os

# Should be env var - see https://github.com/cerebrotech/domino/pull/39055/files
def get_host(host = None):
    if host is not None:
        return host
    host = os.getenv("FLYTE_PLATFORM_CONSOLE_ENDPOINT")
    return host


# Alternative to os.getenv - pass in via CLI
def get_project(project = None):
    if project is not None:
        return project
    owner = os.getenv("DOMINO_PROJECT_OWNER")
    name = os.getenv("DOMINO_PROJECT_NAME")
    return f"{owner}/{name}"


# Idea: programmatically fill in the api key
# https://docs.dominodatalab.com/en/latest/api_guide/d982cc/get-api-key/
def get_api_key(api_key = None):
    if api_key is not None:
        return api_key
    raise Exception("Api key is missing. Follow instructions at https://docs.dominodatalab.com/en/latest/api_guide/d982cc/get-api-key/")
