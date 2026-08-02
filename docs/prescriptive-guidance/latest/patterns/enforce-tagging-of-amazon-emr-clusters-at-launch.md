---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enforce-tagging-of-amazon-emr-clusters-at-launch.html
---

# Enforce tagging of Amazon EMR clusters at launch
<a name="enforce-tagging-of-amazon-emr-clusters-at-launch"></a>

*Priyanka Chaudhary, Amazon Web Services*

## Summary
<a name="enforce-tagging-of-amazon-emr-clusters-at-launch-summary"></a>

This pattern provides a security control that ensures that Amazon EMR clusters are tagged when they are created.

Amazon EMR is an Amazon Web Services (AWS) service for processing and analyzing vast amounts of data. Amazon EMR offers an expandable, low-configuration service as an easier alternative to running in-house cluster computing. You can use tagging to categorize AWS resources in different ways, such as by purpose, owner, or environment . For example, you can tag your Amazon EMR clusters by assigning custom metadata to each cluster. A tag consists of a key and value that you define. We recommend that you create a consistent set of tags to meet your organization's requirements. When you add a tag to an Amazon EMR cluster, the tag is also propagated to each active Amazon Elastic Compute Cloud (Amazon EC2) instance that is associated with the cluster. Similarly, when you remove a tag from an Amazon EMR cluster, that tag is removed from each associated, active EC2 instance as well.

The detective control monitors API calls and initiates an Amazon CloudWatch Events event for the [RunJobFlow](https://docs.aws.amazon.com/emr/latest/APIReference/API_RunJobFlow.html), [AddTags](https://docs.aws.amazon.com/emr/latest/APIReference/API_AddTags.html), [RemoveTags](https://docs.aws.amazon.com/emr/latest/APIReference/API_RemoveTags.html), and [CreateTags](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html) APIs. The event calls AWS Lambda, which runs a Python script. The Python function gets the Amazon EMR cluster ID from the JSON input from the event and performs the following checks:
+ Check if the Amazon EMR cluster is configured with tag names that you specify.
+ If not, send an Amazon Simple Notification Service (Amazon SNS) notification to the user with the relevant information: the Amazon EMR cluster name, violation details, AWS Region, AWS account, and Amazon Resource Name (ARN) for Lambda that this notification is sourced from.

## Prerequisites and limitations
<a name="enforce-tagging-of-amazon-emr-clusters-at-launch-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ An Amazon Simple Storage Service (Amazon S3) bucket to upload the provided Lambda code. Or, you can create an S3 bucket for this purpose, as described in the *Epics *section.
+ An active email address where you would like to receive violation notifications.
+ A list of mandatory tags you want to check for.

**Limitations **
+ This security control is regional. You must deploy it in each AWS Region that you want to monitor.

**Product versions**
+ Amazon EMR release 4.8.0 and later.

## Architecture
<a name="enforce-tagging-of-amazon-emr-clusters-at-launch-architecture"></a>

**Workflow architecture **

![Cluster launch, monitoring using APIs, event generation, Lambda function call, notification sent.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/1a4fc0f8-b0c9-4391-9c79-9eb3898d6ecb/images/0d95c414-69d1-4f29-a9e7-09f202e27014.png)

**Automation and scale**
+ If you are using [AWS Organizations](https://aws.amazon.com/organizations/), you can use [AWS Cloudformation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) to deploy this template in multiple accounts that you want to monitor.

## Tools
<a name="enforce-tagging-of-amazon-emr-clusters-at-launch-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) –  AWS CloudFormation helps you model and set up your AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle. You can use a template to describe your resources and their dependencies, and launch and configure them together as a stack, instead of managing resources individually. You can manage and provision stacks across multiple AWS accounts and AWS Regions.
+ [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) - Amazon CloudWatch Events delivers a near real-time stream of system events that describe changes in AWS resources.
+ [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html) - Amazon EMR is web service that simplifies running big data frameworks and processing vast amounts of data efficiently.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) – AWS Lambda is a compute service that supports running code without provisioning or managing servers. Lambda runs your code only when needed and scales automatically, from a few requests per day to thousands per second.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) – Amazon Simple Storage Service (Amazon S3) is an object storage service. You can use Amazon S3 to store and retrieve any amount of data at any time, from anywhere on the web.
+ [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) – Amazon Simple Notification Service (Amazon SNS) coordinates and manages the delivery or sending of messages between publishers and clients, including web servers and email addresses. Subscribers receive all messages published to the topics to which they subscribe, and all subscribers to a topic receive the same messages.

**Code**

This pattern includes the following attachments:
+ `EMRTagValidation.zip` – The Lambda code for the security control.
+ `EMRTagValidation.yml` – The CloudFormation template that sets up the event and Lambda function.

## Epics
<a name="enforce-tagging-of-amazon-emr-clusters-at-launch-epics"></a>

### Set up the S3 bucket
<a name="set-up-the-s3-bucket"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Define the S3 bucket. | On the [Amazon S3 console](https://console.aws.amazon.com/s3/), choose or create an S3 bucket to host the Lambda code .zip file. This S3 bucket must be in the same AWS Region as the Amazon EMR cluster you want to monitor. An Amazon S3 bucket name is globally unique, and the namespace is shared by all AWS accounts. The S3 bucket name cannot include leading slashes. | Cloud architect |
| Upload the Lambda code. | Upload the Lambda code .zip file provided in the *Attachments *section to the S3 bucket.                                               | Cloud architect |

### Deploy the AWS CloudFormation template
<a name="deploy-the-aws-cloudformation-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Launch the AWS CloudFormation template. | Open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/.) in the same AWS Region as your S3 bucket and deploy the template. For more information about deploying AWS CloudFormation templates, see [Creating a stack on the AWS CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) in the CloudFormation documentation. | Cloud architect |
| Complete the parameters in the template. | When you launch the template, you'll be prompted for the following information:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enforce-tagging-of-amazon-emr-clusters-at-launch.html) | Cloud architect |

### Confirm the subscription
<a name="confirm-the-subscription"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Confirm the subscription. | When the CloudFormation template deploys successfully, it sends a subscription email to the email address you provided. You must confirm this email subscription to start receiving violation notifications. | Cloud architect |

## Related resources
<a name="enforce-tagging-of-amazon-emr-clusters-at-launch-resources"></a>
+ [AWS Lambda developer guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
+ [Tagging clusters in Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html)

## Attachments
<a name="attachments-1a4fc0f8-b0c9-4391-9c79-9eb3898d6ecb"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/1a4fc0f8-b0c9-4391-9c79-9eb3898d6ecb/attachments/attachment.zip)
