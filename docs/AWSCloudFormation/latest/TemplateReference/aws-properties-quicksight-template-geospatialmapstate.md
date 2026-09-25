---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-geospatialmapstate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GeospatialMapState
<a name="aws-properties-quicksight-template-geospatialmapstate"></a>

The map state properties for a map.

## Syntax
<a name="aws-properties-quicksight-template-geospatialmapstate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-geospatialmapstate-syntax.json"></a>

```
{
  "[Bounds](#cfn-quicksight-template-geospatialmapstate-bounds)" : {{GeospatialCoordinateBounds}},
  "[MapNavigation](#cfn-quicksight-template-geospatialmapstate-mapnavigation)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-geospatialmapstate-syntax.yaml"></a>

```
  [Bounds](#cfn-quicksight-template-geospatialmapstate-bounds): {{
    GeospatialCoordinateBounds}}
  [MapNavigation](#cfn-quicksight-template-geospatialmapstate-mapnavigation): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-geospatialmapstate-properties"></a>

`Bounds`  <a name="cfn-quicksight-template-geospatialmapstate-bounds"></a>
Property description not available.
*Required*: No
*Type*: [GeospatialCoordinateBounds](aws-properties-quicksight-template-geospatialcoordinatebounds.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MapNavigation`  <a name="cfn-quicksight-template-geospatialmapstate-mapnavigation"></a>
Enables or disables map navigation for a map.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
