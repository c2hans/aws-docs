---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetUserMFAPreference.html
---

# SetUserMFAPreference
<a name="API_SetUserMFAPreference"></a>

Set the user's multi-factor authentication (MFA) method preference, including which MFA factors are activated and if any are preferred. Only one factor can be set as preferred. The preferred MFA factor will be used to authenticate a user if multiple factors are activated. If multiple options are activated and no preference is set, a challenge to choose an MFA option will be returned during sign-in. If an MFA type is activated for a user, the user will be prompted for MFA during all sign-in attempts unless device tracking is turned on and the device has been trusted. If you want MFA to be applied selectively based on the assessed risk level of sign-in attempts, deactivate MFA for users and turn on Adaptive Authentication for the user pool.

This operation doesn't reset an existing TOTP MFA for a user. To register a new TOTP factor for a user, make an [AssociateSoftwareToken](API_AssociateSoftwareToken.md) request. For more information, see [TOTP software token MFA](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa-totp.html).

Authorize this action with a signed-in user's access token. It must include the scope `aws.cognito.signin.user.admin`.

**Note**
Amazon Cognito doesn't evaluate AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can't use IAM credentials to authorize requests, and you can't grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html).

## Request Syntax
<a name="API_SetUserMFAPreference_RequestSyntax"></a>

```
{
   "AccessToken": "{{string}}",
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
   "WebAuthnMfaSettings": {
      "Enabled": {{boolean}}
   }
}
```

## Request Parameters
<a name="API_SetUserMFAPreference_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessToken](#API_SetUserMFAPreference_RequestSyntax) **   <a name="CognitoUserPools-SetUserMFAPreference-request-AccessToken"></a>
A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for `aws.cognito.signin.user.admin`.
Type: String
Pattern: `[A-Za-z0-9-_=.]+`
Required: Yes

 ** [EmailMfaSettings](#API_SetUserMFAPreference_RequestSyntax) **   <a name="CognitoUserPools-SetUserMFAPreference-request-EmailMfaSettings"></a>
User preferences for email message MFA. Activates or deactivates email MFA and sets it as the preferred MFA method when multiple methods are available. To activate this setting, your user pool must be in the [ Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.
Type: [EmailMfaSettingsType](API_EmailMfaSettingsType.md) object
Required: No

 ** [SMSMfaSettings](#API_SetUserMFAPreference_RequestSyntax) **   <a name="CognitoUserPools-SetUserMFAPreference-request-SMSMfaSettings"></a>
User preferences for SMS message MFA. Activates or deactivates SMS MFA and sets it as the preferred MFA method when multiple methods are available.
Type: [SMSMfaSettingsType](API_SMSMfaSettingsType.md) object
Required: No

 ** [SoftwareTokenMfaSettings](#API_SetUserMFAPreference_RequestSyntax) **   <a name="CognitoUserPools-SetUserMFAPreference-request-SoftwareTokenMfaSettings"></a>
User preferences for time-based one-time password (TOTP) MFA. Activates or deactivates TOTP MFA and sets it as the preferred MFA method when multiple methods are available. Users must register a TOTP authenticator before they set this as their preferred MFA method.
Type: [SoftwareTokenMfaSettingsType](API_SoftwareTokenMfaSettingsType.md) object
Required: No

 ** [WebAuthnMfaSettings](#API_SetUserMFAPreference_RequestSyntax) **   <a name="CognitoUserPools-SetUserMFAPreference-request-WebAuthnMfaSettings"></a>
User preferences for passkey MFA. Activates or deactivates passkey MFA for the user. When activated, passkey authentication requires user verification, and passkey sign-in is available when MFA is required. To activate this setting, the `FactorConfiguration` of your user pool `WebAuthnConfiguration` must be `MULTI_FACTOR_WITH_USER_VERIFICATION`. To activate this setting, your user pool must be in the [ Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.
Type: [WebAuthnMfaSettingsType](API_WebAuthnMfaSettingsType.md) object
Required: No

## Response Elements
<a name="API_SetUserMFAPreference_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SetUserMFAPreference_Errors"></a>

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
<a name="API_SetUserMFAPreference_Examples"></a>

### Example
<a name="API_SetUserMFAPreference_Example_1"></a>

The following example request sets TOTP, SMS, and email MFA active, and TOTP MFA as preferred for the current user.

#### Sample Request
<a name="API_SetUserMFAPreference_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.SetUserMFAPreference
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
   "AccessToken": "eyJra456defEXAMPLE",
   "SMSMfaSettings": {
      "Enabled": true,
      "PreferredMfa": false
   },
   "EmailMfaSettings": {
      "Enabled": true,
      "PreferredMfa": false
   },
   "SoftwareTokenMfaSettings": {
      "Enabled": true,
      "PreferredMfa": true
   }
}
```

#### Sample Response
<a name="API_SetUserMFAPreference_Example_1_Response"></a>

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
<a name="API_SetUserMFAPreference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/SetUserMFAPreference)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/SetUserMFAPreference)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/SetUserMFAPreference)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/SetUserMFAPreference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/SetUserMFAPreference)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/SetUserMFAPreference)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/SetUserMFAPreference)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/SetUserMFAPreference)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/SetUserMFAPreference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/SetUserMFAPreference)
