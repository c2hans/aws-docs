---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-dataflowendpointgroupv2-rangedsocketaddress.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::DataflowEndpointGroupV2 RangedSocketAddress
<a name="aws-properties-groundstation-dataflowendpointgroupv2-rangedsocketaddress"></a>

A socket address with a port range.

## Syntax
<a name="aws-properties-groundstation-dataflowendpointgroupv2-rangedsocketaddress-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-dataflowendpointgroupv2-rangedsocketaddress-syntax.json"></a>

```
{
  "[Name](#cfn-groundstation-dataflowendpointgroupv2-rangedsocketaddress-name)" : {{String}},
  "[PortRange](#cfn-groundstation-dataflowendpointgroupv2-rangedsocketaddress-portrange)" : {{IntegerRange}}
}
```

### YAML
<a name="aws-properties-groundstation-dataflowendpointgroupv2-rangedsocketaddress-syntax.yaml"></a>

```
  [Name](#cfn-groundstation-dataflowendpointgroupv2-rangedsocketaddress-name): {{String}}
  [PortRange](#cfn-groundstation-dataflowendpointgroupv2-rangedsocketaddress-portrange): {{
    IntegerRange}}
```

## Properties
<a name="aws-properties-groundstation-dataflowendpointgroupv2-rangedsocketaddress-properties"></a>

`Name`  <a name="cfn-groundstation-dataflowendpointgroupv2-rangedsocketaddress-name"></a>
IPv4 socket address.
*Required*: Yes
*Type*: String
*Pattern*: `^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PortRange`  <a name="cfn-groundstation-dataflowendpointgroupv2-rangedsocketaddress-portrange"></a>
Port range of a socket address.
*Required*: Yes
*Type*: [IntegerRange](aws-properties-groundstation-dataflowendpointgroupv2-integerrange.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
