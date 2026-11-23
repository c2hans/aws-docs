---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_SyncItem.html
---

# SyncItem

A word or punctuation mark in your transcript. Labels such as `SpeakerLabel` and `ChannelLabel` are present only if you enabled the related feature.

## Contents
<a name="API_SyncItem_Contents"></a>

 ** ChannelLabel **   <a name="transcribe-Type-SyncItem-ChannelLabel"></a>
The audio channel this item came from (`ch_0` or `ch_1`). Present if you enabled `ChannelIdentification`.
Item start and end times are measured from the start of the audio, separately for each channel.
Type: String
Required: No

 ** Content **   <a name="transcribe-Type-SyncItem-Content"></a>
The word or punctuation mark. In `RedactedResults`, Amazon Transcribe replaces redacted words with `[PII]`.
Type: String
Required: No

 ** EndTime **   <a name="transcribe-Type-SyncItem-EndTime"></a>
The time, in seconds from the start of your audio, when this item ends.
Type: Double
Required: No

 ** Id **   <a name="transcribe-Type-SyncItem-Id"></a>
The position of this item in the transcript, starting at 0.
Type: Integer
Required: No

 ** LanguageCode **   <a name="transcribe-Type-SyncItem-LanguageCode"></a>
The language of this item, as a locale (for example, `en-US`).
Type: String
Valid Values: `en-US | en-AB | en-AU | en-GB | en-IE | en-IN | en-WL | en-ZA | en-NZ | es-US | es-ES | es-MX | fr-FR | fr-CA | it-IT | de-DE | de-CH | ja-JP | pt-BR | pt-PT | zh-CN | zh-TW | zh-HK | ko-KR`
Required: No

 ** Redactions **   <a name="transcribe-Type-SyncItem-Redactions"></a>
The types of personally identifiable information (PII) that Amazon Transcribe redacted from this item. Present only on redacted items in `RedactedResults`.
Type: Array of [SyncRedaction](API_SyncRedaction.md) objects
Required: No

 ** SpeakerLabel **   <a name="transcribe-Type-SyncItem-SpeakerLabel"></a>
The speaker of this item (for example, `spk_0`). Present if you enabled `ShowSpeakerLabels`.
Type: String
Required: No

 ** StartTime **   <a name="transcribe-Type-SyncItem-StartTime"></a>
The time, in seconds from the start of your audio, when this item starts.
Type: Double
Required: No

 ** VocabularyFilterMatch **   <a name="transcribe-Type-SyncItem-VocabularyFilterMatch"></a>
Indicates whether this item matched a word in your custom vocabulary filter. Present if you included `VocabularyFilterSettings`.
Type: Boolean
Required: No

## See Also
<a name="API_SyncItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/SyncItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/SyncItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/SyncItem)
