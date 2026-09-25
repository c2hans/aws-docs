---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_NotificationTarget.html
---

# NotificationTarget
<a name="API_NotificationTarget"></a>

The destination for a notification.

## Contents
<a name="API_NotificationTarget_Contents"></a>

 ** arn **   <a name="cloudwatchomni-Type-NotificationTarget-arn"></a>
The Amazon Resource Name (ARN) of the notification target. For `slack` and `pagerduty`, an integration ARN as returned by `ListIntegrations`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:.+`
Required: Yes

 ** type **   <a name="cloudwatchomni-Type-NotificationTarget-type"></a>
The type of notification target.
Type: String
Valid Values: `sns | slack | pagerduty`
Required: Yes

 ** metadata **   <a name="cloudwatchomni-Type-NotificationTarget-metadata"></a>
Additional target-specific metadata.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_NotificationTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/NotificationTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/NotificationTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/NotificationTarget)
