---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_TranscribeAudioResults.html
---

# TranscribeAudioResults

A transcript of your audio.

## Contents
<a name="API_TranscribeAudioResults_Contents"></a>

 ** Items **   <a name="transcribe-Type-TranscribeAudioResults-Items"></a>
The words and punctuation in your transcript, with timing and any labels you requested.
Type: Array of [SyncItem](API_SyncItem.md) objects
Required: No

 ** Transcript **   <a name="transcribe-Type-TranscribeAudioResults-Transcript"></a>
The full text of your transcript.
If you enabled `ChannelIdentification`, the text of channel `ch_0` is followed by the text of channel `ch_1`.
Type: String
Required: No

## See Also
<a name="API_TranscribeAudioResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/TranscribeAudioResults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/TranscribeAudioResults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/TranscribeAudioResults)
