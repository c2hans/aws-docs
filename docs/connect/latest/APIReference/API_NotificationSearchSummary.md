---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_NotificationSearchSummary.html
---

# NotificationSearchSummary
<a name="API_NotificationSearchSummary"></a>

Summary information about a notification returned from a search operation.

## Contents
<a name="API_NotificationSearchSummary_Contents"></a>

 ** Arn **   <a name="connect-Type-NotificationSearchSummary-Arn"></a>
The Amazon Resource Name (ARN) of the notification.
Type: String
Required: No

 ** Content **   <a name="connect-Type-NotificationSearchSummary-Content"></a>
The localized content of the notification.
Type: String to string map
Valid Keys: `en_US | de_DE | es_ES | fr_FR | id_ID | it_IT | ja_JP | ko_KR | pt_BR | zh_CN | zh_TW`
Value Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** CreatedAt **   <a name="connect-Type-NotificationSearchSummary-CreatedAt"></a>
The timestamp when the notification was created.
Type: Timestamp
Required: No

 ** ExpiresAt **   <a name="connect-Type-NotificationSearchSummary-ExpiresAt"></a>
The timestamp when the notification expires.
Type: Timestamp
Required: No

 ** Id **   <a name="connect-Type-NotificationSearchSummary-Id"></a>
The unique identifier for the notification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** InstanceId **   <a name="connect-Type-NotificationSearchSummary-InstanceId"></a>
The identifier of the Amazon Connect instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-NotificationSearchSummary-LastModifiedRegion"></a>
The AWS Region where the notification was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-NotificationSearchSummary-LastModifiedTime"></a>
The timestamp when the notification was last modified.
Type: Timestamp
Required: No

 ** Priority **   <a name="connect-Type-NotificationSearchSummary-Priority"></a>
The priority level of the notification.
Type: String
Valid Values: `URGENT | HIGH | LOW`
Required: No

 ** Recipients **   <a name="connect-Type-NotificationSearchSummary-Recipients"></a>
A list of recipient Amazon Resource Names (ARNs).
Type: Array of strings
Array Members: Maximum number of 200 items.
Required: No

 ** Tags **   <a name="connect-Type-NotificationSearchSummary-Tags"></a>
The tags associated with the notification.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_NotificationSearchSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/NotificationSearchSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/NotificationSearchSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/NotificationSearchSummary)
