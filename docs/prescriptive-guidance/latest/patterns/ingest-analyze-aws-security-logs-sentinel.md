---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/ingest-analyze-aws-security-logs-sentinel.html
---

# Ingest and analyze AWS security logs in Microsoft Sentinel
<a name="ingest-analyze-aws-security-logs-sentinel"></a>

*Ivan Girardi and Sebastian Wenzel, Amazon Web Services*

## Summary
<a name="ingest-analyze-aws-security-logs-sentinel-summary"></a>

This pattern describes how to automate the ingestion of AWS security logs, such as AWS CloudTrail logs, Amazon CloudWatch Logs data, Amazon VPC Flow Logs data, and Amazon GuardDuty findings, into Microsoft Sentinel. If your organization uses Microsoft Sentinel as a security information and event management (SIEM) system, this helps you centrally monitor and analyze logs in order to detect security-related events. As soon as the logs are available, they are automatically delivered to an Amazon Simple Storage Service (Amazon S3) bucket in less than 5 minutes. This can help you quickly detect security events in your AWS environment.

Microsoft Sentinel ingests CloudTrail logs in a tabular format that includes the original timestamp for when the event was recorded. The structure of the ingested logs enables query capabilities by using [Kusto Query Language](https://learn.microsoft.com/en-us/azure/sentinel/kusto-overview) in Microsoft Sentinel.

The pattern deploys a monitoring and alerting solution that detects ingestion failures in less than 1 minute. It also includes a notification system that the external SIEM can monitor. You use AWS CloudFormation to deploy the required resources in the logging account.

**Target audience**

This pattern is recommended for users who have experience with AWS Control Tower, AWS Organizations, CloudFormation, AWS Identity and Access Management (IAM), and AWS Key Management Service (AWS KMS).

## Prerequisites and limitations
<a name="ingest-analyze-aws-security-logs-sentinel-prereqs"></a>

**Prerequisites**

The following are the prerequisites for deploying this solution:
+ Active AWS accounts that are managed as an organization in AWS Organizations and are part of an AWS Control Tower landing zone. The organization should include a dedicated account for logging. For instructions, see [Creating and configuring an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html) in the AWS Organizations documentation.
+ A CloudTrail trail that logs events for the entire organization and stores logs in an Amazon S3 bucket in the logging account. For instructions, see [Creating a trail for an organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html).
+ In the logging account, permissions to assume an existing IAM role that has the following permissions:
  + Deploy the resources defined in the provided CloudFormation template.
  + Deploy the provided CloudFormation template.
  + Modify the AWS KMS key policy if the logs are encrypted with a customer managed key.
+ AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).
+ A Microsoft Azure account with a subscription to use Microsoft Sentinel.
+ Enable and set up Microsoft Sentinel. For instructions, see [Enable Microsoft Sentinel and initial features and content](https://learn.microsoft.com/en-us/azure/sentinel/enable-sentinel-features-content) in the Microsoft Sentinel documentation.
+ Meet the prerequisites for setting up the Microsoft Sentinel S3 connector.

**Limitations**
+ This solution forwards the security logs from an Amazon S3 bucket in the logging account to Microsoft Sentinel. Instructions for how to send the logs to Amazon S3 are not explicitly provided.
+ This pattern provides instructions for deployment in an AWS Control Tower landing zone. However, use of AWS Control Tower is not required.
+ This solution is compatible with an environment where the Amazon S3 logging bucket is restricted with [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), such as [Disallow Changes to Bucket Policy for AWS Control Tower Created Amazon S3 Buckets in Log Archive](https://docs.aws.amazon.com/controltower/latest/controlreference/mandatory-controls.html#disallow-policy-changes-s3-buckets-created).
+ This pattern provides instructions for forwarding CloudTrail logs, but you can adapt this solution to send other logs that Microsoft Sentinel supports, such as logs from CloudWatch Logs, Amazon VPC Flow Logs, and GuardDuty.
+ The instructions use the AWS CLI to deploy the CloudFormation template, but you could also use the AWS Management Console. For instructions, see [Using the AWS CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-using-console.html). If you use the console to deploy the stack, deploy the stack in the same AWS Region as the logging bucket.
+ This solution deploys an Amazon Simple Queue Service (Amazon SQS) queue to deliver Amazon S3 notifications. The queue contains messages with the paths of objects uploaded in the Amazon S3 bucket, not actual data. The queue uses SSE-SQS encryption to help protect the content of the messages. If you want to encrypt the SQS queue with SSE-KMS, you can use a customer managed KMS key. For more information, see [Encryption at rest in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html).

## Architecture
<a name="ingest-analyze-aws-security-logs-sentinel-architecture"></a>

This section provides a high-level overview of the architecture that the sample code establishes. The following diagram shows the resources deployed in the logging account in order to ingest logs from an existing Amazon S3 bucket into Microsoft Sentinel.

![Microsoft Sentinel using an Amazon SNS queue to ingest logs from an S3 bucket](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e8438b44-6bce-4863-8657-1d0a843ffb6f/images/38108d9d-88ad-4306-8ad2-01b66a6bf00f.png)

The architecture diagram shows the following resource interactions:

1. In the logging account, Microsoft Sentinel assumes an IAM role through OpenID Connect (OIDC) to access logs in a specific Amazon S3 bucket and Amazon SQS queue.

1. Amazon Simple Notification Service (Amazon SNS) and Amazon S3 use AWS KMS for encryption.

1. Amazon S3 sends notification messages to the Amazon SQS queue whenever it receives new logs.

1. Microsoft Sentinel checks Amazon SQS for new messages. The Amazon SQS queue uses SSE-SQS encryption. The message retention period is set to 14 days.

1. Microsoft Sentinel pulls messages from the Amazon SQS queue. The messages contain the path of the uploaded Amazon S3 objects. Microsoft Sentinel ingests those objects from the Amazon S3 bucket into the Microsoft Azure account.

1. A CloudWatch alarm monitors the Amazon SQS queue. If messages are not received and deleted from the Amazon SQS queue within 5 minutes, then it initiates an Amazon SNS notification that sends an email.

AWS Control Tower helps you set up the foundational organization unit (OU) structure and centralizes CloudTrail logs in the logging account. It also implements mandatory SCPs to protect the logging bucket.

We have provided the target architecture in an AWS Control Tower landing zone, but this is not strictly required. In this diagram, the resources in the management account reflect an AWS Control Tower deployment and a CloudTrail trail that logs events for the entire organization.

This pattern focuses on the deployment of resources in the logging account. If the logs stored in Amazon S3 in your AWS Control Tower landing zone are encrypted with a customer managed KMS key, then you must update the key policy to allow Microsoft Sentinel to decrypt the logs. In an AWS Control Tower landing zone, you manage the key policy from the management account, which is where the key was created.

## Tools
<a name="ingest-analyze-aws-security-logs-sentinel-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) helps you monitor the metrics of your AWS resources and the applications you run on AWS in real time.
+ [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) helps you set up and govern an AWS multi-account environment, following best practices.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that helps you consolidate multiple AWS accounts into an organization that you create and centrally manage.
+ [Amazon Simple Queue Service (Amazon SQS)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) provides a secure, durable, and available hosted queue that helps you integrate and decouple distributed software systems and components.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Other tools**
+ [Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/overview) is a cloud-native SIEM system that provides security orchestration, automation, and response (SOAR).

**Code repository**

The code for this pattern is available in the GitHub [Ingest and analyze AWS security logs in Microsoft Sentinel](https://github.com/aws-samples/ingest-and-analyze-aws-security-logs-in-microsoft-sentinel) repository.

## Best practices
<a name="ingest-analyze-aws-security-logs-sentinel-best-practices"></a>
+ Follow the [principle of least-privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) (IAM documentation).
+ Follow the [Best practices for AWS Control Tower administrators](https://docs.aws.amazon.com/controltower/latest/userguide/best-practices.html) (AWS Control Tower documentation).
+ Follow the [AWS CloudFormation best practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html) (CloudFormation documentation).
+ Use code analysis tools, such as [cfn\_nag](https://github.com/stelligent/cfn_nag), to scan the generated CloudFormation templates. The cfn\_nag tool identifies potential security issues in CloudFormation templates by searching for patterns.

## Epics
<a name="ingest-analyze-aws-security-logs-sentinel-epics"></a>

### Connect Microsoft Sentinel to Amazon S3
<a name="connect-microsoft-sentinel-to-s3"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare the Microsoft Sentinel S3 connector. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/ingest-analyze-aws-security-logs-sentinel.html) | DevOps engineer, General AWS |

### Deploy the CloudFormation stack
<a name="deploy-the-cfnshort-stack"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | In a bash shell, enter the following command. This clones the [Ingest and analyze AWS Security Logs in Microsoft Sentinel](https://github.com/aws-samples/ingest-and-analyze-aws-security-logs-in-microsoft-sentinel) repository.<br />`git clone https://github.com/aws-samples/ingest-and-analyze-aws-security-logs-in-microsoft-sentinel.git` | DevOps engineer, General AWS |
| Assume the IAM role in the logging account. | In the logging account, assume the IAM role that has permissions to deploy the CloudFormation stack. For more information about assuming an IAM role in the AWS CLI, see [Use an IAM role in the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-role.html). | DevOps engineer, General AWS |
| Deploy the stack. | To deploy the CloudFormation stack enter the following command, where:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/ingest-analyze-aws-security-logs-sentinel.html)<pre>aws cloudformation deploy --stack-name cloudtrail-sentinel-integration \<br />    --no-fail-on-empty-changeset \<br />    --template-file template.yml \<br />    --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND \<br />    --parameter-overrides \<br />    ControlTowerS3BucketName="<Bucket name>" \<br />    AzureWorkspaceID="<Sentinel external ID>" \<br />    EmailAddress="<Email address>" \<br />    KMSKeyArn="<Customer managed key ARN>" \<br />    Suffix="<Suffix to avoid name conflicts>" \<br />    OIDCProviderArn="<ARN for the OIDC provider>"</pre> | DevOps engineer, General AWS |
| Copy outputs. | From the output of the CloudFormation stack, copy the values for `SentinelRoleArn` and `SentinelSQS`. You use these values later to complete the configuration in Microsoft Sentinel. | DevOps engineer, General AWS |
| Modify the key policy. | If you aren't using a customer managed KMS key to encrypt the logs in the Amazon S3 bucket, you can skip this step.<br />If the logs are encrypted with a customer managed KMS key, modify the key policy to grant Microsoft Sentinel permission to decrypt the logs. The following is an example key policy. This example policy allows cross-account access if the KMS key is in another AWS account.<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Id": "key-policy",<br />    "Statement": [<br />        ...<br />        {<br />            "Sid": "Grant access to decrypt",<br />            "Effect": "Allow",<br />            "Principal": {<br />                "AWS": "<SentinelRoleArn>"<br />            },<br />            "Action": "kms:Decrypt",<br />            "Resource": "<KeyArn>"<br />        }<br />    ]<br />}</pre> | DevOps engineer, General AWS |

### Configure the connector in Microsoft Sentinel
<a name="configure-the-connector-in-microsoft-sentinel"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Complete the configuration in Microsoft Sentinel. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/ingest-analyze-aws-security-logs-sentinel.html) | DevOps engineer |
| Send Amazon S3 event notifications to Amazon SQS. | Follow the instructions in [Enabling and configuring event notifications using the Amazon S3 console](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html) to configure the Amazon S3 logging bucket to send event notifications to the Amazon SQS queue. If CloudTrail has been configured for the whole organization, logs in the this bucket have the prefix `<OrgID>/AWSLogs/<OrgID>/`, where `<OrgID>` is the organization ID. For more information, see [Viewing details about your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_details.html). | DevOps engineer, General AWS |
| Confirm that the logs are ingested. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/ingest-analyze-aws-security-logs-sentinel.html) | DevOps engineer |

### Validate the solution
<a name="validate-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Compare CloudWatch and Sentinel logs. | In the default configuration of AWS Control Tower, CloudTrail logs are sent to Amazon CloudWatch and stored in the AWS Control Tower management account. For more information, see [Logging and monitoring in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/logging-and-monitoring.html). Use the following steps to confirm that that logs are automatically ingested into Microsoft Sentinel:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/ingest-analyze-aws-security-logs-sentinel.html) | DevOps engineer, General AWS |

## Related resources
<a name="ingest-analyze-aws-security-logs-sentinel-resources"></a>

**AWS documentation and resources**
+ [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/) (AWS CLI documentation)
+ [Optionally configure AWS KMS keys](https://docs.aws.amazon.com/controltower/latest/userguide/configure-kms-keys.html) (AWS Control Tower documentation)
+ [Encryption at rest in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html) (Amazon SQS documentation)
+ [How do I keep mailing list recipients from unsubscribing everyone on the list from my Amazon SNS topic emails?](https://repost.aws/knowledge-center/prevent-unsubscribe-all-sns-topic) (AWS Knowledge Center)

**Microsoft documentation**
+ [Connect Microsoft Sentinel to Amazon Web Services to ingest AWS service log data](https://learn.microsoft.com/en-us/azure/sentinel/connect-aws?tabs=s3)
+ [Kusto Query Language in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/kusto-overview)
