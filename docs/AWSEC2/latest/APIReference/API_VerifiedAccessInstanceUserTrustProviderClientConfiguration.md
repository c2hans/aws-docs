---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VerifiedAccessInstanceUserTrustProviderClientConfiguration.html
---

# VerifiedAccessInstanceUserTrustProviderClientConfiguration
<a name="API_VerifiedAccessInstanceUserTrustProviderClientConfiguration"></a>

Describes the trust provider.

## Contents
<a name="API_VerifiedAccessInstanceUserTrustProviderClientConfiguration_Contents"></a>

 ** authorizationEndpoint **
The authorization endpoint of the IdP.
Type: String
Required: No

 ** clientId **
The OAuth 2.0 client identifier.
Type: String
Required: No

 ** clientSecret **
The OAuth 2.0 client secret.
Type: String
Required: No

 ** issuer **
The OIDC issuer identifier of the IdP.
Type: String
Required: No

 ** pkceEnabled **
Indicates whether Proof of Key Code Exchange (PKCE) is enabled.
Type: Boolean
Required: No

 ** publicSigningKeyEndpoint **
The public signing key endpoint.
Type: String
Required: No

 ** scopes **
The set of user claims to be requested from the IdP.
Type: String
Required: No

 ** tokenEndpoint **
The token endpoint of the IdP.
Type: String
Required: No

 ** type **
The trust provider type.
Type: String
Valid Values: `iam-identity-center | oidc`
Required: No

 ** userInfoEndpoint **
The user info endpoint of the IdP.
Type: String
Required: No

## See Also
<a name="API_VerifiedAccessInstanceUserTrustProviderClientConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VerifiedAccessInstanceUserTrustProviderClientConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VerifiedAccessInstanceUserTrustProviderClientConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VerifiedAccessInstanceUserTrustProviderClientConfiguration)
