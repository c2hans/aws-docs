---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ProviderPrefix.html
---

# ProviderPrefix
<a name="API_ProviderPrefix"></a>

The configuration that controls how a provider prefix is applied to model IDs during translation.

## Contents
<a name="API_ProviderPrefix_Contents"></a>

 ** separator **   <a name="bedrockagentcorecontrol-Type-ProviderPrefix-separator"></a>
The single character that separates the provider prefix from the model name (for example, `.`). The default is `.`.
Type: String
Length Constraints: Fixed length of 1.
Required: No

 ** strip **   <a name="bedrockagentcorecontrol-Type-ProviderPrefix-strip"></a>
Whether clients can omit the provider prefix from model IDs. If `true`, the gateway accepts model IDs without the prefix and restores the full prefixed form before forwarding to the provider. The default is `false`.
Type: Boolean
Required: No

## See Also
<a name="API_ProviderPrefix_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ProviderPrefix)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ProviderPrefix)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ProviderPrefix)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
