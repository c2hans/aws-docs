---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_WhatsAppCallPermissionLimit.html
---

# WhatsAppCallPermissionLimit
<a name="API_WhatsAppCallPermissionLimit"></a>

A time-bound restriction on a calling action, such as the number of calls allowed within a time period.

## Contents
<a name="API_WhatsAppCallPermissionLimit_Contents"></a>

 ** currentUsage **   <a name="Social-Type-WhatsAppCallPermissionLimit-currentUsage"></a>
The number of times the action has been used within the current time period.
Type: Integer
Required: Yes

 ** maxAllowed **   <a name="Social-Type-WhatsAppCallPermissionLimit-maxAllowed"></a>
The maximum number of times the action is allowed within the time period.
Type: Integer
Required: Yes

 ** timePeriod **   <a name="Social-Type-WhatsAppCallPermissionLimit-timePeriod"></a>
The time period over which the limit applies, as an ISO 8601 duration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Required: Yes

 ** limitExpirationTime **   <a name="Social-Type-WhatsAppCallPermissionLimit-limitExpirationTime"></a>
The time when the limit resets. This value is present only when the current usage has reached the maximum allowed.
Type: Timestamp
Required: No

## See Also
<a name="API_WhatsAppCallPermissionLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/WhatsAppCallPermissionLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/WhatsAppCallPermissionLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/WhatsAppCallPermissionLimit)
