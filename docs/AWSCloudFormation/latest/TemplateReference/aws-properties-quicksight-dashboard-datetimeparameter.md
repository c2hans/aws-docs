---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-datetimeparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DateTimeParameter
<a name="aws-properties-quicksight-dashboard-datetimeparameter"></a>

A date-time parameter.

## Syntax
<a name="aws-properties-quicksight-dashboard-datetimeparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-datetimeparameter-syntax.json"></a>

```
{
  "[Name](#cfn-quicksight-dashboard-datetimeparameter-name)" : {{String}},
  "[Values](#cfn-quicksight-dashboard-datetimeparameter-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-datetimeparameter-syntax.yaml"></a>

```
  [Name](#cfn-quicksight-dashboard-datetimeparameter-name): {{String}}
  [Values](#cfn-quicksight-dashboard-datetimeparameter-values): {{
    - String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-datetimeparameter-properties"></a>

`Name`  <a name="cfn-quicksight-dashboard-datetimeparameter-name"></a>
A display name for the date-time parameter.
*Required*: Yes
*Type*: String
*Pattern*: `\S`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-dashboard-datetimeparameter-values"></a>
The values for the date-time parameter.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
