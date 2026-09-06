---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetTokensFromRefreshToken.html
---

# GetTokensFromRefreshToken
<a name="API_GetTokensFromRefreshToken"></a>

Given a refresh token, issues new ID, access, and optionally refresh tokens for the user who owns the submitted token. This operation issues a new refresh token and invalidates the original refresh token after an optional grace period when refresh token rotation is enabled. If refresh token rotation is disabled, issues new ID and access tokens only.

For information about enabling refresh token rotation and the retry grace period, see [RefreshTokenRotationType](API_RefreshTokenRotationType.md).

This data type is a request parameter of [CreateUserPoolClient](API_CreateUserPoolClient.md) and [UpdateUserPoolClient](API_UpdateUserPoolClient.md), and a response parameter of [DescribeUserPoolClient](API_DescribeUserPoolClient.md).

## Request Syntax
<a name="API_GetTokensFromRefreshToken_RequestSyntax"></a>

```
{
   "ClientId": "{{string}}",
   "ClientMetadata": {
      "{{string}}" : "{{string}}"
   },
   "ClientSecret": "{{string}}",
   "DeviceKey": "{{string}}",
   "RefreshToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetTokensFromRefreshToken_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientId](#API_GetTokensFromRefreshToken_RequestSyntax) **   <a name="CognitoUserPools-GetTokensFromRefreshToken-request-ClientId"></a>
The app client that issued the refresh token to the user who wants to request new tokens.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+]+`
Required: Yes

 ** [ClientMetadata](#API_GetTokensFromRefreshToken_RequestSyntax) **   <a name="CognitoUserPools-GetTokensFromRefreshToken-request-ClientMetadata"></a>
A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers. You create custom workflows by assigning AWS Lambda functions to user pool triggers.
When Amazon Cognito invokes any of these functions, it passes a JSON payload, which the function receives as input. This payload contains a `clientMetadata` attribute that provides the data that you assigned to the ClientMetadata parameter in your request. In your function code, you can process the `clientMetadata` value to enhance your workflow for your specific needs.
To review the Lambda trigger types that Amazon Cognito invokes at runtime with API requests, see [ Connecting API actions to Lambda triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-working-with-lambda-triggers.html#lambda-triggers-by-event) in the *Amazon Cognito Developer Guide*.
When you use the `ClientMetadata` parameter, note that Amazon Cognito won't do the following:
+ Store the `ClientMetadata` value. This data is available only to AWS Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration doesn't include triggers, the `ClientMetadata` parameter serves no purpose.
+ Validate the `ClientMetadata` value.
+ Encrypt the `ClientMetadata` value. Don't send sensitive information in this parameter.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 131072.
Value Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** [ClientSecret](#API_GetTokensFromRefreshToken_RequestSyntax) **   <a name="CognitoUserPools-GetTokensFromRefreshToken-request-ClientSecret"></a>
The client secret of the requested app client, if the client has a secret.
Type: String
Length Constraints: Minimum length of 24. Maximum length of 64.
Pattern: `[\w+]+`
Required: No

 ** [DeviceKey](#API_GetTokensFromRefreshToken_RequestSyntax) **   <a name="CognitoUserPools-GetTokensFromRefreshToken-request-DeviceKey"></a>
When you enable device remembering, Amazon Cognito issues a device key that you can use for device authentication that bypasses multi-factor authentication (MFA). To implement `GetTokensFromRefreshToken` in a user pool with device remembering, you must capture the device key from the initial authentication request. If your application doesn't provide the key of a registered device, Amazon Cognito issues a new one. You must provide the confirmed device key in this request if device remembering is enabled in your user pool.
For more information about device remembering, see [Working with devices](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-f-]+`
Required: No

 ** [RefreshToken](#API_GetTokensFromRefreshToken_RequestSyntax) **   <a name="CognitoUserPools-GetTokensFromRefreshToken-request-RefreshToken"></a>
A valid refresh token that can authorize the request for new tokens. When refresh token rotation is active in the requested app client, this token is invalidated after the request is complete and after an optional grace period.
Type: String
Pattern: `[A-Za-z0-9-_=.]+`
Required: Yes

## Response Syntax
<a name="API_GetTokensFromRefreshToken_ResponseSyntax"></a>

```
{
   "AuthenticationResult": {
      "AccessToken": "string",
      "ExpiresIn": number,
      "IdToken": "string",
      "NewDeviceMetadata": {
         "DeviceGroupKey": "string",
         "DeviceKey": "string"
      },
      "RefreshToken": "string",
      "TokenType": "string"
   }
}
```

## Response Elements
<a name="API_GetTokensFromRefreshToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthenticationResult](#API_GetTokensFromRefreshToken_ResponseSyntax) **   <a name="CognitoUserPools-GetTokensFromRefreshToken-response-AuthenticationResult"></a>
The object that your application receives after authentication. Contains tokens and information for device authentication.
This data type is a response parameter of authentication operations like [InitiateAuth](API_InitiateAuth.md), [AdminInitiateAuth](API_AdminInitiateAuth.md), [RespondToAuthChallenge](API_RespondToAuthChallenge.md), [AdminRespondToAuthChallenge](API_AdminRespondToAuthChallenge.md), and [GetTokensFromRefreshToken](#API_GetTokensFromRefreshToken). `GetTokensFromRefreshToken` doesn't return `NewDeviceMetadata`.
Type: [AuthenticationResultType](API_AuthenticationResultType.md) object

## Errors
<a name="API_GetTokensFromRefreshToken_Errors"></a>

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

 ** RefreshTokenReuseException **
This exception is throw when your application requests token refresh with a refresh token that has been invalidated by refresh-token rotation.
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
<a name="API_GetTokensFromRefreshToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/GetTokensFromRefreshToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/GetTokensFromRefreshToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/GetTokensFromRefreshToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/GetTokensFromRefreshToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/GetTokensFromRefreshToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/GetTokensFromRefreshToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/GetTokensFromRefreshToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/GetTokensFromRefreshToken)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/GetTokensFromRefreshToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/GetTokensFromRefreshToken)
