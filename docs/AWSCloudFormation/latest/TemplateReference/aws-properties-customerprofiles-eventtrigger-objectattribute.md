---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-eventtrigger-objectattribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::EventTrigger ObjectAttribute
<a name="aws-properties-customerprofiles-eventtrigger-objectattribute"></a>

The criteria that a specific object attribute must meet to trigger the destination.

## Syntax
<a name="aws-properties-customerprofiles-eventtrigger-objectattribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-eventtrigger-objectattribute-syntax.json"></a>

```
{
  "[ComparisonOperator](#cfn-customerprofiles-eventtrigger-objectattribute-comparisonoperator)" : {{String}},
  "[FieldName](#cfn-customerprofiles-eventtrigger-objectattribute-fieldname)" : {{String}},
  "[Source](#cfn-customerprofiles-eventtrigger-objectattribute-source)" : {{String}},
  "[Values](#cfn-customerprofiles-eventtrigger-objectattribute-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-customerprofiles-eventtrigger-objectattribute-syntax.yaml"></a>

```
  [ComparisonOperator](#cfn-customerprofiles-eventtrigger-objectattribute-comparisonoperator): {{String}}
  [FieldName](#cfn-customerprofiles-eventtrigger-objectattribute-fieldname): {{String}}
  [Source](#cfn-customerprofiles-eventtrigger-objectattribute-source): {{String}}
  [Values](#cfn-customerprofiles-eventtrigger-objectattribute-values): {{
    - String}}
```

## Properties
<a name="aws-properties-customerprofiles-eventtrigger-objectattribute-properties"></a>

`ComparisonOperator`  <a name="cfn-customerprofiles-eventtrigger-objectattribute-comparisonoperator"></a>
The operator used to compare an attribute against a list of values.
*Required*: Yes
*Type*: String
*Allowed values*: `INCLUSIVE | EXCLUSIVE | CONTAINS | BEGINS_WITH | ENDS_WITH | GREATER_THAN | LESS_THAN | GREATER_THAN_OR_EQUAL | LESS_THAN_OR_EQUAL | EQUAL | BEFORE | AFTER | ON | BETWEEN | NOT_BETWEEN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldName`  <a name="cfn-customerprofiles-eventtrigger-objectattribute-fieldname"></a>
A field defined within an object type.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-customerprofiles-eventtrigger-objectattribute-source"></a>
An attribute contained within a source object.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-customerprofiles-eventtrigger-objectattribute-values"></a>
The amount of time of the specified unit.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `255 | 10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
