---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-agent-agenttag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Agent AgentTag
<a name="aws-properties-quicksight-agent-agenttag"></a>

A key-value pair that represents a resource tag assigned to the agent.

## Syntax
<a name="aws-properties-quicksight-agent-agenttag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-agent-agenttag-syntax.json"></a>

```
{
  "[Key](#cfn-quicksight-agent-agenttag-key)" : {{String}},
  "[Value](#cfn-quicksight-agent-agenttag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-agent-agenttag-syntax.yaml"></a>

```
  [Key](#cfn-quicksight-agent-agenttag-key): {{String}}
  [Value](#cfn-quicksight-agent-agenttag-value): {{String}}
```

## Properties
<a name="aws-properties-quicksight-agent-agenttag-properties"></a>

`Key`  <a name="cfn-quicksight-agent-agenttag-key"></a>
The key of the resource tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-quicksight-agent-agenttag-value"></a>
The value of the resource tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
