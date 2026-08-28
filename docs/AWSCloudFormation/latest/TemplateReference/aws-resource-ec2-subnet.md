---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-subnet.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::Subnet
<a name="aws-resource-ec2-subnet"></a>

Specifies a subnet for the specified VPC.

For an IPv4 only subnet, specify an IPv4 CIDR block. If the VPC has an IPv6 CIDR block, you can create an IPv6 only subnet or a dual stack subnet instead. For an IPv6 only subnet, specify an IPv6 CIDR block. For a dual stack subnet, specify both an IPv4 CIDR block and an IPv6 CIDR block.

For more information, see [Subnets for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html) in the *Amazon VPC User Guide*.

## Syntax
<a name="aws-resource-ec2-subnet-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-subnet-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::Subnet",
  "Properties" : {
      "[AssignIpv6AddressOnCreation](#cfn-ec2-subnet-assignipv6addressoncreation)" : {{Boolean}},
      "[AvailabilityZone](#cfn-ec2-subnet-availabilityzone)" : {{String}},
      "[AvailabilityZoneId](#cfn-ec2-subnet-availabilityzoneid)" : {{String}},
      "[CidrBlock](#cfn-ec2-subnet-cidrblock)" : {{String}},
      "[EnableDns64](#cfn-ec2-subnet-enabledns64)" : {{Boolean}},
      "[EnableLniAtDeviceIndex](#cfn-ec2-subnet-enablelniatdeviceindex)" : {{Integer}},
      "[Ipv4IpamPoolId](#cfn-ec2-subnet-ipv4ipampoolid)" : {{String}},
      "[Ipv4NetmaskLength](#cfn-ec2-subnet-ipv4netmasklength)" : {{Integer}},
      "[Ipv6CidrBlock](#cfn-ec2-subnet-ipv6cidrblock)" : {{String}},
      "[Ipv6IpamPoolId](#cfn-ec2-subnet-ipv6ipampoolid)" : {{String}},
      "[Ipv6Native](#cfn-ec2-subnet-ipv6native)" : {{Boolean}},
      "[Ipv6NetmaskLength](#cfn-ec2-subnet-ipv6netmasklength)" : {{Integer}},
      "[MapPublicIpOnLaunch](#cfn-ec2-subnet-mappubliciponlaunch)" : {{Boolean}},
      "[OutpostArn](#cfn-ec2-subnet-outpostarn)" : {{String}},
      "[PrivateDnsNameOptionsOnLaunch](#cfn-ec2-subnet-privatednsnameoptionsonlaunch)" : {{PrivateDnsNameOptionsOnLaunch}},
      "[Tags](#cfn-ec2-subnet-tags)" : {{[ Tag, ... ]}},
      "[VpcId](#cfn-ec2-subnet-vpcid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-subnet-syntax.yaml"></a>

```
Type: AWS::EC2::Subnet
Properties:
  [AssignIpv6AddressOnCreation](#cfn-ec2-subnet-assignipv6addressoncreation): {{Boolean}}
  [AvailabilityZone](#cfn-ec2-subnet-availabilityzone): {{String}}
  [AvailabilityZoneId](#cfn-ec2-subnet-availabilityzoneid): {{String}}
  [CidrBlock](#cfn-ec2-subnet-cidrblock): {{String}}
  [EnableDns64](#cfn-ec2-subnet-enabledns64): {{Boolean}}
  [EnableLniAtDeviceIndex](#cfn-ec2-subnet-enablelniatdeviceindex): {{Integer}}
  [Ipv4IpamPoolId](#cfn-ec2-subnet-ipv4ipampoolid): {{String}}
  [Ipv4NetmaskLength](#cfn-ec2-subnet-ipv4netmasklength): {{Integer}}
  [Ipv6CidrBlock](#cfn-ec2-subnet-ipv6cidrblock): {{String}}
  [Ipv6IpamPoolId](#cfn-ec2-subnet-ipv6ipampoolid): {{String}}
  [Ipv6Native](#cfn-ec2-subnet-ipv6native): {{Boolean}}
  [Ipv6NetmaskLength](#cfn-ec2-subnet-ipv6netmasklength): {{Integer}}
  [MapPublicIpOnLaunch](#cfn-ec2-subnet-mappubliciponlaunch): {{Boolean}}
  [OutpostArn](#cfn-ec2-subnet-outpostarn): {{String}}
  [PrivateDnsNameOptionsOnLaunch](#cfn-ec2-subnet-privatednsnameoptionsonlaunch): {{
    PrivateDnsNameOptionsOnLaunch}}
  [Tags](#cfn-ec2-subnet-tags): {{
    - Tag}}
  [VpcId](#cfn-ec2-subnet-vpcid): {{String}}
```

## Properties
<a name="aws-resource-ec2-subnet-properties"></a>

`AssignIpv6AddressOnCreation`  <a name="cfn-ec2-subnet-assignipv6addressoncreation"></a>
Indicates whether a network interface created in this subnet receives an IPv6 address. The default value is `false`.
If you specify `AssignIpv6AddressOnCreation`, you must also specify an IPv6 CIDR block.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AvailabilityZone`  <a name="cfn-ec2-subnet-availabilityzone"></a>
The Availability Zone of the subnet.
If you update this property, you must also update the `CidrBlock` property.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AvailabilityZoneId`  <a name="cfn-ec2-subnet-availabilityzoneid"></a>
The AZ ID of the subnet.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CidrBlock`  <a name="cfn-ec2-subnet-cidrblock"></a>
The IPv4 CIDR block assigned to the subnet.
If you update this property, we create a new subnet, and then delete the existing one.
*Required*: Conditional
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnableDns64`  <a name="cfn-ec2-subnet-enabledns64"></a>
Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations.
You must first configure a NAT gateway in a public subnet (separate from the subnet containing the IPv6-only workloads). For example, the subnet containing the NAT gateway should have a `0.0.0.0/0` route pointing to the internet gateway. For more information, see [Configure DNS64 and NAT64](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-nat64-dns64.html#nat-gateway-nat64-dns64-walkthrough) in the *Amazon Virtual Private Cloud User Guide*.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableLniAtDeviceIndex`  <a name="cfn-ec2-subnet-enablelniatdeviceindex"></a>
 Indicates the device position for local network interfaces in this subnet. For example, `1` indicates local network interfaces in this subnet are the secondary network interface (eth1).
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv4IpamPoolId`  <a name="cfn-ec2-subnet-ipv4ipampoolid"></a>
An IPv4 IPAM pool ID for the subnet.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ipv4NetmaskLength`  <a name="cfn-ec2-subnet-ipv4netmasklength"></a>
An IPv4 netmask length for the subnet.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ipv6CidrBlock`  <a name="cfn-ec2-subnet-ipv6cidrblock"></a>
The IPv6 CIDR block.
If you specify `AssignIpv6AddressOnCreation`, you must also specify an IPv6 CIDR block.
*Required*: Conditional
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Ipv6IpamPoolId`  <a name="cfn-ec2-subnet-ipv6ipampoolid"></a>
An IPv6 IPAM pool ID for the subnet.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ipv6Native`  <a name="cfn-ec2-subnet-ipv6native"></a>
Indicates whether this is an IPv6 only subnet. For more information, see [Subnet basics](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html#subnet-basics) in the *Amazon Virtual Private Cloud User Guide*.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ipv6NetmaskLength`  <a name="cfn-ec2-subnet-ipv6netmasklength"></a>
An IPv6 netmask length for the subnet.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MapPublicIpOnLaunch`  <a name="cfn-ec2-subnet-mappubliciponlaunch"></a>
Indicates whether instances launched in this subnet receive a public IPv4 address. The default value is `false`.
AWS charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the *Public IPv4 Address* tab on the [VPC pricing page](https://aws.amazon.com/vpc/pricing/).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutpostArn`  <a name="cfn-ec2-subnet-outpostarn"></a>
The Amazon Resource Name (ARN) of the Outpost.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrivateDnsNameOptionsOnLaunch`  <a name="cfn-ec2-subnet-privatednsnameoptionsonlaunch"></a>
The hostname type for EC2 instances launched into this subnet and how DNS A and AAAA record queries to the instances should be handled. For more information, see [Amazon EC2 instance hostname types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html) in the *Amazon Elastic Compute Cloud User Guide*.
Available options:
+ EnableResourceNameDnsAAAARecord (true \| false)
+ EnableResourceNameDnsARecord (true \| false)
+ HostnameType (ip-name \| resource-name)
*Required*: No
*Type*: [PrivateDnsNameOptionsOnLaunch](aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ec2-subnet-tags"></a>
Any tags assigned to the subnet.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-subnet-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-ec2-subnet-vpcid"></a>
The ID of the VPC the subnet is in.
If you update this property, you must also update the `CidrBlock` property.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-subnet-return-values"></a>

### Ref
<a name="aws-resource-ec2-subnet-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the subnet.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-subnet-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-subnet-return-values-fn--getatt-fn--getatt"></a>

`AvailabilityZone`  <a name="AvailabilityZone-fn::getatt"></a>
The Availability Zone of this subnet. For example, `us-east-1a`.

`AvailabilityZoneId`  <a name="AvailabilityZoneId-fn::getatt"></a>
The Availability Zone ID of this subnet. For example, `use1-az1`.

`CidrBlock`  <a name="CidrBlock-fn::getatt"></a>
The IPv4 CIDR blocks that are associated with the subnet.

`Ipv6CidrBlocks`  <a name="Ipv6CidrBlocks-fn::getatt"></a>
The IPv6 CIDR blocks that are associated with the subnet.

`NetworkAclAssociationId`  <a name="NetworkAclAssociationId-fn::getatt"></a>
The ID of the network ACL that is associated with the subnet's VPC, such as `acl-5fb85d36`.

`OutpostArn`  <a name="OutpostArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Outpost.

`SubnetId`  <a name="SubnetId-fn::getatt"></a>
The ID of the subnet.

`VpcId`  <a name="VpcId-fn::getatt"></a>
The ID of the subnet's VPC, such as `vpc-11ad4878`.

## Examples
<a name="aws-resource-ec2-subnet--examples"></a>

**Topics**
+ [Subnet with an IPv4 CIDR](#aws-resource-ec2-subnet--examples--Subnet_with_an_IPv4_CIDR)
+ [Subnet with an IPv6 CIDR](#aws-resource-ec2-subnet--examples--Subnet_with_an_IPv6_CIDR)

### Subnet with an IPv4 CIDR
<a name="aws-resource-ec2-subnet--examples--Subnet_with_an_IPv4_CIDR"></a>

The following example creates a subnet with an IPv4 CIDR in a VPC with an IPv4 CIDR of 10.0.0.0/16. The VPC is declared elsewhere in the same template.

#### JSON
<a name="aws-resource-ec2-subnet--examples--Subnet_with_an_IPv4_CIDR--json"></a>

```
"mySubnet" : {
   "Type" : "AWS::EC2::Subnet",
   "Properties" : {
      "VpcId" : { "Ref" : "myVPC" },
      "CidrBlock" : "10.0.0.0/24",
      "AvailabilityZone" : "us-east-1a",
      "Tags" : [ { "Key" : "stack", "Value" : "production" } ]
   }
}
```

#### YAML
<a name="aws-resource-ec2-subnet--examples--Subnet_with_an_IPv4_CIDR--yaml"></a>

```
  mySubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref myVPC
      CidrBlock: 10.0.0.0/24
      AvailabilityZone: "us-east-1a"
      Tags:
      - Key: stack
        Value: production
```

### Subnet with an IPv6 CIDR
<a name="aws-resource-ec2-subnet--examples--Subnet_with_an_IPv6_CIDR"></a>

The following example creates a subnet with an IPv6 CIDR in a VPC with an IPv6 CIDR provided by Amazon. The VPC is declared elsewhere in the same template. The example uses the [Fn:Cidr](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-cidr.html) intrinsic function to select an IPv6 range with a /64 netmask for the subnet.

#### JSON
<a name="aws-resource-ec2-subnet--examples--Subnet_with_an_IPv6_CIDR--json"></a>

```
"mySubnet": {
   "Type": "AWS::EC2::Subnet",
   "Properties": {
      "VpcId": { "Ref": "myVPC" },
      "Ipv6Native": "true",
      "Ipv6CidrBlock": {
         "Fn::Select":
            [ 0, { "Fn::Cidr": [{"Fn::Select": [0, {"Fn::GetAtt": ["myVpc", "Ipv6CidrBlocks"]}]}, 1, 64 ]}]
      },
      "AssignIpv6AddressOnCreation": "true"
   }
}
```

#### YAML
<a name="aws-resource-ec2-subnet--examples--Subnet_with_an_IPv6_CIDR--yaml"></a>

```
  mySubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref myVPC
      Ipv6Native: true
      Ipv6CidrBlock: !Select [ 0, !Cidr [ !Select [ 0, !GetAtt myVpc.Ipv6CidrBlocks], 1, 64 ]]
      AssignIpv6AddressOnCreation: true
```

## See also
<a name="aws-resource-ec2-subnet--seealso"></a>
+ [CreateSubnet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSubnet.html) in the *Amazon EC2 API Reference*
+ [VPC and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html) in the *Amazon VPC User Guide*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
