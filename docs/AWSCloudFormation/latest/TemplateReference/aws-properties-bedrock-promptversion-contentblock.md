---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-promptversion-contentblock.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::PromptVersion ContentBlock
<a name="aws-properties-bedrock-promptversion-contentblock"></a>

A block of content for a message that you pass to, or receive from, a model with the [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) or [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) API operations.

## Syntax
<a name="aws-properties-bedrock-promptversion-contentblock-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-promptversion-contentblock-syntax.json"></a>

```
{
  "[CachePoint](#cfn-bedrock-promptversion-contentblock-cachepoint)" : {{CachePointBlock}},
  "[Text](#cfn-bedrock-promptversion-contentblock-text)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-promptversion-contentblock-syntax.yaml"></a>

```
  [CachePoint](#cfn-bedrock-promptversion-contentblock-cachepoint): {{
    CachePointBlock}}
  [Text](#cfn-bedrock-promptversion-contentblock-text): {{String}}
```

## Properties
<a name="aws-properties-bedrock-promptversion-contentblock-properties"></a>

`CachePoint`  <a name="cfn-bedrock-promptversion-contentblock-cachepoint"></a>
CachePoint to include in the message.
*Required*: No
*Type*: [CachePointBlock](aws-properties-bedrock-promptversion-cachepointblock.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Text`  <a name="cfn-bedrock-promptversion-contentblock-text"></a>
Text to include in the message.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
