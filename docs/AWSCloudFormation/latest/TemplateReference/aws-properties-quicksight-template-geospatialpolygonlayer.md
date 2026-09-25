---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-geospatialpolygonlayer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GeospatialPolygonLayer
<a name="aws-properties-quicksight-template-geospatialpolygonlayer"></a>

The geospatial polygon layer.

## Syntax
<a name="aws-properties-quicksight-template-geospatialpolygonlayer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-geospatialpolygonlayer-syntax.json"></a>

```
{
  "[Style](#cfn-quicksight-template-geospatialpolygonlayer-style)" : {{GeospatialPolygonStyle}}
}
```

### YAML
<a name="aws-properties-quicksight-template-geospatialpolygonlayer-syntax.yaml"></a>

```
  [Style](#cfn-quicksight-template-geospatialpolygonlayer-style): {{
    GeospatialPolygonStyle}}
```

## Properties
<a name="aws-properties-quicksight-template-geospatialpolygonlayer-properties"></a>

`Style`  <a name="cfn-quicksight-template-geospatialpolygonlayer-style"></a>
The visualization style for a polygon layer.
*Required*: Yes
*Type*: [GeospatialPolygonStyle](aws-properties-quicksight-template-geospatialpolygonstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
