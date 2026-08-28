---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-geospatialwindowoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GeospatialWindowOptions
<a name="aws-properties-quicksight-analysis-geospatialwindowoptions"></a>

The window options of the geospatial map visual.

## Syntax
<a name="aws-properties-quicksight-analysis-geospatialwindowoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-geospatialwindowoptions-syntax.json"></a>

```
{
  "[Bounds](#cfn-quicksight-analysis-geospatialwindowoptions-bounds)" : {{GeospatialCoordinateBounds}},
  "[MapZoomMode](#cfn-quicksight-analysis-geospatialwindowoptions-mapzoommode)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-geospatialwindowoptions-syntax.yaml"></a>

```
  [Bounds](#cfn-quicksight-analysis-geospatialwindowoptions-bounds): {{
    GeospatialCoordinateBounds}}
  [MapZoomMode](#cfn-quicksight-analysis-geospatialwindowoptions-mapzoommode): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-geospatialwindowoptions-properties"></a>

`Bounds`  <a name="cfn-quicksight-analysis-geospatialwindowoptions-bounds"></a>
The bounds options (north, south, west, east) of the geospatial window options.
*Required*: No
*Type*: [GeospatialCoordinateBounds](aws-properties-quicksight-analysis-geospatialcoordinatebounds.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MapZoomMode`  <a name="cfn-quicksight-analysis-geospatialwindowoptions-mapzoommode"></a>
The map zoom modes (manual, auto) of the geospatial window options.
*Required*: No
*Type*: String
*Allowed values*: `AUTO | MANUAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
