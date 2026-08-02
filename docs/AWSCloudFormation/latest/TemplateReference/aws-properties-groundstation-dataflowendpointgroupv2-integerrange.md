---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-dataflowendpointgroupv2-integerrange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::DataflowEndpointGroupV2 IntegerRange
<a name="aws-properties-groundstation-dataflowendpointgroupv2-integerrange"></a>

An integer range that has a minimum and maximum value.

## Syntax
<a name="aws-properties-groundstation-dataflowendpointgroupv2-integerrange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-dataflowendpointgroupv2-integerrange-syntax.json"></a>

```
{
  "[Maximum](#cfn-groundstation-dataflowendpointgroupv2-integerrange-maximum)" : {{Integer}},
  "[Minimum](#cfn-groundstation-dataflowendpointgroupv2-integerrange-minimum)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-groundstation-dataflowendpointgroupv2-integerrange-syntax.yaml"></a>

```
  [Maximum](#cfn-groundstation-dataflowendpointgroupv2-integerrange-maximum): {{Integer}}
  [Minimum](#cfn-groundstation-dataflowendpointgroupv2-integerrange-minimum): {{Integer}}
```

## Properties
<a name="aws-properties-groundstation-dataflowendpointgroupv2-integerrange-properties"></a>

`Maximum`  <a name="cfn-groundstation-dataflowendpointgroupv2-integerrange-maximum"></a>
A maximum value.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Minimum`  <a name="cfn-groundstation-dataflowendpointgroupv2-integerrange-minimum"></a>
A minimum value.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
