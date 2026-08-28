---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-prompt-systemcontentblock.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Prompt SystemContentBlock
<a name="aws-properties-bedrock-prompt-systemcontentblock"></a>

Contains configurations for instructions to provide the model for how to handle input. To learn more, see [Using the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-call.html).

## Syntax
<a name="aws-properties-bedrock-prompt-systemcontentblock-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-prompt-systemcontentblock-syntax.json"></a>

```
{
  "[CachePoint](#cfn-bedrock-prompt-systemcontentblock-cachepoint)" : {{CachePointBlock}},
  "[Text](#cfn-bedrock-prompt-systemcontentblock-text)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-prompt-systemcontentblock-syntax.yaml"></a>

```
  [CachePoint](#cfn-bedrock-prompt-systemcontentblock-cachepoint): {{
    CachePointBlock}}
  [Text](#cfn-bedrock-prompt-systemcontentblock-text): {{String}}
```

## Properties
<a name="aws-properties-bedrock-prompt-systemcontentblock-properties"></a>

`CachePoint`  <a name="cfn-bedrock-prompt-systemcontentblock-cachepoint"></a>
CachePoint to include in the system prompt.
*Required*: No
*Type*: [CachePointBlock](aws-properties-bedrock-prompt-cachepointblock.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Text`  <a name="cfn-bedrock-prompt-systemcontentblock-text"></a>
A system prompt for the model.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
