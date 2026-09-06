---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_AmazonTranscribeProcessorConfiguration.html
---

# AmazonTranscribeProcessorConfiguration
<a name="API_media-pipelines-chime_AmazonTranscribeProcessorConfiguration"></a>

A structure that contains the configuration settings for an Amazon Transcribe processor.

**Note**
Calls to this API must include a `LanguageCode`, `IdentifyLanguage`, or `IdentifyMultipleLanguages` parameter. If you include more than one of those parameters, your transcription job fails.

## Contents
<a name="API_media-pipelines-chime_AmazonTranscribeProcessorConfiguration_Contents"></a>

 ** ContentIdentificationType **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeProcessorConfiguration-ContentIdentificationType"></a>
Labels all personally identifiable information (PII) identified in your transcript.
Content identification is performed at the segment level; PII specified in `PiiEntityTypes` is flagged upon complete transcription of an audio segment.
You can’t set `ContentIdentificationType` and `ContentRedactionType` in the same request. If you set both, your request returns a `BadRequestException`.
For more information, see [Redacting or identifying personally identifiable information](https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html) in the *Amazon Transcribe Developer Guide*.
Type: String
Valid Values: `PII`
Required: No

 ** ContentRedactionType **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeProcessorConfiguration-ContentRedactionType"></a>
Redacts all personally identifiable information (PII) identified in your transcript.
Content redaction is performed at the segment level; PII specified in PiiEntityTypes is redacted upon complete transcription of an audio segment.
You can’t set ContentRedactionType and ContentIdentificationType in the same request. If you set both, your request returns a `BadRequestException`.
For more information, see [Redacting or identifying personally identifiable information](https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html) in the *Amazon Transcribe Developer Guide*.
Type: String
Valid Values: `PII`
Required: No

 ** EnablePartialResultsStabilization **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeProcessorConfiguration-EnablePartialResultsStabilization"></a>
Enables partial result stabilization for your transcription. Partial result stabilization can reduce latency in your output, but may impact accuracy.
For more information, see [Partial-result stabilization](https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization) in the *Amazon Transcribe Developer Guide*.
Type: Boolean
Required: No

 ** FilterPartialResults **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeProcessorConfiguration-FilterPartialResults"></a>
If true, `TranscriptEvents` with `IsPartial: true` are filtered out of the insights target.
Type: Boolean
Required: No

 ** IdentifyLanguage **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeProcessorConfiguration-IdentifyLanguage"></a>
Turns language identification on or off.
Type: Boolean
Required: No

 ** IdentifyMultipleLanguages **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeProcessorConfiguration-IdentifyMultipleLanguages"></a>
Turns language identification on or off for multiple languages.
Calls to this API must include a `LanguageCode`, `IdentifyLanguage`, or `IdentifyMultipleLanguages` parameter. If you include more than one of those parameters, your transcription job fails.
Type: Boolean
Required: No

 ** LanguageCode **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeProcessorConfiguration-LanguageCode"></a>
The language code that represents the language spoken in your audio.
If you're unsure of the language spoken in your audio, consider using `IdentifyLanguage` to enable automatic language identification.
For a list of languages that real-time Call Analytics supports, see the [Supported languages table](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html) in the *Amazon Transcribe Developer Guide*.
Type: String
Valid Values: `en-US | en-GB | es-US | fr-CA | fr-FR | en-AU | it-IT | de-DE | pt-BR`
Required: No

 ** LanguageModelName **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeProcessorConfiguration-LanguageModelName"></a>
The name of the custom language model that you want to use when processing your transcription. Note that language model names are case sensitive.
The language of the specified language model must match the language code you specify in your transcription request. If the languages don't match, the custom language model isn't applied. There are no errors or warnings associated with a language mismatch.
For more information, see [Custom language models](https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html) in the *Amazon Transcribe Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^[0-9a-zA-Z._-]+`
Required: No

 ** LanguageOptions **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeProcessorConfiguration-LanguageOptions"></a>
The language options for the transcription, such as automatic language detection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^[a-zA-Z-,]+`
Required: No

 ** PartialResultsStability **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeProcessorConfiguration-PartialResultsStability"></a>
The level of stability to use when you enable partial results stabilization (`EnablePartialResultsStabilization`).
Low stability provides the highest accuracy. High stability transcribes faster, but with slightly lower accuracy.
For more information, see [Partial-result stabilization](https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization) in the *Amazon Transcribe Developer Guide*.
Type: String
Valid Values: `high | medium | low`
Required: No

 ** PiiEntityTypes **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeProcessorConfiguration-PiiEntityTypes"></a>
The types of personally identifiable information (PII) to redact from a transcript. You can include as many types as you'd like, or you can select `ALL`.
To include `PiiEntityTypes` in your Call Analytics request, you must also include `ContentIdentificationType` or `ContentRedactionType`, but you can't include both.
Values must be comma-separated and can include: `ADDRESS`, `BANK_ACCOUNT_NUMBER`, `BANK_ROUTING`, `CREDIT_DEBIT_CVV`, `CREDIT_DEBIT_EXPIRY`, `CREDIT_DEBIT_NUMBER`, `EMAIL`, `NAME`, `PHONE`, `PIN`, `SSN`, or `ALL`.
If you leave this parameter empty, the default behavior is equivalent to `ALL`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[A-Z_, ]+`
Required: No

 ** PreferredLanguage **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeProcessorConfiguration-PreferredLanguage"></a>
The preferred language for the transcription.
Type: String
Valid Values: `en-US | en-GB | es-US | fr-CA | fr-FR | en-AU | it-IT | de-DE | pt-BR`
Required: No

 ** ShowSpeakerLabel **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeProcessorConfiguration-ShowSpeakerLabel"></a>
Enables speaker partitioning (diarization) in your transcription output. Speaker partitioning labels the speech from individual speakers in your media file.
For more information, see [Partitioning speakers (diarization)](https://docs.aws.amazon.com/transcribe/latest/dg/diarization.html) in the *Amazon Transcribe Developer Guide*.
Type: Boolean
Required: No

 ** VocabularyFilterMethod **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeProcessorConfiguration-VocabularyFilterMethod"></a>
The vocabulary filtering method used in your Call Analytics transcription.
Type: String
Valid Values: `remove | mask | tag`
Required: No

 ** VocabularyFilterName **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeProcessorConfiguration-VocabularyFilterName"></a>
The name of the custom vocabulary filter that you specified in your Call Analytics request.
Length Constraints: Minimum length of 1. Maximum length of 200.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^[0-9a-zA-Z._-]+`
Required: No

 ** VocabularyFilterNames **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeProcessorConfiguration-VocabularyFilterNames"></a>
The names of the custom vocabulary filter or filters using during transcription.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3000.
Pattern: `^[a-zA-Z0-9,-._]+`
Required: No

 ** VocabularyName **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeProcessorConfiguration-VocabularyName"></a>
The name of the custom vocabulary that you specified in your Call Analytics request.
Length Constraints: Minimum length of 1. Maximum length of 200.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^[0-9a-zA-Z._-]+`
Required: No

 ** VocabularyNames **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeProcessorConfiguration-VocabularyNames"></a>
The names of the custom vocabulary or vocabularies used during transcription.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3000.
Pattern: `^[a-zA-Z0-9,-._]+`
Required: No

## See Also
<a name="API_media-pipelines-chime_AmazonTranscribeProcessorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/AmazonTranscribeProcessorConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/AmazonTranscribeProcessorConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/AmazonTranscribeProcessorConfiguration)
