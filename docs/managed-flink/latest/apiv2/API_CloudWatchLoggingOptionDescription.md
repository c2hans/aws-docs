---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CloudWatchLoggingOptionDescription.html
---

# CloudWatchLoggingOptionDescription
<a name="API_CloudWatchLoggingOptionDescription"></a>

Describes the Amazon CloudWatch logging option.

## Contents
<a name="API_CloudWatchLoggingOptionDescription_Contents"></a>

 ** LogStreamARN **   <a name="APIReference-Type-CloudWatchLoggingOptionDescription-LogStreamARN"></a>
The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** CloudWatchLoggingOptionId **   <a name="APIReference-Type-CloudWatchLoggingOptionDescription-CloudWatchLoggingOptionId"></a>
The ID of the CloudWatch logging option description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** RoleARN **   <a name="APIReference-Type-CloudWatchLoggingOptionDescription-RoleARN"></a>
The IAM ARN of the role to use to send application messages.
Provided for backward compatibility. Applications created with the current API version have an application-level service execution role rather than a resource-level role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

## See Also
<a name="API_CloudWatchLoggingOptionDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/CloudWatchLoggingOptionDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/CloudWatchLoggingOptionDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/CloudWatchLoggingOptionDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
