---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_AudioMetadata.html
---

# AudioMetadata
<a name="API_AudioMetadata"></a>

Metadata information about an audio stream. An array of `AudioMetadata` objects for the audio streams found in a stored video is returned by [GetSegmentDetection](API_GetSegmentDetection.md).

## Contents
<a name="API_AudioMetadata_Contents"></a>

 ** Codec **   <a name="rekognition-Type-AudioMetadata-Codec"></a>
The audio codec used to encode or decode the audio stream.
Type: String
Required: No

 ** DurationMillis **   <a name="rekognition-Type-AudioMetadata-DurationMillis"></a>
The duration of the audio stream in milliseconds.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** NumberOfChannels **   <a name="rekognition-Type-AudioMetadata-NumberOfChannels"></a>
The number of audio channels in the segment.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** SampleRate **   <a name="rekognition-Type-AudioMetadata-SampleRate"></a>
The sample rate for the audio stream.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_AudioMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/AudioMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/AudioMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/AudioMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
