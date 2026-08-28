---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalTranscriptEvent.html
---

# MedicalTranscriptEvent
<a name="API_streaming_MedicalTranscriptEvent"></a>

The `MedicalTranscriptEvent` associated with a `MedicalTranscriptResultStream`.

Contains a set of transcription results from one or more audio segments, along with additional information per your request parameters.

## Contents
<a name="API_streaming_MedicalTranscriptEvent_Contents"></a>

 ** Transcript **   <a name="transcribe-Type-streaming_MedicalTranscriptEvent-Transcript"></a>
Contains `Results`, which contains a set of transcription results from one or more audio segments, along with additional information per your request parameters. This can include information relating to alternative transcriptions, channel identification, partial result stabilization, language identification, and other transcription-related data.
Type: [MedicalTranscript](API_streaming_MedicalTranscript.md) object
Required: No

## See Also
<a name="API_streaming_MedicalTranscriptEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/MedicalTranscriptEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/MedicalTranscriptEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/MedicalTranscriptEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Transcribe. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transcribe` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
