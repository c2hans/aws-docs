---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_AgentSkillsDescriptor.html
---

# AgentSkillsDescriptor
<a name="API_AgentSkillsDescriptor"></a>

 The agent skills descriptor configuration for a registry record.

## Contents
<a name="API_AgentSkillsDescriptor_Contents"></a>

 ** skillMd **   <a name="BedrockAgentCore-Type-AgentSkillsDescriptor-skillMd"></a>
 The skill description in markdown format.
Type: [SkillMdDefinition](API_SkillMdDefinition.md) object
Required: Yes

 ** skillDefinition **   <a name="BedrockAgentCore-Type-AgentSkillsDescriptor-skillDefinition"></a>
 The structured skill definition with a schema version and content.
Type: [SkillDefinition](API_SkillDefinition.md) object
Required: No

## See Also
<a name="API_AgentSkillsDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/AgentSkillsDescriptor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/AgentSkillsDescriptor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/AgentSkillsDescriptor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
