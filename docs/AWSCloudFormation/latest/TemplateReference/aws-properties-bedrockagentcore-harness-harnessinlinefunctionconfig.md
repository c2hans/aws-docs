---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessinlinefunctionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessInlineFunctionConfig
<a name="aws-properties-bedrockagentcore-harness-harnessinlinefunctionconfig"></a>

Configuration for an inline function tool. When the agent calls this tool, the tool call is returned to the caller for external execution.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessinlinefunctionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessinlinefunctionconfig-syntax.json"></a>

```
{
  "[Description](#cfn-bedrockagentcore-harness-harnessinlinefunctionconfig-description)" : {{String}},
  "[InputSchema](#cfn-bedrockagentcore-harness-harnessinlinefunctionconfig-inputschema)" : {{Json}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessinlinefunctionconfig-syntax.yaml"></a>

```
  [Description](#cfn-bedrockagentcore-harness-harnessinlinefunctionconfig-description): {{String}}
  [InputSchema](#cfn-bedrockagentcore-harness-harnessinlinefunctionconfig-inputschema): {{Json}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessinlinefunctionconfig-properties"></a>

`Description`  <a name="cfn-bedrockagentcore-harness-harnessinlinefunctionconfig-description"></a>
Description of what the tool does, provided to the model.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputSchema`  <a name="cfn-bedrockagentcore-harness-harnessinlinefunctionconfig-inputschema"></a>
JSON Schema describing the tool's input parameters.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
