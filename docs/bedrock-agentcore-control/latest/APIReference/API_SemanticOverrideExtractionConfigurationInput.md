---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_SemanticOverrideExtractionConfigurationInput.html
---

# SemanticOverrideExtractionConfigurationInput
<a name="API_SemanticOverrideExtractionConfigurationInput"></a>

Input for semantic override extraction configuration in a memory strategy.

## Contents
<a name="API_SemanticOverrideExtractionConfigurationInput_Contents"></a>

 ** appendToPrompt **   <a name="bedrockagentcorecontrol-Type-SemanticOverrideExtractionConfigurationInput-appendToPrompt"></a>
The text to append to the prompt for semantic extraction.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30000.
Required: Yes

 ** modelId **   <a name="bedrockagentcorecontrol-Type-SemanticOverrideExtractionConfigurationInput-modelId"></a>
The model ID to use for semantic extraction.
Type: String
Required: Yes

## See Also
<a name="API_SemanticOverrideExtractionConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/SemanticOverrideExtractionConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/SemanticOverrideExtractionConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/SemanticOverrideExtractionConfigurationInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
