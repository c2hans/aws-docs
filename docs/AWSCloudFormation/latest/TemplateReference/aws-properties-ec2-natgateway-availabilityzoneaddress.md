---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-natgateway-availabilityzoneaddress.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::NatGateway AvailabilityZoneAddress
<a name="aws-properties-ec2-natgateway-availabilityzoneaddress"></a>

For regional NAT gateways only: The configuration specifying which Elastic IP address (EIP) to use for handling outbound NAT traffic from a specific Availability Zone.

A regional NAT gateway is a single NAT Gateway that works across multiple availability zones (AZs) in your VPC, providing redundancy, scalability and availability across all the AZs in a Region.

For more information, see [Regional NAT gateways for automatic multi-AZ expansion](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html) in the *Amazon VPC User Guide*.

## Syntax
<a name="aws-properties-ec2-natgateway-availabilityzoneaddress-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-natgateway-availabilityzoneaddress-syntax.json"></a>

```
{
  "[AllocationIds](#cfn-ec2-natgateway-availabilityzoneaddress-allocationids)" : {{[ String, ... ]}},
  "[AvailabilityZone](#cfn-ec2-natgateway-availabilityzoneaddress-availabilityzone)" : {{String}},
  "[AvailabilityZoneId](#cfn-ec2-natgateway-availabilityzoneaddress-availabilityzoneid)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-natgateway-availabilityzoneaddress-syntax.yaml"></a>

```
  [AllocationIds](#cfn-ec2-natgateway-availabilityzoneaddress-allocationids): {{
    - String}}
  [AvailabilityZone](#cfn-ec2-natgateway-availabilityzoneaddress-availabilityzone): {{String}}
  [AvailabilityZoneId](#cfn-ec2-natgateway-availabilityzoneaddress-availabilityzoneid): {{String}}
```

## Properties
<a name="aws-properties-ec2-natgateway-availabilityzoneaddress-properties"></a>

`AllocationIds`  <a name="cfn-ec2-natgateway-availabilityzoneaddress-allocationids"></a>
The allocation IDs of the Elastic IP addresses (EIPs) to be used for handling outbound NAT traffic in this specific Availability Zone.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AvailabilityZone`  <a name="cfn-ec2-natgateway-availabilityzoneaddress-availabilityzone"></a>
For regional NAT gateways only: The Availability Zone where this specific NAT gateway configuration will be active. Each AZ in a regional NAT gateway has its own configuration to handle outbound NAT traffic from that AZ.
A regional NAT gateway is a single NAT Gateway that works across multiple availability zones (AZs) in your VPC, providing redundancy, scalability and availability across all the AZs in a Region.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AvailabilityZoneId`  <a name="cfn-ec2-natgateway-availabilityzoneaddress-availabilityzoneid"></a>
For regional NAT gateways only: The ID of the Availability Zone where this specific NAT gateway configuration will be active. Each AZ in a regional NAT gateway has its own configuration to handle outbound NAT traffic from that AZ. Use this instead of AvailabilityZone for consistent identification of AZs across AWS Regions.
A regional NAT gateway is a single NAT Gateway that works across multiple availability zones (AZs) in your VPC, providing redundancy, scalability and availability across all the AZs in a Region.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
