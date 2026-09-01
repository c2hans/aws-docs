---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_CloudWatchLogsUpdateInput.html
---

# CloudWatchLogsUpdateInput
<a name="API_CloudWatchLogsUpdateInput"></a>

The updated Amazon CloudWatch Logs settings for a channel.

## Contents
<a name="API_CloudWatchLogsUpdateInput_Contents"></a>

 ** Enabled **   <a name="Streams-Type-CloudWatchLogsUpdateInput-Enabled"></a>
Specifies whether logging to Amazon CloudWatch Logs is enabled.
Type: Boolean
Required: Yes

 ** LogGroupName **   <a name="Streams-Type-CloudWatchLogsUpdateInput-LogGroupName"></a>
The name of the Amazon CloudWatch Logs log group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** LogStreamName **   <a name="Streams-Type-CloudWatchLogsUpdateInput-LogStreamName"></a>
The name of the Amazon CloudWatch Logs log stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[^:*]*`
Required: No

## See Also
<a name="API_CloudWatchLogsUpdateInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/CloudWatchLogsUpdateInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/CloudWatchLogsUpdateInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/CloudWatchLogsUpdateInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
