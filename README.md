# python-sample 
This is Visual Studio Team Services CI example for python project.

This project includes example with function sum_two that sums two arguments.
It also icludes several unittests and flake8 style check configuration.

The CI should:
1. Install requirements
2. Run flake8 on the project to check for style errors
3. Run unittests stored in tests directory.

CI was configured to run on python 2.7.

If you want to change python version that is being used, change following versionSpec in .vsts-ci.yml

## Setup
In order to use this example you need to create organisation in VSTS

Then you need to enable Preview Feature for YAML.
It would not be visible for your user, you need to switch to your organisation.

Then enable Build YAML definitions.

Go to builds create new one and choose YAML template.

## Known issues

Following line defiens which queue will be used.
```
queue: 'Hosted Linux Preview'
```
That queue agent might not exist for you (in documentation there was `Hosted Linux` wchich was not available)

You can check queue agents that are available in the settings.

## Based on
1. [Build a repository with YAML](https://docs.microsoft.com/en-us/vsts/pipelines/get-started-yaml)
2. [Python Pipeline example](https://docs.microsoft.com/en-us/vsts/pipelines/languages/python)
3. [YAML build not visible](https://github.com/MicrosoftDocs/vsts-docs/issues/996)
