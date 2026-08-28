---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-measurefield.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis MeasureField
<a name="aws-properties-quicksight-analysis-measurefield"></a>

The measure (metric) type field.

## Syntax
<a name="aws-properties-quicksight-analysis-measurefield-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-measurefield-syntax.json"></a>

```
{
  "[CalculatedMeasureField](#cfn-quicksight-analysis-measurefield-calculatedmeasurefield)" : {{CalculatedMeasureField}},
  "[CategoricalMeasureField](#cfn-quicksight-analysis-measurefield-categoricalmeasurefield)" : {{CategoricalMeasureField}},
  "[DateMeasureField](#cfn-quicksight-analysis-measurefield-datemeasurefield)" : {{DateMeasureField}},
  "[NumericalMeasureField](#cfn-quicksight-analysis-measurefield-numericalmeasurefield)" : {{NumericalMeasureField}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-measurefield-syntax.yaml"></a>

```
  [CalculatedMeasureField](#cfn-quicksight-analysis-measurefield-calculatedmeasurefield): {{
    CalculatedMeasureField}}
  [CategoricalMeasureField](#cfn-quicksight-analysis-measurefield-categoricalmeasurefield): {{
    CategoricalMeasureField}}
  [DateMeasureField](#cfn-quicksight-analysis-measurefield-datemeasurefield): {{
    DateMeasureField}}
  [NumericalMeasureField](#cfn-quicksight-analysis-measurefield-numericalmeasurefield): {{
    NumericalMeasureField}}
```

## Properties
<a name="aws-properties-quicksight-analysis-measurefield-properties"></a>

`CalculatedMeasureField`  <a name="cfn-quicksight-analysis-measurefield-calculatedmeasurefield"></a>
The calculated measure field only used in pivot tables.
*Required*: No
*Type*: [CalculatedMeasureField](aws-properties-quicksight-analysis-calculatedmeasurefield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CategoricalMeasureField`  <a name="cfn-quicksight-analysis-measurefield-categoricalmeasurefield"></a>
The measure type field with categorical type columns.
*Required*: No
*Type*: [CategoricalMeasureField](aws-properties-quicksight-analysis-categoricalmeasurefield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DateMeasureField`  <a name="cfn-quicksight-analysis-measurefield-datemeasurefield"></a>
The measure type field with date type columns.
*Required*: No
*Type*: [DateMeasureField](aws-properties-quicksight-analysis-datemeasurefield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumericalMeasureField`  <a name="cfn-quicksight-analysis-measurefield-numericalmeasurefield"></a>
The measure type field with numerical type columns.
*Required*: No
*Type*: [NumericalMeasureField](aws-properties-quicksight-analysis-numericalmeasurefield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
