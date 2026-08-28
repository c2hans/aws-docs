---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enforce-automatic-tagging-of-amazon-rds-databases-at-launch.html
---

# Enforce automatic tagging of Amazon RDS databases at launch
<a name="enforce-automatic-tagging-of-amazon-rds-databases-at-launch"></a>

*Susanne Kangnoh and Archit Mathur, Amazon Web Services*

## Summary
<a name="enforce-automatic-tagging-of-amazon-rds-databases-at-launch-summary"></a>

Amazon Relational Database Service (Amazon RDS) is a web service that makes it easier to set up, operate, and scale a relational database in the Amazon Web Services (AWS) Cloud. It provides cost-efficient, resizable capacity for an industry-standard relational database and manages common database administration tasks.

You can use tagging to categorize your AWS resources in different ways. Relational database tagging is useful when you have many resources in your account and you want to quickly identify a specific resource based on the tags. You can use Amazon RDS tags to add custom metadata to your RDS DB instances. A tag consists of a user-defined key and value. We recommend that you create a consistent set of tags to meet your organization's requirements.

This pattern provides an AWS CloudFormation template to help you monitor and tag RDS DB instances. The template creates an Amazon CloudWatch Events event that watches for the AWS CloudTrail **CreateDBInstance **event. (CloudTrail captures API calls for Amazon RDS as events.) When it detects this event, it calls an AWS Lambda function that automatically applies tag keys and values that you define. The template also sends out a notification that the instance has been tagged, by using Amazon Simple Notification Service (Amazon SNS).

## Prerequisites and limitations
<a name="enforce-automatic-tagging-of-amazon-rds-databases-at-launch-prerequisites-and-limitations"></a>

**Prerequisites **
+ An active AWS account.
+ An Amazon Simple Storage Service (Amazon S3) bucket to upload the Lambda code.
+ An email address where you would like to receive tagging notifications.

**Limitations **
+ The solution supports CloudTrail **CreateDBInstance** events. It does not create notifications for any other events.

## Architecture
<a name="enforce-automatic-tagging-of-amazon-rds-databases-at-launch-architecture"></a>

**Workflow architecture**

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/5541bc1e-e00f-4b5a-94b7-bb1808b5591a/images/ec0bcf92-f986-4af3-bfe7-d2c5e04051c5.png)

**Automation and scale**
+ You can use the AWS CloudFormation template multiple times for different AWS Regions and accounts. You need to run the template only once in each Region or account.

## Tools
<a name="enforce-automatic-tagging-of-amazon-rds-databases-at-launch-tools"></a>

**AWS services**
+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) – AWS CloudTrail is an AWS service that helps you with governance, compliance, and operational and risk auditing of your AWS account. Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail.
+ [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) – Amazon CloudWatch Events delivers a near real-time stream of system events that describe changes in AWS resources. CloudWatch Events becomes aware of operational changes as they occur and takes corrective action as necessary, by sending messages to respond to the environment, activating functions, making changes, and capturing state information.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) – AWS Lambda is a compute service that supports running code without needing to provision or manage servers. Lambda runs your code only when needed and scales automatically, from a few requests per day to thousands per second. You pay only for the compute time that you consume—there is no charge when your code is not running.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html) – Amazon Simple Storage Service (Amazon S3) is a highly scalable object storage service that can be used for a wide range of storage solutions, including websites, mobile applications, backups, and data lakes.
+ [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) – Amazon Simple Notification Service (Amazon SNS) is a web service that enables applications, end-users, and devices to instantly send and receive notifications from the cloud.

**Code **

This pattern includes an attachment with two files:
+ `index.zip` is a compressed file that includes the Lambda code for this pattern.
+ `rds.yaml` is a CloudFormation template that deploys the Lambda code.

See the *Epics *section for information about how to use these files.

## Epics
<a name="enforce-automatic-tagging-of-amazon-rds-databases-at-launch-epics"></a>

### Deploy the Lambda code
<a name="deploy-the-lambda-code"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Upload the code to an S3 bucket. | Create a new S3 bucket or use an existing S3 bucket to upload the attached `index.zip` file (Lambda code). This bucket must be in the same AWS Region as the resources (RDS DB instances) that you want to monitor. | Cloud architect |
| Deploy the CloudFormation template. | Open the Cloudformation console in the same AWS Region as the S3 bucket, and deploy the `rds.yaml` file that's provided in the attachment. In the next epic, provide values for the template parameters. | Cloud architect |

### Complete the parameters in the CloudFormation template
<a name="complete-the-parameters-in-the-cloudformation-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Provide the S3 bucket name. | Enter the name of the S3 bucket that you created or selected in the first epic. This S3 bucket contains the .zip file for the Lambda code and must be in the same AWS Region as the CloudFormation template and the RDS DB instances that you want to monitor. | Cloud architect |
| Provide the S3 key. | Provide the location of the Lambda code .zip file in your S3 bucket, without leading slashes (for example, `index.zip` or `controls/index.zip`). | Cloud architect |
| Provide an email address. | Provide an active email address where you want to receive violation notifications. | Cloud architect |
| Specify a logging level. | Specify the logging level and verbosity. `Info` designates detailed informational messages on the application’s progress and should be used only for debugging. `Error` designates error events that could still allow the application to continue running. `Warning` designates potentially harmful situations. | Cloud architect |
| Enter the tag keys and values for your RDS DB instances. | Enter the required tag keys and values that you want to automatically apply to the RDS instance. For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the AWS documentation. | Cloud architect |

### Confirm the subscription
<a name="confirm-the-subscription"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Confirm the email subscription. | When the CloudFormation template deploys successfully, it sends a subscription email message to the email address you provided. To receive notifications when your instances are tagged, you must confirm this email subscription. | Cloud architect |

## Related resources
<a name="enforce-automatic-tagging-of-amazon-rds-databases-at-launch-related-resources"></a>
+ [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html) (Amazon S3 documentation)
+ [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) (Amazon Aurora documentation)
+ [Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/upload-objects.html) (Amazon S3 documentation)
+ [Creating a CloudWatch Events rule that triggers on an AWS API call using AWS CloudTrail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-CloudTrail-Rule.html) (Amazon CloudWatch documentation)

## Attachments
<a name="attachments-5541bc1e-e00f-4b5a-94b7-bb1808b5591a"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/5541bc1e-e00f-4b5a-94b7-bb1808b5591a/attachments/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
