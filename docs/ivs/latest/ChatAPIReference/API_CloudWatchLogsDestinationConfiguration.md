---
source_url: https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_CloudWatchLogsDestinationConfiguration.html
---

# CloudWatchLogsDestinationConfiguration
<a name="API_CloudWatchLogsDestinationConfiguration"></a>

Specifies a CloudWatch Logs location where chat logs will be stored.

## Contents
<a name="API_CloudWatchLogsDestinationConfiguration_Contents"></a>

 ** logGroupName **   <a name="ivs-Type-CloudWatchLogsDestinationConfiguration-logGroupName"></a>
Name of the Amazon Cloudwatch Logs destination where chat activity will be logged.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: Yes

## See Also
<a name="API_CloudWatchLogsDestinationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivschat-2020-07-14/CloudWatchLogsDestinationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivschat-2020-07-14/CloudWatchLogsDestinationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivschat-2020-07-14/CloudWatchLogsDestinationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
