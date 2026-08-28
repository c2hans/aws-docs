---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-steps-integration.html
---

# Add integration
<a name="build-and-manage-steps-integration"></a>

MLflow integration allows you to use MLflow with pipelines to select a tracking server or serverless application, choose an experiment, and log metrics.

## Key concepts
<a name="add-integration-key-concepts"></a>

**Default app creation** - A default MLflow application will be created when you enter the pipeline visual editor.

**Integrations panel** - A new integrations panel includes MLflow, which you can select and configure.

**Update app and experiment** - The option to override selected application and experiment during the pipeline execution.

## How it works
<a name="add-integration-how-it-works"></a>
+ Go to **Pipeline Visual Editor**
+ Choose **Integration** on the toolbar
+ Choose **MLflow**
+ Configure the MLflow app and experiment

## Example screenshots
<a name="add-integration-example-screenshots"></a>

Integrations side panel

![The to do description.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/screenshot-pipeline-1.png)

MLflow configuration

![The to do description.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/screenshot-pipeline-2.png)

How to override experiment during pipeline execution

![The to do description.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/screenshot-pipeline-3.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
