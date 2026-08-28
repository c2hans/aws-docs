---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/aws-identity-and-access-management-iam.html
---

# AWS Identity and Access Management (IAM)
<a name="aws-identity-and-access-management-iam"></a>

## Managing access in the AWS Cloud
<a name="managing-access-in-the-aws-cloud"></a>

[AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) is a service that allows customers to control who can access AWS resources and under what conditions. It enables fine-grained permission management aligned with the GDPR principle of data protection by design.

When a new [AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html) is created, a [root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html) is also created with full administrative privileges. AWS strongly recommends that the root user be used only for essential tasks, such as initial account setup or billing administration. For all other activities, customers should create [IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) or [roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) and assign only the permissions necessary to perform specific tasks. This approach aligns with the [principle of least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) and is foundational to a secure environment.

IAM supports both long-term credentials (for users) and short-term credentials (for roles). For example, customers can use IAM roles to allow an [Amazon EC2](https://aws.amazon.com/ec2/) instance to access objects in an [Amazon S3](https://aws.amazon.com/s3/) bucket or allow a [AWS Lambda function](https://aws.amazon.com/lambda/) to write logs to [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html). The same pattern applies when enabling secure access to services such as [Amazon RDS](https://aws.amazon.com/rds/), [Amazon DynamoDB](https://aws.amazon.com/dynamodb/), or [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/).

## Organizing access across accounts
<a name="organizing-access-across-accounts"></a>

Customers managing multi-account environments can use [AWS Organizations](https://aws.amazon.com/organizations/) to apply [Service Control Policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) across accounts. SCPs define broad permissions boundaries and can, for instance, restrict actions available to the root user. AWS provides [examples of SCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_example-scps.html) to help customers implement common controls.

## Detecting unintended access with IAM Access Analyzer
<a name="detecting-unintended-access-with-iam-access-analyzer"></a>

IAM includes features to help customers continuously monitor how access is granted across their environment. [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) evaluates resource policies and identifies unintended external access. It supports multiple resource types, including [Amazon S3 buckets](https://aws.amazon.com/s3/), [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/) keys, [Lambda functions](https://aws.amazon.com/lambda/), and [SQS queues](https://aws.amazon.com/sqs/).

When used with S3, IAM Access Analyzer can alert customers if a bucket is publicly accessible or shared across AWS accounts. AWS recommends enabling [Block Public Access settings](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) to prevent unintentional exposure. If access is required for a specific use case, customers should test application behavior and apply precise controls.

## Monitoring root account usage and detecting threats
<a name="monitoring-root-account-usage-and-detecting-threats"></a>

[AWS GuardDuty](https://aws.amazon.com/guardduty/) can detect when root credentials are used in ways that may signal a security concern. The system generates findings such as [Policy:IAMUser/RootCredentialUsage](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings.html) when root access is detected, enabling customers to investigate and take action.

## Refining permissions with access history
<a name="refining-permissions-with-access-history"></a>

IAM provides [last accessed information](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html), a feature that shows when IAM roles, users, or policies were last used.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
