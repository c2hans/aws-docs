---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioBedrockFunctionExecutionRolePolicy.html
---

# AWS policy: SageMakerStudioBedrockFunctionExecutionRolePolicy
<a name="security-iam-awsmanpol-SageMakerStudioBedrockFunctionExecutionRolePolicy"></a>

This policy allows AWS Lambda to access an Amazon Bedrock function component's configuration in Amazon SageMaker Unified Studio.

This is the main policy for the Amazon Bedrock IDE function execution role. This role is part of the AmazonBedrockFunction environment blueprint.

This policy grants the AWS Lambda service access to an Amazon Bedrock IDE function’s configuration, including AWS Secrets Manager secrets and an AWS KMS key.
+ AWS Secrets Manager permissions are required for AWS Lambda to access the Amazon Bedrock IDE function’s API keys while fulfilling API requests.
+ AWS KMS permissions are required to access AWS Secrets Manager secrets encrypted with a customer managed key.

This policy allows the AWS Lambda service to access specific resources tagged with the same project ID as the service role. This tag restriction effectively only permits access to resources in the same project. By default, project users are not allowed to change service role tags.

To view the permissions for this policy, see [SageMakerStudioBedrockFunctionExecutionRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/SageMakerStudioBedrockFunctionExecutionRolePolicy.html) in the *AWS Managed Policy Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
