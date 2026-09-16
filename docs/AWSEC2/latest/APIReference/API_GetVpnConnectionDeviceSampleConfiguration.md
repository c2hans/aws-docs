---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetVpnConnectionDeviceSampleConfiguration.html
---

# GetVpnConnectionDeviceSampleConfiguration
<a name="API_GetVpnConnectionDeviceSampleConfiguration"></a>

Download an AWS-provided sample configuration file to be used with the customer gateway device specified for your Site-to-Site VPN connection.

## Request Parameters
<a name="API_GetVpnConnectionDeviceSampleConfiguration_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InternetKeyExchangeVersion**
The IKE version to be used in the sample configuration file for your customer gateway device. You can specify one of the following versions: `ikev1` or `ikev2`.
Type: String
Required: No

 **SampleType**
The type of sample configuration to generate. Valid values are "compatibility" (includes IKEv1) or "recommended" (throws UnsupportedOperationException for IKEv1).
Type: String
Required: No

 **VpnConnectionDeviceTypeId**
Device identifier provided by the `GetVpnConnectionDeviceTypes` API.
Type: String
Required: Yes

 **VpnConnectionId**
The `VpnConnectionId` specifies the Site-to-Site VPN connection used for the sample configuration.
Type: String
Required: Yes

## Response Elements
<a name="API_GetVpnConnectionDeviceSampleConfiguration_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **vpnConnectionDeviceSampleConfiguration**
Sample configuration file for the specified customer gateway device.
Type: String

## Errors
<a name="API_GetVpnConnectionDeviceSampleConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetVpnConnectionDeviceSampleConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetVpnConnectionDeviceSampleConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetVpnConnectionDeviceSampleConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetVpnConnectionDeviceSampleConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetVpnConnectionDeviceSampleConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetVpnConnectionDeviceSampleConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetVpnConnectionDeviceSampleConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetVpnConnectionDeviceSampleConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetVpnConnectionDeviceSampleConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetVpnConnectionDeviceSampleConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetVpnConnectionDeviceSampleConfiguration)
