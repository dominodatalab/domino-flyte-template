# {{ cookiecutter.project_name }}

A template for the recommended layout of a Flyte enabled repository for code written in python using [flytekit](https://docs.flyte.org/projects/flytekit/en/latest/).

## Usage

To get up and running with your Flyte project, we recommend following the
[Flyte getting started guide](https://docs.flyte.org/en/latest/getting_started.html).

1. a few notes about things to modify in the workflow and how to run the pipeline from the command line

## Notes

`pyflyte init rliu --template ~/domino-flyte-template-0.0.1`

`pyflyte init rliu --template /usr/local/share/domino-flyte-template-0.0.1`

Configure the host, project, api_key or the next step will fail.

```sh
cd rliu/workflows
pyflyte run domino_job.py domino_job_workflow --command mlflow-job.py
```