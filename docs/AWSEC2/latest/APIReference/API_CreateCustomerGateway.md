---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateCustomerGateway.html
---

# CreateCustomerGateway
<a name="API_CreateCustomerGateway"></a>

Provides information to AWS about your customer gateway device. The customer gateway device is the appliance at your end of the VPN connection. You must provide the IP address of the customer gateway device’s external interface. The IP address must be static and can be behind a device performing network address translation (NAT).

For devices that use Border Gateway Protocol (BGP), you can also provide the device's BGP Autonomous System Number (ASN). You can use an existing ASN assigned to your network. If you don't have an ASN already, you can use a private ASN. For more information, see [Customer gateway options for your Site-to-Site VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/cgw-options.html) in the * AWS Site-to-Site VPN User Guide*.

To create more than one customer gateway with the same VPN type, IP address, and BGP ASN, specify a unique device name for each customer gateway. An identical request returns information about the existing customer gateway; it doesn't create a new customer gateway.

## Request Parameters
<a name="API_CreateCustomerGateway_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **BgpAsn**
For customer gateway devices that support BGP, specify the device's ASN. You must specify either `BgpAsn` or `BgpAsnExtended` when creating the customer gateway. If the ASN is larger than `2,147,483,647`, you must use `BgpAsnExtended`.
Default: 65000
Valid values: `1` to `2,147,483,647`
Type: Integer
Required: No

 **BgpAsnExtended**
For customer gateway devices that support BGP, specify the device's ASN. You must specify either `BgpAsn` or `BgpAsnExtended` when creating the customer gateway. If the ASN is larger than `2,147,483,647`, you must use `BgpAsnExtended`.
Valid values: `2,147,483,648` to `4,294,967,295`
Type: Long
Required: No

 **CertificateArn**
The Amazon Resource Name (ARN) for the customer gateway certificate.
Type: String
Required: No

 **DeviceName**
A name for the customer gateway device.
Length Constraints: Up to 255 characters.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **IpAddress**
The IP address for the customer gateway device's outside interface. The address must be static. If `OutsideIpAddressType` in your VPN connection options is set to `PrivateIpv4`, you can use an RFC6598 or RFC1918 private IPv4 address. If `OutsideIpAddressType` is set to `Ipv6`, you can use an IPv6 address.
Type: String
Required: No

 **PublicIp**
 *This member has been deprecated.* The Internet-routable IP address for the customer gateway's outside interface. The address must be static.
Type: String
Required: No

 **TagSpecification.N**
The tags to apply to the customer gateway.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **Type**
The type of VPN connection that this customer gateway supports (`ipsec.1`).
Type: String
Valid Values: `ipsec.1`
Required: Yes

## Response Elements
<a name="API_CreateCustomerGateway_ResponseElements"></a>

The following elements are returned by the service.

 **customerGateway**
Information about the customer gateway.
Type: [CustomerGateway](API_CustomerGateway.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateCustomerGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateCustomerGateway_Examples"></a>

### Example
<a name="API_CreateCustomerGateway_Example_1"></a>

This example creates a customer gateway with the name `my-device`, the IP address `12.1.2.3`, and BGP ASN `65534`.

#### Sample Request
<a name="API_CreateCustomerGateway_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateCustomerGateway
&Type=ipsec.1
&IpAddress=12.1.2.3
&BgpAsn=65534
&DeviceName=my-device
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateCustomerGateway_Example_1_Response"></a>

```
<CreateCustomerGatewayResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
   <customerGateway>
      <customerGatewayId>cgw-11223344556677abc</customerGatewayId>
      <state>pending</state>
      <type>ipsec.1</type>
      <ipAddress>12.1.2.3</ipAddress>
      <bgpAsn>65534</bgpAsn>
      <deviceName>my-device</deviceName>
      <tagSet/>
   </customerGateway>
</CreateCustomerGatewayResponse>
```

## See Also
<a name="API_CreateCustomerGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateCustomerGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateCustomerGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateCustomerGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateCustomerGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateCustomerGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateCustomerGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateCustomerGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateCustomerGateway)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateCustomerGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateCustomerGateway)
