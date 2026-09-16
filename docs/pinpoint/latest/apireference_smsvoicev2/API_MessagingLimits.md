---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_MessagingLimits.html
---

# MessagingLimits
<a name="API_MessagingLimits"></a>

The messaging limits that apply to an origination identity, such as a phone number, sender ID, or RCS agent. Includes the per-capability send rates and, for supported origination identities, advisory per-provider daily message caps.

## Contents
<a name="API_MessagingLimits_Contents"></a>

 ** DailyMessageCaps **   <a name="pinpoint-Type-MessagingLimits-DailyMessageCaps"></a>
The advisory maximum number of messages that can be sent per day, keyed by provider (for example, `T-MOBILE`). Applies to 10DLC phone numbers and is omitted when no daily cap applies.
Type: String to long map
Required: No

 ** RateLimits **   <a name="pinpoint-Type-MessagingLimits-RateLimits"></a>
The maximum send rate for each supported capability, in messages per second. The map is keyed by capability, such as `SMS`, `MMS`, `VOICE`, or `RCS`.
Type: String to long map
Required: No

## See Also
<a name="API_MessagingLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/MessagingLimits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/MessagingLimits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/MessagingLimits)
