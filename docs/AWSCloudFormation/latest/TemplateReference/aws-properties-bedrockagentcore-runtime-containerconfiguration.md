---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-runtime-containerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime ContainerConfiguration
<a name="aws-properties-bedrockagentcore-runtime-containerconfiguration"></a>

Representation of a container configuration.

## Syntax
<a name="aws-properties-bedrockagentcore-runtime-containerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-runtime-containerconfiguration-syntax.json"></a>

```
{
  "[ContainerUri](#cfn-bedrockagentcore-runtime-containerconfiguration-containeruri)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-runtime-containerconfiguration-syntax.yaml"></a>

```
  [ContainerUri](#cfn-bedrockagentcore-runtime-containerconfiguration-containeruri): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-runtime-containerconfiguration-properties"></a>

`ContainerUri`  <a name="cfn-bedrockagentcore-runtime-containerconfiguration-containeruri"></a>
The ECR URI of the container.
*Required*: Yes
*Type*: String
*Pattern*: `^(([0-9]{12})\.dkr\.ecr\.([a-z0-9-]+)\.([a-z0-9-]+(?:\.[a-z0-9-]+)+)|public\.ecr\.aws)/((?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*)(?::([^:@]{1,300}))?(?:@(.+))?$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
