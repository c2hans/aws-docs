---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ChallengeResponseType.html
---

# ChallengeResponseType
<a name="API_ChallengeResponseType"></a>

The responses to the challenge that you received in the previous request. Each challenge has its own required response parameters. The following examples are partial JSON request bodies that highlight challenge-response parameters.

**Important**
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

This data type is a request parameter of [RespondToAuthChallenge](API_RespondToAuthChallenge.md) and [AdminRespondToAuthChallenge](API_AdminRespondToAuthChallenge.md).

## Contents
<a name="API_ChallengeResponseType_Contents"></a>

 ** ChallengeName **   <a name="CognitoUserPools-Type-ChallengeResponseType-ChallengeName"></a>
The type of challenge that your previous authentication request returned in the parameter `ChallengeName`, for example `SMS_MFA`.
Type: String
Valid Values: `Password | Mfa`
Required: No

 ** ChallengeResponse **   <a name="CognitoUserPools-Type-ChallengeResponseType-ChallengeResponse"></a>
The set of key-value pairs that provides a response to the requested challenge.
Type: String
Valid Values: `Success | Failure`
Required: No

## See Also
<a name="API_ChallengeResponseType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/ChallengeResponseType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/ChallengeResponseType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/ChallengeResponseType)
