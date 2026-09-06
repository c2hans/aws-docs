---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessenvironmentartifact.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessEnvironmentArtifact
<a name="aws-properties-bedrockagentcore-harness-harnessenvironmentartifact"></a>

The environment artifact for a harness, such as a container image containing custom dependencies.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessenvironmentartifact-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessenvironmentartifact-syntax.json"></a>

```
{
  "[ContainerConfiguration](#cfn-bedrockagentcore-harness-harnessenvironmentartifact-containerconfiguration)" : {{ContainerConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessenvironmentartifact-syntax.yaml"></a>

```
  [ContainerConfiguration](#cfn-bedrockagentcore-harness-harnessenvironmentartifact-containerconfiguration): {{
    ContainerConfiguration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessenvironmentartifact-properties"></a>

`ContainerConfiguration`  <a name="cfn-bedrockagentcore-harness-harnessenvironmentartifact-containerconfiguration"></a>
Representation of a container configuration.
*Required*: No
*Type*: [ContainerConfiguration](aws-properties-bedrockagentcore-harness-containerconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
