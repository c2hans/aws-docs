---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_TranscriptEvent.html
---

# TranscriptEvent
<a name="API_streaming_TranscriptEvent"></a>

The `TranscriptEvent` associated with a `TranscriptResultStream`.

Contains a set of transcription results from one or more audio segments, along with additional information per your request parameters.

## Contents
<a name="API_streaming_TranscriptEvent_Contents"></a>

 ** Transcript **   <a name="transcribe-Type-streaming_TranscriptEvent-Transcript"></a>
Contains `Results`, which contains a set of transcription results from one or more audio segments, along with additional information per your request parameters. This can include information relating to alternative transcriptions, channel identification, partial result stabilization, language identification, and other transcription-related data.
Type: [Transcript](API_streaming_Transcript.md) object
Required: No

## See Also
<a name="API_streaming_TranscriptEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/TranscriptEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/TranscriptEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/TranscriptEvent)
