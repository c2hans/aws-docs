---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/subscribe-a-lambda-function-to-event-notifications-from-s3-buckets-in-different-aws-regions.html
---

# Subscribe a Lambda function to event notifications from S3 buckets in different AWS Regions
<a name="subscribe-a-lambda-function-to-event-notifications-from-s3-buckets-in-different-aws-regions"></a>

*Suresh Konathala, Amazon Web Services*

*Andrew Preston and Arindom Sarkar, None*

## Summary
<a name="subscribe-a-lambda-function-to-event-notifications-from-s3-buckets-in-different-aws-regions-summary"></a>

[Amazon Simple Storage Service (Amazon S3) Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/NotificationHowTo.html) publishes notifications for certain events in your S3 bucket (for example, object created events, object removal events, or restore object events). You can use an AWS Lambda function to process these notifications according to your application’s requirements. However, the Lambda function can’t directly subscribe to notifications from S3 buckets that are hosted in different AWS Regions.

This pattern’s approach deploys a [fanout scenario](https://docs.aws.amazon.com/sns/latest/dg/sns-common-scenarios.html) to process Amazon S3 notifications from cross-Region S3 buckets by using an Amazon Simple Notification Service (Amazon SNS) topic for each Region. These Regional SNS topics send the Amazon S3 event notifications to an Amazon Simple Queue Service (Amazon SQS) queue in a central Region that also contains your Lambda function. The Lambda function subscribes to this SQS queue and processes the event notifications according to your organization’s requirements.

## Prerequisites and limitations
<a name="subscribe-a-lambda-function-to-event-notifications-from-s3-buckets-in-different-aws-regions-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ Existing S3 buckets in multiple Regions, including a central Region to host the Amazon SQS queue and Lambda function.
+ AWS Command Line Interface (AWS CLI), installed and configured. For more information about this, see [Installing, updating, and uninstalling the AWS CLI ](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) in the AWS CLI documentation.
+ Familiarity with the fanout scenario in Amazon SNS. For more information about this, see [Common Amazon SNS scenarios](https://docs.aws.amazon.com/sns/latest/dg/sns-common-scenarios.html) in the Amazon SNS documentation.

## Architecture
<a name="subscribe-a-lambda-function-to-event-notifications-from-s3-buckets-in-different-aws-regions-architecture"></a>

The following diagram shows the architecture for this pattern’s approach.

![Workflow uses Amazon SNS, S3, and SQS to process event notifications from cross-Region S3 buckets.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/cf6c1804-8c41-46f1-9f17-ff361708c595/images/760cf4c0-0cb3-48d1-92ae-1cf0fa8ae076.png)

The diagram shows the following workflow:

1. Amazon S3 sends event notifications about S3 buckets (for example, object created, object removed, or object restored) to an SNS topic in the same Region.

1. The SNS topic publishes the event to an SQS queue in the central Region.

1. The SQS queue is configured as the event source for your Lambda function and buffers the event messages for the Lambda function.

1. The Lambda function polls the SQS queue for messages and processes the Amazon S3 event notifications according to your application’s requirements.

**Technology stack  **
+ Lambda
+ Amazon SNS
+ Amazon SQS
+ Amazon S3

## Tools
<a name="subscribe-a-lambda-function-to-event-notifications-from-s3-buckets-in-different-aws-regions-tools"></a>
+ [AWS CLI ](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)– The AWS Command Line Interface (AWS CLI) is an open-source tool for interacting with AWS services through commands in your command-line shell. With minimal configuration, you can run AWS CLI commands that implement functionality equivalent to that provided by the browser-based AWS Management Console from a command prompt.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) – AWS CloudFormation helps you model and set up your AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle. You can use a template to describe your resources and their dependencies, and launch and configure them together as a stack, instead of managing resources individually. You can manage and provision stacks across multiple AWS accounts and AWS Regions.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) – AWS Lambda is a compute service that supports running code without provisioning or managing servers. Lambda runs your code only when needed and scales automatically, from a few requests per day to thousands per second. You pay only for the compute time that you consume—there is no charge when your code is not running.
+ [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) – Amazon Simple Notification Service (Amazon SNS) coordinates and manages the delivery or sending of messages between publishers and clients, including web servers and email addresses. Subscribers receive all messages published to the topics to which they subscribe, and all subscribers to a topic receive the same messages.
+ [Amazon SQS ](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)– Amazon Simple Queue Service (Amazon SQS) offers a secure, durable, and available hosted queue that lets you integrate and decouple distributed software systems and components. Amazon SQS supports both standard and FIFO queues.

## Epics
<a name="subscribe-a-lambda-function-to-event-notifications-from-s3-buckets-in-different-aws-regions-epics"></a>

### Create the SQS queue and Lambda function in your central Region
<a name="create-the-sqs-queue-and-lambda-function-in-your-central-region"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an SQS queue with a Lambda trigger. | Sign in to the AWS Management Console and use the instructions from the tutorial [Using Lambda with Amazon SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs-example.html) in the AWS Lambda documentation to create the following resources in your central Region:+ A Lambda execution role<br />+ A Lambda function to process the Amazon S3 events<br />+ An SQS queueMake sure that you configure the SQS queue as the event source for your Lambda function. | AWS DevOps, Cloud architect |

### Create an SNS topic and set up event notifications for the S3 buckets in each required Region
<a name="create-an-sns-topic-and-set-up-event-notifications-for-the-s3-buckets-in-each-required-region"></a>

| Task | Description | Skills required |
| --- | --- | --- |
|  Create an SNS topic to receive Amazon S3 event notifications. | Create an SNS topic in a Region that you want to receive Amazon S3 event notifications from. For more information about this, see [Creating an SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html) in the Amazon SNS documentation. Make sure that you record your SNS topic’s Amazon Resource Name (ARN).  | AWS DevOps, Cloud architect |
| Subscribe the SNS topic to the central SQS queue. | Subscribe your SNS topic to the SQS queue hosted by your central Region. For more information about this, see [Subscribing to an SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html) in the Amazon SNS documentation. | AWS DevOps, Cloud architect |
| Update the SNS topic's access policy.  | 1. Open the Amazon SNS console, choose **Topics**, and then choose the SNS topic that you created earlier.<br />2. Choose **Edit** and then expand the **Access policy - optional** section.<br />3. Attach the following access policy to your SNS topic to allow `sns:publish` permission for Amazon S3 and then choose **Save**:<pre>{<br />  "Version": "2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Sid": "0",<br />      "Effect": "Allow",<br />      "Principal": {<br />        "Service": "s3.amazonaws.com"<br />      },<br />      "Action": "sns:Publish",<br />      "Resource": "arn:aws:sns:us-west-2::s3Events-SNSTopic-us-west-2"<br />    }<br />  ]<br />}</pre> | AWS DevOps, Cloud architect |
| Set up notifications for each S3 bucket in the Region. | Set up event notifications for each S3 bucket in the Region. For more information about this, see [Enabling and configuring event notifications using the Amazon S3 console](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html) in the Amazon S3 documentation.In the **Destination** section, choose **SNS topic** and specify the ARN of the SNS topic that you created earlier. | AWS DevOps, Cloud architect |
| Repeat this epic for all required Regions. | Repeat the tasks in this epic for each Region that you want to receive Amazon S3 event notifications from, including your central Region. | AWS DevOps, Cloud architect |

## Related resources
<a name="subscribe-a-lambda-function-to-event-notifications-from-s3-buckets-in-different-aws-regions-resources"></a>
+ [Configuring an access policy](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-add-permissions.html) (Amazon SQS documentation)
+ [Configuring an SQS queue as an event source](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource) (AWS Lambda documentation)
+ [Configuring an SQS queue to initiate a Lambda function](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-lambda-function-trigger.html) (Amazon SQS documentation)
+ [AWS::Lambda::Function resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html) (AWS CloudFormation documentation)
