---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/training-plan-extension-using-api-cli-sdk.html
---

# Extend a training plan using the SageMaker API or AWS CLI
<a name="training-plan-extension-using-api-cli-sdk"></a>

SageMaker training plans support extending training plans programmatically through its API. You can interact with the training plans API using the AWS CLI or SageMaker SDKs.

The training plan extension involves the following API actions:
+ **`SearchTrainingPlanOfferings`:** Search for available extension offerings by specifying your training plan ARN and desired extension duration. The API returns extension offerings in the `TrainingPlanExtensionOfferings` field.
+ **`ExtendTrainingPlan`:** Purchase a specific extension offering to extend your training plan by providing the `TrainingPlanExtensionOfferingId`. This reserves the additional compute capacity and updates your training plan's end date.
+ **`DescribeTrainingPlanExtensionHistory`:** View the complete extension history for a training plan, including all past extensions with their status, dates, and payment information.

**Topics**
+ [Search for extension offerings](search-extension-offerings-api-cli-sdk.md)
+ [Purchase an extension](extend-training-plan-api-cli-sdk.md)
+ [View extension history](describe-extension-history-api-cli-sdk.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
