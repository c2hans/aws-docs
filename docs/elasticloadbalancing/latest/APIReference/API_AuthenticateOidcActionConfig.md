---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_AuthenticateOidcActionConfig.html
---

# AuthenticateOidcActionConfig
<a name="API_AuthenticateOidcActionConfig"></a>

Request parameters when using an identity provider (IdP) that is compliant with OpenID Connect (OIDC) to authenticate users.

## Contents
<a name="API_AuthenticateOidcActionConfig_Contents"></a>

 ** AuthorizationEndpoint **
The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
Type: String
Required: Yes

 ** ClientId **
The OAuth 2.0 client identifier.
Type: String
Required: Yes

 ** Issuer **
The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
Type: String
Required: Yes

 ** TokenEndpoint **
The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
Type: String
Required: Yes

 ** UserInfoEndpoint **
The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
Type: String
Required: Yes

 ** AuthenticationRequestExtraParams **  AuthenticationRequestExtraParams.entry.N.key (key)  AuthenticationRequestExtraParams.entry.N.value (value)
The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
Type: String to string map
Required: No

 ** ClientSecret **
The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you are modifying a rule, you can omit this parameter if you set `UseExistingClientSecret` to true.
Type: String
Required: No

 ** OnUnauthenticatedRequest **
The behavior if the user is not authenticated. The following are possible values:
+ deny`` - Return an HTTP 401 Unauthorized error.
+ allow`` - Allow the request to be forwarded to the target.
+ authenticate`` - Redirect the request to the IdP authorization endpoint. This is the default value.
Type: String
Valid Values: `deny | allow | authenticate`
Required: No

 ** Scope **
The set of user claims to be requested from the IdP. The default is `openid`.
To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
Type: String
Required: No

 ** SessionCookieName **
The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
Type: String
Required: No

 ** SessionTimeout **
The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
Type: Long
Required: No

 ** UseExistingClientSecret **
Indicates whether to use the existing client secret when modifying a rule. If you are creating a rule, you can omit this parameter or set it to false.
Type: Boolean
Required: No

## See Also
<a name="API_AuthenticateOidcActionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/AuthenticateOidcActionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/AuthenticateOidcActionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/AuthenticateOidcActionConfig)
