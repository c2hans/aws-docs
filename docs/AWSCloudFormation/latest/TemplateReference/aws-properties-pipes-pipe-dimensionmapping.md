---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-dimensionmapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe DimensionMapping
<a name="aws-properties-pipes-pipe-dimensionmapping"></a>

Maps source data to a dimension in the target Timestream for LiveAnalytics table.

For more information, see [Amazon Timestream for LiveAnalytics concepts](https://docs.aws.amazon.com/timestream/latest/developerguide/concepts.html)

## Syntax
<a name="aws-properties-pipes-pipe-dimensionmapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-dimensionmapping-syntax.json"></a>

```
{
  "[DimensionName](#cfn-pipes-pipe-dimensionmapping-dimensionname)" : {{String}},
  "[DimensionValue](#cfn-pipes-pipe-dimensionmapping-dimensionvalue)" : {{String}},
  "[DimensionValueType](#cfn-pipes-pipe-dimensionmapping-dimensionvaluetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-dimensionmapping-syntax.yaml"></a>

```
  [DimensionName](#cfn-pipes-pipe-dimensionmapping-dimensionname): {{String}}
  [DimensionValue](#cfn-pipes-pipe-dimensionmapping-dimensionvalue): {{String}}
  [DimensionValueType](#cfn-pipes-pipe-dimensionmapping-dimensionvaluetype): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-dimensionmapping-properties"></a>

`DimensionName`  <a name="cfn-pipes-pipe-dimensionmapping-dimensionname"></a>
The metadata attributes of the time series. For example, the name and Availability Zone of an Amazon EC2 instance or the name of the manufacturer of a wind turbine are dimensions.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DimensionValue`  <a name="cfn-pipes-pipe-dimensionmapping-dimensionvalue"></a>
Dynamic path to the dimension value in the source event.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DimensionValueType`  <a name="cfn-pipes-pipe-dimensionmapping-dimensionvaluetype"></a>
The data type of the dimension for the time-series data.
*Required*: Yes
*Type*: String
*Allowed values*: `VARCHAR`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
