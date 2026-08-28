---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-parameterselectablevalues.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template ParameterSelectableValues
<a name="aws-properties-quicksight-template-parameterselectablevalues"></a>

A list of selectable values that are used in a control.

## Syntax
<a name="aws-properties-quicksight-template-parameterselectablevalues-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-parameterselectablevalues-syntax.json"></a>

```
{
  "[LinkToDataSetColumn](#cfn-quicksight-template-parameterselectablevalues-linktodatasetcolumn)" : {{ColumnIdentifier}},
  "[Values](#cfn-quicksight-template-parameterselectablevalues-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-parameterselectablevalues-syntax.yaml"></a>

```
  [LinkToDataSetColumn](#cfn-quicksight-template-parameterselectablevalues-linktodatasetcolumn): {{
    ColumnIdentifier}}
  [Values](#cfn-quicksight-template-parameterselectablevalues-values): {{
    - String}}
```

## Properties
<a name="aws-properties-quicksight-template-parameterselectablevalues-properties"></a>

`LinkToDataSetColumn`  <a name="cfn-quicksight-template-parameterselectablevalues-linktodatasetcolumn"></a>
The column identifier that fetches values from the data set.
*Required*: No
*Type*: [ColumnIdentifier](aws-properties-quicksight-template-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-template-parameterselectablevalues-values"></a>
The values that are used in `ParameterSelectableValues`.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `50000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
