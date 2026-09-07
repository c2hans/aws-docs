---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_NotificationReceptorAPI_SQSTransportArticle.html
---

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# Notification Handling Using Amazon SQS
<a name="ApiReference_NotificationReceptorAPI_SQSTransportArticle"></a>

Your application can use the Amazon Simple Queue Service (Amazon SQS) to handle Mechanical Turk notifications. By using Amazon SQS, your notifications are guaranteed to be delivered at least once. For more information about guaranteed delivery of notifications, see [Guaranteed Delivery](#ApiReference_NotificationReceptorAPI_SQSTransportArticle-guaranteed-delivery). For more information about, see [Amazon SQS](http://aws.amazon.com/sqs/).

## Creating an SQS Queue
<a name="ApiReference_NotificationReceptorAPI_SQSTransportArticle-creating-queue"></a>

You must create an Amazon SQS queue before using the SQS transport type in notification-related calls. Mechanical Turk does not create an Amazon SQS queue for you. An SQS queue can be created through the Amazon SQS API or by using the [AWS Console](http://aws.amazon.com/console/). For more information, see the [Amazon SQS documentation](http://aws.amazon.com/documentation/sqs/).

## Configuring an SQS Queue
<a name="ApiReference_NotificationReceptorAPI_SQSTransportArticle-configuring-queue"></a>

Your Amazon SQS queue permissions must be configured to allow a Mechanical Turk system account to call the `sqs:SendMessage'` action on your queue. Whether you use the management console UI or the API to configure permissions, consider the following:
+ You must add a permission that enables the account principal 'arn:aws:iam::755651556756:user/MTurk-SQS' to call [SendMessage](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QuerySendMessage.html) on your queue.
+ Your [SendMessage](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QuerySendMessage.html) permission must add an action of 'aws:SecureTransport' set to 'true'.

  Mechanical Turk always uses the secure transport; this ensures that you only enable the level of access that will actually be used.
+ You must not provide any additional permissions to this account to ensure that you only allow the access that will actually be used.
+ You should consider disallowing all other access to your queue from other accounts.

  This makes it easy for you to be sure that available messages were sent by Mechanical Turk.

  If you enable [SendMessage](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QuerySendMessage.html) for other accounts to this queue, or if you plan to send messages to this queue from your AWS account, you should check the sending identity for every message that you receive from the queue. You can do this by requesting the `SenderId` attribute in your call to [ReceiveMessage](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QueryReceiveMessage.html). This value will be `AIDAIXO4EZE6RHVSXIN4E`. Amazon SQS provides this value as a strong guarantee of the authenticated identity of the sender, so if it matches, you can be sure the message came from Mechanical Turk.

  For more information, see the [Amazon SQS Developer Guide](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/Welcome.html) and [Amazon SQS API Reference](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Welcome.html).

## Amazon SQS Policy Document Example
<a name="ApiReference_NotificationReceptorAPI_SQSTransportArticle-policy-document"></a>

 The following example policy document only creates the [SendMessage](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QuerySendMessage.html) permission for the Mechanical Turk account. You can add additional restrictions, such as setting the `aws:SecureTransport` value. For more information about policy documents, see the [Amazon SQS Developer Guide](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/Welcome.html).

## Configuring Permissions Using the AWS Console
<a name="ApiReference_NotificationReceptorAPI_SQSTransportArticle-config-console"></a>

**To configure permissions in the AWS Console:**

1. Sign in to the AWS Management Console and open the Amazon SQS console at [https://console.aws.amazon.com/sqs/](https://console.aws.amazon.com/sqs/).

1. Select your queue, and then select **Permissions**.

1. Click **Edit Policy Document**.

1. Enter a policy document similar to the example.

## Configuring Permissions Using the Amazon SQS API
<a name="ApiReference_NotificationReceptorAPI_SQSTransportArticle-config-api"></a>

 Call the Amazon SQS [SetQueueAttributes](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QuerySetQueueAttributes.html) action with the `Attribute.Name` parameter set to Policy. You can call `SetQueueAttributes` with a policy document similar to the example policy document. Do not use the Amazon SQS `AddPermission` action for configuring permissions on this queue. If you programmatically create a queue and apply a policy document to it, you must ensure the 'Resource' value in the policy document is updated with the correct queue name.

## Testing Your Queue
<a name="ApiReference_NotificationReceptorAPI_SQSTransportArticle-testing-queue"></a>

To test your permissions, call the Mechanical Turk [SendTestEventNotification](ApiReference_SendTestEventNotificationOperation.md) operation with a `Transport` of 'SQS' and your queue URL as the Destination.

## Guaranteed Delivery
<a name="ApiReference_NotificationReceptorAPI_SQSTransportArticle-guaranteed-delivery"></a>

Using Amazon SQS provides a guaranteed at-least-once delivery of each message. Mechanical Turk ensures that it calls [SendMessage](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QuerySendMessage.html) at least once for each message. SQS then provides guarantees regarding message persistence and message delivery.

Rarely, the same message may show up twice in the queue. This is an attribute of Amazon SQS's nature as a distributed system.

 If you take action on your queue that prevents Mechanical Turk from publishing to it, we cannot guarantee delivery of the messages that would have been sent to your queue. For instance, such actions may include:
+ Modifying the permissions on your queue in a way that prevents our account from calling [SendMessage](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QuerySendMessage.html) successfully.
+ Deleting or disabling your queue.

## SQS Message Ordering
<a name="ApiReference_NotificationReceptorAPI_SQSTransportArticle-message-ordering"></a>

You should expect that messages may arrive out of order. For information about message ordering behavior, see the [SQS documentation](http://aws.amazon.com/documentation/sqs/).

## Multiple SQS Queues
<a name="ApiReference_NotificationReceptorAPI_SQSTransportArticle-multiple-queues"></a>

You may use a different queue for each HITType that you configure with notifications.

Mechanical Turk does not provide the ability to route events within a HITType to different queues. For example, you might prefer to have AssignmentSubmitted events for a HITType delivered to a different queue than HITReviewable events for that same HITType. Mechanical Turk will publish both events to the same queue. You can split the events into different queues by running an SQS client that pulls the messages and republishes them to different queues depending on the event type.

## SQS Message Payload
<a name="ApiReference_NotificationReceptorAPI_SQSTransportArticle-message-payload"></a>

The body of each SQS message is a JSON-encoded structure that provides support for multiple events in each message.

The JSON-encoded structure contains the following:
+ EventDocVersion: This is the requested version that is passed in the call to [SetHITTypeNotification](ApiReference_SetHITTypeNotificationOperation.md), such as '2006-05-05'. For a requested version, Mechanical Turk will not change the structure or definition of the output payload structure in a way that is not backward-compatible.
+ EventDocId: A unique identifier for the Mechanical Turk. In rare cases, you may receive two different SQS messages for the same event, which can be detected by tracking the EventDocId values you have already seen.
+ CustomerId: Your customerId.
+ Events: A list of Event structures, described next.

The Event structure contains the following:
+ EventType: A value corresponding to the EventType value in the notification specification data structure.
+ EventTimestamp: A dateTime in the Coordinated Universal Time time zone, such as 2005-01-31T23:59:59Z.
+ HITTypeId: The HIT type ID for the event.
+ HITId: The HIT ID for the event.
+ AssignmentId: The assignment ID for the event, if applicable.

## Double Delivery
<a name="ApiReference_NotificationReceptorAPI_SQSTransportArticle-double-delivery"></a>

Amazon SQS already provides a 'MessageId' value that enables double-delivery detection in the typical SQS case. However, when receiving messages from Mechanical Turk, we recommend that you use the EventDocId value for double-delivery detection. This will cover an additional scenario in which you may see the same EventDocId in two messages with distinct MessageIds.

Most messages are safe to process twice, since they represent independent one-way state changes. Consider whether detection of repeated messages is important for your application. You may be able to simply process the message and ignore it if it appears to have been applied already.
