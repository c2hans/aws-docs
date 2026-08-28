---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CustomExtractionConfiguration.html
---

# CustomExtractionConfiguration
<a name="API_CustomExtractionConfiguration"></a>

Contains custom extraction configuration information.

## Contents
<a name="API_CustomExtractionConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** episodicExtractionOverride **   <a name="bedrockagentcorecontrol-Type-CustomExtractionConfiguration-episodicExtractionOverride"></a>
The configurations to override the default extraction step for the episodic memory strategy.
Type: [EpisodicExtractionOverride](API_EpisodicExtractionOverride.md) object
Required: No

 ** semanticExtractionOverride **   <a name="bedrockagentcorecontrol-Type-CustomExtractionConfiguration-semanticExtractionOverride"></a>
The semantic extraction override configuration.
Type: [SemanticExtractionOverride](API_SemanticExtractionOverride.md) object
Required: No

 ** userPreferenceExtractionOverride **   <a name="bedrockagentcorecontrol-Type-CustomExtractionConfiguration-userPreferenceExtractionOverride"></a>
The user preference extraction override configuration.
Type: [UserPreferenceExtractionOverride](API_UserPreferenceExtractionOverride.md) object
Required: No

## See Also
<a name="API_CustomExtractionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CustomExtractionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CustomExtractionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CustomExtractionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
