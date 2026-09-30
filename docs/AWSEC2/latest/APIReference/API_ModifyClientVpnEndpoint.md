---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyClientVpnEndpoint.html
---

# ModifyClientVpnEndpoint
<a name="API_ModifyClientVpnEndpoint"></a>

Modifies the specified Client VPN endpoint. Modifying the DNS server resets existing client connections.

## Request Parameters
<a name="API_ModifyClientVpnEndpoint_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientConnectOptions**
The options for managing connection authorization for new client connections.
Type: [ClientConnectOptions](API_ClientConnectOptions.md) object
Required: No

 **ClientLoginBannerOptions**
Options for enabling a customizable text banner that will be displayed on AWS provided clients when a VPN session is established.
Type: [ClientLoginBannerOptions](API_ClientLoginBannerOptions.md) object
Required: No

 **ClientRouteEnforcementOptions**
Client route enforcement is a feature of the Client VPN service that helps enforce administrator defined routes on devices connected through the VPN. T his feature helps improve your security posture by ensuring that network traffic originating from a connected client is not inadvertently sent outside the VPN tunnel.
Client route enforcement works by monitoring the route table of a connected device for routing policy changes to the VPN connection. If the feature detects any VPN routing policy modifications, it will automatically force an update to the route table, reverting it back to the expected route configurations.
Type: [ClientRouteEnforcementOptions](API_ClientRouteEnforcementOptions.md) object
Required: No

 **ClientVpnEndpointId**
The ID of the Client VPN endpoint to modify.
Type: String
Required: Yes

 **ConnectionLogOptions**
Information about the client connection logging options.
If you enable client connection logging, data about client connections is sent to a Cloudwatch Logs log stream. The following information is logged:
+ Client connection requests
+ Client connection results (successful and unsuccessful)
+ Reasons for unsuccessful client connection requests
+ Client connection termination time
Type: [ConnectionLogOptions](API_ConnectionLogOptions.md) object
Required: No

 **Description**
A brief description of the Client VPN endpoint.
Type: String
Required: No

 **DevicePostureOptions**
The device posture options for the Client VPN endpoint. Specifying this parameter replaces the entire device posture configuration for the endpoint. To disable device posture and remove all device trust providers, specify `false` for `Enabled`.
Type: [DevicePostureOptions](API_DevicePostureOptions.md) object
Required: No

 **DisconnectOnSessionTimeout**
Indicates whether the client VPN session is disconnected after the maximum timeout specified in `sessionTimeoutHours` is reached. If `true`, users are prompted to reconnect client VPN. If `false`, client VPN attempts to reconnect automatically. The default value is `true`.
Type: Boolean
Required: No

 **DnsServers**
Information about the DNS servers to be used by Client VPN connections. A Client VPN endpoint can have up to two DNS servers.
Type: [DnsServersOptionsModifyStructure](API_DnsServersOptionsModifyStructure.md) object
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **SecurityGroupId.N**
The IDs of one or more security groups to apply to the target network.
Type: Array of strings
Required: No

 **SelfServicePortal**
Specify whether to enable the self-service portal for the Client VPN endpoint.
Type: String
Valid Values: `enabled | disabled`
Required: No

 **ServerCertificateArn**
The ARN of the server certificate to be used. The server certificate must be provisioned in AWS Certificate Manager (ACM).
Type: String
Required: No

 **SessionTimeoutHours**
The maximum VPN session duration time in hours.
Valid values: `8 | 10 | 12 | 24`
Default value: `24`
Type: Integer
Required: No

 **SplitTunnel**
Indicates whether the VPN is split-tunnel.
For information about split-tunnel VPN endpoints, see [Split-tunnel AWS Client VPN endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/split-tunnel-vpn.html) in the * AWS Client VPN Administrator Guide*.
Type: Boolean
Required: No

 **TransitGatewayConfiguration**
The Transit Gateway configuration for the Client VPN endpoint. This option is currently not supported.
Type: [TransitGatewayConfigurationInputStructure](API_TransitGatewayConfigurationInputStructure.md) object
Required: No

 **VpcId**
The ID of the VPC to associate with the Client VPN endpoint.
Type: String
Required: No

 **VpnPort**
The port number to assign to the Client VPN endpoint for TCP and UDP traffic.
Valid Values: `443` \| `1194`
Default Value: `443`
Type: Integer
Required: No

## Response Elements
<a name="API_ModifyClientVpnEndpoint_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, it returns an error.
Type: Boolean

## Errors
<a name="API_ModifyClientVpnEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyClientVpnEndpoint_Examples"></a>

### Example
<a name="API_ModifyClientVpnEndpoint_Example_1"></a>

This example modifies a Client VPN endpoint's description.

#### Sample Request
<a name="API_ModifyClientVpnEndpoint_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyClientVpnEndpoint
&ClientVpnEndpointId=cvpn-endpoint-00c5d11fc4EXAMPLE
&Description=my-client-vpn-endpoint
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyClientVpnEndpoint_Example_1_Response"></a>

```
<ModifyClientVpnEndpointResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>fe4813d3-1e79-4f67-bbd7-3186eEXAMPLE</requestId>
    <return>true</return>
</ModifyClientVpnEndpointResponse>
```

## See Also
<a name="API_ModifyClientVpnEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyClientVpnEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyClientVpnEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyClientVpnEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyClientVpnEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyClientVpnEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyClientVpnEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyClientVpnEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyClientVpnEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyClientVpnEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyClientVpnEndpoint)
