---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-natgateway.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::NatGateway
<a name="aws-resource-ec2-natgateway"></a>

Specifies a network address translation (NAT) gateway in the specified subnet. You can create either a public NAT gateway or a private NAT gateway. The default is a public NAT gateway. If you create a public NAT gateway, you must specify an elastic IP address.

With a NAT gateway, instances in a private subnet can connect to the internet, other AWS services, or an on-premises network using the IP address of the NAT gateway. For more information, see [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in the *Amazon VPC User Guide*.

If you add a default route (`AWS::EC2::Route` resource) that points to a NAT gateway, specify the NAT gateway ID for the route's `NatGatewayId` property.

**Important**
When you associate an Elastic IP address or secondary Elastic IP address with a public NAT gateway, the network border group of the Elastic IP address must match the network border group of the Availability Zone (AZ) that the public NAT gateway is in. Otherwise, the NAT gateway fails to launch. You can see the network border group for the AZ by viewing the details of the subnet. Similarly, you can view the network border group for the Elastic IP address by viewing its details. For more information, see [Allocate an Elastic IP address](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eips.html#allocate-eip) in the *Amazon VPC User Guide*.

## Syntax
<a name="aws-resource-ec2-natgateway-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-natgateway-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::NatGateway",
  "Properties" : {
      "[AllocationId](#cfn-ec2-natgateway-allocationid)" : {{String}},
      "[AvailabilityMode](#cfn-ec2-natgateway-availabilitymode)" : {{String}},
      "[AvailabilityZoneAddresses](#cfn-ec2-natgateway-availabilityzoneaddresses)" : {{[ AvailabilityZoneAddress, ... ]}},
      "[ConnectivityType](#cfn-ec2-natgateway-connectivitytype)" : {{String}},
      "[MaxDrainDurationSeconds](#cfn-ec2-natgateway-maxdraindurationseconds)" : {{Integer}},
      "[PrivateIpAddress](#cfn-ec2-natgateway-privateipaddress)" : {{String}},
      "[SecondaryAllocationIds](#cfn-ec2-natgateway-secondaryallocationids)" : {{[ String, ... ]}},
      "[SecondaryPrivateIpAddressCount](#cfn-ec2-natgateway-secondaryprivateipaddresscount)" : {{Integer}},
      "[SecondaryPrivateIpAddresses](#cfn-ec2-natgateway-secondaryprivateipaddresses)" : {{[ String, ... ]}},
      "[SubnetId](#cfn-ec2-natgateway-subnetid)" : {{String}},
      "[Tags](#cfn-ec2-natgateway-tags)" : {{[ Tag, ... ]}},
      "[VpcId](#cfn-ec2-natgateway-vpcid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-natgateway-syntax.yaml"></a>

```
Type: AWS::EC2::NatGateway
Properties:
  [AllocationId](#cfn-ec2-natgateway-allocationid): {{String}}
  [AvailabilityMode](#cfn-ec2-natgateway-availabilitymode): {{String}}
  [AvailabilityZoneAddresses](#cfn-ec2-natgateway-availabilityzoneaddresses): {{
    - AvailabilityZoneAddress}}
  [ConnectivityType](#cfn-ec2-natgateway-connectivitytype): {{String}}
  [MaxDrainDurationSeconds](#cfn-ec2-natgateway-maxdraindurationseconds): {{Integer}}
  [PrivateIpAddress](#cfn-ec2-natgateway-privateipaddress): {{String}}
  [SecondaryAllocationIds](#cfn-ec2-natgateway-secondaryallocationids): {{
    - String}}
  [SecondaryPrivateIpAddressCount](#cfn-ec2-natgateway-secondaryprivateipaddresscount): {{Integer}}
  [SecondaryPrivateIpAddresses](#cfn-ec2-natgateway-secondaryprivateipaddresses): {{
    - String}}
  [SubnetId](#cfn-ec2-natgateway-subnetid): {{String}}
  [Tags](#cfn-ec2-natgateway-tags): {{
    - Tag}}
  [VpcId](#cfn-ec2-natgateway-vpcid): {{String}}
```

## Properties
<a name="aws-resource-ec2-natgateway-properties"></a>

`AllocationId`  <a name="cfn-ec2-natgateway-allocationid"></a>
[Public NAT gateway only] The allocation ID of the Elastic IP address that's associated with the NAT gateway. This property is required for a public NAT gateway and cannot be specified with a private NAT gateway.
*Required*: Conditional
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AvailabilityMode`  <a name="cfn-ec2-natgateway-availabilitymode"></a>
Indicates whether this is a zonal (single-AZ) or regional (multi-AZ) NAT gateway.
A zonal NAT gateway is a NAT Gateway that provides redundancy and scalability within a single availability zone. A regional NAT gateway is a single NAT Gateway that works across multiple availability zones (AZs) in your VPC, providing redundancy, scalability and availability across all the AZs in a Region.
For more information, see [Regional NAT gateways for automatic multi-AZ expansion](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html) in the *Amazon VPC User Guide*.
*Required*: No
*Type*: String
*Allowed values*: `zonal | regional`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AvailabilityZoneAddresses`  <a name="cfn-ec2-natgateway-availabilityzoneaddresses"></a>
For regional NAT gateways only: Specifies which Availability Zones you want the NAT gateway to support and the Elastic IP addresses (EIPs) to use in each AZ. The regional NAT gateway uses these EIPs to handle outbound NAT traffic from their respective AZs. If not specified, the NAT gateway will automatically expand to new AZs and associate EIPs upon detection of an elastic network interface. If you specify this parameter, auto-expansion is disabled and you must manually manage AZ coverage.
A regional NAT gateway is a single NAT Gateway that works across multiple availability zones (AZs) in your VPC, providing redundancy, scalability and availability across all the AZs in a Region.
For more information, see [Regional NAT gateways for automatic multi-AZ expansion](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html) in the *Amazon VPC User Guide*.
*Required*: No
*Type*: Array of [AvailabilityZoneAddress](aws-properties-ec2-natgateway-availabilityzoneaddress.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectivityType`  <a name="cfn-ec2-natgateway-connectivitytype"></a>
Indicates whether the NAT gateway supports public or private connectivity. The default is public connectivity.
*Required*: No
*Type*: String
*Allowed values*: `private | public`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxDrainDurationSeconds`  <a name="cfn-ec2-natgateway-maxdraindurationseconds"></a>
The maximum amount of time to wait (in seconds) before forcibly releasing the IP addresses if connections are still in progress. Default value is 350 seconds.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `4000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateIpAddress`  <a name="cfn-ec2-natgateway-privateipaddress"></a>
The private IPv4 address to assign to the NAT gateway. If you don't provide an address, a private IPv4 address will be automatically assigned.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecondaryAllocationIds`  <a name="cfn-ec2-natgateway-secondaryallocationids"></a>
Secondary EIP allocation IDs. For more information, see [Create a NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-working-with.html) in the *Amazon VPC User Guide*.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecondaryPrivateIpAddressCount`  <a name="cfn-ec2-natgateway-secondaryprivateipaddresscount"></a>
[Private NAT gateway only] The number of secondary private IPv4 addresses you want to assign to the NAT gateway. For more information about secondary addresses, see [Create a NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-creating) in the *Amazon Virtual Private Cloud User Guide*.
`SecondaryPrivateIpAddressCount` and `SecondaryPrivateIpAddresses` cannot be set at the same time.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecondaryPrivateIpAddresses`  <a name="cfn-ec2-natgateway-secondaryprivateipaddresses"></a>
Secondary private IPv4 addresses. For more information about secondary addresses, see [Create a NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-creating) in the *Amazon Virtual Private Cloud User Guide*.
`SecondaryPrivateIpAddressCount` and `SecondaryPrivateIpAddresses` cannot be set at the same time.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetId`  <a name="cfn-ec2-natgateway-subnetid"></a>
The ID of the subnet in which the NAT gateway is located.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-natgateway-tags"></a>
The tags for the NAT gateway.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-natgateway-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-ec2-natgateway-vpcid"></a>
The ID of the VPC in which the NAT gateway is located.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-natgateway-return-values"></a>

### Ref
<a name="aws-resource-ec2-natgateway-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the NAT gateway. For example, `nat-0a12bc456789de0fg`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-natgateway-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-natgateway-return-values-fn--getatt-fn--getatt"></a>

`AutoProvisionZones`  <a name="AutoProvisionZones-fn::getatt"></a>
For regional NAT gateways only: Indicates whether AWS automatically manages AZ coverage. When enabled, the NAT gateway associates EIPs in all AZs where your VPC has subnets to handle outbound NAT traffic, expands to new AZs when you create subnets there, and retracts from AZs where you've removed all subnets. When disabled, you must manually manage which AZs the NAT gateway supports and their corresponding EIPs.
A regional NAT gateway is a single NAT Gateway that works across multiple availability zones (AZs) in your VPC, providing redundancy, scalability and availability across all the AZs in a Region.
For more information, see [Regional NAT gateways for automatic multi-AZ expansion](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html) in the *Amazon VPC User Guide*.

`AutoScalingIps`  <a name="AutoScalingIps-fn::getatt"></a>
For regional NAT gateways only: Indicates whether AWS automatically allocates additional Elastic IP addresses (EIPs) in an AZ when the NAT gateway needs more ports due to increased concurrent connections to a single destination from that AZ.
For more information, see [Regional NAT gateways for automatic multi-AZ expansion](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html) in the *Amazon VPC User Guide*.

`EniId`  <a name="EniId-fn::getatt"></a>
The ID of the network interface.

`NatGatewayId`  <a name="NatGatewayId-fn::getatt"></a>
The ID of the NAT gateway.

`RouteTableId`  <a name="RouteTableId-fn::getatt"></a>
For regional NAT gateways only, this is the ID of the NAT gateway.

## Examples
<a name="aws-resource-ec2-natgateway--examples"></a>

### NAT gateway
<a name="aws-resource-ec2-natgateway--examples--NAT_gateway"></a>

The following example creates a public NAT gateway and a route that sends all internet-bound traffic from the private subnet with EC2 instances to the NAT gateway. A public NAT gateway uses an elastic IP address to provide it with a public IP address that doesn't change. Note that the route table for the public subnet with the NAT gateway must also have a route that sends all internet-bound traffic to an internet gateway, so that the NAT gateway can connect to the internet.

#### JSON
<a name="aws-resource-ec2-natgateway--examples--NAT_gateway--json"></a>

```
"NATGateway" : {
   "Type" : "AWS::EC2::NatGateway",
   "Properties" : {
      "AllocationId" : {
          "Fn::GetAtt" : ["NATGatewayEIP", "AllocationId"]
      },
      "SubnetId" : {
          "Ref" : "PublicSubnet"
      },
      "Tags" : [
          {"Key" : "stack", "Value" : "production" }
      ]
     }
},
"NATGatewayEIP" : {
   "Type" : "AWS::EC2::EIP",
   "Properties" : {
      "Domain" : "vpc"
   }
},
"RouteNATGateway" : {
   "Type" : "AWS::EC2::Route",
   "Properties" : {
      "RouteTableId" : { "Ref" : "PrivateRouteTable" },
      "DestinationCidrBlock" : "0.0.0.0/0",
      "NatGatewayId" : { "Ref" : "NATGateway" }
   }
}
```

#### YAML
<a name="aws-resource-ec2-natgateway--examples--NAT_gateway--yaml"></a>

```
NATGateway:
   Type: AWS::EC2::NatGateway
   Properties:
      AllocationId: !GetAtt NATGatewayEIP.AllocationId
      SubnetId: !Ref PublicSubnet
      Tags:
      - Key: stack
        Value: production
NATGatewayEIP:
   Type: AWS::EC2::EIP
   Properties:
      Domain: vpc
RouteNATGateway:
   Type: AWS::EC2::Route
   Properties:
      RouteTableId: !Ref PrivateRouteTable
      DestinationCidrBlock: '0.0.0.0/0'
      NatGatewayId: !Ref NATGateway
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
