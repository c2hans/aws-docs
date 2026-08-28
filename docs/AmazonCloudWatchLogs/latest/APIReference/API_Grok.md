---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_Grok.html
---

# Grok
<a name="API_Grok"></a>

This processor uses pattern matching to parse and structure unstructured data. This processor can also extract fields from log messages.

For more information about this processor including examples, see [grok](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Configurable.html#CloudWatch-Logs-Transformation-Grok) in the *CloudWatch Logs User Guide*.

## Contents
<a name="API_Grok_Contents"></a>

 ** match **   <a name="CWL-Type-Grok-match"></a>
The grok pattern to match against the log event. For a list of supported grok patterns, see [Supported grok patterns](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Configurable.html#CloudWatch-Logs-Transformation-Grok).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** source **   <a name="CWL-Type-Grok-source"></a>
The path to the field in the log event that you want to parse. If you omit this value, the whole log message is parsed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_Grok_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/Grok)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/Grok)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/Grok)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
