---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AuthenticationResultType.html
---

# AuthenticationResultType
<a name="API_AuthenticationResultType"></a>

The object that your application receives after authentication. Contains tokens and information for device authentication.

This data type is a response parameter of authentication operations like [InitiateAuth](API_InitiateAuth.md), [AdminInitiateAuth](API_AdminInitiateAuth.md), [RespondToAuthChallenge](API_RespondToAuthChallenge.md), [AdminRespondToAuthChallenge](API_AdminRespondToAuthChallenge.md), and [GetTokensFromRefreshToken](API_GetTokensFromRefreshToken.md). `GetTokensFromRefreshToken` doesn't return `NewDeviceMetadata`.

## Contents
<a name="API_AuthenticationResultType_Contents"></a>

 ** AccessToken **   <a name="CognitoUserPools-Type-AuthenticationResultType-AccessToken"></a>
Your user's access token.
Type: String
Pattern: `[A-Za-z0-9-_=.]+`
Required: No

 ** ExpiresIn **   <a name="CognitoUserPools-Type-AuthenticationResultType-ExpiresIn"></a>
The expiration period of the authentication result in seconds.
Type: Integer
Required: No

 ** IdToken **   <a name="CognitoUserPools-Type-AuthenticationResultType-IdToken"></a>
Your user's ID token.
Type: String
Pattern: `[A-Za-z0-9-_=.]+`
Required: No

 ** NewDeviceMetadata **   <a name="CognitoUserPools-Type-AuthenticationResultType-NewDeviceMetadata"></a>
The new device metadata from an authentication result.
Type: [NewDeviceMetadataType](API_NewDeviceMetadataType.md) object
Required: No

 ** RefreshToken **   <a name="CognitoUserPools-Type-AuthenticationResultType-RefreshToken"></a>
Your user's refresh token.
Type: String
Pattern: `[A-Za-z0-9-_=.]+`
Required: No

 ** TokenType **   <a name="CognitoUserPools-Type-AuthenticationResultType-TokenType"></a>
The intended use of the token, for example `Bearer`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

## See Also
<a name="API_AuthenticationResultType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AuthenticationResultType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AuthenticationResultType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AuthenticationResultType)
