---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-customcolor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard CustomColor
<a name="aws-properties-quicksight-dashboard-customcolor"></a>

Determines the color that's applied to a particular data value in a column.

## Syntax
<a name="aws-properties-quicksight-dashboard-customcolor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-customcolor-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-dashboard-customcolor-color)" : {{String}},
  "[FieldValue](#cfn-quicksight-dashboard-customcolor-fieldvalue)" : {{String}},
  "[SpecialValue](#cfn-quicksight-dashboard-customcolor-specialvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-customcolor-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-dashboard-customcolor-color): {{String}}
  [FieldValue](#cfn-quicksight-dashboard-customcolor-fieldvalue): {{String}}
  [SpecialValue](#cfn-quicksight-dashboard-customcolor-specialvalue): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-customcolor-properties"></a>

`Color`  <a name="cfn-quicksight-dashboard-customcolor-color"></a>
The color that is applied to the data value.
*Required*: Yes
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldValue`  <a name="cfn-quicksight-dashboard-customcolor-fieldvalue"></a>
The data value that the color is applied to.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpecialValue`  <a name="cfn-quicksight-dashboard-customcolor-specialvalue"></a>
The value of a special data value.
*Required*: No
*Type*: String
*Allowed values*: `EMPTY | NULL | OTHER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
