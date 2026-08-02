---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpnGateway.html
---

# CreateVpnGateway
<a name="API_CreateVpnGateway"></a>

Creates a virtual private gateway. A virtual private gateway is the endpoint on the VPC side of your VPN connection. You can create a virtual private gateway before creating the VPC itself.

For more information, see [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) in the * AWS Site-to-Site VPN User Guide*.

## Request Parameters
<a name="API_CreateVpnGateway_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AmazonSideAsn**
A private Autonomous System Number (ASN) for the Amazon side of a BGP session. If you're using a 16-bit ASN, it must be in the 64512 to 65534 range. If you're using a 32-bit ASN, it must be in the 4200000000 to 4294967294 range.
Default: 64512
Type: Long
Required: No

 **AvailabilityZone**
The Availability Zone for the virtual private gateway.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **TagSpecification.N**
The tags to apply to the virtual private gateway.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **Type**
The type of VPN connection this virtual private gateway supports.
Type: String
Valid Values: `ipsec.1`
Required: Yes

## Response Elements
<a name="API_CreateVpnGateway_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **vpnGateway**
Information about the virtual private gateway.
Type: [VpnGateway](API_VpnGateway.md) object

## Errors
<a name="API_CreateVpnGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateVpnGateway_Examples"></a>

### Example 1
<a name="API_CreateVpnGateway_Example_1"></a>

This example creates a virtual private gateway.

#### Sample Request
<a name="API_CreateVpnGateway_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateVpnGateway
&Type=ipsec.1
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateVpnGateway_Example_1_Response"></a>

```
<CreateVpnGatewayResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
  <vpnGateway>
        <vpnGatewayId>vgw-fe4aa197</vpnGatewayId>
        <state>available</state>
        <type>ipsec.1</type>
        <amazonSideAsn>64512</amazonSideAsn>
        <attachments/>
    </vpnGateway>
</CreateVpnGatewayResponse>
```

### Example 2
<a name="API_CreateVpnGateway_Example_2"></a>

This example creates a virtual private gateway and specifies a private ASN of 65001 for the Amazon side of the gateway.

#### Sample Request
<a name="API_CreateVpnGateway_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateVpnGateway
&Type=ipsec.1
&AmazonSideAsn=65001
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateVpnGateway_Example_2_Response"></a>

```
<CreateVpnGatewayResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>fe90b404-d4e5-4153-8677-31dexample</requestId>
    <vpnGateway>
        <vpnGatewayId>vgw-f74aa19e</vpnGatewayId>
        <state>available</state>
        <type>ipsec.1</type>
        <amazonSideAsn>65001</amazonSideAsn>
        <attachments/>
    </vpnGateway>
</CreateVpnGatewayResponse>
```

## See Also
<a name="API_CreateVpnGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateVpnGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateVpnGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateVpnGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateVpnGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateVpnGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateVpnGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateVpnGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateVpnGateway)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateVpnGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateVpnGateway)
