---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_UpdateNotificationSettingsOperation.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

# UpdateNotificationSettings
<a name="ApiReference_UpdateNotificationSettingsOperation"></a>

## Description
<a name="ApiReference_UpdateNotificationSettingsOperation-description"></a>

The `UpdateNotificationSettings` operation creates, updates, disables or re-enables notifications for a HIT type.

 If you call the UpdateNotificationSettings operation for a HIT type that already has a notification specification, the operation replaces the old specification with a new one.

 You can call the UpdateNotificationSettings operation to enable or disable notifications for the HIT type, without having to modify the notification specification itself.

 You can call this operation at any time to change the value of the of the Active parameter of a HIT type. You can specify changes to the Active status without specifying a new notification specification (the Notification parameter).

 To change the Active status of a HIT type's notifications, the HIT type must already have a notification specification, or one must be provided in the same call to UpdateNotificationSettings.

## Request Syntax
<a name="ApiReference_UpdateNotificationSettingsOperation-request-syntax"></a>

```
{
  "HITTypeId": {{String}},

  "Notification": {{Notification data structure}},

  "Active": {{Boolean}}
 }
```

## Request Parameters
<a name="ApiReference_UpdateNotificationSettingsOperation-request-parameters"></a>

 The request accepts the following data in JSON format:

| Name | Description | Required |
| --- | --- | --- |
|  ` HITTypeId `  | The the HITTypeID whose notification specification is being updated.<br />Type: String | Yes |
|  ` Notification `  | The notification specification for the HIT type.<br />Type: [Notification](ApiReference_NotificationDataStructureArticle.md) data structure | Conditional |
|  ` Active `  | Specifies whether notifications are sent for HITs of this HIT type, according to the notification specification. You must specify either the Notification parameter or the Active parameter for the call to SetHITTypeNotification to succeed.<br />Type: Boolean | Conditional |

## Response Elements
<a name="ApiReference_UpdateNotificationSettingsOperation-response-elements"></a>

 A successful request for the `UpdateNotificationSettings` operation returns with no errors and an empty body.
