---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/send-a-notification-when-an-iam-user-is-created.html
---

# Send a notification when an IAM user is created
<a name="send-a-notification-when-an-iam-user-is-created"></a>

*Mansi Suratwala and Sergiy Shevchenko, Amazon Web Services*

## Summary
<a name="send-a-notification-when-an-iam-user-is-created-summary"></a>

On Amazon Web Services (AWS), you can use this pattern to deploy an AWS CloudFormation template to receive notifications automatically when AWS Identity and Access Management (IAM) users are created.

Using IAM, you can manage access to AWS services and resources securely. You can create and manage AWS users and groups, and use permissions to allow and deny those users and groups access to AWS resources.

The CloudFormation template creates an Amazon CloudWatch Events event and an AWS Lambda function. The event uses AWS CloudTrail to monitor for any IAM user being created in the AWS account. If a user is created, the CloudWatch Events event initiates a Lambda function, which sends you an Amazon Simple Notification Service (Amazon SNS) notification informing you of the new user creation event.

## Prerequisites and limitations
<a name="send-a-notification-when-an-iam-user-is-created-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An AWS CloudTrail trail created and deployed

**Limitations **
+ The AWS CloudFormation template must be deployed for `CreateUser` only.

## Architecture
<a name="send-a-notification-when-an-iam-user-is-created-architecture"></a>

**Target technology stack  **
+ IAM
+ AWS CloudTrail
+ Amazon CloudWatch Events
+ AWS Lambda
+ Amazon Simple Storage Service (Amazon S3)
+ Amazon SNS

**Target architecture **

![Process from user to IAM to CloudTrail to CloudWatch Events to Lambda and an S3 bucket, ending with SNS email notification.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/5487fbff-72e7-4da4-a970-a4542e89824d/images/c73532fd-8e95-45a5-843d-1864eb4df227.png)

**Automation and scale**

You can use the AWS CloudFormation template multiple times for different AWS Regions and accounts. You need to run it only once in each Region or account. To automate deployment to multiple accounts, use [AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html). The CloudFormation template will be able to deploy all the required resources in each account.

## Tools
<a name="send-a-notification-when-an-iam-user-is-created-tools"></a>

**Tools**
+ [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) – AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) – AWS CloudFormation helps you model and set up your Amazon Web Services resources so that you can spend less time managing those resources and more time focusing on your applications that run in AWS. You create a template that describes all the AWS resources that you want, and CloudFormation takes care of provisioning and configuring those resources for you.
+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) – AWS CloudTrail helps you manage governance, compliance, and operational and risk auditing of your AWS account. Actions taken by a user, a role, or an AWS service are recorded as events in CloudTrail. Events include actions taken in the AWS Management Console, AWS Command Line Interface, and AWS SDKs and APIs.
+ [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) – Amazon CloudWatch Events delivers a near-real-time stream of system events that describe changes in AWS resources.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) – AWS Lambda is a compute service that supports running code without provisioning or managing servers. Lambda runs your code only when needed and scales automatically, from a few requests per day to thousands per second.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) – Amazon Simple Storage Service (Amazon S3) is storage for the internet. You can use Amazon S3 to store and retrieve any amount of data at any time, from anywhere on the web.
+ [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) – Amazon Simple Notification Service (Amazon SNS) is a managed service that provides message delivery using Lambda, HTTP, email, mobile push notifications, and mobile text messages (SMS).

**Code **

A .zip file of the project is available as an attachment.

## Epics
<a name="send-a-notification-when-an-iam-user-is-created-epics"></a>

### Create the S3 bucket for the Lambda script
<a name="create-the-s3-bucket-for-the-lambda-script"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Define the S3 bucket. | Open the Amazon S3 console, and choose or create an S3 bucket. This S3 bucket will host the Lambda code .zip file. The S3 bucket name cannot contain leading slashes. | Cloud architect |

### Upload the Lambda code to the S3 bucket
<a name="upload-the-lambda-code-to-the-s3-bucket"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Upload the Lambda code. | Upload the Lambda code .zip file provided in the *Attachments* section to the S3 bucket that you defined. | Cloud architect |

### Deploy the CloudFormation template
<a name="deploy-the-cloudformation-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the CloudFormation template. | On the CloudFormation console, deploy the CloudFormation `createIAMuser.yaml` template that's provided as an attachment to this pattern. In the next epic, provide values for the template parameters. | Cloud architect |

### Complete the parameters in the CloudFormation template
<a name="complete-the-parameters-in-the-cloudformation-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Provide the S3 bucket name. | Enter the name of the S3 bucket that you created or chose in the first epic. | Cloud architect |
| Provide the S3 key. | Provide the location of the Lambda code .zip file in your S3 bucket, without leading slashes (for example, `<directory>/<file-name>.zip`). | Cloud architect |
| Provide an email address. | Provide an active email address to receive Amazon SNS notifications. | Cloud architect |
| Define the logging level. | Define the logging level and frequency for your Lambda function. `Info` designates detailed informational messages on the application’s progress. `Error` designates error events that could still allow the application to continue running. `Warning` designates potentially harmful situations. | Cloud architect |

### Confirm the subscription
<a name="confirm-the-subscription"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Confirm the subscription. | When the template successfully deploys, it sends a subscription email message to the email address provided. To receive notifications, you must confirm this email subscription. | Cloud architect |

## Related resources
<a name="send-a-notification-when-an-iam-user-is-created-resources"></a>
+ [Creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html?icmpid=docs_console_unmapped)
+ [Creating an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html)
+ [Uploading files to an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/upload-objects.html)
+ [Deploying a CloudFormation template](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html)
+ [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)
+ [Creating a CloudWatch Events rule that triggers on an AWS API call using AWS CloudTrail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-CloudTrail-Rule.html)

## Attachments
<a name="attachments-5487fbff-72e7-4da4-a970-a4542e89824d"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/5487fbff-72e7-4da4-a970-a4542e89824d/attachments/attachment.zip)
