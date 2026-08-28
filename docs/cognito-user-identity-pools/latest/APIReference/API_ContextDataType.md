---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ContextDataType.html
---

# ContextDataType
<a name="API_ContextDataType"></a>

Contextual user data used for evaluating the risk of an authentication event by user pool threat protection.

This data type is a request parameter of server-side authentication operations like [AdminInitiateAuth](API_AdminInitiateAuth.md) and [AdminRespondToAuthChallenge](API_AdminRespondToAuthChallenge.md).

## Contents
<a name="API_ContextDataType_Contents"></a>

 ** HttpHeaders **   <a name="CognitoUserPools-Type-ContextDataType-HttpHeaders"></a>
The HTTP headers from your user's authentication request.
Type: Array of [HttpHeader](API_HttpHeader.md) objects
Required: Yes

 ** IpAddress **   <a name="CognitoUserPools-Type-ContextDataType-IpAddress"></a>
The source IP address of your user's device.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: Yes

 ** ServerName **   <a name="CognitoUserPools-Type-ContextDataType-ServerName"></a>
The name of your application's service endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: Yes

 ** ServerPath **   <a name="CognitoUserPools-Type-ContextDataType-ServerPath"></a>
The path of your application's service endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: Yes

 ** EncodedData **   <a name="CognitoUserPools-Type-ContextDataType-EncodedData"></a>
Encoded device-fingerprint details that your app collected with the Amazon Cognito context data collection library. For more information, see [Adding user device and session data to API requests](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-adaptive-authentication.html#user-pool-settings-adaptive-authentication-device-fingerprint).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

## See Also
<a name="API_ContextDataType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/ContextDataType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/ContextDataType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/ContextDataType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
