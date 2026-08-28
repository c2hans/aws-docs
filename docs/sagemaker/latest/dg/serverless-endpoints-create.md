---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-create.html
---

# Serverless endpoint creation
<a name="serverless-endpoints-create"></a>

**Important**
Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker resources must also grant permissions to add tags to those resources. The permission to add tags to resources is required because Studio and Studio Classic automatically tag any resources they create. If an IAM policy allows Studio and Studio Classic to create resources but does not allow tagging, "AccessDenied" errors can occur when trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions).
[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md) that give permissions to create SageMaker resources already include permissions to add tags while creating those resources.

To create a serverless endpoint, you can use the Amazon SageMaker AI console, the APIs, or the AWS CLI. You can create a serverless endpoint using a similar process as a [real-time endpoint](realtime-endpoints.md).

**Topics**
+ [Create a model](serverless-endpoints-create-model.md)
+ [Create an endpoint configuration](serverless-endpoints-create-config.md)
+ [Create an endpoint](serverless-endpoints-create-endpoint.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
