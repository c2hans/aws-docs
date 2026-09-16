---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSubnet.html
---

# CreateSubnet
<a name="API_CreateSubnet"></a>

Creates a subnet in the specified VPC. For an IPv4 only subnet, specify an IPv4 CIDR block. If the VPC has an IPv6 CIDR block, you can create an IPv6 only subnet or a dual stack subnet instead. For an IPv6 only subnet, specify an IPv6 CIDR block. For a dual stack subnet, specify both an IPv4 CIDR block and an IPv6 CIDR block.

A subnet CIDR block must not overlap the CIDR block of an existing subnet in the VPC. After you create a subnet, you can't change its CIDR block.

The allowed size for an IPv4 subnet is between a /28 netmask (16 IP addresses) and a /16 netmask (65,536 IP addresses). AWS reserves both the first four and the last IPv4 address in each subnet's CIDR block. They're not available for your use.

If you've associated an IPv6 CIDR block with your VPC, you can associate an IPv6 CIDR block with a subnet when you create it.

If you add more than one subnet to a VPC, they're set up in a star topology with a logical router in the middle.

When you stop an instance in a subnet, it retains its private IPv4 address. It's therefore possible to have a subnet with no running instances (they're all stopped), but no remaining IP addresses available.

For more information, see [Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_CreateSubnet_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AvailabilityZone**
The Availability Zone or Local Zone for the subnet.
Default: AWS selects one for you. If you create more than one subnet in your VPC, we do not necessarily select a different zone for each subnet.
To create a subnet in a Local Zone, set this value to the Local Zone ID, for example `us-west-2-lax-1a`. For information about the Regions that support Local Zones, see [Available Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/available-local-zones.html).
To create a subnet in an Outpost, set this value to the Availability Zone for the Outpost and specify the Outpost ARN.
Type: String
Required: No

 **AvailabilityZoneId**
The AZ ID or the Local Zone ID of the subnet.
Type: String
Required: No

 **CidrBlock**
The IPv4 network range for the subnet, in CIDR notation. For example, `10.0.0.0/24`. We modify the specified CIDR block to its canonical form; for example, if you specify `100.68.0.18/18`, we modify it to `100.68.0.0/18`.
This parameter is not supported for an IPv6 only subnet.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Ipv4IpamPoolId**
An IPv4 IPAM pool ID for the subnet.
Type: String
Required: No

 **Ipv4NetmaskLength**
An IPv4 netmask length for the subnet.
Type: Integer
Required: No

 **Ipv6CidrBlock**
The IPv6 network range for the subnet, in CIDR notation. This parameter is required for an IPv6 only subnet.
Type: String
Required: No

 **Ipv6IpamPoolId**
An IPv6 IPAM pool ID for the subnet.
Type: String
Required: No

 **Ipv6Native**
Indicates whether to create an IPv6 only subnet.
Type: Boolean
Required: No

 **Ipv6NetmaskLength**
An IPv6 netmask length for the subnet.
Type: Integer
Required: No

 **OutpostArn**
The Amazon Resource Name (ARN) of the Outpost. If you specify an Outpost ARN, you must also specify the Availability Zone of the Outpost subnet.
Type: String
Required: No

 **TagSpecification.N**
The tags to assign to the subnet.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **VpcId**
The ID of the VPC.
Type: String
Required: Yes

## Response Elements
<a name="API_CreateSubnet_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **subnet**
Information about the subnet.
Type: [Subnet](API_Subnet.md) object

## Errors
<a name="API_CreateSubnet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateSubnet_Examples"></a>

### Example 1
<a name="API_CreateSubnet_Example_1"></a>

This example creates a subnet with CIDR block `10.0.1.0/24` in the VPC with the ID `vpc-1a2b3c4d`.

#### Sample Request
<a name="API_CreateSubnet_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateSubnet
&VpcId=vpc-1a2b3c4d
&CidrBlock=10.0.1.0/24
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateSubnet_Example_1_Response"></a>

```
<CreateSubnetResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>e6cb93f0-eb09-40ee-b9aa-16db90a0524f</requestId>
    <subnet>
        <subnetId>subnet-0397b6c47c42e4dc0</subnetId>
        <subnetArn>arn:aws:ec2:us-east-2:111122223333:subnet/subnet-0397b6c47cEXAMPLE</subnetArn>
        <state>pending</state>
        <ownerId>111122223333</ownerId>
        <vpcId>vpc-06b7830650EXAMPLE</vpcId>
        <cidrBlock>10.0.0.0/24</cidrBlock>
        <ipv6CidrBlockAssociationSet/>
        <availableIpAddressCount>251</availableIpAddressCount>
        <availabilityZone>us-east-2a</availabilityZone>
        <availabilityZoneId>use2-az1</availabilityZoneId>
        <defaultForAz>false</defaultForAz>
        <mapPublicIpOnLaunch>false</mapPublicIpOnLaunch>
        <assignIpv6AddressOnCreation>false</assignIpv6AddressOnCreation>
    </subnet>
</CreateSubnetResponse>
```

### Example 2
<a name="API_CreateSubnet_Example_2"></a>

This example creates a subnet with an IPv6 CIDR block in the VPC `vpc-1a2b3c4d`.

#### Sample Request
<a name="API_CreateSubnet_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateSubnet
&VpcId=vpc-07e8ffd50fEXAMPLE
&CidrBlock=10.0.1.0/24
&Ipv6CidrBlock=2600:1f16:115:200::/64
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateSubnet_Example_2_Response"></a>

```
<CreateSubnetResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
  <subnet>
   <subnetId>subnet-02bf4c428bEXAMPLE</subnetId>
   <subnetArn>arn:aws:ec2:us-east-2:111122223333:subnet/subnet-02bf4c428bEXAMPLE</subnetArn>
   <state>available</state>
   <ownerId>111122223333</ownerId>
   <vpcId>vpc-07e8ffd50fEXAMPLE</vpcId>
   <cidrBlock>10.0.0.0/24</cidrBlock>
   <ipv6CidrBlockAssociationSet>
      <item>
       <ipv6CidrBlock>2600:1f16:115:200::/64</ipv6CidrBlock>
       <associationId>subnet-cidr-assoc-002afb9f3cEXAMPLE</associationId>
       <ipv6CidrBlockState>
          <state>associated</state>
       </ipv6CidrBlockState>
    </item>
    </ipv6CidrBlockAssociationSet>
    <availableIpAddressCount>251</availableIpAddressCount>
    <availabilityZone>us-east-2b</availabilityZone>
    <availabilityZoneId>use2-az2</availabilityZoneId>
    <defaultForAz>false</defaultForAz>
    <mapPublicIpOnLaunch>false</mapPublicIpOnLaunch>
    <assignIpv6AddressOnCreation>false</assignIpv6AddressOnCreation
  </subnet>
</CreateSubnetResponse>
```

### Example 3
<a name="API_CreateSubnet_Example_3"></a>

This example creates a subnet with an IPv6 CIDR block in the specified Local Zone.

#### Sample Request
<a name="API_CreateSubnet_Example_3_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateSubnet
&VpcId=vpc-07e8ffd50fEXAMPLE
&CidrBlock=10.0.1.0/24
&Ipv6CidrBlock=2600:1f16:115:200::/64
&AvailabilityZone=us-west-2-lax-1a
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateSubnet_Example_3_Response"></a>

```
<CreateSubnetResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
 <subnet>
    <subnetId>subnet-093cb4a1ecEXAMPLE</subnetId>
    <subnetArn>arn:aws:ec2:us-west-2:111122223333:subnet/subnet-093cb4a1ecEXAMPLE</subnetArn><subnetArn>
   <state>available</state>
   <ownerId>111122223333</ownerId>
   <vpcId>vpc-07d80fe1a43298172</vpcId>
   <cidrBlock>10.0.0.0/24</cidrBlock>
   <ipv6CidrBlockAssociationSet>
      <item>
       <ipv6CidrBlock>2600:1f16:115:200::/64</ipv6CidrBlock>
       <associationId>subnet-cidr-assoc-002afb9f3cEXAMPLE</associationId>
       <ipv6CidrBlockState>
          <state>associated</state>
       </ipv6CidrBlockState>
    </item>
    </ipv6CidrBlockAssociationSet>
    <availableIpAddressCount>251</availableIpAddressCount>
    <availabilityZone>us-west-2-lax-1a</availabilityZone>
     <availabilityZoneId>usw2-lax1-az1</availabilityZoneId>
    <defaultForAz>false</defaultForAz>
    <mapPublicIpOnLaunch>false</mapPublicIpOnLaunch>
    <assignIpv6AddressOnCreation>false</assignIpv6AddressOnCreation
  </subnet>
</CreateSubnetResponse>
```

## See Also
<a name="API_CreateSubnet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateSubnet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateSubnet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateSubnet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateSubnet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateSubnet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateSubnet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateSubnet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateSubnet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateSubnet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateSubnet)
