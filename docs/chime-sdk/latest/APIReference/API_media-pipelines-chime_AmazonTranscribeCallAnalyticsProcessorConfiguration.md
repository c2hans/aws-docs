---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_AmazonTranscribeCallAnalyticsProcessorConfiguration.html
---

# AmazonTranscribeCallAnalyticsProcessorConfiguration
<a name="API_media-pipelines-chime_AmazonTranscribeCallAnalyticsProcessorConfiguration"></a>

A structure that contains the configuration settings for an Amazon Transcribe call analytics processor.

## Contents
<a name="API_media-pipelines-chime_AmazonTranscribeCallAnalyticsProcessorConfiguration_Contents"></a>

 ** LanguageCode **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeCallAnalyticsProcessorConfiguration-LanguageCode"></a>
The language code in the configuration.
Type: String
Valid Values: `en-US | en-GB | es-US | fr-CA | fr-FR | en-AU | it-IT | de-DE | pt-BR`
Required: Yes

 ** CallAnalyticsStreamCategories **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeCallAnalyticsProcessorConfiguration-CallAnalyticsStreamCategories"></a>
By default, all `CategoryEvents` are sent to the insights target. If this parameter is specified, only included categories are sent to the insights target.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^[0-9a-zA-Z._-]+`
Required: No

 ** ContentIdentificationType **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeCallAnalyticsProcessorConfiguration-ContentIdentificationType"></a>
Labels all personally identifiable information (PII) identified in your transcript.
Content identification is performed at the segment level; PII specified in `PiiEntityTypes` is flagged upon complete transcription of an audio segment.
You can’t set `ContentIdentificationType` and `ContentRedactionType` in the same request. If you do, your request returns a `BadRequestException`.
For more information, see [Redacting or identifying personally identifiable information](https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html) in the *Amazon Transcribe Developer Guide*.
Type: String
Valid Values: `PII`
Required: No

 ** ContentRedactionType **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeCallAnalyticsProcessorConfiguration-ContentRedactionType"></a>
Redacts all personally identifiable information (PII) identified in your transcript.
Content redaction is performed at the segment level; PII specified in `PiiEntityTypes` is redacted upon complete transcription of an audio segment.
You can’t set `ContentRedactionType` and `ContentIdentificationType` in the same request. If you do, your request returns a `BadRequestException`.
For more information, see [Redacting or identifying personally identifiable information](https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html) in the *Amazon Transcribe Developer Guide*.
Type: String
Valid Values: `PII`
Required: No

 ** EnablePartialResultsStabilization **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeCallAnalyticsProcessorConfiguration-EnablePartialResultsStabilization"></a>
Enables partial result stabilization for your transcription. Partial result stabilization can reduce latency in your output, but may impact accuracy. For more information, see [Partial-result stabilization](https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization) in the *Amazon Transcribe Developer Guide*.
Type: Boolean
Required: No

 ** FilterPartialResults **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeCallAnalyticsProcessorConfiguration-FilterPartialResults"></a>
If true, `UtteranceEvents` with `IsPartial: true` are filtered out of the insights target.
Type: Boolean
Required: No

 ** LanguageModelName **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeCallAnalyticsProcessorConfiguration-LanguageModelName"></a>
Specifies the name of the custom language model to use when processing a transcription. Note that language model names are case sensitive.
The language of the specified language model must match the language code specified in the transcription request. If the languages don't match, the custom language model isn't applied. Language mismatches don't generate errors or warnings.
For more information, see [Custom language models](https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html) in the *Amazon Transcribe Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^[0-9a-zA-Z._-]+`
Required: No

 ** PartialResultsStability **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeCallAnalyticsProcessorConfiguration-PartialResultsStability"></a>
Specifies the level of stability to use when you enable partial results stabilization (`EnablePartialResultsStabilization`).
Low stability provides the highest accuracy. High stability transcribes faster, but with slightly lower accuracy.
For more information, see [Partial-result stabilization](https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization) in the *Amazon Transcribe Developer Guide*.
Type: String
Valid Values: `high | medium | low`
Required: No

 ** PiiEntityTypes **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeCallAnalyticsProcessorConfiguration-PiiEntityTypes"></a>
Specifies the types of personally identifiable information (PII) to redact from a transcript. You can include as many types as you'd like, or you can select `ALL`.
To include `PiiEntityTypes` in your Call Analytics request, you must also include `ContentIdentificationType` or `ContentRedactionType`, but you can't include both.
Values must be comma-separated and can include: `ADDRESS`, `BANK_ACCOUNT_NUMBER`, `BANK_ROUTING`, `CREDIT_DEBIT_CVV`, `CREDIT_DEBIT_EXPIRY`, `CREDIT_DEBIT_NUMBER`, `EMAIL`, `NAME`, `PHONE`, `PIN`, `SSN`, or `ALL`.
Length Constraints: Minimum length of 1. Maximum length of 300.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[A-Z_, ]+`
Required: No

 ** PostCallAnalyticsSettings **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeCallAnalyticsProcessorConfiguration-PostCallAnalyticsSettings"></a>
The settings for a post-call analysis task in an analytics configuration.
Type: [PostCallAnalyticsSettings](API_media-pipelines-chime_PostCallAnalyticsSettings.md) object
Required: No

 ** VocabularyFilterMethod **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeCallAnalyticsProcessorConfiguration-VocabularyFilterMethod"></a>
Specifies how to apply a vocabulary filter to a transcript.
To replace words with **\*\*\***, choose `mask`.
To delete words, choose `remove`.
To flag words without changing them, choose `tag`.
Type: String
Valid Values: `remove | mask | tag`
Required: No

 ** VocabularyFilterName **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeCallAnalyticsProcessorConfiguration-VocabularyFilterName"></a>
Specifies the name of the custom vocabulary filter to use when processing a transcription. Note that vocabulary filter names are case sensitive.
If the language of the specified custom vocabulary filter doesn't match the language identified in your media, the vocabulary filter is not applied to your transcription.
For more information, see [Using vocabulary filtering with unwanted words](https://docs.aws.amazon.com/transcribe/latest/dg/vocabulary-filtering.html) in the *Amazon Transcribe Developer Guide*.
Length Constraints: Minimum length of 1. Maximum length of 200.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^[0-9a-zA-Z._-]+`
Required: No

 ** VocabularyName **   <a name="chimesdk-Type-media-pipelines-chime_AmazonTranscribeCallAnalyticsProcessorConfiguration-VocabularyName"></a>
Specifies the name of the custom vocabulary to use when processing a transcription. Note that vocabulary names are case sensitive.
If the language of the specified custom vocabulary doesn't match the language identified in your media, the custom vocabulary is not applied to your transcription.
For more information, see [Custom vocabularies](https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html) in the *Amazon Transcribe Developer Guide*.
Length Constraints: Minimum length of 1. Maximum length of 200.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^[0-9a-zA-Z._-]+`
Required: No

## See Also
<a name="API_media-pipelines-chime_AmazonTranscribeCallAnalyticsProcessorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/AmazonTranscribeCallAnalyticsProcessorConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/AmazonTranscribeCallAnalyticsProcessorConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/AmazonTranscribeCallAnalyticsProcessorConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
