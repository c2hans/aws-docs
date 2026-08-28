---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_NotificationReceptorAPI_SNSTransportArticle.html
---

# Notification Handling Using Amazon SNS
<a name="ApiReference_NotificationReceptorAPI_SNSTransportArticle"></a>

 Your application can use the Amazon Simple Notification Service (Amazon SNS) to handle Mechanical Turk notifications. For more information about Amazon SNS, see [Amazon SNS](http://aws.amazon.com/sns/).

## Creating an SNS Topic
<a name="ApiReference_NotificationReceptorAPI_SNSTransportArticle-creating-topic"></a>

 You must create an Amazon SNS topic before using the SNS transport type in notification-related calls. Mechanical Turk does not create an Amazon SNS topic for you. An SNS topic can be created through the Amazon SNS API or by using the [AWS Console](http://aws.amazon.com/console/). For more information, see the [Amazon SNS documentation](http://aws.amazon.com/documentation/sns/).

## Configuring an SNS Topic
<a name="ApiReference_NotificationReceptorAPI_SNSTransportArticle-configuring-topic"></a>

Your Amazon SNS topic permissions must be configured to allow a Mechanical Turk system account to publish to your topic. Whether you use the management console UI or the API to configure permissions, consider the following:
+ You must add a permission that enables the Mechanical Turk service principal **mturk-requester.amazonaws.com** to [Publish](http://docs.aws.amazon.com/sns/latest/api/API_Publish.html) to your topic.
+  You should ensure that only notifications from your Mechanical Turk account can be published to your topic. This can be done using a `StringEquals` IAM Policy Condition for the IAM Policy Condition Key `aws:SourceAccount` in your SNS Topic Policy doc. Set the `aws:SourceAccount` value equal to the AWS Account Id that is linked to your Mechanical Turk account.

   You can determine the AWS Account Id that is linked to your Mechanical Turk account by visiting the [Mechanical Turk Developer](https://requester.mturk.com/developer) page.

   For more information on the use of IAM Policy Conditions, see the [ IAM Policy Condition Element documentation](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#Condition).
+ Your [Publish](http://docs.aws.amazon.com/sns/latest/api/API_Publish.html) permission must add an action of `aws:SecureTransport` set to **true**.
+ Limit the permissions you apply to this topic to those that will actually be used.
+ You should consider disallowing all other access to your topic from other accounts.

  This makes it easy for you to be sure that all messages were sent by Mechanical Turk.

  For more information, see the [Amazon SNS Developer Guide](http://docs.aws.amazon.com/sns/latest/dg/welcome.html) and [Amazon SNS API Reference](http://docs.aws.amazon.com/sns/latest/api/Welcome.html).

## Amazon SNS Policy Document Example
<a name="ApiReference_NotificationReceptorAPI_SNSTransportArticle-policy-document"></a>

 The following example policy document only creates the [Publish](http://docs.aws.amazon.com/sns/latest/api/API_Publish.html) permission for the Mechanical Turk account. You can add additional restrictions. For more information about policy documents, see the [Amazon SNS Developer Guide](http://docs.aws.amazon.com/sns/latest/dg/welcome.html).

## Configuring Permissions Using the AWS Console
<a name="ApiReference_NotificationReceptorAPI_SNSTransportArticle-config-console"></a>

**To configure permissions in the AWS Console:**

1. Sign in to the AWS Management Console and open the Amazon SNS console at [https://console.aws.amazon.com/sns/](https://console.aws.amazon.com/sns/).

1. Select your topic, and then select **Actions**.

1. Click **Edit Topic Policy**.

1. Enter a policy document similar to the example.

## Configuring Permissions Using the Amazon SNS API
<a name="ApiReference_NotificationReceptorAPI_SNSTransportArticle-config-api"></a>

 Call the Amazon SNS [SetTopicAttributes](http://docs.aws.amazon.com/sns/latest/api/API_SetTopicAttributes.html) action with the `AttributeName` parameter set to **Policy**. You can call `SetTopicAttributes` with a policy document similar to the example policy document. Do not use the Amazon SNS `AddPermission` action for configuring permissions on this topic. If you programmatically create a topic and apply a policy document to it, you must ensure the `Resource` value in the policy document is updated with the correct topic name.

## Testing Your Topic
<a name="ApiReference_NotificationReceptorAPI_SNSTransportArticle-testing-topic"></a>

To test your permissions, call the Mechanical Turk [SendTestEventNotification](ApiReference_SendTestEventNotificationOperation.md) operation with a `Transport` of **SNS** and your topic ARN as the `Destination`.

## SNS Message Payload
<a name="ApiReference_NotificationReceptorAPI_SNSTransportArticle-message-payload"></a>

The body of each SNS message is a JSON-encoded structure that provides support for multiple events in each message.

The JSON-encoded structure contains the following:
+ EventDocVersion: This is the requested version that is passed in the call to [UpdateNotificationSettings](ApiReference_UpdateNotificationSettingsOperation.md), such as **2014-08-15**. For a requested version, Mechanical Turk will not change the structure or definition of the output payload structure in a way that is not backward-compatible.
+ EventDocId: A unique identifier for the Mechanical Turk event. In rare cases, you may receive two different SNS messages for the same event, which can be detected by tracking the EventDocId values you have already seen.
+ CustomerId: Your Customer Id.
+ Events: A list of Event structures, described next.

The Event structure contains the following:
+ EventType: A value corresponding to the EventType value in the notification specification data structure.
+ EventTimestamp: A dateTime in the Coordinated Universal Time time zone, such as **2005-01-31T23:59:59Z**.
+ HITTypeId: The HIT type ID for the event.
+ HITId: The HIT ID for the event.
+ AssignmentId: The assignment ID for the event, if applicable.

## Double Delivery
<a name="ApiReference_NotificationReceptorAPI_SNSTransportArticle-double-delivery"></a>

When receiving messages from Mechanical Turk, we recommend that you use the `EventDocId` value for double-delivery detection.

Most messages are safe to process twice, since they represent independent one-way state changes. Consider whether detection of repeated messages is important for your application. You may be able to simply process the message and ignore it if it appears to have been applied already.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
