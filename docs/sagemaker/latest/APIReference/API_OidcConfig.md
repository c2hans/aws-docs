---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OidcConfig.html
---

# OidcConfig
<a name="API_OidcConfig"></a>

Use this parameter to configure your OIDC Identity Provider (IdP).

## Contents
<a name="API_OidcConfig_Contents"></a>

 ** AuthorizationEndpoint **   <a name="sagemaker-Type-OidcConfig-AuthorizationEndpoint"></a>
The OIDC IdP authorization endpoint used to configure your private workforce.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `https://\S+`
Required: Yes

 ** ClientId **   <a name="sagemaker-Type-OidcConfig-ClientId"></a>
The OIDC IdP client ID used to configure your private workforce.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[ -~]+`
Required: Yes

 ** ClientSecret **   <a name="sagemaker-Type-OidcConfig-ClientSecret"></a>
The OIDC IdP client secret used to configure your private workforce.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[ -~]+`
Required: Yes

 ** Issuer **   <a name="sagemaker-Type-OidcConfig-Issuer"></a>
The OIDC IdP issuer used to configure your private workforce.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `https://\S+`
Required: Yes

 ** JwksUri **   <a name="sagemaker-Type-OidcConfig-JwksUri"></a>
The OIDC IdP JSON Web Key Set (Jwks) URI used to configure your private workforce.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `https://\S+`
Required: Yes

 ** LogoutEndpoint **   <a name="sagemaker-Type-OidcConfig-LogoutEndpoint"></a>
The OIDC IdP logout endpoint used to configure your private workforce.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `https://\S+`
Required: Yes

 ** TokenEndpoint **   <a name="sagemaker-Type-OidcConfig-TokenEndpoint"></a>
The OIDC IdP token endpoint used to configure your private workforce.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `https://\S+`
Required: Yes

 ** UserInfoEndpoint **   <a name="sagemaker-Type-OidcConfig-UserInfoEndpoint"></a>
The OIDC IdP user information endpoint used to configure your private workforce.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `https://\S+`
Required: Yes

 ** AuthenticationRequestExtraParams **   <a name="sagemaker-Type-OidcConfig-AuthenticationRequestExtraParams"></a>
A string to string map of identifiers specific to the custom identity provider (IdP) being used.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 0. Maximum length of 512.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 0. Maximum length of 512.
Value Pattern: `.*`
Required: No

 ** Scope **   <a name="sagemaker-Type-OidcConfig-Scope"></a>
An array of string identifiers used to refer to the specific pieces of user data or claims that the client application wants to access.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[!#-\[\]-~]+( [!#-\[\]-~]+)*`
Required: No

## See Also
<a name="API_OidcConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/OidcConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/OidcConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/OidcConfig)
