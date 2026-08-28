---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_CloudWatchLoggingOptions.html
---

# CloudWatchLoggingOptions
<a name="API_CloudWatchLoggingOptions"></a>

Describes the Amazon CloudWatch logging options for your Firehose stream.

## Contents
<a name="API_CloudWatchLoggingOptions_Contents"></a>

 ** Enabled **   <a name="Firehose-Type-CloudWatchLoggingOptions-Enabled"></a>
Enables or disables CloudWatch logging.
Type: Boolean
Required: No

 ** LogGroupName **   <a name="Firehose-Type-CloudWatchLoggingOptions-LogGroupName"></a>
The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]*`
Required: No

 ** LogStreamName **   <a name="Firehose-Type-CloudWatchLoggingOptions-LogStreamName"></a>
The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `[^:*]*`
Required: No

## See Also
<a name="API_CloudWatchLoggingOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/CloudWatchLoggingOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/CloudWatchLoggingOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/CloudWatchLoggingOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
