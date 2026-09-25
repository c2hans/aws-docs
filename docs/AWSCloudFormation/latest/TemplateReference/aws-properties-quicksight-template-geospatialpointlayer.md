---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-geospatialpointlayer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GeospatialPointLayer
<a name="aws-properties-quicksight-template-geospatialpointlayer"></a>

The geospatial Point layer.

## Syntax
<a name="aws-properties-quicksight-template-geospatialpointlayer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-geospatialpointlayer-syntax.json"></a>

```
{
  "[Style](#cfn-quicksight-template-geospatialpointlayer-style)" : {{GeospatialPointStyle}}
}
```

### YAML
<a name="aws-properties-quicksight-template-geospatialpointlayer-syntax.yaml"></a>

```
  [Style](#cfn-quicksight-template-geospatialpointlayer-style): {{
    GeospatialPointStyle}}
```

## Properties
<a name="aws-properties-quicksight-template-geospatialpointlayer-properties"></a>

`Style`  <a name="cfn-quicksight-template-geospatialpointlayer-style"></a>
The visualization style for a point layer.
*Required*: Yes
*Type*: [GeospatialPointStyle](aws-properties-quicksight-template-geospatialpointstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
