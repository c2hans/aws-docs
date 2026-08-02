---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-dataflowendpointgroup-integerrange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::DataflowEndpointGroup IntegerRange
<a name="aws-properties-groundstation-dataflowendpointgroup-integerrange"></a>

An integer range that has a minimum and maximum value.

## Syntax
<a name="aws-properties-groundstation-dataflowendpointgroup-integerrange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-dataflowendpointgroup-integerrange-syntax.json"></a>

```
{
  "[Maximum](#cfn-groundstation-dataflowendpointgroup-integerrange-maximum)" : {{Integer}},
  "[Minimum](#cfn-groundstation-dataflowendpointgroup-integerrange-minimum)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-groundstation-dataflowendpointgroup-integerrange-syntax.yaml"></a>

```
  [Maximum](#cfn-groundstation-dataflowendpointgroup-integerrange-maximum): {{Integer}}
  [Minimum](#cfn-groundstation-dataflowendpointgroup-integerrange-minimum): {{Integer}}
```

## Properties
<a name="aws-properties-groundstation-dataflowendpointgroup-integerrange-properties"></a>

`Maximum`  <a name="cfn-groundstation-dataflowendpointgroup-integerrange-maximum"></a>
A maximum value.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Minimum`  <a name="cfn-groundstation-dataflowendpointgroup-integerrange-minimum"></a>
A minimum value.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
