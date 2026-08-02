---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UserNotificationSummary.html
---

# UserNotificationSummary
<a name="API_UserNotificationSummary"></a>

Summary information about a notification for a specific user, including the user's read status.

## Contents
<a name="API_UserNotificationSummary_Contents"></a>

 ** Content **   <a name="connect-Type-UserNotificationSummary-Content"></a>
The localized content of the notification.
Type: String to string map
Valid Keys: `en_US | de_DE | es_ES | fr_FR | id_ID | it_IT | ja_JP | ko_KR | pt_BR | zh_CN | zh_TW`
Value Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** CreatedAt **   <a name="connect-Type-UserNotificationSummary-CreatedAt"></a>
The timestamp when the notification was created.
Type: Timestamp
Required: No

 ** ExpiresAt **   <a name="connect-Type-UserNotificationSummary-ExpiresAt"></a>
The timestamp when the notification expires.
Type: Timestamp
Required: No

 ** InstanceId **   <a name="connect-Type-UserNotificationSummary-InstanceId"></a>
The identifier of the Amazon Connect instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** NotificationId **   <a name="connect-Type-UserNotificationSummary-NotificationId"></a>
The unique identifier for the notification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** NotificationStatus **   <a name="connect-Type-UserNotificationSummary-NotificationStatus"></a>
The status of the notification for this user. Valid values are READ, UNREAD, and HIDDEN.
Type: String
Valid Values: `READ | UNREAD | HIDDEN`
Required: No

 ** Priority **   <a name="connect-Type-UserNotificationSummary-Priority"></a>
The priority level of the notification.
Type: String
Valid Values: `URGENT | HIGH | LOW`
Required: No

 ** RecipientId **   <a name="connect-Type-UserNotificationSummary-RecipientId"></a>
The identifier of the recipient user.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** Source **   <a name="connect-Type-UserNotificationSummary-Source"></a>
The source that created the notification. Valid values are CUSTOMER, RULES, and SYSTEM.
Type: String
Valid Values: `CUSTOMER | RULES | SYSTEM`
Required: No

## See Also
<a name="API_UserNotificationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UserNotificationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UserNotificationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UserNotificationSummary)
