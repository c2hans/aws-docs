---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender-instance-recommendation.html
---

# Inference recommendations
<a name="inference-recommender-instance-recommendation"></a>

Inference recommendation jobs run a set of load tests on recommended instance types or a serverless endpoint. Inference recommendation jobs use performance metrics that are based on load tests using the sample data you provided during model version registration.

**Note**
Before you create an Inference Recommender recommendation job, make sure you have satisfied the [Prerequisites for using Amazon SageMaker Inference Recommender](inference-recommender-prerequisites.md).

The following demonstrates how to use Amazon SageMaker Inference Recommender to create an inference recommendation based on your model type using the AWS SDK for Python (Boto3), AWS CLI, and Amazon SageMaker Studio Classic, and the SageMaker AI console

**Topics**
+ [Create an inference recommendation](instance-recommendation-create.md)
+ [Get your inference recommendation job results](instance-recommendation-results.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
