---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/ensure-amazon-emr-logging-to-amazon-s3-is-enabled-at-launch.html
---

# Ensure Amazon EMR logging to Amazon S3 is enabled at launch
<a name="ensure-amazon-emr-logging-to-amazon-s3-is-enabled-at-launch"></a>

*Priyanka Chaudhary, Amazon Web Services*

## Summary
<a name="ensure-amazon-emr-logging-to-amazon-s3-is-enabled-at-launch-summary"></a>

This pattern provides a security control that monitors logging configuration for Amazon EMR clusters running on Amazon Web Services (AWS).

Amazon EMR is an AWS tool for big data processing and analysis. Amazon EMR offers the expandable low-configuration service as an alternative to running in-house cluster computing. Amazon EMR provides two types of EMR clusters.
+ **Transient Amazon EMR clusters**: Transient Amazon EMR clusters automatically shut down and stop incurring costs when processing is finished.
+ **Persistent Amazon EMR clusters**: Persistent Amazon EMR clusters continue to run after the data processing job is complete.

Amazon EMR and Hadoop both produce log files that report status on the cluster. By default, these are written to the master node in the **/mnt/var/log/** directory. Depending on how you configure the cluster when you launch it, you can also save these logs to Amazon Simple Storage Service (Amazon S3) and view them through the graphical debugging tool. Note that Amazon S3 logging can be specified only when the cluster is launched. With this configuration, logs are sent from the primary node to the Amazon S3 location every 5 minutes. For transient clusters, Amazon S3 logging is important because the clusters disappear when processing is complete, and these log files can be use to debug any failed jobs.

The pattern uses an AWS CloudFormation template to deploy a security control that monitors for API calls and starts Amazon CloudWatch Events on "RunJobFlow." The trigger invokes AWS Lambda, which runs a Python script. The Lambda function retrieves the EMR cluster ID from the event JSON input and also checks for an Amazon S3 log URI. If an Amazon S3 URI is not found, the Lambda function sends an Amazon Simple Notification Service (Amazon SNS) notification detailing the EMR cluster name, violation details, AWS Region, AWS account, and the Lambda Amazon Resource Name (ARN) that the notification is sourced from.

## Prerequisites and limitations
<a name="ensure-amazon-emr-logging-to-amazon-s3-is-enabled-at-launch-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An S3 bucket for the Lambda code .zip file
+ An email address where you want to receive the violation notification

**Limitations**
+ This detective control is regional and must be deployed in the AWS Regions you intend to monitor.

**Product versions**
+ Amazon EMR release 4.8.0 and later

## Architecture
<a name="ensure-amazon-emr-logging-to-amazon-s3-is-enabled-at-launch-architecture"></a>

**Target technology stack**
+ Amazon CloudWatch Events event
+ Amazon EMR
+ Lambda function
+ S3 bucket
+ Amazon SNS

**Target architecture**

![Workflow for ensuring that Amazon EMR logging to Amazon S3 is enabled at launch.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/079af32e-0418-4bb2-bc20-c67ea5ac3b6e/images/3ba125cb-018a-4ace-838f-8c20992ecc20.png)

**Automation and scale**
+ If you are using AWS Organizations, you can use [AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) to deploy this template in multiple accounts that you want to monitor.

## Tools
<a name="ensure-amazon-emr-logging-to-amazon-s3-is-enabled-at-launch-tools"></a>

**Tools**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) – AWS CloudFormation helps you model and set up AWS resources using infrastructure as code.
+ [AWS Cloudwatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) – AWS CloudWatch Events delivers a near real-time stream of system events that describe changes in AWS resources.
+ [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html) – Amazon EMR is a managed cluster platform that simplifies running big data frameworks.
+ [AWS Lambda](https://aws.amazon.com/lambda/) – AWS Lambda supports running code without provisioning or managing servers. Lambda runs your code only when needed and scales automatically, from a few requests per day to thousands per second.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html) – Amazon S3 is a web services interface that you can use to store and retrieve any amount of data from anywhere on the web.
+ [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) – Amazon SNS is a web service that coordinates and manages the delivery or sending of messages between publishers and clients, including web servers and email addresses.

**Code**
+ A .zip file of the project is available as an attachment.

## Epics
<a name="ensure-amazon-emr-logging-to-amazon-s3-is-enabled-at-launch-epics"></a>

### Define the S3 bucket
<a name="define-the-s3-bucket"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Define the S3 bucket. | To host the Lambda code .zip file, choose or create an S3 bucket with a unique name that does not contain leading slashes. An S3 bucket name is globally unique, and the namespace is shared by all AWS accounts. Your S3 bucket needs to be in the same AWS Region as the Amazon EMR cluster that is being evaluated. | Cloud Architect |

### Upload the Lambda code to the S3 bucket
<a name="upload-the-lambda-code-to-the-s3-bucket"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Upload the Lambda code to the S3 bucket. | Upload the Lambda code .zip file that's provided in the "Attachments" section to the S3 bucket. The S3 bucket must be in the same Region as the Amazon EMR cluster that is being evaluated. | Cloud Architect |

### Deploy the AWS CloudFormation template
<a name="deploy-the-aws-cloudformation-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the AWS CloudFormation template. | On the AWS CloudFormation console, in the same Region as your S3 bucket, deploy the AWS CloudFormation template that's provided as an attachment to this pattern. In the next epic, provide the values for the parameters. For more information about deploying AWS CloudFormation templates, see the "Related resources" section. | Cloud Architect |

### Complete the parameters in the AWS CloudFormation template
<a name="complete-the-parameters-in-the-aws-cloudformation-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Name the S3 bucket. | Enter the name of the S3 bucket that you created in the first epic. | Cloud Architect |
| Provide the Amazon S3 key. | Provide the location of the Lambda code .zip file in your S3 bucket, without leading slashes (for example, <directory>/<file-name>.zip). | Cloud Architect |
| Provide an email address. | Provide an active email address to receive Amazon SNS notifications. | Cloud Architect |
| Define the logging level. | Define the logging level and frequency for your Lambda function. "Info" designates detailed informational messages on the application’s progress. "Error" designates error events that could still allow the application to continue running. "Warning" designates potentially harmful situations. | Cloud Architect |

### Confirm the subscription
<a name="confirm-the-subscription"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Confirm the subscription. | When the template successfully deploys, it sends a subscription email message to the email address provided. You must confirm this email subscription to receive violation notifications. | Cloud Architect |

## Related resources
<a name="ensure-amazon-emr-logging-to-amazon-s3-is-enabled-at-launch-resources"></a>
+ [AWS Lambda](https://aws.amazon.com/lambda/)
+ [Amazon EMR logging](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-debugging.html)
+ [Deploying AWS CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html)

## Attachments
<a name="attachments-079af32e-0418-4bb2-bc20-c67ea5ac3b6e"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/079af32e-0418-4bb2-bc20-c67ea5ac3b6e/attachments/attachment.zip)
