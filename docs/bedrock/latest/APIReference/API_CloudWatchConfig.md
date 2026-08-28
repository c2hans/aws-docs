---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CloudWatchConfig.html
---

# CloudWatchConfig
<a name="API_CloudWatchConfig"></a>

CloudWatch logging configuration.

## Contents
<a name="API_CloudWatchConfig_Contents"></a>

 ** logGroupName **   <a name="bedrock-Type-CloudWatchConfig-logGroupName"></a>
The log group name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** roleArn **   <a name="bedrock-Type-CloudWatchConfig-roleArn"></a>
The role Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`
Required: Yes

 ** largeDataDeliveryS3Config **   <a name="bedrock-Type-CloudWatchConfig-largeDataDeliveryS3Config"></a>
S3 configuration for delivering a large amount of data.
Type: [S3Config](API_S3Config.md) object
Required: No

## See Also
<a name="API_CloudWatchConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CloudWatchConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CloudWatchConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CloudWatchConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
