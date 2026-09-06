---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-geospatialpolygonlayer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GeospatialPolygonLayer
<a name="aws-properties-quicksight-analysis-geospatialpolygonlayer"></a>

The geospatial polygon layer.

## Syntax
<a name="aws-properties-quicksight-analysis-geospatialpolygonlayer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-geospatialpolygonlayer-syntax.json"></a>

```
{
  "[Style](#cfn-quicksight-analysis-geospatialpolygonlayer-style)" : {{GeospatialPolygonStyle}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-geospatialpolygonlayer-syntax.yaml"></a>

```
  [Style](#cfn-quicksight-analysis-geospatialpolygonlayer-style): {{
    GeospatialPolygonStyle}}
```

## Properties
<a name="aws-properties-quicksight-analysis-geospatialpolygonlayer-properties"></a>

`Style`  <a name="cfn-quicksight-analysis-geospatialpolygonlayer-style"></a>
The visualization style for a polygon layer.
*Required*: Yes
*Type*: [GeospatialPolygonStyle](aws-properties-quicksight-analysis-geospatialpolygonstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
