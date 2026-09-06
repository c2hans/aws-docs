---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-geospatialsolidcolor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GeospatialSolidColor
<a name="aws-properties-quicksight-analysis-geospatialsolidcolor"></a>

The definition for a solid color.

## Syntax
<a name="aws-properties-quicksight-analysis-geospatialsolidcolor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-geospatialsolidcolor-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-analysis-geospatialsolidcolor-color)" : {{String}},
  "[State](#cfn-quicksight-analysis-geospatialsolidcolor-state)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-geospatialsolidcolor-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-analysis-geospatialsolidcolor-color): {{String}}
  [State](#cfn-quicksight-analysis-geospatialsolidcolor-state): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-geospatialsolidcolor-properties"></a>

`Color`  <a name="cfn-quicksight-analysis-geospatialsolidcolor-color"></a>
The color and opacity values for the color.
*Required*: Yes
*Type*: String
*Pattern*: `^#[A-F0-9]{6}(?:[A-F0-9]{2})?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`State`  <a name="cfn-quicksight-analysis-geospatialsolidcolor-state"></a>
Enables and disables the view state of the color.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
