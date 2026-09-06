---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RcsStandaloneCard.html
---

# RcsStandaloneCard
<a name="API_RcsStandaloneCard"></a>

A standalone rich card with media, title, description, and suggested actions.

## Contents
<a name="API_RcsStandaloneCard_Contents"></a>

 ** CardContent **   <a name="pinpoint-Type-RcsStandaloneCard-CardContent"></a>
The content of the rich card, including title, description, media, and card-level suggested actions.
Type: [RcsCardContent](API_RcsCardContent.md) object
Required: Yes

 ** CardOrientation **   <a name="pinpoint-Type-RcsStandaloneCard-CardOrientation"></a>
The orientation of the rich card. Valid values are HORIZONTAL and VERTICAL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[A-Z_]+`
Required: Yes

 ** ThumbnailImageAlignment **   <a name="pinpoint-Type-RcsStandaloneCard-ThumbnailImageAlignment"></a>
The alignment of the thumbnail image in a horizontal card. Valid values are LEFT and RIGHT. Only applicable when CardOrientation is HORIZONTAL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[A-Z_]+`
Required: No

## See Also
<a name="API_RcsStandaloneCard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RcsStandaloneCard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RcsStandaloneCard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RcsStandaloneCard)
