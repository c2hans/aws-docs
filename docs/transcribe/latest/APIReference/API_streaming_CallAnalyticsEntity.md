---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_CallAnalyticsEntity.html
---

# CallAnalyticsEntity
<a name="API_streaming_CallAnalyticsEntity"></a>

Contains entities identified as personally identifiable information (PII) in your transcription output, along with various associated attributes. Examples include category, confidence score, content, type, and start and end times.

## Contents
<a name="API_streaming_CallAnalyticsEntity_Contents"></a>

 ** BeginOffsetMillis **   <a name="transcribe-Type-streaming_CallAnalyticsEntity-BeginOffsetMillis"></a>
The time, in milliseconds, from the beginning of the audio stream to the start of the identified entity.
Type: Long
Required: No

 ** Category **   <a name="transcribe-Type-streaming_CallAnalyticsEntity-Category"></a>
The category of information identified. For example, `PII`.
Type: String
Required: No

 ** Confidence **   <a name="transcribe-Type-streaming_CallAnalyticsEntity-Confidence"></a>
The confidence score associated with the identification of an entity in your transcript.
Confidence scores are values between 0 and 1. A larger value indicates a higher probability that the identified entity correctly matches the entity spoken in your media.
Type: Double
Required: No

 ** Content **   <a name="transcribe-Type-streaming_CallAnalyticsEntity-Content"></a>
The word or words that represent the identified entity.
Type: String
Required: No

 ** EndOffsetMillis **   <a name="transcribe-Type-streaming_CallAnalyticsEntity-EndOffsetMillis"></a>
The time, in milliseconds, from the beginning of the audio stream to the end of the identified entity.
Type: Long
Required: No

 ** Type **   <a name="transcribe-Type-streaming_CallAnalyticsEntity-Type"></a>
The type of PII identified. For example, `NAME` or `CREDIT_DEBIT_NUMBER`.
Type: String
Required: No

## See Also
<a name="API_streaming_CallAnalyticsEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/CallAnalyticsEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/CallAnalyticsEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/CallAnalyticsEntity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Transcribe. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transcribe` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
