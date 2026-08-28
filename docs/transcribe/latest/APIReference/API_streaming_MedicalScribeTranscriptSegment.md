---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalScribeTranscriptSegment.html
---

# MedicalScribeTranscriptSegment
<a name="API_streaming_MedicalScribeTranscriptSegment"></a>

Contains a set of transcription results, along with additional information of the segment.

## Contents
<a name="API_streaming_MedicalScribeTranscriptSegment_Contents"></a>

 ** BeginAudioTime **   <a name="transcribe-Type-streaming_MedicalScribeTranscriptSegment-BeginAudioTime"></a>
The start time, in milliseconds, of the segment.
Type: Double
Required: No

 ** ChannelId **   <a name="transcribe-Type-streaming_MedicalScribeTranscriptSegment-ChannelId"></a>
Indicates which audio channel is associated with the `MedicalScribeTranscriptSegment`.
If `MedicalScribeChannelDefinition` is not provided in the `MedicalScribeConfigurationEvent`, then this field will not be included.
Type: String
Required: No

 ** Content **   <a name="transcribe-Type-streaming_MedicalScribeTranscriptSegment-Content"></a>
Contains transcribed text of the segment.
Type: String
Required: No

 ** EndAudioTime **   <a name="transcribe-Type-streaming_MedicalScribeTranscriptSegment-EndAudioTime"></a>
The end time, in milliseconds, of the segment.
Type: Double
Required: No

 ** IsPartial **   <a name="transcribe-Type-streaming_MedicalScribeTranscriptSegment-IsPartial"></a>
Indicates if the segment is complete.
If `IsPartial` is `true`, the segment is not complete. If `IsPartial` is `false`, the segment is complete.
Type: Boolean
Required: No

 ** Items **   <a name="transcribe-Type-streaming_MedicalScribeTranscriptSegment-Items"></a>
Contains words, phrases, or punctuation marks in your segment.
Type: Array of [MedicalScribeTranscriptItem](API_streaming_MedicalScribeTranscriptItem.md) objects
Required: No

 ** SegmentId **   <a name="transcribe-Type-streaming_MedicalScribeTranscriptSegment-SegmentId"></a>
The identifier of the segment.
Type: String
Required: No

## See Also
<a name="API_streaming_MedicalScribeTranscriptSegment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/MedicalScribeTranscriptSegment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/MedicalScribeTranscriptSegment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/MedicalScribeTranscriptSegment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Transcribe. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transcribe` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
