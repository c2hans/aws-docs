---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-geospatialcolor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GeospatialColor
<a name="aws-properties-quicksight-template-geospatialcolor"></a>

The visualization properties for solid, gradient, and categorical colors.

## Syntax
<a name="aws-properties-quicksight-template-geospatialcolor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-geospatialcolor-syntax.json"></a>

```
{
  "[Categorical](#cfn-quicksight-template-geospatialcolor-categorical)" : {{GeospatialCategoricalColor}},
  "[Gradient](#cfn-quicksight-template-geospatialcolor-gradient)" : {{GeospatialGradientColor}},
  "[Solid](#cfn-quicksight-template-geospatialcolor-solid)" : {{GeospatialSolidColor}}
}
```

### YAML
<a name="aws-properties-quicksight-template-geospatialcolor-syntax.yaml"></a>

```
  [Categorical](#cfn-quicksight-template-geospatialcolor-categorical): {{
    GeospatialCategoricalColor}}
  [Gradient](#cfn-quicksight-template-geospatialcolor-gradient): {{
    GeospatialGradientColor}}
  [Solid](#cfn-quicksight-template-geospatialcolor-solid): {{
    GeospatialSolidColor}}
```

## Properties
<a name="aws-properties-quicksight-template-geospatialcolor-properties"></a>

`Categorical`  <a name="cfn-quicksight-template-geospatialcolor-categorical"></a>
The visualization properties for the categorical color.
*Required*: No
*Type*: [GeospatialCategoricalColor](aws-properties-quicksight-template-geospatialcategoricalcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Gradient`  <a name="cfn-quicksight-template-geospatialcolor-gradient"></a>
The visualization properties for the gradient color.
*Required*: No
*Type*: [GeospatialGradientColor](aws-properties-quicksight-template-geospatialgradientcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Solid`  <a name="cfn-quicksight-template-geospatialcolor-solid"></a>
The visualization properties for the solid color.
*Required*: No
*Type*: [GeospatialSolidColor](aws-properties-quicksight-template-geospatialsolidcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
