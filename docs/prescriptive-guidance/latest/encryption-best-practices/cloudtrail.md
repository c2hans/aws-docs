---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/cloudtrail.html
---

# AWS CloudTrail
<a name="cloudtrail"></a>

[AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) helps you audit the governance, compliance, and operational and risk of your AWS account.

Consider the following encryption best practices for this service:
+ CloudTrail logs should be encrypted using a customer managed AWS KMS key. Choose a KMS key that is in the same region as the S3 bucket that receives your log files. For more information, see [Updating a trail to use your KMS key](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create-kms-key-policy-for-cloudtrail-update-trail.html).
+ As an additional security layer, enable log file validation for trails. This helps you determine whether a log file was modified, deleted, or unchanged after CloudTrail delivered it. For instructions, see [Enabling log file integrity validation for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-enabling.html).
+ Use interface VPC endpoints to enable CloudTrail to communicate with resources in other VPCs without traversing the public internet. For more information, see [Using AWS CloudTrail with interface VPC endpoints](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-and-interface-VPC.html).
+ Add an `aws:SourceArn` condition key to the KMS key policy to ensure that CloudTrail uses the KMS key only for a specific trail or trails. For more information, see [Configure AWS KMS key policies for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create-kms-key-policy-for-cloudtrail.html).
+ In AWS Config, implement the [cloud-trail-encryption-enabled](https://docs.aws.amazon.com/config/latest/developerguide/cloud-trail-encryption-enabled.html) AWS managed rule to validate and enforce log file encryption.
+ If CloudTrail is configured to send notifications through Amazon Simple Notification Service (Amazon SNS) topics, add an `aws:SourceArn` (or optionally `aws:SourceAccount`) condition key to the CloudTrail policy statement to prevent unauthorized account access to the SNS topic. For more information, see [Amazon SNS topic policy for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-permissions-for-sns-notifications.html).
+ If you are using AWS Organizations, create an organization trail that logs all events for the AWS accounts in that organization. This includes the management account and all member accounts in the organization. For more information, see [Creating a trail for an organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html).
+ Create a trail that [applies to all AWS Regions](https://aws.amazon.com/blogs/mt/aws-cloudtrail-best-practices/) where you store corporate data, to record AWS account activity in those Regions. When AWS launches a new Region, CloudTrail automatically includes the new Region and logs events in that Region.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
