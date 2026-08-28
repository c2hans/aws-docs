---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_NotificationDataStructureArticle.html
---

# Notification
<a name="ApiReference_NotificationDataStructureArticle"></a>

## Description
<a name="ApiReference_NotificationDataStructureArticle-description"></a>

 The Notification data structure describes a HIT event notification for a HIT type.

## Elements
<a name="ApiReference_NotificationDataStructureArticle-elements"></a>

 The Notification structure can contain the elements described in the following table. When the structure is used in a request, elements described as **Required** must be included for the request to succeed.

| Name | Description | Required |
| --- | --- | --- |
|  `Destination`  | The destination for notification messages. <br />Type: String+  For Amazon Simple Queue Service (Amazon SQS) notifications (if `Transport` is **SQS**), this is the URL for your Amazon SQS queue. For more information, see [Notification Handling Using Amazon SQS](ApiReference_NotificationReceptorAPI_SQSTransportArticle.md).  <br />+  For Amazon Simple Notification Service (Amazon SNS) notifications (if `Transport` is **SNS**), this is the ARN for your Amazon SNS topic. For more information, see [Notification Handling Using Amazon SNS](ApiReference_NotificationReceptorAPI_SNSTransportArticle.md).  <br />Default: None | Yes |
|  `Transport`  | The method Amazon Mechanical Turk uses to send the notification.<br />Type: String<br />Valid Values: SQS \| SNS<br />Default: None | Yes |
|  `Version`  | The version of the Notification data structure schema to use.<br />Type: String<br />Valid Values: 2014-08-15<br />Default: None | Yes |
|  `EventTypes`  | The array of one or more events that should cause notifications to be sent. The Ping event is only valid for the [SendTestEventNotification](ApiReference_SendTestEventNotificationOperation.md) operation.<br />Type: Array of Strings<br />Valid Values: AssignmentAccepted \| AssignmentAbandoned \| AssignmentReturned \| AssignmentSubmitted \| AssignmentRejected \| AssignmentApproved \| HITCreated \| HITExtended \| HITDisposed \| HITReviewable \| HITExpired \| Ping<br />Default: None | Yes |

## Example
<a name="ApiReference_NotificationDataStructureArticle-example"></a>

In the following example, the notification specification specifies that an event notification message will be published to an SNS topic when a Worker accepts a HIT.

```
{
  Destination:"arn:aws:sns:us-east-1:7429088EXAMPLE:my_mturk_topic",
  Transport: "SNS",
  Version:"2014-08-15",
  EventTypes:["AssignmentAccepted"]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
