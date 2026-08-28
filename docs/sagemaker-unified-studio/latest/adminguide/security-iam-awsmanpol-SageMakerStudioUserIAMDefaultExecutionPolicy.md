---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioUserIAMDefaultExecutionPolicy.html
---

# AWS policy: SageMakerStudioUserIAMDefaultExecutionPolicy
<a name="security-iam-awsmanpol-SageMakerStudioUserIAMDefaultExecutionPolicy"></a>

This is the default execution policy for using IAM roles with Amazon SageMaker Unified Studio. This policy grants access to users to access resources. This does not grant access to data resources.
+ Amazon DataZone permissions are required to access DataZone resources such as Project and Asset.
+ AWS Identity and Access Management permissions are required to list IAM roles, create service-linked roles, and pass roles when provisioning resources.
+ AWS STS permissions are required to assume other roles for accessing resources in cross-account.
+ Amazon S3 permissions are required to list S3 buckets and allow cross-account object read.
+ AWS Lake Formation permissions are required to describe AWS Lake Formation resources.
+ Amazon Redshift Query Editor permissions are required to interact with the query editor in Amazon SageMaker Unified Studio.
+ Amazon Redshift Data API API permissions are required to run SQL statements using the Data API.
+ Amazon Redshift Serverless permissions are required for discovery of Redshift Serverless.
+ Amazon Redshift permissions are required for discovery of Redshift clusters.
+ Amazon Bedrock permissions are required to interact with Bedrock APIs in Amazon SageMaker Unified Studio.
+ Amazon EventBridge Scheduler permissions are required to interact with one-click scheduling in Amazon SageMaker Unified Studio.
+ Amazon DynamoDB permissions are required to enable federated connections to external data.
+ Amazon Athena permissions are required to interact with Query Editor in Amazon SageMaker Unified Studio.
+ AWS Secrets Manager permissions are required to access secrets for connections.
+ Amazon CodeWhisperer permissions are required to generate code recommendation.
+ Amazon ECR permissions are required to run SageMaker training jobs.
+ Amazon MWAA permissions are required to manage and schedule workflows.
+ AWS KMS permissions are required to support customer managed key. Resources provisioned by Amazon SageMaker Unified Studio can be encrypted with your customer managed key.

To view the permissions for this policy, see [SageMakerStudioUserIAMDefaultExecutionPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/SageMakerStudioUserIAMDefaultExecutionPolicy.html) in the *AWS Managed Policy Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
