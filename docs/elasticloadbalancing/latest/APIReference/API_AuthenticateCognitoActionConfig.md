---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_AuthenticateCognitoActionConfig.html
---

# AuthenticateCognitoActionConfig
<a name="API_AuthenticateCognitoActionConfig"></a>

Request parameters to use when integrating with Amazon Cognito to authenticate users.

## Contents
<a name="API_AuthenticateCognitoActionConfig_Contents"></a>

 ** UserPoolArn **
The Amazon Resource Name (ARN) of the Amazon Cognito user pool.
Type: String
Required: Yes

 ** UserPoolClientId **
The ID of the Amazon Cognito user pool client.
Type: String
Required: Yes

 ** UserPoolDomain **
The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.
Type: String
Required: Yes

 ** AuthenticationRequestExtraParams **  AuthenticationRequestExtraParams.entry.N.key (key)  AuthenticationRequestExtraParams.entry.N.value (value)
The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
Type: String to string map
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

## See Also
<a name="API_AuthenticateCognitoActionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/AuthenticateCognitoActionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/AuthenticateCognitoActionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/AuthenticateCognitoActionConfig)
