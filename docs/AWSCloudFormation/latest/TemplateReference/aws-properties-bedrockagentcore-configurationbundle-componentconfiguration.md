---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-configurationbundle-componentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::ConfigurationBundle ComponentConfiguration
<a name="aws-properties-bedrockagentcore-configurationbundle-componentconfiguration"></a>

The configuration for a component within a configuration bundle. The component type is inferred from the component identifier ARN.

## Syntax
<a name="aws-properties-bedrockagentcore-configurationbundle-componentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-configurationbundle-componentconfiguration-syntax.json"></a>

```
{
  "[Configuration](#cfn-bedrockagentcore-configurationbundle-componentconfiguration-configuration)" : {{Json}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-configurationbundle-componentconfiguration-syntax.yaml"></a>

```
  [Configuration](#cfn-bedrockagentcore-configurationbundle-componentconfiguration-configuration): {{Json}}
```

## Properties
<a name="aws-properties-bedrockagentcore-configurationbundle-componentconfiguration-properties"></a>

`Configuration`  <a name="cfn-bedrockagentcore-configurationbundle-componentconfiguration-configuration"></a>
The configuration values as a flexible JSON document.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
