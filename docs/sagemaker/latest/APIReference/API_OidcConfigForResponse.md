---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OidcConfigForResponse.html
---

# OidcConfigForResponse
<a name="API_OidcConfigForResponse"></a>

Your OIDC IdP workforce configuration.

## Contents
<a name="API_OidcConfigForResponse_Contents"></a>

 ** AuthenticationRequestExtraParams **   <a name="sagemaker-Type-OidcConfigForResponse-AuthenticationRequestExtraParams"></a>
A string to string map of identifiers specific to the custom identity provider (IdP) being used.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 0. Maximum length of 512.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 0. Maximum length of 512.
Value Pattern: `.*`
Required: No

 ** AuthorizationEndpoint **   <a name="sagemaker-Type-OidcConfigForResponse-AuthorizationEndpoint"></a>
The OIDC IdP authorization endpoint used to configure your private workforce.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `https://\S+`
Required: No

 ** ClientId **   <a name="sagemaker-Type-OidcConfigForResponse-ClientId"></a>
The OIDC IdP client ID used to configure your private workforce.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[ -~]+`
Required: No

 ** Issuer **   <a name="sagemaker-Type-OidcConfigForResponse-Issuer"></a>
The OIDC IdP issuer used to configure your private workforce.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `https://\S+`
Required: No

 ** JwksUri **   <a name="sagemaker-Type-OidcConfigForResponse-JwksUri"></a>
The OIDC IdP JSON Web Key Set (Jwks) URI used to configure your private workforce.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `https://\S+`
Required: No

 ** LogoutEndpoint **   <a name="sagemaker-Type-OidcConfigForResponse-LogoutEndpoint"></a>
The OIDC IdP logout endpoint used to configure your private workforce.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `https://\S+`
Required: No

 ** Scope **   <a name="sagemaker-Type-OidcConfigForResponse-Scope"></a>
An array of string identifiers used to refer to the specific pieces of user data or claims that the client application wants to access.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[!#-\[\]-~]+( [!#-\[\]-~]+)*`
Required: No

 ** TokenEndpoint **   <a name="sagemaker-Type-OidcConfigForResponse-TokenEndpoint"></a>
The OIDC IdP token endpoint used to configure your private workforce.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `https://\S+`
Required: No

 ** UserInfoEndpoint **   <a name="sagemaker-Type-OidcConfigForResponse-UserInfoEndpoint"></a>
The OIDC IdP user information endpoint used to configure your private workforce.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `https://\S+`
Required: No

## See Also
<a name="API_OidcConfigForResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/OidcConfigForResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/OidcConfigForResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/OidcConfigForResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
