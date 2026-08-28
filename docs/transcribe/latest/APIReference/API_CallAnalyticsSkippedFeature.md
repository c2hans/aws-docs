---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_CallAnalyticsSkippedFeature.html
---

# CallAnalyticsSkippedFeature
<a name="API_CallAnalyticsSkippedFeature"></a>

Represents a skipped analytics feature during the analysis of a call analytics job.

The `Feature` field indicates the type of analytics feature that was skipped.

The `Message` field contains additional information or a message explaining why the analytics feature was skipped.

The `ReasonCode` field provides a code indicating the reason why the analytics feature was skipped.

## Contents
<a name="API_CallAnalyticsSkippedFeature_Contents"></a>

 ** Feature **   <a name="transcribe-Type-CallAnalyticsSkippedFeature-Feature"></a>
Indicates the type of analytics feature that was skipped during the analysis of a call analytics job.
Type: String
Valid Values: `GENERATIVE_SUMMARIZATION`
Required: No

 ** Message **   <a name="transcribe-Type-CallAnalyticsSkippedFeature-Message"></a>
Contains additional information or a message explaining why a specific analytics feature was skipped during the analysis of a call analytics job.
Type: String
Required: No

 ** ReasonCode **   <a name="transcribe-Type-CallAnalyticsSkippedFeature-ReasonCode"></a>
Provides a code indicating the reason why a specific analytics feature was skipped during the analysis of a call analytics job.
Type: String
Valid Values: `INSUFFICIENT_CONVERSATION_CONTENT | FAILED_SAFETY_GUIDELINES`
Required: No

## See Also
<a name="API_CallAnalyticsSkippedFeature_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/CallAnalyticsSkippedFeature)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/CallAnalyticsSkippedFeature)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/CallAnalyticsSkippedFeature)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Transcribe. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transcribe` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
