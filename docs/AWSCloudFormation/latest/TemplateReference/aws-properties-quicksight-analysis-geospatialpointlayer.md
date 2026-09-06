---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-geospatialpointlayer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GeospatialPointLayer
<a name="aws-properties-quicksight-analysis-geospatialpointlayer"></a>

The geospatial Point layer.

## Syntax
<a name="aws-properties-quicksight-analysis-geospatialpointlayer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-geospatialpointlayer-syntax.json"></a>

```
{
  "[Style](#cfn-quicksight-analysis-geospatialpointlayer-style)" : {{GeospatialPointStyle}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-geospatialpointlayer-syntax.yaml"></a>

```
  [Style](#cfn-quicksight-analysis-geospatialpointlayer-style): {{
    GeospatialPointStyle}}
```

## Properties
<a name="aws-properties-quicksight-analysis-geospatialpointlayer-properties"></a>

`Style`  <a name="cfn-quicksight-analysis-geospatialpointlayer-style"></a>
The visualization style for a point layer.
*Required*: Yes
*Type*: [GeospatialPointStyle](aws-properties-quicksight-analysis-geospatialpointstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
