---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ModelEntry.html
---

# ModelEntry
<a name="API_ModelEntry"></a>

A model entry that specifies a model supported for an inference operation.

## Contents
<a name="API_ModelEntry_Contents"></a>

 ** model **   <a name="bedrockagentcorecontrol-Type-ModelEntry-model"></a>
The model ID or glob pattern that identifies the model (for example, `anthropic.claude-opus-*` or `openai.gpt-oss-*`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\-\._\*\?@]+(/[a-zA-Z0-9\-\._\*\?@]+)*`
Required: Yes

## See Also
<a name="API_ModelEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ModelEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ModelEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ModelEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
