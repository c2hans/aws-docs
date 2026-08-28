---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-filledmapaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard FilledMapAggregatedFieldWells
<a name="aws-properties-quicksight-dashboard-filledmapaggregatedfieldwells"></a>

The aggregated field well of the filled map.

## Syntax
<a name="aws-properties-quicksight-dashboard-filledmapaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-filledmapaggregatedfieldwells-syntax.json"></a>

```
{
  "[Geospatial](#cfn-quicksight-dashboard-filledmapaggregatedfieldwells-geospatial)" : {{[ DimensionField, ... ]}},
  "[Values](#cfn-quicksight-dashboard-filledmapaggregatedfieldwells-values)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-filledmapaggregatedfieldwells-syntax.yaml"></a>

```
  [Geospatial](#cfn-quicksight-dashboard-filledmapaggregatedfieldwells-geospatial): {{
    - DimensionField}}
  [Values](#cfn-quicksight-dashboard-filledmapaggregatedfieldwells-values): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-filledmapaggregatedfieldwells-properties"></a>

`Geospatial`  <a name="cfn-quicksight-dashboard-filledmapaggregatedfieldwells-geospatial"></a>
The aggregated location field well of the filled map. Values are grouped by location fields.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-dashboard-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-dashboard-filledmapaggregatedfieldwells-values"></a>
The aggregated color field well of a filled map. Values are aggregated based on location fields.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-dashboard-measurefield.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
