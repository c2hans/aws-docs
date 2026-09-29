---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DevicePostureOptions.html
---

# DevicePostureOptions
<a name="API_DevicePostureOptions"></a>

Describes the device posture options for a Client VPN endpoint. Device posture options specify the device trust providers that the endpoint uses to evaluate the security posture of connecting devices.

## Contents
<a name="API_DevicePostureOptions_Contents"></a>

 ** Enabled **
Indicates whether device posture evaluation is enabled for the Client VPN endpoint. Specify `false` to disable device posture, which clears the configured device trust providers.
Type: Boolean
Required: No

 ** TrustProvider.N **
The device trust providers to configure for the Client VPN endpoint.
Type: Array of [ClientVpnTrustProviderRequest](API_ClientVpnTrustProviderRequest.md) objects
Required: No

## See Also
<a name="API_DevicePostureOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DevicePostureOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DevicePostureOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DevicePostureOptions)
