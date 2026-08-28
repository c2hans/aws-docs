---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_KinesisStreamSourceConfiguration.html
---

# KinesisStreamSourceConfiguration
<a name="API_KinesisStreamSourceConfiguration"></a>

The stream and role Amazon Resource Names (ARNs) for a Kinesis data stream used as the source for a Firehose stream.

## Contents
<a name="API_KinesisStreamSourceConfiguration_Contents"></a>

 ** KinesisStreamARN **   <a name="Firehose-Type-KinesisStreamSourceConfiguration-KinesisStreamARN"></a>
The ARN of the source Kinesis data stream. For more information, see [Amazon Kinesis Data Streams ARN Format](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kinesis-streams).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:kinesis:[a-zA-Z0-9\-]+:\d{12}:stream/[a-zA-Z0-9_.-]+`
Required: Yes

 ** RoleARN **   <a name="Firehose-Type-KinesisStreamSourceConfiguration-RoleARN"></a>
The ARN of the role that provides access to the source Kinesis data stream. For more information, see [AWS Identity and Access Management (IAM) ARN Format](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-iam).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

## See Also
<a name="API_KinesisStreamSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/KinesisStreamSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/KinesisStreamSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/KinesisStreamSourceConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
