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
|  `Destination`  | The destination for notification messages. <br />Type: String[See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_NotificationDataStructureArticle.html)<br />Default: None | Yes |
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
