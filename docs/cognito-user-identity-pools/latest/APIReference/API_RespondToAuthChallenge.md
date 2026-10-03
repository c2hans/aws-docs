---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.html
---

# RespondToAuthChallenge
<a name="API_RespondToAuthChallenge"></a>

Some API operations in a user pool generate a challenge, like a prompt for an MFA code, for device authentication that bypasses MFA, or for a custom authentication challenge. A `RespondToAuthChallenge` API request provides the answer to that challenge, like a code or a secure remote password (SRP). The parameters of a response to an authentication challenge vary with the type of challenge.

For more information about custom authentication challenges, see [Custom authentication challenge Lambda triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html).

**Note**
Amazon Cognito doesn't evaluate AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can't use IAM credentials to authorize requests, and you can't grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html).

**Note**
This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with [Amazon Pinpoint](https://console.aws.amazon.com/pinpoint/home/). Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.
If you have never used SMS text messages with Amazon Cognito or any other AWS service, Amazon Simple Notification Service might place your account in the SMS sandbox. In * [sandbox mode](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html) *, you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see [ SMS message settings for Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html) in the *Amazon Cognito Developer Guide*.

## Request Syntax
<a name="API_RespondToAuthChallenge_RequestSyntax"></a>

```
{
   "AnalyticsMetadata": {
      "AnalyticsEndpointId": "{{string}}"
   },
   "ChallengeName": "{{string}}",
   "ChallengeResponses": {
      "{{string}}" : "{{string}}"
   },
   "ClientId": "{{string}}",
   "ClientMetadata": {
      "{{string}}" : "{{string}}"
   },
   "Session": "{{string}}",
   "UserContextData": {
      "EncodedData": "{{string}}",
      "IpAddress": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_RespondToAuthChallenge_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AnalyticsMetadata](#API_RespondToAuthChallenge_RequestSyntax) **   <a name="CognitoUserPools-RespondToAuthChallenge-request-AnalyticsMetadata"></a>
Information that supports analytics outcomes with Amazon Pinpoint, including the user's endpoint ID. The endpoint ID is a destination for Amazon Pinpoint push notifications, for example a device identifier, email address, or phone number.
Type: [AnalyticsMetadataType](API_AnalyticsMetadataType.md) object
Required: No

 ** [ChallengeName](#API_RespondToAuthChallenge_RequestSyntax) **   <a name="CognitoUserPools-RespondToAuthChallenge-request-ChallengeName"></a>
The name of the challenge that you are responding to.
You can't respond to an `ADMIN_NO_SRP_AUTH` challenge with this operation.
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
Required: Yes

 ** [ChallengeResponses](#API_RespondToAuthChallenge_RequestSyntax) **   <a name="CognitoUserPools-RespondToAuthChallenge-request-ChallengeResponses"></a>
The responses to the challenge that you received in the previous request. Each challenge has its own required response parameters. The following examples are partial JSON request bodies that highlight challenge-response parameters.
You must provide a SECRET\_HASH parameter in all challenge responses to an app client that has a client secret. Include a `DEVICE_KEY` for device authentication.
SELECT\_CHALLENGE
 `"ChallengeName": "SELECT_CHALLENGE", "ChallengeResponses": { "USERNAME": "[username]", "ANSWER": "[Challenge name]"}`
Available challenges are `PASSWORD`, `PASSWORD_SRP`, `EMAIL_OTP`, `SMS_OTP`, and `WEB_AUTHN`.
Complete authentication in the `SELECT_CHALLENGE` response for `PASSWORD`, `PASSWORD_SRP`, and `WEB_AUTHN`:
+  `"ChallengeName": "SELECT_CHALLENGE", "ChallengeResponses": { "ANSWER": "WEB_AUTHN", "USERNAME": "[username]", "CREDENTIAL": "[AuthenticationResponseJSON]"}`

  See [ AuthenticationResponseJSON](https://www.w3.org/TR/WebAuthn-3/#dictdef-authenticationresponsejson).
+  `"ChallengeName": "SELECT_CHALLENGE", "ChallengeResponses": { "ANSWER": "PASSWORD", "USERNAME": "[username]", "PASSWORD": "[password]"}`
+  `"ChallengeName": "SELECT_CHALLENGE", "ChallengeResponses": { "ANSWER": "PASSWORD_SRP", "USERNAME": "[username]", "SRP_A": "[SRP_A]"}`
For `SMS_OTP` and `EMAIL_OTP`, respond with the username and answer. Your user pool will send a code for the user to submit in the next challenge response.
+  `"ChallengeName": "SELECT_CHALLENGE", "ChallengeResponses": { "ANSWER": "SMS_OTP", "USERNAME": "[username]"}`
+  `"ChallengeName": "SELECT_CHALLENGE", "ChallengeResponses": { "ANSWER": "EMAIL_OTP", "USERNAME": "[username]"}`
WEB\_AUTHN
 `"ChallengeName": "WEB_AUTHN", "ChallengeResponses": { "USERNAME": "[username]", "CREDENTIAL": "[AuthenticationResponseJSON]"}`
See [ AuthenticationResponseJSON](https://www.w3.org/TR/WebAuthn-3/#dictdef-authenticationresponsejson).
PASSWORD
 `"ChallengeName": "PASSWORD", "ChallengeResponses": { "USERNAME": "[username]", "PASSWORD": "[password]"}`
PASSWORD\_SRP
 `"ChallengeName": "PASSWORD_SRP", "ChallengeResponses": { "USERNAME": "[username]", "SRP_A": "[SRP_A]"}`
SMS\_OTP
 `"ChallengeName": "SMS_OTP", "ChallengeResponses": {"SMS_OTP_CODE": "[code]", "USERNAME": "[username]"}`
EMAIL\_OTP
 `"ChallengeName": "EMAIL_OTP", "ChallengeResponses": {"EMAIL_OTP_CODE": "[code]", "USERNAME": "[username]"}`
SMS\_MFA
 `"ChallengeName": "SMS_MFA", "ChallengeResponses": {"SMS_MFA_CODE": "[code]", "USERNAME": "[username]"}`
PASSWORD\_VERIFIER
This challenge response is part of the SRP flow. Amazon Cognito requires that your application respond to this challenge within a few seconds. When the response time exceeds this period, your user pool returns a `NotAuthorizedException` error.
 `"ChallengeName": "PASSWORD_VERIFIER", "ChallengeResponses": {"PASSWORD_CLAIM_SIGNATURE": "[claim_signature]", "PASSWORD_CLAIM_SECRET_BLOCK": "[secret_block]", "TIMESTAMP": [timestamp], "USERNAME": "[username]"}`
CUSTOM\_CHALLENGE
 `"ChallengeName": "CUSTOM_CHALLENGE", "ChallengeResponses": {"USERNAME": "[username]", "ANSWER": "[challenge_answer]"}`
NEW\_PASSWORD\_REQUIRED
 `"ChallengeName": "NEW_PASSWORD_REQUIRED", "ChallengeResponses": {"NEW_PASSWORD": "[new_password]", "USERNAME": "[username]"}`
To set any required attributes that `InitiateAuth` returned in an `requiredAttributes` parameter, add `"userAttributes.[attribute_name]": "[attribute_value]"`. This parameter can also set values for writable attributes that aren't required by your user pool.
In a `NEW_PASSWORD_REQUIRED` challenge response, you can't modify a required attribute that already has a value. In `AdminRespondToAuthChallenge` or `RespondToAuthChallenge`, set a value for any keys that Amazon Cognito returned in the `requiredAttributes` parameter, then use the `AdminUpdateUserAttributes` or `UpdateUserAttributes` API operation to modify the value of any additional attributes.
SOFTWARE\_TOKEN\_MFA
 `"ChallengeName": "SOFTWARE_TOKEN_MFA", "ChallengeResponses": {"USERNAME": "[username]", "SOFTWARE_TOKEN_MFA_CODE": [authenticator_code]}`
DEVICE\_SRP\_AUTH
 `"ChallengeName": "DEVICE_SRP_AUTH", "ChallengeResponses": {"USERNAME": "[username]", "DEVICE_KEY": "[device_key]", "SRP_A": "[srp_a]"}`
DEVICE\_PASSWORD\_VERIFIER
 `"ChallengeName": "DEVICE_PASSWORD_VERIFIER", "ChallengeResponses": {"DEVICE_KEY": "[device_key]", "PASSWORD_CLAIM_SIGNATURE": "[claim_signature]", "PASSWORD_CLAIM_SECRET_BLOCK": "[secret_block]", "TIMESTAMP": [timestamp], "USERNAME": "[username]"}`
MFA\_SETUP
 `"ChallengeName": "MFA_SETUP", "ChallengeResponses": {"USERNAME": "[username]"}, "SESSION": "[Session ID from VerifySoftwareToken]"`
SELECT\_MFA\_TYPE
 `"ChallengeName": "SELECT_MFA_TYPE", "ChallengeResponses": {"USERNAME": "[username]", "ANSWER": "[SMS_MFA|EMAIL_MFA|SOFTWARE_TOKEN_MFA]"}`
For more information about `SECRET_HASH`, see [Computing secret hash values](https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html#cognito-user-pools-computing-secret-hash). For information about `DEVICE_KEY`, see [Working with user devices in your user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html).
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 131072.
Value Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** [ClientId](#API_RespondToAuthChallenge_RequestSyntax) **   <a name="CognitoUserPools-RespondToAuthChallenge-request-ClientId"></a>
The ID of the app client where the user is signing in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+]+`
Required: Yes

 ** [ClientMetadata](#API_RespondToAuthChallenge_RequestSyntax) **   <a name="CognitoUserPools-RespondToAuthChallenge-request-ClientMetadata"></a>
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

 ** [Session](#API_RespondToAuthChallenge_RequestSyntax) **   <a name="CognitoUserPools-RespondToAuthChallenge-request-Session"></a>
The session identifier that maintains the state of authentication requests and challenge responses. If an `AdminInitiateAuth` or `AdminRespondToAuthChallenge` API request results in a determination that your application must pass another challenge, Amazon Cognito returns a session with other challenge parameters. Send this session identifier, unmodified, to the next `AdminRespondToAuthChallenge` request.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 4096.
Required: No

 ** [UserContextData](#API_RespondToAuthChallenge_RequestSyntax) **   <a name="CognitoUserPools-RespondToAuthChallenge-request-UserContextData"></a>
Contextual data about your user session like the device fingerprint, IP address, or location. Amazon Cognito threat protection evaluates the risk of an authentication event based on the context that your app generates and passes to Amazon Cognito when it makes API requests.
For more information, see [Collecting data for threat protection in applications](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-viewing-threat-protection-app.html).
Type: [UserContextDataType](API_UserContextDataType.md) object
Required: No

## Response Syntax
<a name="API_RespondToAuthChallenge_ResponseSyntax"></a>

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
<a name="API_RespondToAuthChallenge_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthenticationResult](#API_RespondToAuthChallenge_ResponseSyntax) **   <a name="CognitoUserPools-RespondToAuthChallenge-response-AuthenticationResult"></a>
The outcome of a successful authentication process. After your application has passed all challenges, Amazon Cognito returns an `AuthenticationResult` with the JSON web tokens (JWTs) that indicate successful sign-in.
Type: [AuthenticationResultType](API_AuthenticationResultType.md) object

 ** [AvailableChallenges](#API_RespondToAuthChallenge_ResponseSyntax) **   <a name="CognitoUserPools-RespondToAuthChallenge-response-AvailableChallenges"></a>
This response parameter lists the available authentication challenges that users can select from in [choice-based authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flows-selection-sdk.html#authentication-flows-selection-choice). For example, they might be able to choose between passkey authentication, a one-time password from an SMS message, and a traditional password.
Type: Array of strings
Valid Values: `SMS_MFA | EMAIL_OTP | SOFTWARE_TOKEN_MFA | SELECT_MFA_TYPE | MFA_SETUP | PASSWORD_VERIFIER | CUSTOM_CHALLENGE | SELECT_CHALLENGE | DEVICE_SRP_AUTH | DEVICE_PASSWORD_VERIFIER | ADMIN_NO_SRP_AUTH | NEW_PASSWORD_REQUIRED | SMS_OTP | PASSWORD | WEB_AUTHN | PASSWORD_SRP`

 ** [ChallengeName](#API_RespondToAuthChallenge_ResponseSyntax) **   <a name="CognitoUserPools-RespondToAuthChallenge-response-ChallengeName"></a>
The name of the next challenge that you must respond to.
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

 ** [ChallengeParameters](#API_RespondToAuthChallenge_ResponseSyntax) **   <a name="CognitoUserPools-RespondToAuthChallenge-response-ChallengeParameters"></a>
The parameters that define your response to the next challenge.
Take the values in `ChallengeParameters` and provide values for them in the `ChallengeResponses` of the next [RespondToAuthChallenge](#API_RespondToAuthChallenge) request.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 131072.
Value Length Constraints: Minimum length of 0. Maximum length of 131072.

 ** [Session](#API_RespondToAuthChallenge_ResponseSyntax) **   <a name="CognitoUserPools-RespondToAuthChallenge-response-Session"></a>
The session identifier that maintains the state of authentication requests and challenge responses. If an `InitiateAuth` or `RespondToAuthChallenge` API request results in a determination that your application must pass another challenge, Amazon Cognito returns a session with other challenge parameters. Send this session identifier, unmodified, to the next `RespondToAuthChallenge` request.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 4096.

## Errors
<a name="API_RespondToAuthChallenge_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AliasExistsException **
This exception is thrown when a user tries to confirm the account with an email address or phone number that has already been supplied as an alias for a different user profile. This exception indicates that an account with this email address or phone already exists in a user pool that you've configured to use email address or phone number as a sign-in alias.
 ** message **
The message that Amazon Cognito sends to the user when the value of an alias attribute is already linked to another user profile.
HTTP Status Code: 400

 ** CodeMismatchException **
This exception is thrown if the provided code doesn't match what the server was expecting.
 ** message **
The message provided when the code mismatch exception is thrown.
HTTP Status Code: 400

 ** ExpiredCodeException **
This exception is thrown if a code has expired.
 ** message **
The message returned when the expired code exception is thrown.
HTTP Status Code: 400

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

 ** InvalidPasswordException **
This exception is thrown when Amazon Cognito encounters an invalid password.
 ** message **
The message returned when Amazon Cognito throws an invalid user password exception.
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

 ** PasswordHistoryPolicyViolationException **
The message returned when a user's new password matches a previous password and doesn't comply with the password-history policy.
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

 ** SoftwareTokenMFANotFoundException **
This exception is thrown when the software token time-based one-time password (TOTP) multi-factor authentication (MFA) isn't activated for the user pool.
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
<a name="API_RespondToAuthChallenge_Examples"></a>

### Example
<a name="API_RespondToAuthChallenge_Example_1"></a>

The following example completes sign-in for the user `testuser` with an email-message OTP. Because no additional challenges are required, the request returns an `AuthenticationResult` with ID, access, and refresh tokens.

#### Sample Request
<a name="API_RespondToAuthChallenge_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.RespondToAuthChallenge
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
  "ChallengeName": "EMAIL_OTP",
  "ClientId": "1example23456789",
  "UserPoolId": "us-west-2_EXAMPLE",
  "ChallengeResponses": {
    "USERNAME" : "testuser",
    "EMAIL_OTP_CODE": "12345678"
  },
  "Session": "AYABeC1-y8qooiuysEv0uM4wAqQAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLXd..."
}
```

#### Sample Response
<a name="API_RespondToAuthChallenge_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive

{
    "AuthenticationResult": {
        "AccessToken": "eyJra456defEXAMPLE",
        "ExpiresIn": 3600,
        "IdToken": "eyJra789ghiEXAMPLE",
        "RefreshToken": "eyJra123abcEXAMPLE",
        "TokenType": "Bearer"
    },
    "ChallengeParameters": {
    }
}
```

## See Also
<a name="API_RespondToAuthChallenge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/RespondToAuthChallenge)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/RespondToAuthChallenge)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/RespondToAuthChallenge)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/RespondToAuthChallenge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/RespondToAuthChallenge)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/RespondToAuthChallenge)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/RespondToAuthChallenge)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/RespondToAuthChallenge)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/RespondToAuthChallenge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/RespondToAuthChallenge)
