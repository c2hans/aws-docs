---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-runtime-agentruntimeartifact.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime AgentRuntimeArtifact
<a name="aws-properties-bedrockagentcore-runtime-agentruntimeartifact"></a>

The artifact of the agent.

## Syntax
<a name="aws-properties-bedrockagentcore-runtime-agentruntimeartifact-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-runtime-agentruntimeartifact-syntax.json"></a>

```
{
  "[CodeConfiguration](#cfn-bedrockagentcore-runtime-agentruntimeartifact-codeconfiguration)" : {{CodeConfiguration}},
  "[ContainerConfiguration](#cfn-bedrockagentcore-runtime-agentruntimeartifact-containerconfiguration)" : {{ContainerConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-runtime-agentruntimeartifact-syntax.yaml"></a>

```
  [CodeConfiguration](#cfn-bedrockagentcore-runtime-agentruntimeartifact-codeconfiguration): {{
    CodeConfiguration}}
  [ContainerConfiguration](#cfn-bedrockagentcore-runtime-agentruntimeartifact-containerconfiguration): {{
    ContainerConfiguration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-runtime-agentruntimeartifact-properties"></a>

`CodeConfiguration`  <a name="cfn-bedrockagentcore-runtime-agentruntimeartifact-codeconfiguration"></a>
The code configuration for the agent runtime artifact, including the source code location and execution settings.
*Required*: No
*Type*: [CodeConfiguration](aws-properties-bedrockagentcore-runtime-codeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContainerConfiguration`  <a name="cfn-bedrockagentcore-runtime-agentruntimeartifact-containerconfiguration"></a>
The container configuration for the agent artifact.
*Required*: No
*Type*: [ContainerConfiguration](aws-properties-bedrockagentcore-runtime-containerconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
