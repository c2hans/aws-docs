---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssignIpv6Addresses.html
---

# AssignIpv6Addresses
<a name="API_AssignIpv6Addresses"></a>

Assigns the specified IPv6 addresses to the specified network interface. You can specify specific IPv6 addresses, or you can specify the number of IPv6 addresses to be automatically assigned from the subnet's IPv6 CIDR block range. You can assign as many IPv6 addresses to a network interface as you can assign private IPv4 addresses, and the limit varies by instance type.

You must specify either the IPv6 addresses or the IPv6 address count in the request.

You can optionally use Prefix Delegation on the network interface. You must specify either the IPV6 Prefix Delegation prefixes, or the IPv6 Prefix Delegation count. For information, see [ Assigning prefixes to network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-prefix-eni.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_AssignIpv6Addresses_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Ipv6AddressCount**
The number of additional IPv6 addresses to assign to the network interface. The specified number of IPv6 addresses are assigned in addition to the existing IPv6 addresses that are already assigned to the network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. You can't use this option if specifying specific IPv6 addresses.
Type: Integer
Required: No

 **Ipv6Addresses.N**
The IPv6 addresses to be assigned to the network interface. You can't use this option if you're specifying a number of IPv6 addresses.
Type: Array of strings
Required: No

 **Ipv6Prefix.N**
One or more IPv6 prefixes assigned to the network interface. You can't use this option if you use the `Ipv6PrefixCount` option.
Type: Array of strings
Required: No

 **Ipv6PrefixCount**
The number of IPv6 prefixes that AWS automatically assigns to the network interface. You cannot use this option if you use the `Ipv6Prefixes` option.
Type: Integer
Required: No

 **NetworkInterfaceId**
The ID of the network interface.
Type: String
Required: Yes

## Response Elements
<a name="API_AssignIpv6Addresses_ResponseElements"></a>

The following elements are returned by the service.

 **assignedIpv6Addresses**
The new IPv6 addresses assigned to the network interface. Existing IPv6 addresses that were assigned to the network interface before the request are not included.
Type: Array of strings

 **assignedIpv6PrefixSet**
The IPv6 prefixes that are assigned to the network interface.
Type: Array of strings

 **networkInterfaceId**
The ID of the network interface.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_AssignIpv6Addresses_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_AssignIpv6Addresses_Examples"></a>

### Example 1
<a name="API_AssignIpv6Addresses_Example_1"></a>

This example assigns two IPv6 addresses (`2001:db8:1234:1a00::123` and `2001:db8:1234:1a00::456`) to the specified network interface.

#### Sample Request
<a name="API_AssignIpv6Addresses_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=AssignIpv6Addresses
&NetworkInterfaceId=eni-d83388b1
&Ipv6Addresses.1=2001:db8:1234:1a00::123
&Ipv6Addresses.2=2001:db8:1234:1a00::456
&AUTHPARAMS
```

#### Sample Response
<a name="API_AssignIpv6Addresses_Example_1_Response"></a>

```
<AssignIpv6AddressesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>c36d17eb-a0ba-4d38-8727-example</requestId>
    <networkInterfaceId>eni-d83388b1</networkInterfaceId>
    <assignedIpv6Addresses>
        <item>2001:db8:1234:1a00::123</item>
        <item>2001:db8:1234:1a00::456</item>
    </assignedIpv6Addresses>
</AssignIpv6AddressesResponse>
```

### Example 2
<a name="API_AssignIpv6Addresses_Example_2"></a>

This example assigns two IPv6 addresses to the specified network interface. Amazon EC2 automatically assigns the addresses from the available IPv6 addresses within the subnet's IPv6 CIDR block range.

#### Sample Request
<a name="API_AssignIpv6Addresses_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=AssignIpv6Addresses
&NetworkInterfaceId=eni-d83388b1
&Ipv6AddressCount=2
&AUTHPARAMS
```

#### Sample Response
<a name="API_AssignIpv6Addresses_Example_2_Response"></a>

```
<AssignIpv6AddressesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>c36d17eb-a0ba-4d38-8727-example</requestId>
    <networkInterfaceId>eni-d83388b1</networkInterfaceId>
    <assignedIpv6Addresses>
        <item>2001:db8:1234:1a00:3304:8879:34cf:4071</item>
        <item>2002:db8:1234:1a00:9691:9503:25ad:1761</item>
    </assignedIpv6Addresses>
</AssignIpv6AddressesResponse>
```

## See Also
<a name="API_AssignIpv6Addresses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AssignIpv6Addresses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AssignIpv6Addresses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AssignIpv6Addresses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AssignIpv6Addresses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AssignIpv6Addresses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AssignIpv6Addresses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AssignIpv6Addresses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AssignIpv6Addresses)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AssignIpv6Addresses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AssignIpv6Addresses)
