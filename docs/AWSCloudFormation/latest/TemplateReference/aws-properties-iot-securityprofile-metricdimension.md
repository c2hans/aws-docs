---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-securityprofile-metricdimension.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::SecurityProfile MetricDimension
<a name="aws-properties-iot-securityprofile-metricdimension"></a>

The dimension of the metric.

## Syntax
<a name="aws-properties-iot-securityprofile-metricdimension-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-securityprofile-metricdimension-syntax.json"></a>

```
{
  "[DimensionName](#cfn-iot-securityprofile-metricdimension-dimensionname)" : {{String}},
  "[Operator](#cfn-iot-securityprofile-metricdimension-operator)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-securityprofile-metricdimension-syntax.yaml"></a>

```
  [DimensionName](#cfn-iot-securityprofile-metricdimension-dimensionname): {{String}}
  [Operator](#cfn-iot-securityprofile-metricdimension-operator): {{String}}
```

## Properties
<a name="aws-properties-iot-securityprofile-metricdimension-properties"></a>

`DimensionName`  <a name="cfn-iot-securityprofile-metricdimension-dimensionname"></a>
The name of the dimension.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9:_-]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Operator`  <a name="cfn-iot-securityprofile-metricdimension-operator"></a>
Operators are constructs that perform logical operations. Valid values are `IN` and `NOT_IN`.
*Required*: No
*Type*: String
*Allowed values*: `IN | NOT_IN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
