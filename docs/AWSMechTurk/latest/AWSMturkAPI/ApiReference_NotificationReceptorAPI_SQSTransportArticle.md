---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_NotificationReceptorAPI_SQSTransportArticle.html
---

# Notification Handling Using Amazon SQS
<a name="ApiReference_NotificationReceptorAPI_SQSTransportArticle"></a>

Your application can use the Amazon Simple Queue Service (Amazon SQS) to handle Mechanical Turk notifications. By using Amazon SQS, your notifications are guaranteed to be delivered at least once. For more information about guaranteed delivery of notifications, see [Guaranteed Delivery](#ApiReference_NotificationReceptorAPI_SQSTransportArticle-guaranteed-delivery). For more information about, see [Amazon SQS](http://aws.amazon.com/sqs/).

## Creating an SQS Queue
<a name="ApiReference_NotificationReceptorAPI_SQSTransportArticle-creating-queue"></a>

You must create an Amazon SQS queue before using the SQS transport type in notification-related calls. Mechanical Turk does not create an Amazon SQS queue for you. An SQS queue can be created through the Amazon SQS API or by using the [AWS Console](http://aws.amazon.com/console/). For more information, see the [Amazon SQS documentation](http://aws.amazon.com/documentation/sqs/).

## Configuring an SQS Queue
<a name="ApiReference_NotificationReceptorAPI_SQSTransportArticle-configuring-queue"></a>

Your Amazon SQS queue permissions must be configured to allow a Mechanical Turk system account to call the `sqs:SendMessage` action on your queue. Whether you use the management console UI or the API to configure permissions, consider the following:
+ You must add a permission that enables the Mechanical Turk service principal **mturk-requester.amazonaws.com** to call [SendMessage](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QuerySendMessage.html) on your queue.
+ Your [SendMessage](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QuerySendMessage.html) permission must add an action of `aws:SecureTransport` set to **true**.
+ Limit the permissions you apply to this queue to those that will actually be used.
+ You should consider disallowing all other access to your queue from other accounts.

  This makes it easy for you to be sure that available messages were sent by Mechanical Turk.

  If you enable [SendMessage](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QuerySendMessage.html) for other accounts to this queue, or if you plan to send messages to this queue from your AWS account, you should check the sending identity for every message that you receive from the queue. You can do this by requesting the `SenderId` attribute in your call to [ReceiveMessage](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QueryReceiveMessage.html). This value will be **AIDAIXO4EZE6RHVSXIN4E**. Amazon SQS provides this value as a strong guarantee of the authenticated identity of the sender, so if it matches, you can be sure the message came from Mechanical Turk.

  For more information, see the [Amazon SQS Developer Guide](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/Welcome.html) and [Amazon SQS API Reference](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Welcome.html).

## Amazon SQS Policy Document Example
<a name="ApiReference_NotificationReceptorAPI_SQSTransportArticle-policy-document"></a>

 The following example policy document only creates the [SendMessage](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QuerySendMessage.html) permission for the Mechanical Turk account. You can add additional restrictions. For more information about policy documents, see the [Amazon SQS Developer Guide](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/Welcome.html).

## Configuring Permissions Using the AWS Console
<a name="ApiReference_NotificationReceptorAPI_SQSTransportArticle-config-console"></a>

**To configure permissions in the AWS Console:**

1. Sign in to the AWS Management Console and open the Amazon SQS console at [https://console.aws.amazon.com/sqs/](https://console.aws.amazon.com/sqs/).

1. Select your queue, and then select **Permissions**.

1. Click **Edit Policy Document**.

1. Enter a policy document similar to the example.

## Configuring Permissions Using the Amazon SQS API
<a name="ApiReference_NotificationReceptorAPI_SQSTransportArticle-config-api"></a>

 Call the Amazon SQS [SetQueueAttributes](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QuerySetQueueAttributes.html) action with the `Attribute.Name` parameter set to **Policy**. You can call `SetQueueAttributes` with a policy document similar to the example policy document. Do not use the Amazon SQS `AddPermission` action for configuring permissions on this queue. If you programmatically create a queue and apply a policy document to it, you must ensure the `Resource` value in the policy document is updated with the correct queue name.

## Testing Your Queue
<a name="ApiReference_NotificationReceptorAPI_SQSTransportArticle-testing-queue"></a>

To test your permissions, call the Mechanical Turk [SendTestEventNotification](ApiReference_SendTestEventNotificationOperation.md) operation with a `Transport` of **SQS** and your queue URL as the `Destination`.

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
+ EventDocVersion: This is the requested version that is passed in the call to [UpdateNotificationSettings](ApiReference_UpdateNotificationSettingsOperation.md), such as **2014-08-15**. For a requested version, Mechanical Turk will not change the structure or definition of the output payload structure in a way that is not backward-compatible.
+ EventDocId: A unique identifier for the Mechanical Turk event. In rare cases, you may receive two different SQS messages for the same event, which can be detected by tracking the EventDocId values you have already seen.
+ CustomerId: Your Customer Id.
+ Events: A list of Event structures, described next.

The Event structure contains the following:
+ EventType: A value corresponding to the EventType value in the notification specification data structure.
+ EventTimestamp: A dateTime in the Coordinated Universal Time time zone, such as **2005-01-31T23:59:59Z**.
+ HITTypeId: The HIT type ID for the event.
+ HITId: The HIT ID for the event.
+ AssignmentId: The assignment ID for the event, if applicable.

## Double Delivery
<a name="ApiReference_NotificationReceptorAPI_SQSTransportArticle-double-delivery"></a>

Amazon SQS already provides a `MessageId` value that enables double-delivery detection in the typical SQS case. However, when receiving messages from Mechanical Turk, we recommend that you use the EventDocId value for double-delivery detection. This will cover an additional scenario in which you may see the same EventDocId in two messages with distinct MessageIds.

Most messages are safe to process twice, since they represent independent one-way state changes. Consider whether detection of repeated messages is important for your application. You may be able to simply process the message and ignore it if it appears to have been applied already.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
