---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/security-1.html
---

# Security
<a name="security-1"></a>

 When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit [AWS Cloud Security](https://aws.amazon.com/security/).

## Amazon DynamoDB
<a name="amazon-dynamodb"></a>

 All user data stored in DynamoDB is encrypted at rest using encryption keys stored in [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS). We recommend enforcing [AWS managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt) because you have permission to [audit their use](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html) in AWS CloudTrail logs. Refer to [Managing encrypted tables in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/encryption.tutorial.html) for more information.

Consider enabling DynamoDB Data Plane Events for CloudTrail logging to gain insights into the data operations in DynamoDB tables, according to your use cases and your regulatory and compliance requirements. Refer to [Logging DynamoDB operations by using AWS CloudTrail](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/logging-using-cloudtrail.html) for more information. Additionally, consider implementing [AWS Config](https://aws.amazon.com/config/) to actively monitor DynamoDB configuration changes

## CloudWatch Logs
<a name="cloudwatch-logs"></a>

 We recommend [changing the retention period](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SettingLogRetention) of your [CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) according to your use cases and your regulatory and compliance requirements.

## IAM roles
<a name="iam-roles"></a>

 IAM roles allow you to assign granular access policies and permissions to services and users on the AWS Cloud. This Guidance creates IAM roles that grant the Guidance's resources permission to access the Amazon Glacier vault, write logs, and create EventBridge targets.
