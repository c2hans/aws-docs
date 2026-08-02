---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-data-ingestion-from-aws-data-exchange-into-amazon-s3.html
---

# Automate data ingestion from AWS Data Exchange into Amazon S3
<a name="automate-data-ingestion-from-aws-data-exchange-into-amazon-s3"></a>

*Adnan Alvee and Manikanta Gona, Amazon Web Services*

## Summary
<a name="automate-data-ingestion-from-aws-data-exchange-into-amazon-s3-summary"></a>

This pattern provides an CloudFormation template that enables you to automatically ingest data from AWS Data Exchange into your data lake in Amazon Simple Storage Service (Amazon S3).

AWS Data Exchange is a service that makes it easy to securely exchange file-based data sets in the AWS Cloud. AWS Data Exchange data sets are subscription-based. As a subscriber, you can also access data set revisions as providers publish new data.

The CloudFormation template creates an event in Amazon CloudWatch Events and an AWS Lambda function. The event watches for any updates to the data set you have subscribed to. If there is an update, CloudWatch initiates a Lambda function, which copies the data over to the S3 bucket you specify. When the data has been copied successfully, Lambda sends you an Amazon Simple Notification Service (Amazon SNS) notification.

## Prerequisites and limitations
<a name="automate-data-ingestion-from-aws-data-exchange-into-amazon-s3-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ Subscription to a data set in AWS Data Exchange

**Limitations **
+ The CloudFormation template must be deployed separately for each subscribed data set in AWS Data Exchange.

## Architecture
<a name="automate-data-ingestion-from-aws-data-exchange-into-amazon-s3-architecture"></a>

**Target technology stack  **
+ AWS Lambda
+ Amazon S3
+ AWS Data Exchange
+ Amazon CloudWatch
+ Amazon SNS

**Target architecture **

![CloudWatch initiates a Lambda function to copy data to S3 bucket and send Amazon SNS notification.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/059816dc-5a71-4942-9c7f-ac977072eebc/images/ec021620-47c1-4fb5-95a9-3b8985accc56.png)

**Automation and scale**

You can use the CloudFormation template multiple times for the data sets you want to ingest into the data lake.

## Tools
<a name="automate-data-ingestion-from-aws-data-exchange-into-amazon-s3-tools"></a>
+ [AWS Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/what-is.html) makes it easy for AWS customers to securely exchange file-based data sets in the AWS Cloud. As a subscriber, you can find and subscribe to hundreds of products from qualified data providers. Then, you can quickly download the data set or copy it to Amazon S3 for use across a variety of AWS analytics and machine learning services. Anyone with an AWS account can be an AWS Data Exchange subscriber.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) lets you run code without provisioning or managing servers. Lambda runs your code only when needed and scales automatically, from a few requests per day to thousands per second. You pay only for the compute time you consume; there is no charge when your code isn't running. With Lambda, you can run code for virtually any type of application or backend service with zero administration. Lambda runs your code on a high-availability compute infrastructure and manages all the compute resources, including server and operating system maintenance, capacity provisioning and automatic scaling, code monitoring, and logging.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/gsg/GetStartedWithS3.html) provides storage for the internet. You can use Amazon S3 to store and retrieve any amount of data at any time, from anywhere on the web.
+ [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) delivers a near real-time stream of system events that describe changes in AWS resources. Using simple rules that you can quickly set up, you can match events and route them to one or more target functions or streams. CloudWatch Events becomes aware of operational changes as they occur. It responds to these operational changes and takes corrective action as necessary, by sending messages to respond to the environment, activating functions, making changes, and capturing state information. You can also use CloudWatch Events to schedule automated actions that self-initiate at certain times using **cron** or **rate** expressions.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) enables applications, end-users, and devices to instantly send and receive notifications from the cloud. Amazon SNS provides topics (communication channels) for high-throughput, push-based, many-to-many messaging. Using Amazon SNS topics, publishers can distribute messages to a large number of subscribers for parallel processing, including Amazon Simple Queue Service (Amazon SQS) queues, Lambda functions, and HTTP/S webhooks. You can also use Amazon SNS to send notifications to end users using mobile push, SMS, and email.

## Epics
<a name="automate-data-ingestion-from-aws-data-exchange-into-amazon-s3-epics"></a>

### Subscribe to a data set
<a name="subscribe-to-a-data-set"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Subscribe to a data set. | In the AWS Data Exchange console, subscribe to a dataset. For instructions, see [Subscribing to data products on AWS Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/subscribe-to-data-sets.html) in the AWS documentation. | General AWS |
| Note the data set attributes. | Note the AWS Region, ID, and revision ID for the data set. You will need this for the CloudFormation template in the next step. | General AWS |

### Deploy the CloudFormation template
<a name="deploy-the-cfn-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an S3 bucket and folder. | If you already have a data lake in Amazon S3, create a folder to store the data to ingest from AWS Data Exchange. If you are deploying the template for testing purposes, create a new S3 bucket, and note the bucket name and folder prefix for the next step. | General AWS |
| Deploy the CloudFormation template. | Deploy the CloudFormation template that's provided as an attachment to this pattern. For instructions, see the [CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html).<br />Configure the following parameters to correspond to your AWS account, data set, and S3 bucket settings: **Dataset AWS Region**, **Dataset ID**, **Revision ID**, **S3 Bucket Name** (for example, `DOC-EXAMPLE-BUCKET`), **Folder Prefix** (for example, `myfolder/`), and **Email for SNS Notification**. You can set the **Dataset Name** parameter to any name. When you deploy the template, it runs a Lambda function to automatically ingest the first set of data available in the data set. Subsequent ingestion then takes place automatically, as new data arrives in the data set. | General AWS |

## Related resources
<a name="automate-data-ingestion-from-aws-data-exchange-into-amazon-s3-resources"></a>
+ [Subscribing to data products on AWS Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/subscribe-to-data-sets.html) (AWS Data Exchange documentation)

## Attachments
<a name="attachments-059816dc-5a71-4942-9c7f-ac977072eebc"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/059816dc-5a71-4942-9c7f-ac977072eebc/attachments/attachment.zip)
