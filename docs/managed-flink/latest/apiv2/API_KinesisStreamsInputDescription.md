---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_KinesisStreamsInputDescription.html
---

# KinesisStreamsInputDescription
<a name="API_KinesisStreamsInputDescription"></a>

For a SQL-based Kinesis Data Analytics application, describes the Kinesis data stream that is configured as the streaming source in the application input configuration.

## Contents
<a name="API_KinesisStreamsInputDescription_Contents"></a>

 ** ResourceARN **   <a name="APIReference-Type-KinesisStreamsInputDescription-ResourceARN"></a>
The Amazon Resource Name (ARN) of the Kinesis data stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** RoleARN **   <a name="APIReference-Type-KinesisStreamsInputDescription-RoleARN"></a>
The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

## See Also
<a name="API_KinesisStreamsInputDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/KinesisStreamsInputDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/KinesisStreamsInputDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/KinesisStreamsInputDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
