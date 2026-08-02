---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiagent-tagcondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent TagCondition
<a name="aws-properties-wisdom-aiagent-tagcondition"></a>

An object that can be used to specify tag conditions.

## Syntax
<a name="aws-properties-wisdom-aiagent-tagcondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiagent-tagcondition-syntax.json"></a>

```
{
  "[Key](#cfn-wisdom-aiagent-tagcondition-key)" : {{String}},
  "[Value](#cfn-wisdom-aiagent-tagcondition-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-aiagent-tagcondition-syntax.yaml"></a>

```
  [Key](#cfn-wisdom-aiagent-tagcondition-key): {{String}}
  [Value](#cfn-wisdom-aiagent-tagcondition-value): {{String}}
```

## Properties
<a name="aws-properties-wisdom-aiagent-tagcondition-properties"></a>

`Key`  <a name="cfn-wisdom-aiagent-tagcondition-key"></a>
The tag key in the tag condition.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-wisdom-aiagent-tagcondition-value"></a>
The tag value in the tag condition.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
