---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_TranscribeAudioMetadata.html
---

# TranscribeAudioMetadata

Information about your audio.

## Contents
<a name="API_TranscribeAudioMetadata_Contents"></a>

 ** LanguageCode **   <a name="transcribe-Type-TranscribeAudioMetadata-LanguageCode"></a>
The language of your transcript, as a locale (for example, `en-US`). Present if you used `LanguageDetectionMode`.
Type: String
Valid Values: `en-US | en-AB | en-AU | en-GB | en-IE | en-IN | en-WL | en-ZA | en-NZ | es-US | es-ES | es-MX | fr-FR | fr-CA | it-IT | de-DE | de-CH | ja-JP | pt-BR | pt-PT | zh-CN | zh-TW | zh-HK | ko-KR`
Required: No

 ** LanguageCodes **   <a name="transcribe-Type-TranscribeAudioMetadata-LanguageCodes"></a>
The language identified in your audio, and how long it's spoken. Present if you used `LanguageDetectionMode`.
Type: Array of [SyncLanguageCodeItem](API_SyncLanguageCodeItem.md) objects
Required: No

 ** MediaFormat **   <a name="transcribe-Type-TranscribeAudioMetadata-MediaFormat"></a>
The format of your audio, as detected by Amazon Transcribe.
Type: String
Valid Values: `mp3 | mp4 | wav | flac | ogg | amr | webm | m4a`
Required: No

 ** MediaSampleRateHertz **   <a name="transcribe-Type-TranscribeAudioMetadata-MediaSampleRateHertz"></a>
The sample rate of your audio, in hertz, as detected by Amazon Transcribe.
Type: Integer
Valid Range: Minimum value of 8000. Maximum value of 48000.
Required: No

 ** NumberOfChannels **   <a name="transcribe-Type-TranscribeAudioMetadata-NumberOfChannels"></a>
The number of audio channels in your media. Present if you enabled `ChannelIdentification`.
Type: Integer
Required: No

 ** SpeakersCount **   <a name="transcribe-Type-TranscribeAudioMetadata-SpeakersCount"></a>
The number of speakers identified in your audio. Present if you enabled `ShowSpeakerLabels`.
Type: Integer
Required: No

## See Also
<a name="API_TranscribeAudioMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/TranscribeAudioMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/TranscribeAudioMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/TranscribeAudioMetadata)
