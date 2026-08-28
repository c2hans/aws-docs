---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AudioSourceDetails.html
---

# AudioSourceDetails
<a name="API_AudioSourceDetails"></a>

Details about an audio source, including its identifier, format, and time information.

## Contents
<a name="API_AudioSourceDetails_Contents"></a>

 ** audioExtractionType **   <a name="qbusiness-Type-AudioSourceDetails-audioExtractionType"></a>
The type of audio extraction performed on the content.
Type: String
Valid Values: `TRANSCRIPT | SUMMARY`
Required: No

 ** endTimeMilliseconds **   <a name="qbusiness-Type-AudioSourceDetails-endTimeMilliseconds"></a>
The ending timestamp in milliseconds for the relevant audio segment.
Type: Long
Required: No

 ** mediaId **   <a name="qbusiness-Type-AudioSourceDetails-mediaId"></a>
Unique identifier for the audio media file.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

 ** mediaMimeType **   <a name="qbusiness-Type-AudioSourceDetails-mediaMimeType"></a>
The MIME type of the audio file (e.g., audio/mp3, audio/wav).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** startTimeMilliseconds **   <a name="qbusiness-Type-AudioSourceDetails-startTimeMilliseconds"></a>
The starting timestamp in milliseconds for the relevant audio segment.
Type: Long
Required: No

## See Also
<a name="API_AudioSourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/AudioSourceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/AudioSourceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/AudioSourceDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
