---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html
---

# CreateNetworkInterface
<a name="API_CreateNetworkInterface"></a>

Creates a network interface in the specified subnet.

The number of IP addresses you can assign to a network interface varies by instance type.

For more information about network interfaces, see [Elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_CreateNetworkInterface_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **ConnectionTrackingSpecification**
A connection tracking specification for the network interface.
Type: [ConnectionTrackingSpecificationRequest](API_ConnectionTrackingSpecificationRequest.md) object
Required: No

 **Description**
A description for the network interface.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **EnablePrimaryIpv6**
If you’re creating a network interface in a dual-stack or IPv6-only subnet, you have the option to assign a primary IPv6 IP address. A primary IPv6 address is an IPv6 GUA address associated with an ENI that you have enabled to use a primary IPv6 address. Use this option if the instance that this ENI will be attached to relies on its IPv6 address not changing. AWS will automatically assign an IPv6 address associated with the ENI attached to your instance to be the primary IPv6 address. Once you enable an IPv6 GUA address to be a primary IPv6, you cannot disable it. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. If you have multiple IPv6 addresses associated with an ENI attached to your instance and you enable a primary IPv6 address, the first IPv6 GUA address associated with the ENI becomes the primary IPv6 address.
Type: Boolean
Required: No

 **InterfaceType**
The type of network interface. The default is `interface`.
If you specify `efa-only`, do not assign any IP addresses to the network interface. EFA-only network interfaces do not support IP addresses.
Type: String
Valid Values: `interface | efa | efa-only | trunk`
Required: No

 **Ipv4Prefix.N**
The IPv4 prefixes assigned to the network interface.
You can't specify IPv4 prefixes if you've specified one of the following: a count of IPv4 prefixes, specific private IPv4 addresses, or a count of private IPv4 addresses.
Type: Array of [Ipv4PrefixSpecificationRequest](API_Ipv4PrefixSpecificationRequest.md) objects
Required: No

 **Ipv4PrefixCount**
The number of IPv4 prefixes that AWS automatically assigns to the network interface.
You can't specify a count of IPv4 prefixes if you've specified one of the following: specific IPv4 prefixes, specific private IPv4 addresses, or a count of private IPv4 addresses.
Type: Integer
Required: No

 **Ipv6AddressCount**
The number of IPv6 addresses to assign to a network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range.
You can't specify a count of IPv6 addresses using this parameter if you've specified one of the following: specific IPv6 addresses, specific IPv6 prefixes, or a count of IPv6 prefixes.
If your subnet has the `AssignIpv6AddressOnCreation` attribute set, you can override that setting by specifying 0 as the IPv6 address count.
Type: Integer
Required: No

 **Ipv6Addresses.N**
The IPv6 addresses from the IPv6 CIDR block range of your subnet.
You can't specify IPv6 addresses using this parameter if you've specified one of the following: a count of IPv6 addresses, specific IPv6 prefixes, or a count of IPv6 prefixes.
Type: Array of [InstanceIpv6Address](API_InstanceIpv6Address.md) objects
Required: No

 **Ipv6Prefix.N**
The IPv6 prefixes assigned to the network interface.
You can't specify IPv6 prefixes if you've specified one of the following: a count of IPv6 prefixes, specific IPv6 addresses, or a count of IPv6 addresses.
Type: Array of [Ipv6PrefixSpecificationRequest](API_Ipv6PrefixSpecificationRequest.md) objects
Required: No

 **Ipv6PrefixCount**
The number of IPv6 prefixes that AWS automatically assigns to the network interface.
You can't specify a count of IPv6 prefixes if you've specified one of the following: specific IPv6 prefixes, specific IPv6 addresses, or a count of IPv6 addresses.
Type: Integer
Required: No

 **Operator**
Reserved for internal use.
Type: [OperatorRequest](API_OperatorRequest.md) object
Required: No

 **PrivateIpAddress**
The primary private IPv4 address of the network interface. If you don't specify an IPv4 address, Amazon EC2 selects one for you from the subnet's IPv4 CIDR range. If you specify an IP address, you cannot indicate any IP addresses specified in `privateIpAddresses` as primary (only one IP address can be designated as primary).
Type: String
Required: No

 **PrivateIpAddresses.N**
The private IPv4 addresses.
You can't specify private IPv4 addresses if you've specified one of the following: a count of private IPv4 addresses, specific IPv4 prefixes, or a count of IPv4 prefixes.
Type: Array of [PrivateIpAddressSpecification](API_PrivateIpAddressSpecification.md) objects
Required: No

 **SecondaryPrivateIpAddressCount**
The number of secondary private IPv4 addresses to assign to a network interface. When you specify a number of secondary IPv4 addresses, Amazon EC2 selects these IP addresses within the subnet's IPv4 CIDR range. You can't specify this option and specify more than one private IP address using `privateIpAddresses`.
You can't specify a count of private IPv4 addresses if you've specified one of the following: specific private IPv4 addresses, specific IPv4 prefixes, or a count of IPv4 prefixes.
Type: Integer
Required: No

 **SecurityGroupId.N**
The IDs of the security groups.
Type: Array of strings
Required: No

 **SubnetId**
The ID of the subnet to associate with the network interface.
Type: String
Required: Yes

 **TagSpecification.N**
The tags to apply to the new network interface.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateNetworkInterface_ResponseElements"></a>

The following elements are returned by the service.

 **clientToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **networkInterface**
Information about the network interface.
Type: [NetworkInterface](API_NetworkInterface.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateNetworkInterface_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateNetworkInterface_Examples"></a>

### Example 1
<a name="API_CreateNetworkInterface_Example_1"></a>

This example creates a network interface in the specified subnet with a primary IPv4 address that is automatically selected by Amazon EC2.

#### Sample Request
<a name="API_CreateNetworkInterface_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateNetworkInterface
&SubnetId=subnet-b2a249da
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateNetworkInterface_Example_1_Response"></a>

```
<CreateNetworkInterfaceResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
 <requestId>8dbe591e-5a22-48cb-b948-example</requestId>
    <networkInterface>
        <networkInterfaceId>eni-cfca76a6</networkInterfaceId>
        <subnetId>subnet-b2a249da</subnetId>
        <vpcId>vpc-c31dafaa</vpcId>
        <availabilityZone>ap-southeast-1b</availabilityZone>
        <description/>
        <ownerId>251839141158</ownerId>
        <requesterManaged>false</requesterManaged>
        <status>available</status>
        <macAddress>02:74:b0:72:79:61</macAddress>
        <privateIpAddress>10.0.2.157</privateIpAddress>
        <privateDnsName>ip-10-0-2-157.ap-southeast-1.compute.internal</privateDnsName>
        <sourceDestCheck>true</sourceDestCheck>
        <groupSet>
            <item>
                <groupId>sg-1a2b3c4d</groupId>
                <groupName>default</groupName>
            </item>
        </groupSet>
        <tagSet/>
        <privateIpAddressesSet>
            <item>
                <privateIpAddress>10.0.2.157</privateIpAddress>
                <privateDnsName>ip-10-0-2-157.ap-southeast-1.compute.internal</privateDnsName>
                <primary>true</primary>
            </item>
        </privateIpAddressesSet>
        <ipv6AddressesSet/>
    </networkInterface>
</CreateNetworkInterfaceResponse>
```

### Example 2
<a name="API_CreateNetworkInterface_Example_2"></a>

This example creates a network interface in the specified subnet with a primary IPv4 address of `10.0.2.140` and four secondary private IPv4 addresses that are automatically selected by Amazon EC2.

#### Sample Request
<a name="API_CreateNetworkInterface_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateNetworkInterface
&PrivateIpAddresses.1.Primary=true
&PrivateIpAddresses.1.PrivateIpAddress=10.0.2.140
&SecondaryPrivateIpAddressCount=4
&SubnetId=subnet-a61dafcf
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateNetworkInterface_Example_2_Response"></a>

```
<CreateNetworkInterfaceResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
 <requestId>bd78c839-0895-4fac-a17f-example</requestId>
    <networkInterface>
        <networkInterfaceId>eni-1bcb7772</networkInterfaceId>
        <subnetId>subnet-a61dafcf</subnetId>
        <vpcId>vpc-c31dafaa</vpcId>
        <availabilityZone>ap-southeast-1b</availabilityZone>
        <description/>
        <ownerId>251839141158</ownerId>
        <requesterManaged>false</requesterManaged>
        <status>pending</status>
        <macAddress>02:74:b0:70:7f:1a</macAddress>
        <privateIpAddress>10.0.2.140</privateIpAddress>
        <sourceDestCheck>true</sourceDestCheck>
        <groupSet>
            <item>
                <groupId>sg-1a2b3c4d</groupId>
                <groupName>default</groupName>
            </item>
        </groupSet>
        <tagSet/>
        <privateIpAddressesSet>
            <item>
                <privateIpAddress>10.0.2.140</privateIpAddress>
                <primary>true</primary>
            </item>
            <item>
                <privateIpAddress>10.0.2.172</privateIpAddress>
                <primary>false</primary>
            </item>
            <item>
                <privateIpAddress>10.0.2.169</privateIpAddress>
                <primary>false</primary>
            </item>
            <item>
                <privateIpAddress>10.0.2.170</privateIpAddress>
                <primary>false</primary>
            </item>
            <item>
                <privateIpAddress>10.0.2.171</privateIpAddress>
                <primary>false</primary>
            </item>
        </privateIpAddressesSet>
        <ipv6AddressesSet/>
    </networkInterface>
</CreateNetworkInterfaceResponse>
```

### Example 3
<a name="API_CreateNetworkInterface_Example_3"></a>

This example creates a network interface with a primary private IPv4 address of 10.0.2.130 and two secondary IPv4 addresses of 10.0.2.132 and 10.0.2.133.

#### Sample Request
<a name="API_CreateNetworkInterface_Example_3_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateNetworkInterface
&PrivateIpAddresses.1.Primary=true
&PrivateIpAddresses.1.PrivateIpAddress=10.0.2.130
&PrivateIpAddresses.2.Primary=false
&PrivateIpAddresses.2.PrivateIpAddress=10.0.2.132
&PrivateIpAddresses.3.Primary=false
&PrivateIpAddresses.3.PrivateIpAddress=10.0.2.133
&SubnetId=subnet-a61dafcf
&AUTHPARAMS
```

### Example 4
<a name="API_CreateNetworkInterface_Example_4"></a>

This example creates a network interface with a primary private IPv4 address of 10.0.2.130 and two IPv6 addresses that are selected by Amazon EC2.

#### Sample Request
<a name="API_CreateNetworkInterface_Example_4_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateNetworkInterface
&PrivateIpAddresses.1.Primary=true
&PrivateIpAddresses.1.PrivateIpAddress=10.0.2.130
&Ipv6AddressCount=2
&SubnetId=subnet-a61dafcf
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateNetworkInterface_Example_4_Response"></a>

```
<CreateNetworkInterfaceResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
<requestId>a9565f4c-f928-4113-859b-example</requestId>
    <networkInterface>
        <networkInterfaceId>eni-41c47828</networkInterfaceId>
        <subnetId>subnet-a61dafcf</subnetId>
        <vpcId>vpc-c31dafaa</vpcId>
        <availabilityZone>ap-southeast-1b</availabilityZone>
        <description/>
        <ownerId>251839141158</ownerId>
        <requesterManaged>false</requesterManaged>
        <status>pending</status>
        <macAddress>02:74:b0:78:bf:ab</macAddress>
        <privateIpAddress>10.0.2.130</privateIpAddress>
        <sourceDestCheck>true</sourceDestCheck>
        <groupSet>
            <item>
                <groupId>sg-188d9f74</groupId>
                <groupName>default</groupName>
            </item>
        </groupSet>
        <tagSet/>
        <privateIpAddressesSet>
            <item>
                <privateIpAddress>10.0.2.130</privateIpAddress>
                <primary>true</primary>
            </item>
        </privateIpAddressesSet>
        <ipv6AddressesSet>
         <item>
           <ipv6Address>2001:db8:1234:1a00::123</ipv6Address>
         </item>
         <item>
           <ipv6Address>2001:db8:1234:1a00::456</ipv6Address>
         </item>
       </ipv6AddressesSet>
    </networkInterface>
</CreateNetworkInterfaceResponse>
```

## See Also
<a name="API_CreateNetworkInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateNetworkInterface)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateNetworkInterface)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateNetworkInterface)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateNetworkInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateNetworkInterface)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateNetworkInterface)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateNetworkInterface)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateNetworkInterface)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateNetworkInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateNetworkInterface)
