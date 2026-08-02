---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2ClientVpnEndpointAuthenticationOptionsDetails.html
---

# AwsEc2ClientVpnEndpointAuthenticationOptionsDetails
<a name="API_AwsEc2ClientVpnEndpointAuthenticationOptionsDetails"></a>

 Information about the authentication method used by the Client VPN endpoint.

## Contents
<a name="API_AwsEc2ClientVpnEndpointAuthenticationOptionsDetails_Contents"></a>

 ** ActiveDirectory **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointAuthenticationOptionsDetails-ActiveDirectory"></a>
 Information about the Active Directory, if applicable. With Active Directory authentication, clients are authenticated against existing Active Directory groups.
Type: [AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetails](API_AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetails.md) object
Required: No

 ** FederatedAuthentication **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointAuthenticationOptionsDetails-FederatedAuthentication"></a>
 Information about the IAM SAML identity provider, if applicable.
Type: [AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetails](API_AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetails.md) object
Required: No

 ** MutualAuthentication **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointAuthenticationOptionsDetails-MutualAuthentication"></a>
 Information about the authentication certificates, if applicable.
Type: [AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetails](API_AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetails.md) object
Required: No

 ** Type **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointAuthenticationOptionsDetails-Type"></a>
 The authentication type used.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2ClientVpnEndpointAuthenticationOptionsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2ClientVpnEndpointAuthenticationOptionsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2ClientVpnEndpointAuthenticationOptionsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2ClientVpnEndpointAuthenticationOptionsDetails)
