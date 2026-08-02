---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetUserAuthFactors.html
---

# GetUserAuthFactors
<a name="API_GetUserAuthFactors"></a>

Lists the authentication options for the currently signed-in user. Returns the following:

1. The user's multi-factor authentication (MFA) preferences.

1. The user's options for choice-based authentication with the `USER_AUTH` flow.

   The list of options in the response to this query are eligible [RespondToAuthChallenge:ChallengeName](API_RespondToAuthChallenge.md#CognitoUserPools-RespondToAuthChallenge-request-ChallengeName) selections for `PREFERRED_CHALLENGE` and are returned in [InitiateAuth:AvailableChallenges](API_InitiateAuth.md#CognitoUserPools-InitiateAuth-response-AvailableChallenges) when you don't request a `PREFERRED_CHALLENGE`. The [InitiateAuth:AuthParameters](API_InitiateAuth.md#CognitoUserPools-InitiateAuth-request-AuthParameters) and [RespondToAuthChallenge:ChallengeResponses](API_RespondToAuthChallenge.md#CognitoUserPools-RespondToAuthChallenge-request-ChallengeResponses) are specific to each challenge.

Authorize this action with a signed-in user's access token. It must include the scope `aws.cognito.signin.user.admin`.

**Note**
Amazon Cognito doesn't evaluate AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can't use IAM credentials to authorize requests, and you can't grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html).

## Request Syntax
<a name="API_GetUserAuthFactors_RequestSyntax"></a>

```
{
   "AccessToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetUserAuthFactors_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessToken](#API_GetUserAuthFactors_RequestSyntax) **   <a name="CognitoUserPools-GetUserAuthFactors-request-AccessToken"></a>
A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for `aws.cognito.signin.user.admin`.
Type: String
Pattern: `[A-Za-z0-9-_=.]+`
Required: Yes

## Response Syntax
<a name="API_GetUserAuthFactors_ResponseSyntax"></a>

```
{
   "ConfiguredUserAuthFactors": [ "string" ],
   "PreferredMfaSetting": "string",
   "UserMFASettingList": [ "string" ],
   "Username": "string"
}
```

## Response Elements
<a name="API_GetUserAuthFactors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfiguredUserAuthFactors](#API_GetUserAuthFactors_ResponseSyntax) **   <a name="CognitoUserPools-GetUserAuthFactors-response-ConfiguredUserAuthFactors"></a>
The authentication types that are available to the user with `USER_AUTH` sign-in, for example `["PASSWORD", "WEB_AUTHN"]`.
 `PASSWORD` can only be used as a first authentication factor. `SOFTWARE_TOKEN` can only be used as an MFA factor. `EMAIL_OTP`, `SMS_OTP`, and `WEB_AUTHN` can be used as either a first authentication factor or an MFA factor. `WEB_AUTHN` is available as an MFA factor only when passkey MFA is enabled at the user pool level.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 8 items.
Valid Values: `PASSWORD | EMAIL_OTP | SMS_OTP | WEB_AUTHN | SOFTWARE_TOKEN`

 ** [PreferredMfaSetting](#API_GetUserAuthFactors_ResponseSyntax) **   <a name="CognitoUserPools-GetUserAuthFactors-response-PreferredMfaSetting"></a>
The challenge method that Amazon Cognito returns to the user in response to sign-in requests. Users can prefer SMS message, email message, or TOTP MFA.
Change preferred MFA methods for a user with [SetUserMFAPreference](API_SetUserMFAPreference.md) or [AdminSetUserMFAPreference](API_AdminSetUserMFAPreference.md).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.

 ** [UserMFASettingList](#API_GetUserAuthFactors_ResponseSyntax) **   <a name="CognitoUserPools-GetUserAuthFactors-response-UserMFASettingList"></a>
The MFA options that are activated for the user. The possible values in this list are `SMS_MFA`, `EMAIL_OTP`, and `SOFTWARE_TOKEN_MFA`.
SMS and email message MFA are always available to users when your user pool is configured with [CreateUserPool:SmsConfiguration](API_CreateUserPool.md#CognitoUserPools-CreateUserPool-request-SmsConfiguration) or [CreateUserPool:EmailConfiguration](API_CreateUserPool.md#CognitoUserPools-CreateUserPool-request-EmailConfiguration) in `DEVELOPER` mode, respectively. Whether Amazon Cognito presents an MFA challenge and the format of the challenge are set by the `PreferredMfa` boolean of [SetUserMFAPreference](API_SetUserMFAPreference.md).
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 131072.

 ** [Username](#API_GetUserAuthFactors_ResponseSyntax) **   <a name="CognitoUserPools-GetUserAuthFactors-response-Username"></a>
The name of the user who is eligible for the authentication factors in the response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`

## Errors
<a name="API_GetUserAuthFactors_Errors"></a>

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

 ** PasswordResetRequiredException **
This exception is thrown when a password reset is required.
 ** message **
The message returned when a password reset is required.
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

 ** UserNotConfirmedException **
This exception is thrown when a user isn't confirmed successfully.
 ** message **
The message returned when a user isn't confirmed successfully.
HTTP Status Code: 400

 ** UserNotFoundException **
This exception is thrown when a user isn't found.
 ** message **
The message returned when a user isn't found.
HTTP Status Code: 400

## Examples
<a name="API_GetUserAuthFactors_Examples"></a>

### Example
<a name="API_GetUserAuthFactors_Example_1"></a>

The following example request returns the sign-in factors for the current user. They have TOTP MFA set up.

#### Sample Request
<a name="API_GetUserAuthFactors_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.GetUserAuthFactors
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
   "AccessToken": "eyJra456defEXAMPLE"
}
```

#### Sample Response
<a name="API_GetUserAuthFactors_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{
    "ConfiguredUserAuthFactors": [
        "PASSWORD",
        "EMAIL_OTP",
        "SMS_OTP",
        "WEB_AUTHN",
        "SOFTWARE_TOKEN"
    ],
    "Username": "testuser"
}
```

## See Also
<a name="API_GetUserAuthFactors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/GetUserAuthFactors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/GetUserAuthFactors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/GetUserAuthFactors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/GetUserAuthFactors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/GetUserAuthFactors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/GetUserAuthFactors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/GetUserAuthFactors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/GetUserAuthFactors)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/GetUserAuthFactors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/GetUserAuthFactors)
