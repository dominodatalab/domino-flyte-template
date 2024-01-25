# {{ cookiecutter.project_name }}

A template for the recommended layout of a Flyte enabled repository for Domino jobs. Based on [flytekit](https://docs.flyte.org/projects/flytekit/en/latest/).

## Usage

`pyflyte init [your-template-name] --template /usr/local/share/domino-flyte-template-0.0.1`

Docs: https://docs.dominodatalab.com/en/latest/api_guide/d982cc/get-api-key/
Configure the api_key or this will fail.
```sh
cd [your-template-name]/workflows
pyflyte run domino_job.py domino_job_workflow --command mlflow-job.py --api_key [your-api-key]
```