---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.html
---

# AdminInitiateAuth
<a name="API_AdminInitiateAuth"></a>

Starts sign-in for applications with a server-side component, for example a traditional web application. This operation specifies the authentication flow that you'd like to begin. The authentication flow that you specify must be supported in your app client configuration. For more information about authentication flows, see [Authentication flows](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow-methods.html).

**Note**
This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with [Amazon Pinpoint](https://console.aws.amazon.com/pinpoint/home/). Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.
If you have never used SMS text messages with Amazon Cognito or any other AWS service, Amazon Simple Notification Service might place your account in the SMS sandbox. In * [sandbox mode](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html) *, you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see [ SMS message settings for Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html) in the *Amazon Cognito Developer Guide*.

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_AdminInitiateAuth_RequestSyntax"></a>

```
{
   "AnalyticsMetadata": {
      "AnalyticsEndpointId": "{{string}}"
   },
   "AuthFlow": "{{string}}",
   "AuthParameters": {
      "{{string}}" : "{{string}}"
   },
   "ClientId": "{{string}}",
   "ClientMetadata": {
      "{{string}}" : "{{string}}"
   },
   "ContextData": {
      "EncodedData": "{{string}}",
      "HttpHeaders": [
         {
            "headerName": "{{string}}",
            "headerValue": "{{string}}"
         }
      ],
      "IpAddress": "{{string}}",
      "ServerName": "{{string}}",
      "ServerPath": "{{string}}"
   },
   "Session": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_AdminInitiateAuth_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AnalyticsMetadata](#API_AdminInitiateAuth_RequestSyntax) **   <a name="CognitoUserPools-AdminInitiateAuth-request-AnalyticsMetadata"></a>
Information that supports analytics outcomes with Amazon Pinpoint, including the user's endpoint ID. The endpoint ID is a destination for Amazon Pinpoint push notifications, for example a device identifier, email address, or phone number.
Type: [AnalyticsMetadataType](API_AnalyticsMetadataType.md) object
Required: No

 ** [AuthFlow](#API_AdminInitiateAuth_RequestSyntax) **   <a name="CognitoUserPools-AdminInitiateAuth-request-AuthFlow"></a>
The authentication flow that you want to initiate. Each `AuthFlow` has linked `AuthParameters` that you must submit. The following are some example flows.
Include the required [AdminInitiateAuth:AuthParameters](#CognitoUserPools-AdminInitiateAuth-request-AuthParameters) for the flow that you choose.
USER\_AUTH
The entry point for [choice-based authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flows-selection-sdk.html#authentication-flows-selection-choice) with passwords, one-time passwords, and WebAuthn authenticators. Request a preferred authentication type or review available authentication types. From the offered authentication types, select one in a challenge response and then authenticate with that method in an additional challenge response. To activate this setting, your user pool must be in the [ Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.
USER\_SRP\_AUTH
Username-password authentication with the Secure Remote Password (SRP) protocol. For more information, see [Use SRP password verification in custom authentication flow](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow.html#Using-SRP-password-verification-in-custom-authentication-flow).
REFRESH\_TOKEN\_AUTH and REFRESH\_TOKEN
Receive new ID and access tokens when you pass a `REFRESH_TOKEN` parameter with a valid refresh token as the value. For more information, see [Using the refresh token](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-the-refresh-token.html).
CUSTOM\_AUTH
Custom authentication with Lambda triggers. For more information, see [Custom authentication challenge Lambda triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html).
ADMIN\_USER\_PASSWORD\_AUTH
Server-side username-password authentication with the password sent directly in the request. For more information about client-side and server-side authentication, see [SDK authorization models](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flows-public-server-side.html).
 `USER_PASSWORD_AUTH` is a flow type of [InitiateAuth](API_InitiateAuth.md) and isn't valid for AdminInitiateAuth.
Type: String
Valid Values: `USER_SRP_AUTH | REFRESH_TOKEN_AUTH | REFRESH_TOKEN | CUSTOM_AUTH | ADMIN_NO_SRP_AUTH | USER_PASSWORD_AUTH | ADMIN_USER_PASSWORD_AUTH | USER_AUTH`
Required: Yes

 ** [AuthParameters](#API_AdminInitiateAuth_RequestSyntax) **   <a name="CognitoUserPools-AdminInitiateAuth-request-AuthParameters"></a>
The authentication parameters. These are inputs corresponding to the `AuthFlow` that you're invoking.
The following are some authentication flows and their parameters. Add a `SECRET_HASH` parameter if your app client has a client secret. Add `DEVICE_KEY` if you want to bypass multi-factor authentication with a remembered device.
USER\_AUTH
+  `USERNAME` (required)
+  `PREFERRED_CHALLENGE`. If you don't provide a value for `PREFERRED_CHALLENGE`, Amazon Cognito responds with the `AvailableChallenges` parameter that specifies the available sign-in methods.
+  `TARGET_ACR_VALUES`. An optional, space-separated list of the authentication context class reference (ACR) level URIs that you want the user to reach. List the levels in priority order, from highest to lowest. Amazon Cognito attempts the highest-priority level that the user can satisfy, and falls back through the list. Amazon Cognito ignores any value that it doesn't recognize. If none of the requested values are valid, Amazon Cognito returns an error.

  Requesting step-up authentication with this parameter requires the Essentials or Plus feature plan. On a lower feature plan, AdminInitiateAuth returns a FeatureUnavailableInTierException. `USERNAME` is required. When you provide an `ACCESS_TOKEN`, you must also provide `TARGET_ACR_VALUES`. Amazon Cognito returns an error if you provide an `ACCESS_TOKEN` without `TARGET_ACR_VALUES`. The `USERNAME` that you provide must match the user that the `ACCESS_TOKEN` was issued for.

  For more information about step-up authentication and how Amazon Cognito handles multi-factor authentication requirements, see [Step-up authentication with ACR and AMR](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-step-up-authentication.html) in the *Amazon Cognito Developer Guide*.
+  `MAX_AGE`. An optional integer that sets the maximum number of seconds allowed since the user last authenticated. If the user's most recent authentication is older than this value, Amazon Cognito discards the authentication-methods credit from any access token that you provide and processes the request as a fresh authentication toward the target level. The access token itself remains valid.
USER\_SRP\_AUTH
+  `USERNAME` (required)
+  `SRP_A` (required)
ADMIN\_USER\_PASSWORD\_AUTH
+  `USERNAME` (required)
+  `PASSWORD` (required)
REFRESH\_TOKEN\_AUTH/REFRESH\_TOKEN
+  `REFRESH_TOKEN`(required)
CUSTOM\_AUTH
+  `USERNAME` (required)
+  `ChallengeName: SRP_A` (when preceding custom authentication with SRP authentication)
+  `SRP_A: (An SRP_A value)` (when preceding custom authentication with SRP authentication)
For more information about `SECRET_HASH`, see [Computing secret hash values](https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html#cognito-user-pools-computing-secret-hash). For information about `DEVICE_KEY`, see [Working with user devices in your user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html).
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 131072.
Value Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** [ClientId](#API_AdminInitiateAuth_RequestSyntax) **   <a name="CognitoUserPools-AdminInitiateAuth-request-ClientId"></a>
The ID of the app client where the user wants to sign in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+]+`
Required: Yes

 ** [ClientMetadata](#API_AdminInitiateAuth_RequestSyntax) **   <a name="CognitoUserPools-AdminInitiateAuth-request-ClientMetadata"></a>
A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers. You create custom workflows by assigning AWS Lambda functions to user pool triggers.
When Amazon Cognito invokes any of these functions, it passes a JSON payload, which the function receives as input. This payload contains a `clientMetadata` attribute that provides the data that you assigned to the ClientMetadata parameter in your request. In your function code, you can process the `clientMetadata` value to enhance your workflow for your specific needs.
To review the Lambda trigger types that Amazon Cognito invokes at runtime with API requests, see [ Connecting API actions to Lambda triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-working-with-lambda-triggers.html#lambda-triggers-by-event) in the *Amazon Cognito Developer Guide*.
The `ClientMetadata` value is passed as input to the functions for only the following triggers:
+ Pre signup
+ Pre authentication
+ User migration
This request also invokes the functions for the following triggers, but doesn't pass `ClientMetadata`:
+ Post authentication
+ Custom message
+ Pre token generation
+ Create auth challenge
+ Define auth challenge
+ Custom email sender
+ Custom SMS sender
When you use the `ClientMetadata` parameter, note that Amazon Cognito won't do the following:
+ Store the `ClientMetadata` value. This data is available only to AWS Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration doesn't include triggers, the `ClientMetadata` parameter serves no purpose.
+ Validate the `ClientMetadata` value.
+ Encrypt the `ClientMetadata` value. Don't send sensitive information in this parameter.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 131072.
Value Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** [ContextData](#API_AdminInitiateAuth_RequestSyntax) **   <a name="CognitoUserPools-AdminInitiateAuth-request-ContextData"></a>
Contextual data about your user session like the device fingerprint, IP address, or location. Amazon Cognito threat protection evaluates the risk of an authentication event based on the context that your app generates and passes to Amazon Cognito when it makes API requests.
For more information, see [Collecting data for threat protection in applications](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-viewing-threat-protection-app.html).
Type: [ContextDataType](API_ContextDataType.md) object
Required: No

 ** [Session](#API_AdminInitiateAuth_RequestSyntax) **   <a name="CognitoUserPools-AdminInitiateAuth-request-Session"></a>
The optional session ID from a `ConfirmSignUp` API request. You can sign in a user directly from the sign-up process with an `AuthFlow` of `USER_AUTH` and `AuthParameters` of `EMAIL_OTP` or `SMS_OTP`, depending on how your user pool sent the confirmation-code message.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 4096.
Required: No

 ** [UserPoolId](#API_AdminInitiateAuth_RequestSyntax) **   <a name="CognitoUserPools-AdminInitiateAuth-request-UserPoolId"></a>
The ID of the user pool where the user wants to sign in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_AdminInitiateAuth_ResponseSyntax"></a>

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
   },
   "AvailableChallenges": [ "string" ],
   "ChallengeName": "string",
   "ChallengeParameters": {
      "string" : "string"
   },
   "Session": "string"
}
```

## Response Elements
<a name="API_AdminInitiateAuth_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthenticationResult](#API_AdminInitiateAuth_ResponseSyntax) **   <a name="CognitoUserPools-AdminInitiateAuth-response-AuthenticationResult"></a>
The outcome of successful authentication. This is only returned if the user pool has no additional challenges to return. If Amazon Cognito returns another challenge, the response includes `ChallengeName`, `ChallengeParameters`, and `Session` so that your user can answer the challenge.
Type: [AuthenticationResultType](API_AuthenticationResultType.md) object

 ** [AvailableChallenges](#API_AdminInitiateAuth_ResponseSyntax) **   <a name="CognitoUserPools-AdminInitiateAuth-response-AvailableChallenges"></a>
This response parameter lists the available authentication challenges that users can select from in [choice-based authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flows-selection-sdk.html#authentication-flows-selection-choice). For example, they might be able to choose between passkey authentication, a one-time password from an SMS message, and a traditional password.
Type: Array of strings
Valid Values: `SMS_MFA | EMAIL_OTP | SOFTWARE_TOKEN_MFA | SELECT_MFA_TYPE | MFA_SETUP | PASSWORD_VERIFIER | CUSTOM_CHALLENGE | SELECT_CHALLENGE | DEVICE_SRP_AUTH | DEVICE_PASSWORD_VERIFIER | ADMIN_NO_SRP_AUTH | NEW_PASSWORD_REQUIRED | SMS_OTP | PASSWORD | WEB_AUTHN | PASSWORD_SRP`

 ** [ChallengeName](#API_AdminInitiateAuth_ResponseSyntax) **   <a name="CognitoUserPools-AdminInitiateAuth-response-ChallengeName"></a>
The name of the challenge that you're responding to with this call. This is returned in the `AdminInitiateAuth` response if you must pass another challenge.
Possible challenges include the following:
All of the following challenges require `USERNAME` and, when the app client has a client secret, `SECRET_HASH` in the parameters. Include a `DEVICE_KEY` for device authentication.
+  `WEB_AUTHN`: Respond to the challenge with the results of a successful authentication with a WebAuthn authenticator, or passkey, as `CREDENTIAL`. Examples of WebAuthn authenticators include biometric devices and security keys.
+  `PASSWORD`: Respond with the user's password as `PASSWORD`.
+  `PASSWORD_SRP`: Respond with the initial SRP secret as `SRP_A`.
+  `SELECT_CHALLENGE`: Respond with a challenge selection as `ANSWER`. It must be one of the challenge types in the `AvailableChallenges` response parameter. Add the parameters of the selected challenge, for example `USERNAME` and `SMS_OTP`.
+  `SMS_MFA`: Respond with the code that your user pool delivered in an SMS message, as `SMS_MFA_CODE`
+  `EMAIL_MFA`: Respond with the code that your user pool delivered in an email message, as `EMAIL_MFA_CODE`
+  `EMAIL_OTP`: Respond with the code that your user pool delivered in an email message, as `EMAIL_OTP_CODE` .
+  `SMS_OTP`: Respond with the code that your user pool delivered in an SMS message, as `SMS_OTP_CODE`.
+  `PASSWORD_VERIFIER`: Respond with the second stage of SRP secrets as `PASSWORD_CLAIM_SIGNATURE`, `PASSWORD_CLAIM_SECRET_BLOCK`, and `TIMESTAMP`.
+  `CUSTOM_CHALLENGE`: This is returned if your custom authentication flow determines that the user should pass another challenge before tokens are issued. The parameters of the challenge are determined by your Lambda function and issued in the `ChallengeParameters` of a challenge response.
+  `DEVICE_SRP_AUTH`: Respond with the initial parameters of device SRP authentication. For more information, see [Signing in with a device](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html#user-pools-remembered-devices-signing-in-with-a-device).
+  `DEVICE_PASSWORD_VERIFIER`: Respond with `PASSWORD_CLAIM_SIGNATURE`, `PASSWORD_CLAIM_SECRET_BLOCK`, and `TIMESTAMP` after client-side SRP calculations. For more information, see [Signing in with a device](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html#user-pools-remembered-devices-signing-in-with-a-device).
+  `NEW_PASSWORD_REQUIRED`: For users who are required to change their passwords after successful first login. Respond to this challenge with `NEW_PASSWORD` and any required attributes that Amazon Cognito returned in the `requiredAttributes` parameter. You can also set values for attributes that aren't required by your user pool and that your app client can write.

  Amazon Cognito only returns this challenge for users who have temporary passwords. When you create passwordless users, you must provide values for all required attributes.
**Note**
In a `NEW_PASSWORD_REQUIRED` challenge response, you can't modify a required attribute that already has a value. In `AdminRespondToAuthChallenge` or `RespondToAuthChallenge`, set a value for any keys that Amazon Cognito returned in the `requiredAttributes` parameter, then use the `AdminUpdateUserAttributes` or `UpdateUserAttributes` API operation to modify the value of any additional attributes.
+  `MFA_SETUP`: For users who are required to setup an MFA factor before they can sign in. The MFA types activated for the user pool will be listed in the challenge parameters `MFAS_CAN_SETUP` value.

  To set up time-based one-time password (TOTP) MFA, use the session returned in this challenge from `InitiateAuth` or `AdminInitiateAuth` as an input to `AssociateSoftwareToken`. Then, use the session returned by `VerifySoftwareToken` as an input to `RespondToAuthChallenge` or `AdminRespondToAuthChallenge` with challenge name `MFA_SETUP` to complete sign-in.

  To set up SMS or email MFA, collect a `phone_number` or `email` attribute for the user. Then restart the authentication flow with an `InitiateAuth` or `AdminInitiateAuth` request.
Type: String
Valid Values: `SMS_MFA | EMAIL_OTP | SOFTWARE_TOKEN_MFA | SELECT_MFA_TYPE | MFA_SETUP | PASSWORD_VERIFIER | CUSTOM_CHALLENGE | SELECT_CHALLENGE | DEVICE_SRP_AUTH | DEVICE_PASSWORD_VERIFIER | ADMIN_NO_SRP_AUTH | NEW_PASSWORD_REQUIRED | SMS_OTP | PASSWORD | WEB_AUTHN | PASSWORD_SRP`

 ** [ChallengeParameters](#API_AdminInitiateAuth_ResponseSyntax) **   <a name="CognitoUserPools-AdminInitiateAuth-response-ChallengeParameters"></a>
The parameters of an authentication challenge. Amazon Cognito returns challenge parameters as a guide to the responses your user or application must provide for the returned `ChallengeName`. Calculate responses to the challenge parameters and pass them in the `ChallengeParameters` of `AdminRespondToAuthChallenge`.
All challenges require `USERNAME` and, when the app client has a client secret, `SECRET_HASH`.
In SRP challenges, Amazon Cognito returns the `username` attribute in `USER_ID_FOR_SRP` instead of any email address, preferred username, or phone number alias that you might have specified in your `AdminInitiateAuth` request. You must use the username and not an alias in the `ChallengeResponses` of your challenge response.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 131072.
Value Length Constraints: Minimum length of 0. Maximum length of 131072.

 ** [Session](#API_AdminInitiateAuth_ResponseSyntax) **   <a name="CognitoUserPools-AdminInitiateAuth-response-Session"></a>
The session that must be passed to challenge-response requests. If an `AdminInitiateAuth` or `AdminRespondToAuthChallenge` API request results in another authentication challenge, Amazon Cognito returns a session ID and the parameters of the next challenge. Pass this session ID in the `Session` parameter of `AdminRespondToAuthChallenge`.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 4096.

## Errors
<a name="API_AdminInitiateAuth_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** FeatureUnavailableInTierException **
This exception is thrown when a feature that you attempted to use or configure isn't included in your user pool's current feature plan. This can occur when:
+ You configure a feature that your feature plan doesn't support.
+ You make a request that uses a feature that requires a higher feature plan.
To resolve this issue, upgrade your user pool to a feature plan that includes the feature.
HTTP Status Code: 400

 ** InternalErrorException **
This exception is thrown when Amazon Cognito encounters an internal error.
 ** message **
The message returned when Amazon Cognito throws an internal error exception.
HTTP Status Code: 500

 ** InvalidEmailRoleAccessPolicyException **
This exception is thrown when Amazon Cognito isn't allowed to use your email identity. HTTP status code: 400.
 ** message **
The message returned when you have an unverified email address or the identity policy isn't set on an email address that Amazon Cognito can access.
HTTP Status Code: 400

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

 ** InvalidSmsRoleAccessPolicyException **
This exception is returned when the role provided for SMS configuration doesn't have permission to publish using Amazon SNS.
 ** message **
The message returned when the invalid SMS role access policy exception is thrown.
HTTP Status Code: 400

 ** InvalidSmsRoleTrustRelationshipException **
This exception is thrown when the trust relationship is not valid for the role provided for SMS configuration. This can happen if you don't trust `cognito-idp.amazonaws.com` or the external ID provided in the role does not match what is provided in the SMS configuration for the user pool.
 ** message **
The message returned when the role trust relationship for the SMS message is not valid.
HTTP Status Code: 400

 ** InvalidUserPoolConfigurationException **
This exception is thrown when the user pool configuration is not valid.
 ** message **
The message returned when the user pool configuration is not valid.
HTTP Status Code: 400

 ** MFAMethodNotFoundException **
This exception is thrown when Amazon Cognito can't find a multi-factor authentication (MFA) method.
 ** message **
The message returned when Amazon Cognito throws an MFA method not found exception.
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

 ** UnexpectedLambdaException **
This exception is thrown when Amazon Cognito encounters an unexpected exception with AWS Lambda.
 ** message **
The message returned when Amazon Cognito returns an unexpected Lambda exception.
HTTP Status Code: 400

 ** UnsupportedOperationException **
Exception that is thrown when you attempt to perform an operation that isn't enabled for the user pool client.
HTTP Status Code: 400

 ** UserLambdaValidationException **
This exception is thrown when the Amazon Cognito service encounters a user validation exception with the AWS Lambda service.
 ** message **
The message returned when the Amazon Cognito service returns a user validation exception with the Lambda service.
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
<a name="API_AdminInitiateAuth_Examples"></a>

### Example
<a name="API_AdminInitiateAuth_Example_1"></a>

The following example request signs in the user "testuser" to an app client with a client secret. It includes context data for advanced security features and ClientMetadata for Lambda triggers. The device key and device group key in the response indicate that this user pool supports the device-remembering feature.

#### Sample Request
<a name="API_AdminInitiateAuth_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.AdminInitiateAuth
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
    "AuthFlow": "ADMIN_USER_PASSWORD_AUTH",
    "ClientId": "1example23456789",
    "UserPoolId": "us-west-2_EXAMPLE",
    "AuthParameters": {
        "USERNAME": "testuser",
        "PASSWORD": "TestUserPassword1=",
        "SECRET_HASH": "cKtx2L2fvV1FeAbk3iUPgCyXY+5B0ItO0ItxhFaLkeA="
    },
    "ContextData": {
      "EncodedData": "VGhpc0lzTXlFbmNvZGVkRGF0YQ",
      "HttpHeaders": [
         {
            "headerName": "Referer",
            "headerValue": "https://home.example.com"
         }
      ],
      "IpAddress": "192.0.2.100",
      "ServerName": "auth.example.com",
      "ServerPath": "/web/private/program.html"
    },
    "ClientMetadata": {
        "MyTestKey": "MyTestValue"
    }
}
```

#### Sample Response
<a name="API_AdminInitiateAuth_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{
	"AuthenticationResult": {
		"AccessToken": "eyJraACCESSEXAMPLE...",
		"ExpiresIn": 3600,
		"IdToken": "eyJraIDEXAMPLE...",
		"NewDeviceMetadata": {
			"DeviceGroupKey": "-v7w9UcY6",
			"DeviceKey": "us-west-2_a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
		},
		"RefreshToken": "eyJjREFRESHEXAMPLE...",
		"TokenType": "Bearer"
	},
	"ChallengeParameters": {}
}
```

## See Also
<a name="API_AdminInitiateAuth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/AdminInitiateAuth)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/AdminInitiateAuth)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AdminInitiateAuth)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/AdminInitiateAuth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AdminInitiateAuth)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/AdminInitiateAuth)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/AdminInitiateAuth)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/AdminInitiateAuth)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/AdminInitiateAuth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AdminInitiateAuth)
