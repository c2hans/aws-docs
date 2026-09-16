---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminSetUserMFAPreference.html
---

# AdminSetUserMFAPreference
<a name="API_AdminSetUserMFAPreference"></a>

Sets the user's multi-factor authentication (MFA) preference, including which MFA options are activated, and if any are preferred. Only one factor can be set as preferred. The preferred MFA factor will be used to authenticate a user if multiple factors are activated. If multiple options are activated and no preference is set, a challenge to choose an MFA option will be returned during sign-in.

This operation doesn't reset an existing TOTP MFA for a user. To register a new TOTP factor for a user, make an [AssociateSoftwareToken](API_AssociateSoftwareToken.md) request. For more information, see [TOTP software token MFA](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa-totp.html).

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_AdminSetUserMFAPreference_RequestSyntax"></a>

```
{
   "EmailMfaSettings": {
      "Enabled": {{boolean}},
      "PreferredMfa": {{boolean}}
   },
   "SMSMfaSettings": {
      "Enabled": {{boolean}},
      "PreferredMfa": {{boolean}}
   },
   "SoftwareTokenMfaSettings": {
      "Enabled": {{boolean}},
      "PreferredMfa": {{boolean}}
   },
   "Username": "{{string}}",
   "UserPoolId": "{{string}}",
   "WebAuthnMfaSettings": {
      "Enabled": {{boolean}}
   }
}
```

## Request Parameters
<a name="API_AdminSetUserMFAPreference_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EmailMfaSettings](#API_AdminSetUserMFAPreference_RequestSyntax) **   <a name="CognitoUserPools-AdminSetUserMFAPreference-request-EmailMfaSettings"></a>
User preferences for email message MFA. Activates or deactivates email MFA and sets it as the preferred MFA method when multiple methods are available. To activate this setting, your user pool must be in the [ Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.
Type: [EmailMfaSettingsType](API_EmailMfaSettingsType.md) object
Required: No

 ** [SMSMfaSettings](#API_AdminSetUserMFAPreference_RequestSyntax) **   <a name="CognitoUserPools-AdminSetUserMFAPreference-request-SMSMfaSettings"></a>
User preferences for SMS message MFA. Activates or deactivates SMS MFA and sets it as the preferred MFA method when multiple methods are available.
Type: [SMSMfaSettingsType](API_SMSMfaSettingsType.md) object
Required: No

 ** [SoftwareTokenMfaSettings](#API_AdminSetUserMFAPreference_RequestSyntax) **   <a name="CognitoUserPools-AdminSetUserMFAPreference-request-SoftwareTokenMfaSettings"></a>
User preferences for time-based one-time password (TOTP) MFA. Activates or deactivates TOTP MFA and sets it as the preferred MFA method when multiple methods are available.
Type: [SoftwareTokenMfaSettingsType](API_SoftwareTokenMfaSettingsType.md) object
Required: No

 ** [Username](#API_AdminSetUserMFAPreference_RequestSyntax) **   <a name="CognitoUserPools-AdminSetUserMFAPreference-request-Username"></a>
The name of the user that you want to query or modify. The value of this parameter is typically your user's username, but it can be any of their alias attributes. If `username` isn't an alias attribute in your user pool, this value must be the `sub` of a local user or the username of a user from a third-party IdP.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: Yes

 ** [UserPoolId](#API_AdminSetUserMFAPreference_RequestSyntax) **   <a name="CognitoUserPools-AdminSetUserMFAPreference-request-UserPoolId"></a>
The ID of the user pool where you want to set a user's MFA preferences.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

 ** [WebAuthnMfaSettings](#API_AdminSetUserMFAPreference_RequestSyntax) **   <a name="CognitoUserPools-AdminSetUserMFAPreference-request-WebAuthnMfaSettings"></a>
User preferences for passkey MFA. Activates or deactivates passkey MFA for the user. When activated, passkey authentication requires user verification, and passkey sign-in is available when MFA is required. To activate this setting, the `FactorConfiguration` of your user pool `WebAuthnConfiguration` must be `MULTI_FACTOR_WITH_USER_VERIFICATION`. To activate this setting, your user pool must be in the [ Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.
Type: [WebAuthnMfaSettingsType](API_WebAuthnMfaSettingsType.md) object
Required: No

## Response Elements
<a name="API_AdminSetUserMFAPreference_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AdminSetUserMFAPreference_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_AdminSetUserMFAPreference_Examples"></a>

### Example
<a name="API_AdminSetUserMFAPreference_Example_1"></a>

The following example request sets the user "testuser" to have both SMS and TOTP sign-in available, but to prefer SMS messages.

#### Sample Request
<a name="API_AdminSetUserMFAPreference_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.AdminSetUserMFAPreference
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
  "UserPoolId": "us-west-2_EXAMPLE",
  "Username": "testuser",
  "SMSMfaSettings": {
    "Enabled": true,
    "PreferredMfa": true
  },
  "SoftwareTokenMfaSettings": {
    "Enabled": true,
    "PreferredMfa": false
  }
}
```

#### Sample Response
<a name="API_AdminSetUserMFAPreference_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{}
```

## See Also
<a name="API_AdminSetUserMFAPreference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/AdminSetUserMFAPreference)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/AdminSetUserMFAPreference)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AdminSetUserMFAPreference)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/AdminSetUserMFAPreference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AdminSetUserMFAPreference)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/AdminSetUserMFAPreference)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/AdminSetUserMFAPreference)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/AdminSetUserMFAPreference)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/AdminSetUserMFAPreference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AdminSetUserMFAPreference)
