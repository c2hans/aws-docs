---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RcsCarouselCardMedia.html
---

# RcsCarouselCardMedia
<a name="API_RcsCarouselCardMedia"></a>

The media content of a carousel card. Display height is restricted to SHORT or MEDIUM (TALL is not supported in carousels).

## Contents
<a name="API_RcsCarouselCardMedia_Contents"></a>

 ** FileUrl **   <a name="pinpoint-Type-RcsCarouselCardMedia-FileUrl"></a>
The S3 URI of the media file for the carousel card. Maximum 2000 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `(https://|s3://).+`
Required: Yes

 ** Height **   <a name="pinpoint-Type-RcsCarouselCardMedia-Height"></a>
The display height of the media in the carousel card. Valid values are SHORT and MEDIUM.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[A-Z_]+`
Required: No

 ** ThumbnailUrl **   <a name="pinpoint-Type-RcsCarouselCardMedia-ThumbnailUrl"></a>
The S3 URI of an optional thumbnail image for the carousel card media. Maximum 2000 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `(https://|s3://).+`
Required: No

## See Also
<a name="API_RcsCarouselCardMedia_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RcsCarouselCardMedia)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RcsCarouselCardMedia)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RcsCarouselCardMedia)
