---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-geospatialcategoricaldatacolor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GeospatialCategoricalDataColor
<a name="aws-properties-quicksight-analysis-geospatialcategoricaldatacolor"></a>

The categorical data color for a single category.

## Syntax
<a name="aws-properties-quicksight-analysis-geospatialcategoricaldatacolor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-geospatialcategoricaldatacolor-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-analysis-geospatialcategoricaldatacolor-color)" : {{String}},
  "[DataValue](#cfn-quicksight-analysis-geospatialcategoricaldatacolor-datavalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-geospatialcategoricaldatacolor-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-analysis-geospatialcategoricaldatacolor-color): {{String}}
  [DataValue](#cfn-quicksight-analysis-geospatialcategoricaldatacolor-datavalue): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-geospatialcategoricaldatacolor-properties"></a>

`Color`  <a name="cfn-quicksight-analysis-geospatialcategoricaldatacolor-color"></a>
The color and opacity values for the category data color.
*Required*: Yes
*Type*: String
*Pattern*: `^#[A-F0-9]{6}(?:[A-F0-9]{2})?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataValue`  <a name="cfn-quicksight-analysis-geospatialcategoricaldatacolor-datavalue"></a>
The data value for the category data color.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
