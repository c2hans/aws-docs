---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpoint-campaign-setdimension.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pinpoint::Campaign SetDimension
<a name="aws-properties-pinpoint-campaign-setdimension"></a>

Specifies the dimension type and values for a segment dimension.

## Syntax
<a name="aws-properties-pinpoint-campaign-setdimension-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpoint-campaign-setdimension-syntax.json"></a>

```
{
  "[DimensionType](#cfn-pinpoint-campaign-setdimension-dimensiontype)" : {{String}},
  "[Values](#cfn-pinpoint-campaign-setdimension-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-pinpoint-campaign-setdimension-syntax.yaml"></a>

```
  [DimensionType](#cfn-pinpoint-campaign-setdimension-dimensiontype): {{String}}
  [Values](#cfn-pinpoint-campaign-setdimension-values): {{
    - String}}
```

## Properties
<a name="aws-properties-pinpoint-campaign-setdimension-properties"></a>

`DimensionType`  <a name="cfn-pinpoint-campaign-setdimension-dimensiontype"></a>
The type of segment dimension to use. Valid values are: `INCLUSIVE`, endpoints that match the criteria are included in the segment; and, `EXCLUSIVE`, endpoints that match the criteria are excluded from the segment.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-pinpoint-campaign-setdimension-values"></a>
The criteria values to use for the segment dimension. Depending on the value of the `DimensionType` property, endpoints are included or excluded from the segment if their values match the criteria values.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
