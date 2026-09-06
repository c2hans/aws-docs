---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_VideoSourceDetails.html
---

# VideoSourceDetails
<a name="API_VideoSourceDetails"></a>

Details about a video source, including its identifier, format, and time information.

## Contents
<a name="API_VideoSourceDetails_Contents"></a>

 ** endTimeMilliseconds **   <a name="qbusiness-Type-VideoSourceDetails-endTimeMilliseconds"></a>
The ending timestamp in milliseconds for the relevant video segment.
Type: Long
Required: No

 ** mediaId **   <a name="qbusiness-Type-VideoSourceDetails-mediaId"></a>
Unique identifier for the video media file.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

 ** mediaMimeType **   <a name="qbusiness-Type-VideoSourceDetails-mediaMimeType"></a>
The MIME type of the video file (e.g., video/mp4, video/avi).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** startTimeMilliseconds **   <a name="qbusiness-Type-VideoSourceDetails-startTimeMilliseconds"></a>
The starting timestamp in milliseconds for the relevant video segment.
Type: Long
Required: No

 ** videoExtractionType **   <a name="qbusiness-Type-VideoSourceDetails-videoExtractionType"></a>
The type of video extraction performed on the content.
Type: String
Valid Values: `TRANSCRIPT | SUMMARY`
Required: No

## See Also
<a name="API_VideoSourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/VideoSourceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/VideoSourceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/VideoSourceDetails)
