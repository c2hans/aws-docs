---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_OrderedPhoneNumber.html
---

# OrderedPhoneNumber
<a name="API_voice-chime_OrderedPhoneNumber"></a>

A phone number for which an order has been placed.

## Contents
<a name="API_voice-chime_OrderedPhoneNumber_Contents"></a>

 ** E164PhoneNumber **   <a name="chimesdk-Type-voice-chime_OrderedPhoneNumber-E164PhoneNumber"></a>
The phone number, in E.164 format.
Type: String
Pattern: `^\+?[1-9]\d{1,14}$`
Required: No

 ** Status **   <a name="chimesdk-Type-voice-chime_OrderedPhoneNumber-Status"></a>
The phone number status.
Type: String
Valid Values: `Processing | Acquired | Failed`
Required: No

## See Also
<a name="API_voice-chime_OrderedPhoneNumber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/OrderedPhoneNumber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/OrderedPhoneNumber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/OrderedPhoneNumber)
