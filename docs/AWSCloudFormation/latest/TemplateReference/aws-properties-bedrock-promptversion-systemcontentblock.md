---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-promptversion-systemcontentblock.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::PromptVersion SystemContentBlock
<a name="aws-properties-bedrock-promptversion-systemcontentblock"></a>

Contains configurations for instructions to provide the model for how to handle input. To learn more, see [Using the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-call.html).

## Syntax
<a name="aws-properties-bedrock-promptversion-systemcontentblock-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-promptversion-systemcontentblock-syntax.json"></a>

```
{
  "[CachePoint](#cfn-bedrock-promptversion-systemcontentblock-cachepoint)" : {{CachePointBlock}},
  "[Text](#cfn-bedrock-promptversion-systemcontentblock-text)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-promptversion-systemcontentblock-syntax.yaml"></a>

```
  [CachePoint](#cfn-bedrock-promptversion-systemcontentblock-cachepoint): {{
    CachePointBlock}}
  [Text](#cfn-bedrock-promptversion-systemcontentblock-text): {{String}}
```

## Properties
<a name="aws-properties-bedrock-promptversion-systemcontentblock-properties"></a>

`CachePoint`  <a name="cfn-bedrock-promptversion-systemcontentblock-cachepoint"></a>
CachePoint to include in the system prompt.
*Required*: No
*Type*: [CachePointBlock](aws-properties-bedrock-promptversion-cachepointblock.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Text`  <a name="cfn-bedrock-promptversion-systemcontentblock-text"></a>
A system prompt for the model.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
