---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_SendTestEventNotificationOperation.html
---

# SendTestEventNotification
<a name="ApiReference_SendTestEventNotificationOperation"></a>

## Description
<a name="ApiReference_SendTestEventNotificationOperation-description"></a>

The `SendTestEventNotification` operation causes Amazon Mechanical Turk to send a notification message as if a HIT event occurred, according to the provided notification specification. This allows you to test notifications without setting up notifications for a real HIT type and trying to trigger them using the website. When you call this operation, the service sends the test notification immediately.

## Request Syntax
<a name="ApiReference_SendTestEventNotificationOperation-request-syntax"></a>

```
{
  "Notification": {{Notification data structure}},

  "TestEventType": {{An EventType element of the Notification data structure.}}
 }
```

## Request Parameters
<a name="ApiReference_SendTestEventNotificationOperation-request-parameters"></a>

 The request accepts the following data in JSON format:

| Name | Description | Required |
| --- | --- | --- |
|  ` Notification `  | The notification specification to test. This value is identical to the value you would provide to the UpdateNotificationSettings operation when you establish the notification specification for a HIT type.<br />Type: Notification data structure | Yes |
|  ` TestEventType `  | The event to simulate to test the notification specification. This event is included in the test message even if the notification specification does not include the event type. The notification specification does not filter out the test event.<br />Type: An EventType element of the Notification data structure. | Yes |

## Response Elements
<a name="ApiReference_SendTestEventNotificationOperation-response-elements"></a>

 A successful request for the `SendTestEventNotification` operation returns with no errors and an empty body.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
