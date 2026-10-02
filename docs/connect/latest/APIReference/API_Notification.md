---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Notification.html
---

# Notification
<a name="API_Notification"></a>

Contains information about a notification, including its content, priority, recipients, and metadata.

## Contents
<a name="API_Notification_Contents"></a>

 ** Arn **   <a name="connect-Type-Notification-Arn"></a>
The Amazon Resource Name (ARN) of the notification.
Type: String
Required: Yes

 ** Id **   <a name="connect-Type-Notification-Id"></a>
The unique identifier for the notification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** LastModifiedTime **   <a name="connect-Type-Notification-LastModifiedTime"></a>
The timestamp when the notification was last modified.
Type: Timestamp
Required: Yes

 ** Content **   <a name="connect-Type-Notification-Content"></a>
The localized content of the notification. A map where keys are locale codes and values are the notification text in that locale.
Type: String to string map
Valid Keys: `en_US | de_DE | es_ES | fr_FR | id_ID | it_IT | ja_JP | ko_KR | pt_BR | zh_CN | zh_TW`
Value Length Constraints: Minimum length of 0. Maximum length of 3000.
Required: No

 ** CreatedAt **   <a name="connect-Type-Notification-CreatedAt"></a>
The timestamp when the notification was created.
Type: Timestamp
Required: No

 ** ExpiresAt **   <a name="connect-Type-Notification-ExpiresAt"></a>
The timestamp when the notification expires and is no longer displayed to users.
Type: Timestamp
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-Notification-LastModifiedRegion"></a>
The AWS Region where the notification was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** Priority **   <a name="connect-Type-Notification-Priority"></a>
The priority level of the notification. Valid values are URGENT, HIGH, and LOW.
Type: String
Valid Values: `URGENT | HIGH | LOW`
Required: No

 ** Recipients **   <a name="connect-Type-Notification-Recipients"></a>
A list of Amazon Resource Names (ARNs) identifying the recipients of the notification. Maximum of 200 recipients.
Type: Array of strings
Array Members: Maximum number of 200 items.
Required: No

 ** Tags **   <a name="connect-Type-Notification-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, `{ "Tags": {"key1":"value1", "key2":"value2"} }`.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_Notification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/Notification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/Notification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/Notification)
