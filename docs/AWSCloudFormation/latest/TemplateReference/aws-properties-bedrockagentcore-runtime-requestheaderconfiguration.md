---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-runtime-requestheaderconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime RequestHeaderConfiguration
<a name="aws-properties-bedrockagentcore-runtime-requestheaderconfiguration"></a>

Configuration for HTTP request headers that will be passed through to the runtime.

## Syntax
<a name="aws-properties-bedrockagentcore-runtime-requestheaderconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-runtime-requestheaderconfiguration-syntax.json"></a>

```
{
  "[RequestHeaderAllowlist](#cfn-bedrockagentcore-runtime-requestheaderconfiguration-requestheaderallowlist)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-runtime-requestheaderconfiguration-syntax.yaml"></a>

```
  [RequestHeaderAllowlist](#cfn-bedrockagentcore-runtime-requestheaderconfiguration-requestheaderallowlist): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-runtime-requestheaderconfiguration-properties"></a>

`RequestHeaderAllowlist`  <a name="cfn-bedrockagentcore-runtime-requestheaderconfiguration-requestheaderallowlist"></a>
A list of HTTP headers that are allowed to be passed through to the runtime.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
