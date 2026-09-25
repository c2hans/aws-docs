---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-geospatialcategoricaldatacolor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GeospatialCategoricalDataColor
<a name="aws-properties-quicksight-template-geospatialcategoricaldatacolor"></a>

The categorical data color for a single category.

## Syntax
<a name="aws-properties-quicksight-template-geospatialcategoricaldatacolor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-geospatialcategoricaldatacolor-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-template-geospatialcategoricaldatacolor-color)" : {{String}},
  "[DataValue](#cfn-quicksight-template-geospatialcategoricaldatacolor-datavalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-geospatialcategoricaldatacolor-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-template-geospatialcategoricaldatacolor-color): {{String}}
  [DataValue](#cfn-quicksight-template-geospatialcategoricaldatacolor-datavalue): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-geospatialcategoricaldatacolor-properties"></a>

`Color`  <a name="cfn-quicksight-template-geospatialcategoricaldatacolor-color"></a>
The color and opacity values for the category data color.
*Required*: Yes
*Type*: String
*Pattern*: `^#[A-F0-9]{6}(?:[A-F0-9]{2})?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataValue`  <a name="cfn-quicksight-template-geospatialcategoricaldatacolor-datavalue"></a>
The data value for the category data color.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
