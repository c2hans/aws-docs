---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-create-tracking-server.html
---

# MLflow Tracking Servers
<a name="mlflow-create-tracking-server"></a>

An [MLflow Tracking Server](https://mlflow.org/docs/latest/tracking.html#mlflow-tracking-server-optional) is a stand-alone HTTP server that serves multiple REST API endpoints for tracking runs and experiments. A tracking server is required to begin tracking your machine learning (ML) experiments with SageMaker AI and MLflow. You can create a tracking server through the Studio UI, or through the AWS CLI for more granular security customization.

You must have the correct IAM permissions configured to create an MLflow Tracking Server.

**Topics**
+ [Set up IAM permissions for MLflow](mlflow-create-tracking-server-iam.md)
+ [Create a tracking server using Studio](mlflow-create-tracking-server-studio.md)
+ [Create a tracking server using the AWS CLI](mlflow-create-tracking-server-cli.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
