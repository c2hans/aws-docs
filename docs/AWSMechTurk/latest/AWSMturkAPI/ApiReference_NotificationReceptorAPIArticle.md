---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_NotificationReceptorAPIArticle.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

# Managing Notifications
<a name="ApiReference_NotificationReceptorAPIArticle"></a>

**Topics**
+ [Elements of a Notification Message](ApiReference_NotificationAPI_ElementsOfANotification.md)
+ [Notification Handling Using Amazon SQS](ApiReference_NotificationReceptorAPI_SQSTransportArticle.md)
+ [Notification Handling Using Amazon SNS](ApiReference_NotificationReceptorAPI_SNSTransportArticle.md)
+ [Notification](ApiReference_NotificationDataStructureArticle.md)

This section describes how to set up and handle Amazon Mechanical Turk event notification messages. A notification message describes one or more events that happened in regards to a HIT type. For more information, see [Elements of a Notification Message](ApiReference_NotificationAPI_ElementsOfANotification.md).

You can configure Amazon Mechanical Turk to notify you whenever certain events occur during the life cycle of a HIT. Mechanical Turk can send you a notification message when a Worker accepts, abandons, returns, or submits an assignment, when a HIT becomes "reviewable", or when a HIT expires, for any HIT of a given HIT type.

Notifications are specified as part of a HIT type. To set up notifications for a HIT type, you call the [UpdateNotificationSettings](ApiReference_UpdateNotificationSettingsOperation.md) operation with a HIT type ID and a notification specification. For more information about HIT types, see [Understanding HIT Types](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/Concepts_HITTypesArticle.html).

A notification specification is defined by a [Notification](ApiReference_NotificationDataStructureArticle.md) data structure, which describes a HIT event notification for the HIT type. The notification specification is passed as the `Notification` parameter when calling [UpdateNotificationSettings](ApiReference_UpdateNotificationSettingsOperation.md).

Amazon Mechanical Turk can send a notification to an Amazon Simple Queue Service (Amazon SQS) queue or to an Amazon Simple Notification Service (Amazon SNS) topic.

For more information about setting up and handling notifications, see [Creating and Managing Notifications](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/Concepts_NotificationsArticle.html).

 For more information on configuring notifications using SQS, see [Notification Handling Using Amazon SQS](ApiReference_NotificationReceptorAPI_SQSTransportArticle.md).

 For more information on configuring notifications using SNS, see [Notification Handling Using Amazon SNS](ApiReference_NotificationReceptorAPI_SNSTransportArticle.md).

You can test your application's ability to receive notifications using [SendTestEventNotification](ApiReference_SendTestEventNotificationOperation.md).
