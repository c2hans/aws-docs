---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_CallAnalyticsLanguageWithScore.html
---

# CallAnalyticsLanguageWithScore
<a name="API_streaming_CallAnalyticsLanguageWithScore"></a>

The language code that represents the language identified in your audio, including the associated confidence score.

## Contents
<a name="API_streaming_CallAnalyticsLanguageWithScore_Contents"></a>

 ** LanguageCode **   <a name="transcribe-Type-streaming_CallAnalyticsLanguageWithScore-LanguageCode"></a>
The language code of the identified language.
Type: String
Valid Values: `en-US | en-GB | es-US | fr-CA | fr-FR | en-AU | it-IT | de-DE | pt-BR`
Required: No

 ** Score **   <a name="transcribe-Type-streaming_CallAnalyticsLanguageWithScore-Score"></a>
The confidence score associated with the identified language code. Confidence scores are values between zero and one; larger values indicate a higher confidence in the identified language.
Type: Double
Required: No

## See Also
<a name="API_streaming_CallAnalyticsLanguageWithScore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/CallAnalyticsLanguageWithScore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/CallAnalyticsLanguageWithScore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/CallAnalyticsLanguageWithScore)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Transcribe. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transcribe` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
