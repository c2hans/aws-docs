---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SenderIdAndCountry.html
---

# SenderIdAndCountry
<a name="API_SenderIdAndCountry"></a>

 The alphanumeric sender ID in a specific country that you want to describe. For more information on sender IDs see [Requesting sender IDs ](https://docs.aws.amazon.com/sms-voice/latest/userguide/sender-id-request.html) in the * AWS End User Messaging SMS User Guide*.

## Contents
<a name="API_SenderIdAndCountry_Contents"></a>

 ** IsoCountryCode **   <a name="pinpoint-Type-SenderIdAndCountry-IsoCountryCode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: Yes

 ** SenderId **   <a name="pinpoint-Type-SenderIdAndCountry-SenderId"></a>
The unique identifier of the sender.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## See Also
<a name="API_SenderIdAndCountry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/SenderIdAndCountry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/SenderIdAndCountry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/SenderIdAndCountry)
