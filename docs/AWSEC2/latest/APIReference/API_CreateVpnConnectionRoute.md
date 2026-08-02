---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpnConnectionRoute.html
---

# CreateVpnConnectionRoute
<a name="API_CreateVpnConnectionRoute"></a>

Creates a static route associated with a VPN connection between an existing virtual private gateway and a VPN customer gateway. The static route allows traffic to be routed from the virtual private gateway to the VPN customer gateway.

For more information, see [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) in the * AWS Site-to-Site VPN User Guide*.

## Request Parameters
<a name="API_CreateVpnConnectionRoute_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DestinationCidrBlock**
The CIDR block associated with the local subnet of the customer network.
Type: String
Required: Yes

 **VpnConnectionId**
The ID of the VPN connection.
Type: String
Required: Yes

## Response Elements
<a name="API_CreateVpnConnectionRoute_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_CreateVpnConnectionRoute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateVpnConnectionRoute_Examples"></a>

### Example
<a name="API_CreateVpnConnectionRoute_Example_1"></a>

This example creates a static route to the VPN connection for the VPN connection with the ID `vpn-83ad48ea` to the destination CIDR block `11.12.0.0/16`. Note that when using the Query API the "/" is denoted as "%2F".

#### Sample Request
<a name="API_CreateVpnConnectionRoute_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateVpnConnectionRoute
&DestinationCidrBlock=11.12.0.0%2F16
&VpnConnectionId=vpn-83ad48ea
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateVpnConnectionRoute_Example_1_Response"></a>

```
<CreateVpnConnectionRouteResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>4f35a1b2-c2c3-4093-b51f-abb9d7311990</requestId>
    <return>true</return>
</CreateVpnConnectionRouteResponse>
```

## See Also
<a name="API_CreateVpnConnectionRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateVpnConnectionRoute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateVpnConnectionRoute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateVpnConnectionRoute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateVpnConnectionRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateVpnConnectionRoute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateVpnConnectionRoute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateVpnConnectionRoute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateVpnConnectionRoute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateVpnConnectionRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateVpnConnectionRoute)
