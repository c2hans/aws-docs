---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-prompt-cachepointblock.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Prompt CachePointBlock
<a name="aws-properties-bedrock-prompt-cachepointblock"></a>

Defines a section of content to be cached for reuse in subsequent API calls.

## Syntax
<a name="aws-properties-bedrock-prompt-cachepointblock-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-prompt-cachepointblock-syntax.json"></a>

```
{
  "[Type](#cfn-bedrock-prompt-cachepointblock-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-prompt-cachepointblock-syntax.yaml"></a>

```
  [Type](#cfn-bedrock-prompt-cachepointblock-type): {{String}}
```

## Properties
<a name="aws-properties-bedrock-prompt-cachepointblock-properties"></a>

`Type`  <a name="cfn-bedrock-prompt-cachepointblock-type"></a>
Specifies the type of cache point within the CachePointBlock.
*Required*: Yes
*Type*: String
*Allowed values*: `default`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
