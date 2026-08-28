---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-datemeasurefield.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis DateMeasureField
<a name="aws-properties-quicksight-analysis-datemeasurefield"></a>

The measure type field with date type columns.

## Syntax
<a name="aws-properties-quicksight-analysis-datemeasurefield-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-datemeasurefield-syntax.json"></a>

```
{
  "[AggregationFunction](#cfn-quicksight-analysis-datemeasurefield-aggregationfunction)" : {{String}},
  "[Column](#cfn-quicksight-analysis-datemeasurefield-column)" : {{ColumnIdentifier}},
  "[FieldId](#cfn-quicksight-analysis-datemeasurefield-fieldid)" : {{String}},
  "[FormatConfiguration](#cfn-quicksight-analysis-datemeasurefield-formatconfiguration)" : {{DateTimeFormatConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-datemeasurefield-syntax.yaml"></a>

```
  [AggregationFunction](#cfn-quicksight-analysis-datemeasurefield-aggregationfunction): {{String}}
  [Column](#cfn-quicksight-analysis-datemeasurefield-column): {{
    ColumnIdentifier}}
  [FieldId](#cfn-quicksight-analysis-datemeasurefield-fieldid): {{String}}
  [FormatConfiguration](#cfn-quicksight-analysis-datemeasurefield-formatconfiguration): {{
    DateTimeFormatConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-analysis-datemeasurefield-properties"></a>

`AggregationFunction`  <a name="cfn-quicksight-analysis-datemeasurefield-aggregationfunction"></a>
The aggregation function of the measure field.
*Required*: No
*Type*: [String](aws-properties-quicksight-analysis-aggregationfunction.md)
*Allowed values*: `COUNT | DISTINCT_COUNT | MIN | MAX`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Column`  <a name="cfn-quicksight-analysis-datemeasurefield-column"></a>
The column that is used in the `DateMeasureField`.
*Required*: Yes
*Type*: [ColumnIdentifier](aws-properties-quicksight-analysis-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldId`  <a name="cfn-quicksight-analysis-datemeasurefield-fieldid"></a>
The custom field ID.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FormatConfiguration`  <a name="cfn-quicksight-analysis-datemeasurefield-formatconfiguration"></a>
The format configuration of the field.
*Required*: No
*Type*: [DateTimeFormatConfiguration](aws-properties-quicksight-analysis-datetimeformatconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
