---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-parameterselectablevalues.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard ParameterSelectableValues
<a name="aws-properties-quicksight-dashboard-parameterselectablevalues"></a>

A list of selectable values that are used in a control.

## Syntax
<a name="aws-properties-quicksight-dashboard-parameterselectablevalues-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-parameterselectablevalues-syntax.json"></a>

```
{
  "[LinkToDataSetColumn](#cfn-quicksight-dashboard-parameterselectablevalues-linktodatasetcolumn)" : {{ColumnIdentifier}},
  "[Values](#cfn-quicksight-dashboard-parameterselectablevalues-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-parameterselectablevalues-syntax.yaml"></a>

```
  [LinkToDataSetColumn](#cfn-quicksight-dashboard-parameterselectablevalues-linktodatasetcolumn): {{
    ColumnIdentifier}}
  [Values](#cfn-quicksight-dashboard-parameterselectablevalues-values): {{
    - String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-parameterselectablevalues-properties"></a>

`LinkToDataSetColumn`  <a name="cfn-quicksight-dashboard-parameterselectablevalues-linktodatasetcolumn"></a>
The column identifier that fetches values from the data set.
*Required*: No
*Type*: [ColumnIdentifier](aws-properties-quicksight-dashboard-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-dashboard-parameterselectablevalues-values"></a>
The values that are used in `ParameterSelectableValues`.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `50000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
