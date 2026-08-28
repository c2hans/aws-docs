---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/help-enforce-dynamodb-tagging.html
---

# Help enforce DynamoDB tagging
<a name="help-enforce-dynamodb-tagging"></a>

*Mansi Suratwala, Amazon Web Services*

## Summary
<a name="help-enforce-dynamodb-tagging-summary"></a>

This pattern sets up automatic notifications when a predefined Amazon DynamoDB tag is missing or removed from a DynamoDB resource on the Amazon Web Services (AWS) Cloud.

DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with scalability. DynamoDB lets you offload the administrative burdens of operating and scaling a distributed database. When you use DynamoDB, you don't have to worry about hardware provisioning, setup and configuration, replication, software patching, or cluster scaling.

The pattern uses an AWS CloudFormation template, which creates an Amazon CloudWatch Events event and an AWS Lambda function. The event watches for any new or existing DynamoDB tagging information by using AWS CloudTrail. If a predefined tag is missing or removed, CloudWatch triggers a Lambda function, which sends you an Amazon Simple Notification Service (Amazon SNS) notification informing you of the violation.

## Prerequisites and limitations
<a name="help-enforce-dynamodb-tagging-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ An Amazon Simple Storage Service (Amazon S3) bucket for the Lambda .zip file that contains the Python script for running the Lambda function

**Limitations **
+ The solution works only when the `TagResource` or `UntagResource` CloudTrail events occur. It does not create notifications for any other events.

## Architecture
<a name="help-enforce-dynamodb-tagging-architecture"></a>

**Target technology stack  **
+ Amazon DynamoDB
+ AWS CloudTrail
+ Amazon CloudWatch
+ AWS Lambda
+ Amazon S3
+ Amazon SNS

**Target architecture **

![Missing DynamoDB tag triggers CloudWatch event and Lambda function to send Amazon SNS notification.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/638d2b87-e031-4a53-8677-2d62e563746b/images/acc448c5-c39b-40b7-94c0-3534d2e725d7.png)

**Automation and scale**

You can use the AWS CloudFormation template multiple times for different AWS Regions and accounts. You need to run the template only once in each Region or account.

## Tools
<a name="help-enforce-dynamodb-tagging-tools"></a>

**Tools**
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) – DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with scalability.
+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) – CloudTrail is an AWS service that helps you with governance, compliance, and operational and risk auditing of your AWS account. Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail.
+ [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) – Amazon CloudWatch Events delivers a near-real time stream of system events that describe changes in AWS resources.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) – Lambda is a compute service that supports running code without needing to provision or manage servers. Lambda runs your code only when needed and scales automatically, from a few requests per day to thousands per second.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html) – Amazon Simple Storage Service (Amazon S3) is a highly scalable object storage service that can be used for a wide range of storage solutions, including websites, mobile applications, backups, and data lakes.
+ [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) – Amazon Simple Notification Service (Amazon SNS) is a web service that enables applications, end-users, and devices to instantly send and receive notifications from the cloud.

**Code **
+ A .zip file of the project is available as an attachment.

## Epics
<a name="help-enforce-dynamodb-tagging-epics"></a>

### Define the S3 bucket
<a name="define-the-s3-bucket"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Define the S3 bucket. | On the Amazon S3 console, choose or create an S3 bucket with a unique name that does not contain leading slashes. This S3 bucket will host the Lambda code .zip file. Your S3 bucket must be in the same AWS Region as the DynamoDB resource that is being monitored. | Cloud Architect |

### Upload the Lambda code to the S3 bucket
<a name="upload-the-lambda-code-to-the-s3-bucket"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Upload the Lambda code to the S3 bucket. | Upload the Lambda code .zip file provided in the *Attachments* section to the S3 bucket. The S3 bucket must be in the same Region as the DynamoDB resource that is being monitored. | Cloud Architect |

### Deploy the AWS CloudFormation template
<a name="deploy-the-aws-cloudformation-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the AWS CloudFormation template. | On the AWS CloudFormation console, deploy the AWS CloudFormation template that's provided in the *Attachments* section. In the next epic, provide values for the parameters. | Cloud Architect  |

### Complete the parameters in the AWS CloudFormation template
<a name="complete-the-parameters-in-the-aws-cloudformation-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Name the S3 bucket. | Enter the name of the S3 bucket that you created or chose in the first epic. | Cloud Architect |
| Provide the Amazon S3 key. | Provide the location of the Lambda code .zip file in your S3 bucket, without leading slashes (for example, `<folder>/<file-name>.zip`). | Cloud Architect |
| Provide an email address | Provide an active email address to receive Amazon SNS notifications. | Cloud Architect  |
| Define the logging level. | Define the logging level and frequency for your Lambda function. `Info` designates detailed informational messages on the application’s progress. `Error` designates error events that could still allow the application to continue running. `Warning` designates potentially harmful situations. | Cloud Architect |
| Enter the required DynamoDB tag keys. | Be sure that the tags are separated by commas, with no spaces between them (for example, `ApplicationId,CreatedBy,Environment,Organization`). The CloudWatch Events event searches for these tags and sends a notification if they are not found. | Cloud Architect |

### Confirm the subscription.
<a name="confirm-the-subscription"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Confirm the subscription. | When the template successfully deploys, it sends a subscription email to the email address that you provided. To receive violation notifications, you must confirm this email subscription. | Cloud Architect  |

## Related resources
<a name="help-enforce-dynamodb-tagging-resources"></a>
+ [Creating an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html)
+ [Uploading files to an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/upload-objects.html)
+ [Tagging resources in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tagging.Operations.html)
+ [Creating a CloudWatch Events rule that triggers on an AWS API call using AWS CloudTrail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-CloudTrail-Rule.html)

## Attachments
<a name="attachments-638d2b87-e031-4a53-8677-2d62e563746b"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/638d2b87-e031-4a53-8677-2d62e563746b/attachments/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
