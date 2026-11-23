---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_TranscriptResponse.html
---

# TranscriptResponse

Your transcript and information about your audio.

## Contents
<a name="API_TranscriptResponse_Contents"></a>

 ** Metadata **   <a name="transcribe-Type-TranscriptResponse-Metadata"></a>
Information about your audio, such as the detected language, format, and sample rate.
Type: [TranscribeAudioMetadata](API_TranscribeAudioMetadata.md) object
Required: No

 ** RedactedResults **   <a name="transcribe-Type-TranscriptResponse-RedactedResults"></a>
Your transcript with personally identifiable information (PII) redacted. Present only if you included `ContentRedaction` in your request.
Type: [TranscribeAudioResults](API_TranscribeAudioResults.md) object
Required: No

 ** Results **   <a name="transcribe-Type-TranscriptResponse-Results"></a>
Your unredacted transcript.
If you set `RedactionOutput` to `redacted`, Amazon Transcribe doesn't return this field. Use `RedactedResults` instead.
Type: [TranscribeAudioResults](API_TranscribeAudioResults.md) object
Required: No

## See Also
<a name="API_TranscriptResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/TranscriptResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/TranscriptResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/TranscriptResponse)
