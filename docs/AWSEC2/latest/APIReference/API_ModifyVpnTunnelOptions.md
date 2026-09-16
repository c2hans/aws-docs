---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpnTunnelOptions.html
---

# ModifyVpnTunnelOptions
<a name="API_ModifyVpnTunnelOptions"></a>

Modifies the options for a VPN tunnel in an AWS Site-to-Site VPN connection. You can modify multiple options for a tunnel in a single request, but you can only modify one tunnel at a time. For more information, see [Site-to-Site VPN tunnel options for your Site-to-Site VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPNTunnels.html) in the * AWS Site-to-Site VPN User Guide*.

## Request Parameters
<a name="API_ModifyVpnTunnelOptions_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **PreSharedKeyStorage**
Specifies the storage mode for the pre-shared key (PSK). Valid values are `Standard` (stored in Site-to-Site VPN service) or `SecretsManager` (stored in AWS Secrets Manager).
Type: String
Required: No

 **SkipTunnelReplacement**
Choose whether or not to trigger immediate tunnel replacement. This is only applicable when turning on or off `EnableTunnelLifecycleControl`.
Valid values: `True` \| `False`
Type: Boolean
Required: No

 **TunnelOptions**
The tunnel options to modify.
Type: [ModifyVpnTunnelOptionsSpecification](API_ModifyVpnTunnelOptionsSpecification.md) object
Required: Yes

 **VpnConnectionId**
The ID of the AWS Site-to-Site VPN connection.
Type: String
Required: Yes

 **VpnTunnelOutsideIpAddress**
The external IP address of the VPN tunnel.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyVpnTunnelOptions_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **vpnConnection**
Information about the VPN connection.
Type: [VpnConnection](API_VpnConnection.md) object

## Errors
<a name="API_ModifyVpnTunnelOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ModifyVpnTunnelOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyVpnTunnelOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyVpnTunnelOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyVpnTunnelOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyVpnTunnelOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyVpnTunnelOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyVpnTunnelOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyVpnTunnelOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyVpnTunnelOptions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyVpnTunnelOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyVpnTunnelOptions)
