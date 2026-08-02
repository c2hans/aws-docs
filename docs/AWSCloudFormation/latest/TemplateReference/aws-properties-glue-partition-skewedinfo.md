---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-partition-skewedinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Partition SkewedInfo
<a name="aws-properties-glue-partition-skewedinfo"></a>

Specifies skewed values in a table. Skewed values are those that occur with very high frequency.

## Syntax
<a name="aws-properties-glue-partition-skewedinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-partition-skewedinfo-syntax.json"></a>

```
{
  "[SkewedColumnNames](#cfn-glue-partition-skewedinfo-skewedcolumnnames)" : {{[ String, ... ]}},
  "[SkewedColumnValueLocationMaps](#cfn-glue-partition-skewedinfo-skewedcolumnvaluelocationmaps)" : {{Json}},
  "[SkewedColumnValues](#cfn-glue-partition-skewedinfo-skewedcolumnvalues)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-glue-partition-skewedinfo-syntax.yaml"></a>

```
  [SkewedColumnNames](#cfn-glue-partition-skewedinfo-skewedcolumnnames): {{
    - String}}
  [SkewedColumnValueLocationMaps](#cfn-glue-partition-skewedinfo-skewedcolumnvaluelocationmaps): {{Json}}
  [SkewedColumnValues](#cfn-glue-partition-skewedinfo-skewedcolumnvalues): {{
    - String}}
```

## Properties
<a name="aws-properties-glue-partition-skewedinfo-properties"></a>

`SkewedColumnNames`  <a name="cfn-glue-partition-skewedinfo-skewedcolumnnames"></a>
A list of names of columns that contain skewed values.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SkewedColumnValueLocationMaps`  <a name="cfn-glue-partition-skewedinfo-skewedcolumnvaluelocationmaps"></a>
A mapping of skewed values to the columns that contain them.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SkewedColumnValues`  <a name="cfn-glue-partition-skewedinfo-skewedcolumnvalues"></a>
A list of values that appear so frequently as to be considered skewed.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
