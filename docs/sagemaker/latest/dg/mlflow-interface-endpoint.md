---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-interface-endpoint.html
---

# Connecting to an MLflow tracking server through an Interface VPC Endpoint
<a name="mlflow-interface-endpoint"></a>

The MLflow tracking server runs in an Amazon Virtual Private Cloud managed by Amazon SageMaker AI. You can connect to an MLflow tracking server from an endpoint in your own VPC. Your requests to the tracking server are not exposed to the public internet. For more information about connecting your VPC to SageMaker AI, see [Connect to SageMaker AI Within your VPC](interface-vpc-endpoint.md).

**Topics**
+ [Create a VPC Endpoint](mlflow-interface-endpoint-create.md)
+ [Create a VPC Endpoint Policy for SageMaker AI MLflow](mlflow-private-link-policy.md)
+ [Allow Access only from within your VPC](mlflow-private-link-restrict.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
