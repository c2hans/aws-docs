---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ClientVpnTrustProviderRequest.html
---

# ClientVpnTrustProviderRequest
<a name="API_ClientVpnTrustProviderRequest"></a>

Describes a device trust provider to configure for a Client VPN endpoint.

## Contents
<a name="API_ClientVpnTrustProviderRequest_Contents"></a>

 ** PublicSigningKeyUrl **
The URL of the public signing key that is used to verify the identity token issued by the device trust provider.
Type: String
Required: No

 ** TenantId **
The tenant ID associated with your device trust provider account.
Type: String
Required: No

 ** TrustProviderType **
The type of the device trust provider. Possible values include:
+  `crowdstrike` - CrowdStrike device trust provider.
+  `jamf` - Jamf device trust provider.
+  `jumpcloud` - JumpCloud device trust provider.
Type: String
Valid Values: `crowdstrike | jamf | jumpcloud`
Required: No

## See Also
<a name="API_ClientVpnTrustProviderRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ClientVpnTrustProviderRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ClientVpnTrustProviderRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ClientVpnTrustProviderRequest)
