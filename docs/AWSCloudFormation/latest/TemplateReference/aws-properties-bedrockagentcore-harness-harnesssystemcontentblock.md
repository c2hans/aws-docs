---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnesssystemcontentblock.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessSystemContentBlock
<a name="aws-properties-bedrockagentcore-harness-harnesssystemcontentblock"></a>

A content block in the system prompt.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnesssystemcontentblock-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnesssystemcontentblock-syntax.json"></a>

```
{
  "[Text](#cfn-bedrockagentcore-harness-harnesssystemcontentblock-text)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnesssystemcontentblock-syntax.yaml"></a>

```
  [Text](#cfn-bedrockagentcore-harness-harnesssystemcontentblock-text): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnesssystemcontentblock-properties"></a>

`Text`  <a name="cfn-bedrockagentcore-harness-harnesssystemcontentblock-text"></a>
The text content of the system prompt block.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
