---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_KinesisStreamsInput.html
---

# KinesisStreamsInput
<a name="API_KinesisStreamsInput"></a>

 Identifies a Kinesis data stream as the streaming source. You provide the stream's Amazon Resource Name (ARN).

## Contents
<a name="API_KinesisStreamsInput_Contents"></a>

 ** ResourceARN **   <a name="APIReference-Type-KinesisStreamsInput-ResourceARN"></a>
The ARN of the input Kinesis data stream to read.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

## See Also
<a name="API_KinesisStreamsInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/KinesisStreamsInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/KinesisStreamsInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/KinesisStreamsInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
