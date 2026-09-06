---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CustomerGateway.html
---

# CustomerGateway
<a name="API_CustomerGateway"></a>

Describes a customer gateway.

## Contents
<a name="API_CustomerGateway_Contents"></a>

 ** bgpAsn **
The customer gateway device's Border Gateway Protocol (BGP) Autonomous System Number (ASN).
Valid values: `1` to `2,147,483,647`
Type: String
Required: No

 ** bgpAsnExtended **
The customer gateway device's Border Gateway Protocol (BGP) Autonomous System Number (ASN).
Valid values: `2,147,483,648` to `4,294,967,295`
Type: String
Required: No

 ** certificateArn **
The Amazon Resource Name (ARN) for the customer gateway certificate.
Type: String
Required: No

 ** customerGatewayId **
The ID of the customer gateway.
Type: String
Required: No

 ** deviceName **
The name of customer gateway device.
Type: String
Required: No

 ** ipAddress **
 The IP address for the customer gateway device's outside interface. The address must be static. If `OutsideIpAddressType` in your VPN connection options is set to `PrivateIpv4`, you can use an RFC6598 or RFC1918 private IPv4 address. If `OutsideIpAddressType` is set to `PublicIpv4`, you can use a public IPv4 address. If `OutsideIpAddressType` is set to `Ipv6`, you can use a public IPv6 address.
Type: String
Required: No

 ** state **
The current state of the customer gateway (`pending | available | deleting | deleted`).
Type: String
Required: No

 ** TagSet.N **
Any tags assigned to the customer gateway.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** type **
The type of VPN connection the customer gateway supports (`ipsec.1`).
Type: String
Required: No

## See Also
<a name="API_CustomerGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CustomerGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CustomerGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CustomerGateway)
