---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-eventtrigger-intentfiltercondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::EventTrigger IntentFilterCondition
<a name="aws-properties-customerprofiles-eventtrigger-intentfiltercondition"></a>

<a name="aws-properties-customerprofiles-eventtrigger-intentfiltercondition-description"></a>The `IntentFilterCondition` property type specifies Property description not available. for an [AWS::CustomerProfiles::EventTrigger](aws-resource-customerprofiles-eventtrigger.md).

## Syntax
<a name="aws-properties-customerprofiles-eventtrigger-intentfiltercondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-eventtrigger-intentfiltercondition-syntax.json"></a>

```
{
  "[ComparisonOperator](#cfn-customerprofiles-eventtrigger-intentfiltercondition-comparisonoperator)" : {{String}},
  "[Intent](#cfn-customerprofiles-eventtrigger-intentfiltercondition-intent)" : {{Intent}},
  "[Values](#cfn-customerprofiles-eventtrigger-intentfiltercondition-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-customerprofiles-eventtrigger-intentfiltercondition-syntax.yaml"></a>

```
  [ComparisonOperator](#cfn-customerprofiles-eventtrigger-intentfiltercondition-comparisonoperator): {{String}}
  [Intent](#cfn-customerprofiles-eventtrigger-intentfiltercondition-intent): {{
    Intent}}
  [Values](#cfn-customerprofiles-eventtrigger-intentfiltercondition-values): {{
    - String}}
```

## Properties
<a name="aws-properties-customerprofiles-eventtrigger-intentfiltercondition-properties"></a>

`ComparisonOperator`  <a name="cfn-customerprofiles-eventtrigger-intentfiltercondition-comparisonoperator"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `INCLUSIVE | EXCLUSIVE | CONTAINS | GREATER_THAN | LESS_THAN | GREATER_THAN_OR_EQUAL | LESS_THAN_OR_EQUAL | EQUAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Intent`  <a name="cfn-customerprofiles-eventtrigger-intentfiltercondition-intent"></a>
Property description not available.
*Required*: Yes
*Type*: [Intent](aws-properties-customerprofiles-eventtrigger-intent.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-customerprofiles-eventtrigger-intentfiltercondition-values"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `255 | 10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
