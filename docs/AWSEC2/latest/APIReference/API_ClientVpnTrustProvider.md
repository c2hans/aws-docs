---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ClientVpnTrustProvider.html
---

# ClientVpnTrustProvider
<a name="API_ClientVpnTrustProvider"></a>

Information about a device trust provider configured for a Client VPN endpoint.

## Contents
<a name="API_ClientVpnTrustProvider_Contents"></a>

 ** publicSigningKeyUrl **
The URL of the public signing key that is used to verify the identity token issued by the device trust provider.
Type: String
Required: No

 ** tenantId **
The tenant ID associated with your device trust provider account.
Type: String
Required: No

 ** trustProviderType **
The type of the device trust provider. Possible values include:
+  `crowdstrike` - CrowdStrike device trust provider.
+  `jamf` - Jamf device trust provider.
+  `jumpcloud` - JumpCloud device trust provider.
Type: String
Valid Values: `crowdstrike | jamf | jumpcloud`
Required: No

## See Also
<a name="API_ClientVpnTrustProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ClientVpnTrustProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ClientVpnTrustProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ClientVpnTrustProvider)
