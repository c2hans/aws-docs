---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-prompt-contentblock.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Prompt ContentBlock
<a name="aws-properties-bedrock-prompt-contentblock"></a>

A block of content for a message that you pass to, or receive from, a model with the [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) or [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) API operations.

## Syntax
<a name="aws-properties-bedrock-prompt-contentblock-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-prompt-contentblock-syntax.json"></a>

```
{
  "[CachePoint](#cfn-bedrock-prompt-contentblock-cachepoint)" : {{CachePointBlock}},
  "[Text](#cfn-bedrock-prompt-contentblock-text)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-prompt-contentblock-syntax.yaml"></a>

```
  [CachePoint](#cfn-bedrock-prompt-contentblock-cachepoint): {{
    CachePointBlock}}
  [Text](#cfn-bedrock-prompt-contentblock-text): {{String}}
```

## Properties
<a name="aws-properties-bedrock-prompt-contentblock-properties"></a>

`CachePoint`  <a name="cfn-bedrock-prompt-contentblock-cachepoint"></a>
CachePoint to include in the message.
*Required*: No
*Type*: [CachePointBlock](aws-properties-bedrock-prompt-cachepointblock.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Text`  <a name="cfn-bedrock-prompt-contentblock-text"></a>
Text to include in the message.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
