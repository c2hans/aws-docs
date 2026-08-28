---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioAdminIAMConsolePolicy.html
---

# AWS policy: SageMakerStudioAdminIAMConsolePolicy
<a name="security-iam-awsmanpol-SageMakerStudioAdminIAMConsolePolicy"></a>

This policy provides initial administrative and individual setup privileges for Amazon SageMaker Unified Studio via the AWS Management Console and SDK. It grants permissions for launching Amazon SageMaker Unified Studio.
+ Amazon DataZone permissions are required to allow principals full access to all Amazon DataZone actions.
+ AWS Identity and Access Management permissions are required to allow principals to list and get IAM roles, get IAM users and pass roles when creating Amazon DataZone resources.
+ AWS Systems Manager permissions are required to manage parameters to enable Amazon Q.
+ Amazon EC2 permissions are required to describe, create, modify, and delete VPC infrastructure including VPCs, subnets, security groups, internet gateways, NAT gateways, route tables, VPC endpoints, and elastic IP addresses for Amazon SageMaker Unified Studio environments.
+ CloudFormation permissions are required to create and manage infrastructure stacks for Amazon SageMaker Unified Studio deployment.
+ Amazon S3 permissions are required to allow CloudFormation to access template files from S3 buckets, including cross-account scenarios.
+ AWS KMS permissions are required to manage encryption keys, perform encrypt/decrypt operations, and create grants for Amazon DataZone resources.

All EC2 resources must be tagged with `CreatedForUseWithSageMakerUnifiedStudio: true` for creation, modification, and deletion operations to ensure proper resource governance and lifecycle management.

To view the permissions for this policy, see [SageMakerStudioAdminIAMConsolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/SageMakerStudioAdminIAMConsolePolicy.html) in the *AWS Managed Policy Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
