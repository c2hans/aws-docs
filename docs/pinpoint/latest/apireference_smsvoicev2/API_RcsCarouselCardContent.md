---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RcsCarouselCardContent.html
---

# RcsCarouselCardContent
<a name="API_RcsCarouselCardContent"></a>

The content of a carousel card, including title, description, media, and card-level suggested actions. Media height is restricted to SHORT or MEDIUM.

## Contents
<a name="API_RcsCarouselCardContent_Contents"></a>

 ** Description **   <a name="pinpoint-Type-RcsCarouselCardContent-Description"></a>
The description text of the carousel card. Maximum 2000 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

 ** Media **   <a name="pinpoint-Type-RcsCarouselCardContent-Media"></a>
The media content of the carousel card. Media height is restricted to SHORT or MEDIUM (TALL is not supported in carousels).
Type: [RcsCarouselCardMedia](API_RcsCarouselCardMedia.md) object
Required: No

 ** Suggestions **   <a name="pinpoint-Type-RcsCarouselCardContent-Suggestions"></a>
Card-level suggested actions for this carousel card. Maximum 4 suggestions per card.
Type: Array of [RcsSuggestedAction](API_RcsSuggestedAction.md) objects
Array Members: Minimum number of 0 items. Maximum number of 4 items.
Required: No

 ** Title **   <a name="pinpoint-Type-RcsCarouselCardContent-Title"></a>
The title of the carousel card. Maximum 200 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

## See Also
<a name="API_RcsCarouselCardContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RcsCarouselCardContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RcsCarouselCardContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RcsCarouselCardContent)
