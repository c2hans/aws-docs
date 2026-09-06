---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-ec2fleet-reservedcapacityfallbackoptionsrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::EC2Fleet ReservedCapacityFallbackOptionsRequest
<a name="aws-properties-ec2-ec2fleet-reservedcapacityfallbackoptionsrequest"></a>

Describes the fallback behavior for an EC2 Fleet that uses reserved capacity when the reserved capacity is not enough to meet the target capacity. If you don't specify fallback options, EC2 Fleet does not fall back to any other market type after the specified reservation types are exhausted.

## Syntax
<a name="aws-properties-ec2-ec2fleet-reservedcapacityfallbackoptionsrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-ec2fleet-reservedcapacityfallbackoptionsrequest-syntax.json"></a>

```
{
  "[MarketTypes](#cfn-ec2-ec2fleet-reservedcapacityfallbackoptionsrequest-markettypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-ec2fleet-reservedcapacityfallbackoptionsrequest-syntax.yaml"></a>

```
  [MarketTypes](#cfn-ec2-ec2fleet-reservedcapacityfallbackoptionsrequest-markettypes): {{
    - String}}
```

## Properties
<a name="aws-properties-ec2-ec2fleet-reservedcapacityfallbackoptionsrequest-properties"></a>

`MarketTypes`  <a name="cfn-ec2-ec2fleet-reservedcapacityfallbackoptionsrequest-markettypes"></a>
The instance purchasing options to fall back to when the reserved capacity is not enough to meet the target capacity. The only supported value is `on-demand`, which launches On-Demand Instances to fulfill the remaining target capacity.
*Required*: No
*Type*: Array of String
*Allowed values*: `on-demand`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
