---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SpendLimit.html
---

# SpendLimit
<a name="API_SpendLimit"></a>

Describes the current monthly spend limits for sending voice and text messages. For more information on increasing your monthly spend limit, see [ Requesting a spending quota increase ](https://docs.aws.amazon.com/sms-voice/latest/userguide/awssupport-spend-threshold.html) in the * AWS End User Messaging SMS User Guide*.

## Contents
<a name="API_SpendLimit_Contents"></a>

 ** EnforcedLimit **   <a name="pinpoint-Type-SpendLimit-EnforcedLimit"></a>
The maximum amount of money, in US dollars, that you want to be able to spend sending messages each month. This value has to be less than or equal to the amount in `MaxLimit`. To use this custom limit, `Overridden` must be set to true.
Type: Long
Required: Yes

 ** MaxLimit **   <a name="pinpoint-Type-SpendLimit-MaxLimit"></a>
 The maximum amount of money that you are able to spend to send messages each month, in US dollars.
Type: Long
Required: Yes

 ** Name **   <a name="pinpoint-Type-SpendLimit-Name"></a>
The name for the SpendLimit.
Type: String
Valid Values: `TEXT_MESSAGE_MONTHLY_SPEND_LIMIT | VOICE_MESSAGE_MONTHLY_SPEND_LIMIT | MEDIA_MESSAGE_MONTHLY_SPEND_LIMIT | NOTIFY_MESSAGE_MONTHLY_SPEND_LIMIT | RCS_MESSAGE_MONTHLY_SPEND_LIMIT`
Required: Yes

 ** Overridden **   <a name="pinpoint-Type-SpendLimit-Overridden"></a>
When set to `True`, the value that has been specified in the `EnforcedLimit` is used to determine the maximum amount in US dollars that can be spent to send messages each month, in US dollars.
Type: Boolean
Required: Yes

## See Also
<a name="API_SpendLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/SpendLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/SpendLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/SpendLimit)
