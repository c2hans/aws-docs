---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-app-setup.html
---

# MLflow App Setup
<a name="mlflow-app-setup"></a>

An [MLflow App](https://mlflow.org/docs/latest/tracking.html#mlflow-tracking-server-optional) is a stand-alone HTTP server that serves multiple REST API endpoints for tracking runs and experiments. An MLflow App is required to begin tracking your machine learning (ML) experiments with SageMaker AI and MLflow. You can create an MLflow App through the Studio UI, or through the AWS CLI for more granular security customization.

You must have the correct IAM permissions configured to create an MLflow App.

MLflow Apps are the latest managed MLflow offering on SageMaker and should be preferred over existing MLflow Tracking Servers. MLflow Apps offer additional features such as faster startup time, cross-account sharing, integrations with other SageMaker features, and other features beyond the existing MLflow Tracking Servers.

**Topics**
+ [MLflow App Setup Prequisites](mlflow-app-setup-prerequisites.md)
+ [Create MLflow App](mlflow-app-setup-create-app.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
