---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-geospatiallinelayer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard GeospatialLineLayer
<a name="aws-properties-quicksight-dashboard-geospatiallinelayer"></a>

The geospatial Line layer.

## Syntax
<a name="aws-properties-quicksight-dashboard-geospatiallinelayer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-geospatiallinelayer-syntax.json"></a>

```
{
  "[Style](#cfn-quicksight-dashboard-geospatiallinelayer-style)" : {{GeospatialLineStyle}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-geospatiallinelayer-syntax.yaml"></a>

```
  [Style](#cfn-quicksight-dashboard-geospatiallinelayer-style): {{
    GeospatialLineStyle}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-geospatiallinelayer-properties"></a>

`Style`  <a name="cfn-quicksight-dashboard-geospatiallinelayer-style"></a>
The visualization style for a line layer.
*Required*: Yes
*Type*: [GeospatialLineStyle](aws-properties-quicksight-dashboard-geospatiallinestyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
