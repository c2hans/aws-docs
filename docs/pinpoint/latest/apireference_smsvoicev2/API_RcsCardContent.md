---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RcsCardContent.html
---

# RcsCardContent
<a name="API_RcsCardContent"></a>

The content of a rich card, including title, description, media, and card-level suggested actions.

## Contents
<a name="API_RcsCardContent_Contents"></a>

 ** Description **   <a name="pinpoint-Type-RcsCardContent-Description"></a>
The description text of the card. Maximum 2000 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

 ** Media **   <a name="pinpoint-Type-RcsCardContent-Media"></a>
The media content of the card, including the file URL, optional thumbnail, and display height.
Type: [RcsCardMedia](API_RcsCardMedia.md) object
Required: No

 ** Suggestions **   <a name="pinpoint-Type-RcsCardContent-Suggestions"></a>
Card-level suggested actions. Maximum 4 suggestions per card.
Type: Array of [RcsSuggestedAction](API_RcsSuggestedAction.md) objects
Array Members: Minimum number of 0 items. Maximum number of 4 items.
Required: No

 ** Title **   <a name="pinpoint-Type-RcsCardContent-Title"></a>
The title of the card. Maximum 200 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

## See Also
<a name="API_RcsCardContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RcsCardContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RcsCardContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RcsCardContent)
