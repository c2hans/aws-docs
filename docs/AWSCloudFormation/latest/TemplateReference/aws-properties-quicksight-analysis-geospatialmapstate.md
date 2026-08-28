---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-geospatialmapstate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GeospatialMapState
<a name="aws-properties-quicksight-analysis-geospatialmapstate"></a>

The map state properties for a map.

## Syntax
<a name="aws-properties-quicksight-analysis-geospatialmapstate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-geospatialmapstate-syntax.json"></a>

```
{
  "[Bounds](#cfn-quicksight-analysis-geospatialmapstate-bounds)" : {{GeospatialCoordinateBounds}},
  "[MapNavigation](#cfn-quicksight-analysis-geospatialmapstate-mapnavigation)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-geospatialmapstate-syntax.yaml"></a>

```
  [Bounds](#cfn-quicksight-analysis-geospatialmapstate-bounds): {{
    GeospatialCoordinateBounds}}
  [MapNavigation](#cfn-quicksight-analysis-geospatialmapstate-mapnavigation): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-geospatialmapstate-properties"></a>

`Bounds`  <a name="cfn-quicksight-analysis-geospatialmapstate-bounds"></a>
Property description not available.
*Required*: No
*Type*: [GeospatialCoordinateBounds](aws-properties-quicksight-analysis-geospatialcoordinatebounds.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MapNavigation`  <a name="cfn-quicksight-analysis-geospatialmapstate-mapnavigation"></a>
Enables or disables map navigation for a map.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
