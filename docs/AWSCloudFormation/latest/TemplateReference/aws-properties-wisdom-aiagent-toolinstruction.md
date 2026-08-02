---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiagent-toolinstruction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent ToolInstruction
<a name="aws-properties-wisdom-aiagent-toolinstruction"></a>

Instructions for using a tool.

## Syntax
<a name="aws-properties-wisdom-aiagent-toolinstruction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiagent-toolinstruction-syntax.json"></a>

```
{
  "[Examples](#cfn-wisdom-aiagent-toolinstruction-examples)" : {{[ String, ... ]}},
  "[Instruction](#cfn-wisdom-aiagent-toolinstruction-instruction)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-aiagent-toolinstruction-syntax.yaml"></a>

```
  [Examples](#cfn-wisdom-aiagent-toolinstruction-examples): {{
    - String}}
  [Instruction](#cfn-wisdom-aiagent-toolinstruction-instruction): {{String}}
```

## Properties
<a name="aws-properties-wisdom-aiagent-toolinstruction-properties"></a>

`Examples`  <a name="cfn-wisdom-aiagent-toolinstruction-examples"></a>
Examples for using the tool.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Instruction`  <a name="cfn-wisdom-aiagent-toolinstruction-instruction"></a>
The instruction text for the tool.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
