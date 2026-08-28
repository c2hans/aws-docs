---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_HarnessTruncationConfiguration.html
---

# HarnessTruncationConfiguration
<a name="API_HarnessTruncationConfiguration"></a>

Configuration for truncating conversation context when it exceeds model limits.

## Contents
<a name="API_HarnessTruncationConfiguration_Contents"></a>

 ** strategy **   <a name="bedrockagentcorecontrol-Type-HarnessTruncationConfiguration-strategy"></a>
The truncation strategy to use.
Type: String
Valid Values: `sliding_window | summarization | none`
Required: Yes

 ** config **   <a name="bedrockagentcorecontrol-Type-HarnessTruncationConfiguration-config"></a>
The strategy-specific configuration.
Type: [HarnessTruncationStrategyConfiguration](API_HarnessTruncationStrategyConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_HarnessTruncationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessTruncationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessTruncationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessTruncationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
