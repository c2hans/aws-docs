---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ClientAuthenticationResultType.html
---

# ClientAuthenticationResultType
<a name="API_ClientAuthenticationResultType"></a>

The access token and its metadata from a machine-to-machine (M2M) client credentials grant.

This data type is a response parameter of [GetClientToken](API_GetClientToken.md).

## Contents
<a name="API_ClientAuthenticationResultType_Contents"></a>

 ** AccessToken **   <a name="CognitoUserPools-Type-ClientAuthenticationResultType-AccessToken"></a>
The access token for the requested app client. Present this token to a resource server to authorize a request, using the scopes granted in the token.
Type: String
Pattern: `[A-Za-z0-9-_=.]+`
Required: No

 ** ExpiresIn **   <a name="CognitoUserPools-Type-ClientAuthenticationResultType-ExpiresIn"></a>
The number of seconds until the access token expires.
Type: Integer
Required: No

 ** TokenType **   <a name="CognitoUserPools-Type-ClientAuthenticationResultType-TokenType"></a>
The type of the token. For example, `Bearer`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

## See Also
<a name="API_ClientAuthenticationResultType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/ClientAuthenticationResultType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/ClientAuthenticationResultType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/ClientAuthenticationResultType)
