---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetDerivedToken.html
---

# GetDerivedToken
<a name="API_GetDerivedToken"></a>

Exchanges an existing token for a new token that is scoped and audience-bound for a specific downstream service, following the OAuth 2.0 Token Exchange grant type. For more information about the OAuth 2.0 Token Exchange grant type, see [RFC 8693 - OAuth 2.0 Token Exchange](https://tools.ietf.org/html/rfc8693) on the IETF website. Present a `SubjectToken`, the credential that you already hold, to receive a new token appropriate for calling a specific resource server or audience.

If you also present an `ActorToken` that identifies an intermediary service, the issued token carries an `act` claim that identifies the intermediary, and downstream services can distinguish a user acting directly from an intermediary acting on the user's behalf. If you don't present an `ActorToken`, the issued token appears as if the user acted directly.

To use this operation, you must have IAM credentials, or you must present the requesting app client's `ClientId` and, if the client has a secret, `ClientSecret`, in the request.

The requesting app client must have `ALLOW_TOKEN_EXCHANGE_IMPERSONATION` or `ALLOW_TOKEN_EXCHANGE_DELEGATION` in its `ExplicitAuthFlows` (depending on whether you include an `ActorToken`), or the request fails.

## Request Syntax
<a name="API_GetDerivedToken_RequestSyntax"></a>

```
{
   "ActorToken": "{{string}}",
   "ActorTokenProviderName": "{{string}}",
   "ActorTokenType": "{{string}}",
   "Audiences": [ "{{string}}" ],
   "ClientId": "{{string}}",
   "ClientSecret": "{{string}}",
   "RequestedTokenType": "{{string}}",
   "Resources": [ "{{string}}" ],
   "Scopes": [ "{{string}}" ],
   "SubjectToken": "{{string}}",
   "SubjectTokenProviderName": "{{string}}",
   "SubjectTokenType": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDerivedToken_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ActorToken](#API_GetDerivedToken_RequestSyntax) **   <a name="CognitoUserPools-GetDerivedToken-request-ActorToken"></a>
A token that identifies the intermediary service that is exchanging the token on behalf of the user. When you provide an `ActorToken`, the token that Amazon Cognito issues carries an `act` claim that identifies the intermediary, so that downstream services can distinguish a user acting directly from an intermediary acting on the user's behalf.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Pattern: `[A-Za-z0-9-_+/=.]+`
Required: No

 ** [ActorTokenProviderName](#API_GetDerivedToken_RequestSyntax) **   <a name="CognitoUserPools-GetDerivedToken-request-ActorTokenProviderName"></a>
The name of the third-party identity provider that issued the `ActorToken`, if the actor token isn't a Amazon Cognito token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\p{Z}]+`
Required: No

 ** [ActorTokenType](#API_GetDerivedToken_RequestSyntax) **   <a name="CognitoUserPools-GetDerivedToken-request-ActorTokenType"></a>
The type of the `ActorToken` that you provide. Required when you provide an `ActorToken`. Valid values:
+  `ACCESS_TOKEN` – The actor token is an access token.
+  `ID_TOKEN` – The actor token is an ID token.
+  `SAML2` – The actor token is a SAML 2.0 assertion.
Type: String
Valid Values: `ACCESS_TOKEN | ID_TOKEN | SAML2`
Required: No

 ** [Audiences](#API_GetDerivedToken_RequestSyntax) **   <a name="CognitoUserPools-GetDerivedToken-request-Audiences"></a>
The logical name of the target service where you intend to use the issued token. You can't request both `Audiences` and `Resources` in the same request.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
Required: No

 ** [ClientId](#API_GetDerivedToken_RequestSyntax) **   <a name="CognitoUserPools-GetDerivedToken-request-ClientId"></a>
The ID of the app client that requests the token exchange.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+]+`
Required: Yes

 ** [ClientSecret](#API_GetDerivedToken_RequestSyntax) **   <a name="CognitoUserPools-GetDerivedToken-request-ClientSecret"></a>
The client secret of the requested app client, if the client has a secret.
Type: String
Length Constraints: Minimum length of 24. Maximum length of 64.
Pattern: `[\w+]+`
Required: No

 ** [RequestedTokenType](#API_GetDerivedToken_RequestSyntax) **   <a name="CognitoUserPools-GetDerivedToken-request-RequestedTokenType"></a>
The type of token that you want Amazon Cognito to issue. Valid values:
+  `ACCESS_TOKEN` – Issues an access token.
+  `ID_TOKEN` – Issues an ID token.
Amazon Cognito can't issue a SAML assertion, so `SAML2` isn't a valid value for this parameter.
Type: String
Valid Values: `ACCESS_TOKEN | ID_TOKEN`
Required: No

 ** [Resources](#API_GetDerivedToken_RequestSyntax) **   <a name="CognitoUserPools-GetDerivedToken-request-Resources"></a>
The identifier of a resource server in your user pool where you intend to use the issued token. You can't request both `Resources` and `Audiences` in the same request.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
Required: No

 ** [Scopes](#API_GetDerivedToken_RequestSyntax) **   <a name="CognitoUserPools-GetDerivedToken-request-Scopes"></a>
The scopes that you want the new token to have. Amazon Cognito issues a token with the intersection of these requested scopes, the scopes of your `SubjectToken`, and the scopes that are allowed for the requesting app client. If you don't specify any scopes, Amazon Cognito issues a token with the same scopes as your `SubjectToken`.
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
Required: No

 ** [SubjectToken](#API_GetDerivedToken_RequestSyntax) **   <a name="CognitoUserPools-GetDerivedToken-request-SubjectToken"></a>
The token that you want to exchange for a new token. This is the credential that represents the identity of the party on behalf of whom the request is being made.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Pattern: `[A-Za-z0-9-_+/=.]+`
Required: Yes

 ** [SubjectTokenProviderName](#API_GetDerivedToken_RequestSyntax) **   <a name="CognitoUserPools-GetDerivedToken-request-SubjectTokenProviderName"></a>
The name of the third-party identity provider that issued the `SubjectToken`, if the subject token isn't a Amazon Cognito token. Provide this value when your `SubjectToken` came from a SAML or OIDC provider that you registered with your user pool, so that Amazon Cognito can validate it against that provider's configuration. Omit this parameter for a Amazon Cognito ID or access token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\p{Z}]+`
Required: No

 ** [SubjectTokenType](#API_GetDerivedToken_RequestSyntax) **   <a name="CognitoUserPools-GetDerivedToken-request-SubjectTokenType"></a>
The type of the `SubjectToken` that you want to exchange. Valid values:
+  `ACCESS_TOKEN` – The subject token is an access token.
+  `ID_TOKEN` – The subject token is an ID token.
+  `SAML2` – The subject token is a SAML 2.0 assertion.
Type: String
Valid Values: `ACCESS_TOKEN | ID_TOKEN | SAML2`
Required: Yes

## Response Syntax
<a name="API_GetDerivedToken_ResponseSyntax"></a>

```
{
   "ExpiresIn": number,
   "IssuedToken": "string",
   "IssuedTokenType": "string",
   "Scopes": [ "string" ],
   "TokenType": "string"
}
```

## Response Elements
<a name="API_GetDerivedToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExpiresIn](#API_GetDerivedToken_ResponseSyntax) **   <a name="CognitoUserPools-GetDerivedToken-response-ExpiresIn"></a>
The number of seconds until the issued token expires.
Type: Integer

 ** [IssuedToken](#API_GetDerivedToken_ResponseSyntax) **   <a name="CognitoUserPools-GetDerivedToken-response-IssuedToken"></a>
The token that Amazon Cognito issued in response to the token exchange request.
Type: String
Pattern: `[A-Za-z0-9-_=.]+`

 ** [IssuedTokenType](#API_GetDerivedToken_ResponseSyntax) **   <a name="CognitoUserPools-GetDerivedToken-response-IssuedTokenType"></a>
The type of the token in the `IssuedToken` parameter. Valid values:
+  `ACCESS_TOKEN` – The issued token is an access token.
+  `ID_TOKEN` – The issued token is an ID token.
Type: String
Valid Values: `ACCESS_TOKEN | ID_TOKEN`

 ** [Scopes](#API_GetDerivedToken_ResponseSyntax) **   <a name="CognitoUserPools-GetDerivedToken-response-Scopes"></a>
The scopes that Amazon Cognito granted in the issued token.
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\x21\x23-\x5B\x5D-\x7E]+`

 ** [TokenType](#API_GetDerivedToken_ResponseSyntax) **   <a name="CognitoUserPools-GetDerivedToken-response-TokenType"></a>
The type of the issued token. For example, `Bearer`.
Type: String
Valid Values: `Bearer | N_A`

## Errors
<a name="API_GetDerivedToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ForbiddenException **
This exception is thrown when AWS WAF doesn't allow your request based on a web ACL that's associated with your user pool.
 ** message **
The message returned when AWS WAF doesn't allow your request based on a web ACL that's associated with your user pool.
HTTP Status Code: 400

 ** InternalErrorException **
This exception is thrown when Amazon Cognito encounters an internal error.
 ** message **
The message returned when Amazon Cognito throws an internal error exception.
HTTP Status Code: 500

 ** InvalidLambdaResponseException **
This exception is thrown when Amazon Cognito encounters an invalid AWS Lambda response.
 ** message **
The message returned when Amazon Cognito throws an invalid AWS Lambda response exception.
HTTP Status Code: 400

 ** InvalidParameterException **
This exception is thrown when the Amazon Cognito service encounters an invalid parameter.
 ** message **
The message returned when the Amazon Cognito service throws an invalid parameter exception.
 ** reasonCode **
The reason code of the exception.
HTTP Status Code: 400

 ** NotAuthorizedException **
This exception is thrown when a user isn't authorized.
 ** message **
The message returned when the Amazon Cognito service returns a not authorized exception.
HTTP Status Code: 400

 ** OperationNotEnabledException **
This exception is thrown when an operation is not available in the current region or for the current user pool configuration. This can occur when attempting to perform operations that are not supported in secondary replica regions.
HTTP Status Code: 400

 ** ResourceNotFoundException **
This exception is thrown when the Amazon Cognito service can't find the requested resource.
 ** message **
The message returned when the Amazon Cognito service returns a resource not found exception.
HTTP Status Code: 400

 ** TooManyRequestsException **
This exception is thrown when the user has made too many requests for a given operation.
 ** message **
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

 ** UnexpectedLambdaException **
This exception is thrown when Amazon Cognito encounters an unexpected exception with AWS Lambda.
 ** message **
The message returned when Amazon Cognito returns an unexpected Lambda exception.
HTTP Status Code: 400

 ** UserLambdaValidationException **
This exception is thrown when the Amazon Cognito service encounters a user validation exception with the AWS Lambda service.
 ** message **
The message returned when the Amazon Cognito service returns a user validation exception with the Lambda service.
HTTP Status Code: 400

 ** UserNotFoundException **
This exception is thrown when a user isn't found.
 ** message **
The message returned when a user isn't found.
HTTP Status Code: 400

## See Also
<a name="API_GetDerivedToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/GetDerivedToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/GetDerivedToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/GetDerivedToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/GetDerivedToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/GetDerivedToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/GetDerivedToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/GetDerivedToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/GetDerivedToken)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/GetDerivedToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/GetDerivedToken)
