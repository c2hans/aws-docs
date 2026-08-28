---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_CloudWatchLogsSource.html
---

# CloudWatchLogsSource
<a name="API_CloudWatchLogsSource"></a>

The configuration for reading agent traces from CloudWatch Logs.

## Contents
<a name="API_CloudWatchLogsSource_Contents"></a>

 ** logGroupNames **   <a name="BedrockAgentCore-Type-CloudWatchLogsSource-logGroupNames"></a>
The list of CloudWatch log group names to read agent traces from. Maximum of 5 log groups.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

 ** serviceNames **   <a name="BedrockAgentCore-Type-CloudWatchLogsSource-serviceNames"></a>
The list of agent service names to filter traces within the specified log groups.
Type: Array of strings
Array Members: Fixed number of 1 item.
Required: Yes

 ** filterConfig **   <a name="BedrockAgentCore-Type-CloudWatchLogsSource-filterConfig"></a>
Optional filter configuration to narrow down which sessions to evaluate.
Type: [CloudWatchFilterConfig](API_CloudWatchFilterConfig.md) object
Required: No

## See Also
<a name="API_CloudWatchLogsSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CloudWatchLogsSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CloudWatchLogsSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CloudWatchLogsSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
