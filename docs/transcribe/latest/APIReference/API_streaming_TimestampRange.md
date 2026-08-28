---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_TimestampRange.html
---

# TimestampRange
<a name="API_streaming_TimestampRange"></a>

Contains the timestamp range (start time through end time) of a matched category.

## Contents
<a name="API_streaming_TimestampRange_Contents"></a>

 ** BeginOffsetMillis **   <a name="transcribe-Type-streaming_TimestampRange-BeginOffsetMillis"></a>
The time, in milliseconds, from the beginning of the audio stream to the start of the category match.
Type: Long
Required: No

 ** EndOffsetMillis **   <a name="transcribe-Type-streaming_TimestampRange-EndOffsetMillis"></a>
The time, in milliseconds, from the beginning of the audio stream to the end of the category match.
Type: Long
Required: No

## See Also
<a name="API_streaming_TimestampRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/TimestampRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/TimestampRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/TimestampRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Transcribe. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transcribe` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
