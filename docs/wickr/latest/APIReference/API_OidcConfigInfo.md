---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_OidcConfigInfo.html
---

# OidcConfigInfo
<a name="API_OidcConfigInfo"></a>

Contains the OpenID Connect (OIDC) configuration information for Single Sign-On (SSO) authentication, including identity provider settings and client credentials.

## Contents
<a name="API_OidcConfigInfo_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** companyId **   <a name="wickr-Type-OidcConfigInfo-companyId"></a>
Custom identifier your end users will use to sign in with SSO.
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** issuer **   <a name="wickr-Type-OidcConfigInfo-issuer"></a>
The issuer URL of the identity provider, which serves as the base URL for OIDC endpoints and configuration discovery.
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** scopes **   <a name="wickr-Type-OidcConfigInfo-scopes"></a>
The OAuth scopes requested from the identity provider, which determine what user information is accessible (e.g., 'openid profile email').
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** applicationId **   <a name="wickr-Type-OidcConfigInfo-applicationId"></a>
The unique identifier for the registered OIDC application. Valid range is 1-10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** applicationName **   <a name="wickr-Type-OidcConfigInfo-applicationName"></a>
The name of the OIDC application as registered with the identity provider.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** caCertificate **   <a name="wickr-Type-OidcConfigInfo-caCertificate"></a>
The X.509 CA certificate for validating SSL/TLS connections to the identity provider when using self-signed or enterprise certificates.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** clientId **   <a name="wickr-Type-OidcConfigInfo-clientId"></a>
The OAuth client ID assigned by the identity provider for authentication requests.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** clientSecret **   <a name="wickr-Type-OidcConfigInfo-clientSecret"></a>
The OAuth client secret used to authenticate the application with the identity provider.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** customUsername **   <a name="wickr-Type-OidcConfigInfo-customUsername"></a>
A custom field mapping to extract the username from the OIDC token when the standard username claim is insufficient.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** extraAuthParams **   <a name="wickr-Type-OidcConfigInfo-extraAuthParams"></a>
Additional authentication parameters to include in the OIDC authorization request as a query string. Useful for provider-specific extensions.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** redirectUrl **   <a name="wickr-Type-OidcConfigInfo-redirectUrl"></a>
The callback URL where the identity provider redirects users after successful authentication. This URL must be registered with the identity provider.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** secret **   <a name="wickr-Type-OidcConfigInfo-secret"></a>
An additional secret credential used by the identity provider for authentication.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** ssoTokenBufferMinutes **   <a name="wickr-Type-OidcConfigInfo-ssoTokenBufferMinutes"></a>
The grace period in minutes before the SSO token expires when the system should proactively refresh the token to maintain seamless user access.
Type: Integer
Required: No

 ** userId **   <a name="wickr-Type-OidcConfigInfo-userId"></a>
The claim field from the OIDC token to use as the unique user identifier (e.g., 'email', 'sub', or a custom claim).
Type: String
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_OidcConfigInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/OidcConfigInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/OidcConfigInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/OidcConfigInfo)
