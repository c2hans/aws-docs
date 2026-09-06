---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetUserPoolMfaConfig.html
---

# SetUserPoolMfaConfig
<a name="API_SetUserPoolMfaConfig"></a>

Sets user pool multi-factor authentication (MFA) and passkey configuration. For more information about user pool MFA, see [Adding MFA](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html). For more information about WebAuthn passkeys see [Authentication flows](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow-methods.html#amazon-cognito-user-pools-authentication-flow-methods-passkey).

**Note**
This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with [Amazon Pinpoint](https://console.aws.amazon.com/pinpoint/home/). Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.
If you have never used SMS text messages with Amazon Cognito or any other AWS service, Amazon Simple Notification Service might place your account in the SMS sandbox. In * [sandbox mode](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html) *, you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see [ SMS message settings for Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html) in the *Amazon Cognito Developer Guide*.

## Request Syntax
<a name="API_SetUserPoolMfaConfig_RequestSyntax"></a>

```
{
   "EmailMfaConfiguration": {
      "Message": "{{string}}",
      "Subject": "{{string}}"
   },
   "MfaConfiguration": "{{string}}",
   "SmsMfaConfiguration": {
      "SmsAuthenticationMessage": "{{string}}",
      "SmsConfiguration": {
         "EumsSms": {
            "CallerArn": "{{string}}",
            "ConfigurationSetName": "{{string}}",
            "ExternalId": "{{string}}",
            "InEntityId": "{{string}}",
            "InTemplateId": "{{string}}",
            "OriginationIdentity": "{{string}}",
            "Region": "{{string}}"
         },
         "ExternalId": "{{string}}",
         "SnsCallerArn": "{{string}}",
         "SnsRegion": "{{string}}"
      }
   },
   "SoftwareTokenMfaConfiguration": {
      "Enabled": {{boolean}}
   },
   "UserPoolId": "{{string}}",
   "WebAuthnConfiguration": {
      "FactorConfiguration": "{{string}}",
      "RelyingPartyId": "{{string}}",
      "UserVerification": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_SetUserPoolMfaConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EmailMfaConfiguration](#API_SetUserPoolMfaConfig_RequestSyntax) **   <a name="CognitoUserPools-SetUserPoolMfaConfig-request-EmailMfaConfiguration"></a>
Sets configuration for user pool email message MFA and sign-in with one-time passwords (OTPs). Includes the subject and body of the email message template for sign-in and MFA messages. To activate this setting, your user pool must be in the [ Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.
Type: [EmailMfaConfigType](API_EmailMfaConfigType.md) object
Required: No

 ** [MfaConfiguration](#API_SetUserPoolMfaConfig_RequestSyntax) **   <a name="CognitoUserPools-SetUserPoolMfaConfig-request-MfaConfiguration"></a>
Sets multi-factor authentication (MFA) to be on, off, or optional. When `ON`, all users must set up MFA before they can sign in. When `OPTIONAL`, your application must make a client-side determination of whether a user wants to register an MFA device. For user pools with adaptive authentication with threat protection, choose `OPTIONAL`.
When `MfaConfiguration` is `OPTIONAL`, managed login doesn't automatically prompt users to set up MFA. Amazon Cognito generates MFA prompts in API responses and in managed login for users who have chosen and configured a preferred MFA factor.
Type: String
Valid Values: `OFF | ON | OPTIONAL`
Required: No

 ** [SmsMfaConfiguration](#API_SetUserPoolMfaConfig_RequestSyntax) **   <a name="CognitoUserPools-SetUserPoolMfaConfig-request-SmsMfaConfiguration"></a>
Configures user pool SMS messages for MFA. Sets the message template and the SMS message sending configuration for Amazon SNS.
Type: [SmsMfaConfigType](API_SmsMfaConfigType.md) object
Required: No

 ** [SoftwareTokenMfaConfiguration](#API_SetUserPoolMfaConfig_RequestSyntax) **   <a name="CognitoUserPools-SetUserPoolMfaConfig-request-SoftwareTokenMfaConfiguration"></a>
Configures a user pool for time-based one-time password (TOTP) MFA. Enables or disables TOTP.
Type: [SoftwareTokenMfaConfigType](API_SoftwareTokenMfaConfigType.md) object
Required: No

 ** [UserPoolId](#API_SetUserPoolMfaConfig_RequestSyntax) **   <a name="CognitoUserPools-SetUserPoolMfaConfig-request-UserPoolId"></a>
The user pool ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

 ** [WebAuthnConfiguration](#API_SetUserPoolMfaConfig_RequestSyntax) **   <a name="CognitoUserPools-SetUserPoolMfaConfig-request-WebAuthnConfiguration"></a>
The configuration of your user pool for passkey, or WebAuthn, authentication and registration. Includes relying-party configuration, user-verification requirements, and whether passkeys can satisfy MFA requirements.
Type: [WebAuthnConfigurationType](API_WebAuthnConfigurationType.md) object
Required: No

## Response Syntax
<a name="API_SetUserPoolMfaConfig_ResponseSyntax"></a>

```
{
   "EmailMfaConfiguration": {
      "Message": "string",
      "Subject": "string"
   },
   "MfaConfiguration": "string",
   "SmsMfaConfiguration": {
      "SmsAuthenticationMessage": "string",
      "SmsConfiguration": {
         "EumsSms": {
            "CallerArn": "string",
            "ConfigurationSetName": "string",
            "ExternalId": "string",
            "InEntityId": "string",
            "InTemplateId": "string",
            "OriginationIdentity": "string",
            "Region": "string"
         },
         "ExternalId": "string",
         "SnsCallerArn": "string",
         "SnsRegion": "string"
      }
   },
   "SoftwareTokenMfaConfiguration": {
      "Enabled": boolean
   },
   "WebAuthnConfiguration": {
      "FactorConfiguration": "string",
      "RelyingPartyId": "string",
      "UserVerification": "string"
   }
}
```

## Response Elements
<a name="API_SetUserPoolMfaConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EmailMfaConfiguration](#API_SetUserPoolMfaConfig_ResponseSyntax) **   <a name="CognitoUserPools-SetUserPoolMfaConfig-response-EmailMfaConfiguration"></a>
Shows configuration for user pool email message MFA and sign-in with one-time passwords (OTPs). Includes the subject and body of the email message template for sign-in and MFA messages. To activate this setting, your user pool must be in the [ Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.
Type: [EmailMfaConfigType](API_EmailMfaConfigType.md) object

 ** [MfaConfiguration](#API_SetUserPoolMfaConfig_ResponseSyntax) **   <a name="CognitoUserPools-SetUserPoolMfaConfig-response-MfaConfiguration"></a>
Displays multi-factor authentication (MFA) as on, off, or optional. When `ON`, all users must set up MFA before they can sign in. When `OPTIONAL`, your application must make a client-side determination of whether a user wants to register an MFA device. For user pools with adaptive authentication with threat protection, choose `OPTIONAL`.
When `MfaConfiguration` is `OPTIONAL`, managed login doesn't automatically prompt users to set up MFA. Amazon Cognito generates MFA prompts in API responses and in managed login for users who have chosen and configured a preferred MFA factor.
Type: String
Valid Values: `OFF | ON | OPTIONAL`

 ** [SmsMfaConfiguration](#API_SetUserPoolMfaConfig_ResponseSyntax) **   <a name="CognitoUserPools-SetUserPoolMfaConfig-response-SmsMfaConfiguration"></a>
Shows user pool SMS message configuration for MFA and sign-in with SMS-message OTPs. Includes the message template and the SMS message sending configuration for Amazon SNS.
Type: [SmsMfaConfigType](API_SmsMfaConfigType.md) object

 ** [SoftwareTokenMfaConfiguration](#API_SetUserPoolMfaConfig_ResponseSyntax) **   <a name="CognitoUserPools-SetUserPoolMfaConfig-response-SoftwareTokenMfaConfiguration"></a>
Shows user pool configuration for time-based one-time password (TOTP) MFA. Includes TOTP enabled or disabled state.
Type: [SoftwareTokenMfaConfigType](API_SoftwareTokenMfaConfigType.md) object

 ** [WebAuthnConfiguration](#API_SetUserPoolMfaConfig_ResponseSyntax) **   <a name="CognitoUserPools-SetUserPoolMfaConfig-response-WebAuthnConfiguration"></a>
The configuration of your user pool for passkey, or WebAuthn, sign-in with authenticators such as biometric and security-key devices. Includes relying-party configuration and settings for user-verification requirements.
Type: [WebAuthnConfigurationType](API_WebAuthnConfigurationType.md) object

## Errors
<a name="API_SetUserPoolMfaConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
This exception is thrown if two or more modifications are happening concurrently.
 ** message **
The message provided when the concurrent exception is thrown.
HTTP Status Code: 400

 ** FeatureUnavailableInTierException **
This exception is thrown when a feature you attempted to configure isn't available in your current feature plan.
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

## Examples
<a name="API_SetUserPoolMfaConfig_Examples"></a>

### Example
<a name="API_SetUserPoolMfaConfig_Example_1"></a>

The following example request configures optional MFA in the user pool, message configuration and templates, and WebAuthn.

#### Sample Request
<a name="API_SetUserPoolMfaConfig_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.SetUserPoolMfaConfig
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
   "EmailMfaConfiguration": {
      "Message": "Your OTP for MFA or sign-in: use {####}",
      "Subject": "OTP test"
   },
   "MfaConfiguration": "OPTIONAL",
   "SmsMfaConfiguration": {
      "SmsAuthenticationMessage": "Your OTP for MFA or sign-in: use {####}.",
      "SmsConfiguration": {
         "ExternalId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
         "SnsCallerArn": "arn:aws:iam::123456789012:role/service-role/test-SMS-Role",
         "SnsRegion": "us-west-2"
      }
   },
   "SoftwareTokenMfaConfiguration": {
      "Enabled": true
   },
   "UserPoolId": "us-west-2_EXAMPLE",
   "WebAuthnConfiguration": {
      "RelyingPartyId": "auth.example.com",
      "UserVerification": "preferred"
   }
}
```

#### Sample Response
<a name="API_SetUserPoolMfaConfig_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{
    "EmailMfaConfiguration": {
        "Message": "Your OTP for MFA or sign-in: use {####}",
        "Subject": "OTP test"
    },
    "MfaConfiguration": "OPTIONAL",
    "SmsMfaConfiguration": {
        "SmsAuthenticationMessage": "Your OTP for MFA or sign-in: use {####}.",
        "SmsConfiguration": {
            "ExternalId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "SnsCallerArn": "arn:aws:iam::123456789012:role/service-role/test-SMS-Role",
            "SnsRegion": "us-west-2"
        }
    },
    "SoftwareTokenMfaConfiguration": {
        "Enabled": true
    },
    "WebAuthnConfiguration": {
        "RelyingPartyId": "auth.example.com",
        "UserVerification": "preferred"
    }
}
```

## See Also
<a name="API_SetUserPoolMfaConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/SetUserPoolMfaConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/SetUserPoolMfaConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/SetUserPoolMfaConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/SetUserPoolMfaConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/SetUserPoolMfaConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/SetUserPoolMfaConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/SetUserPoolMfaConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/SetUserPoolMfaConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/SetUserPoolMfaConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/SetUserPoolMfaConfig)
