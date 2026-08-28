---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/check-ec2-instances-for-mandatory-tags-at-launch.html
---

# Check EC2 instances for mandatory tags at launch
<a name="check-ec2-instances-for-mandatory-tags-at-launch"></a>

*Susanne Kangnoh and Archit Mathur, Amazon Web Services*

## Summary
<a name="check-ec2-instances-for-mandatory-tags-at-launch-summary"></a>

Amazon Elastic Compute Cloud (Amazon EC2) provides scalable computing capacity in the Amazon Web Services (AWS) Cloud. Using Amazon EC2 eliminates your need to invest in hardware up front, so you can develop and deploy applications faster.

You can use tagging to categorize your AWS resources in different ways. EC2 instance tagging is useful when you have many resources in your account and you want to quickly identify a specific resource based on the tags. You can assign custom metadata to your EC2 instances by using tags. A tag consists of a user-defined key and value. We recommend that you create a consistent set of tags to meet your organization's requirements.

This pattern provides an AWS CloudFormation template to help you monitor EC2 instances for specific tags. The template creates an Amazon CloudWatch Events event that watches for the AWS CloudTrail **TagResource **or **UntagResource** events, to detect new EC2 instance tagging or tag removal. If a predefined tag is missing, it calls an AWS Lambda function, which sends out a violation message to an email address that you provide, by using Amazon Simple Notification Service (Amazon SNS).

## Prerequisites and limitations
<a name="check-ec2-instances-for-mandatory-tags-at-launch-prerequisites-and-limitations"></a>

**Prerequisites **
+ An active AWS account.
+ An Amazon Simple Storage Service (Amazon S3) bucket to upload the provided Lambda code.
+ An email address where you would like to receive violation notifications.

**Limitations **
+ This solution supports CloudTrail **TagResource **or **UntagResource **events. It does not create notifications for any other events.
+ This solution checks only for tag keys. It does not monitor key values.

## Architecture
<a name="check-ec2-instances-for-mandatory-tags-at-launch-architecture"></a>

**Workflow ****architecture **

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/9cd74141-a87f-419e-94b3-0b28fd04a018/images/b48fd21b-a86b-4ec7-b9f6-4f1a64999437.png)

**Automation and scale**
+ You can use the AWS CloudFormation template multiple times for different AWS Regions and accounts. You need to run the template only once in each Region or account.

## Tools
<a name="check-ec2-instances-for-mandatory-tags-at-launch-tools"></a>

**AWS services**
+ [Amazon EC2](https://aws.amazon.com/ec2/) – Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers.
+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) – CloudTrail is an AWS service that helps you with governance, compliance, and operational and risk auditing of your AWS account. Actions taken by a user, role, or AWS service are recorded as events in CloudTrail.
+ [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) – Amazon CloudWatch Events delivers a near real-time stream of system events that describe changes in AWS resources. CloudWatch Events becomes aware of operational changes as they occur and takes corrective action as necessary, by sending messages to respond to the environment, activating functions, making changes, and capturing state information.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) – Lambda is a compute service that supports running code without needing to provision or manage servers. Lambda runs your code only when needed and scales automatically, from a few requests per day to thousands per second.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html) – Amazon Simple Storage Service (Amazon S3) is a highly scalable object storage service that can be used for a wide range of storage solutions, including websites, mobile applications, backups, and data lakes.
+ [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) – Amazon Simple Notification Service (Amazon SNS) is a web service that enables applications, end-users, and devices to instantly send and receive notifications from the cloud.

**Code**

This pattern includes an attachment with two files:
+ `index.zip` is a compressed file that includes the Lambda code for this pattern.
+ `ec2-require-tags.yaml` is a CloudFormation template that deploys the Lambda code.

See the *Epics *section for information about how to use these files.

## Epics
<a name="check-ec2-instances-for-mandatory-tags-at-launch-epics"></a>

### Deploy the Lambda code
<a name="deploy-the-lambda-code"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Upload the code to an S3 bucket. | Create a new S3 bucket or use an existing S3 bucket to upload the attached `index.zip` file (Lambda code). This bucket must be in the same AWS Region as the resources (EC2 instances) that you want to monitor. | Cloud architect |
| Deploy the CloudFormation template. | Open the Cloudformation console in the same AWS Region as the S3 bucket, and deploy the `ec2-require-tags.yaml` file that's provided in the attachment. In the next epic, provide values for the template parameters.   | Cloud architect |

### Complete the parameters in the CloudFormation template
<a name="complete-the-parameters-in-the-cloudformation-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Provide the S3 bucket name. | Enter the name of the S3 bucket that you created or selected in the first epic. This S3 bucket contains the .zip file for the Lambda code and must be in the same AWS Region as the CloudFormation template and the EC2 instances that you want to monitor. | Cloud architect |
| Provide the S3 key. | Provide the location of the Lambda code .zip file in your S3 bucket, without leading slashes (for example, `index.zip` or `controls/index.zip`). | Cloud architect |
| Provide an email address. | Provide an active email address where you want to receive violation notifications. | Cloud architect |
| Define a logging level. | Specify the logging level and verbosity. `Info` designates detailed informational messages on the application’s progress and should be used only for debugging. `Error` designates error events that could still allow the application to continue running. `Warning` designates potentially harmful situations. | Cloud architect |
| Enter the required tag keys. | Enter the tag keys that you want to check for. If you want to specify multiple keys, separate them with commas, without spaces. (For example, `ApplicationId,CreatedBy,Environment,Organization` searches for four keys.) The CloudWatch Events event searches for these tag keys and sends a notification if they are not found. | Cloud architect |

### Confirm the subscription
<a name="confirm-the-subscription"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Confirm the email subscription. | When the CloudFormation template deploys successfully, it sends a subscription email message to the email address you provided. To receive notifications, you must confirm this email subscription.   | Cloud architect |

## Related resources
<a name="check-ec2-instances-for-mandatory-tags-at-launch-related-resources"></a>
+ [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html) (Amazon S3 documentation)
+ [Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/upload-objects.html) (Amazon S3 documentation)
+ [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) (Amazon EC2 documentation)
+ [Creating a CloudWatch Events rule that triggers on an AWS API call using AWS CloudTrail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-CloudTrail-Rule.html) (Amazon CloudWatch documentation)

## Attachments
<a name="attachments-9cd74141-a87f-419e-94b3-0b28fd04a018"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/9cd74141-a87f-419e-94b3-0b28fd04a018/attachments/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
