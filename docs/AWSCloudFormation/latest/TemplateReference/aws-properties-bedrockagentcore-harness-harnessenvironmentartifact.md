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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
