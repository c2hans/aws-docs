---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-geospatialmapaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GeospatialMapAggregatedFieldWells
<a name="aws-properties-quicksight-template-geospatialmapaggregatedfieldwells"></a>

The aggregated field wells for a geospatial map.

## Syntax
<a name="aws-properties-quicksight-template-geospatialmapaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-geospatialmapaggregatedfieldwells-syntax.json"></a>

```
{
  "[Colors](#cfn-quicksight-template-geospatialmapaggregatedfieldwells-colors)" : {{[ DimensionField, ... ]}},
  "[Geospatial](#cfn-quicksight-template-geospatialmapaggregatedfieldwells-geospatial)" : {{[ DimensionField, ... ]}},
  "[Values](#cfn-quicksight-template-geospatialmapaggregatedfieldwells-values)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-geospatialmapaggregatedfieldwells-syntax.yaml"></a>

```
  [Colors](#cfn-quicksight-template-geospatialmapaggregatedfieldwells-colors): {{
    - DimensionField}}
  [Geospatial](#cfn-quicksight-template-geospatialmapaggregatedfieldwells-geospatial): {{
    - DimensionField}}
  [Values](#cfn-quicksight-template-geospatialmapaggregatedfieldwells-values): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-template-geospatialmapaggregatedfieldwells-properties"></a>

`Colors`  <a name="cfn-quicksight-template-geospatialmapaggregatedfieldwells-colors"></a>
The color field wells of a geospatial map.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-template-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Geospatial`  <a name="cfn-quicksight-template-geospatialmapaggregatedfieldwells-geospatial"></a>
The geospatial field wells of a geospatial map. Values are grouped by geospatial fields.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-template-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-template-geospatialmapaggregatedfieldwells-values"></a>
The size field wells of a geospatial map. Values are aggregated based on geospatial fields.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-template-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
