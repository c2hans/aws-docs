---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_CloudWatchLoggingConfiguration.html
---

# CloudWatchLoggingConfiguration
<a name="API_CloudWatchLoggingConfiguration"></a>

Configuration settings for delivering logs to Amazon CloudWatch log groups.

## Contents
<a name="API_CloudWatchLoggingConfiguration_Contents"></a>

 ** Enabled **   <a name="athena-Type-CloudWatchLoggingConfiguration-Enabled"></a>
Enables CloudWatch logging.
Type: Boolean
Required: Yes

 ** LogGroup **   <a name="athena-Type-CloudWatchLoggingConfiguration-LogGroup"></a>
The name of the log group in Amazon CloudWatch Logs where you want to publish your logs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-zA-Z0-9._/-]+$`
Required: No

 ** LogStreamNamePrefix **   <a name="athena-Type-CloudWatchLoggingConfiguration-LogStreamNamePrefix"></a>
Prefix for the CloudWatch log stream name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[^:*]*$`
Required: No

 ** LogTypes **   <a name="athena-Type-CloudWatchLoggingConfiguration-LogTypes"></a>
The types of logs that you want to publish to CloudWatch.
Type: String to array of strings map
Required: No

## See Also
<a name="API_CloudWatchLoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/CloudWatchLoggingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/CloudWatchLoggingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/CloudWatchLoggingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
