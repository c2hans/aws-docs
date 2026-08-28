---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetUserPoolMfaConfig.html
---

# GetUserPoolMfaConfig
<a name="API_GetUserPoolMfaConfig"></a>

Given a user pool ID, returns configuration for sign-in with WebAuthn authenticators and for multi-factor authentication (MFA). This operation describes the following:
+ The WebAuthn relying party (RP) ID and user-verification settings.
+ The required, optional, or disabled state of MFA for all user pool users.
+ The message templates for email and SMS MFA.
+ The enabled or disabled state of time-based one-time password (TOTP) MFA.

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_GetUserPoolMfaConfig_RequestSyntax"></a>

```
{
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetUserPoolMfaConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [UserPoolId](#API_GetUserPoolMfaConfig_RequestSyntax) **   <a name="CognitoUserPools-GetUserPoolMfaConfig-request-UserPoolId"></a>
The ID of the user pool where you want to query WebAuthn and MFA configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_GetUserPoolMfaConfig_ResponseSyntax"></a>

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
<a name="API_GetUserPoolMfaConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EmailMfaConfiguration](#API_GetUserPoolMfaConfig_ResponseSyntax) **   <a name="CognitoUserPools-GetUserPoolMfaConfig-response-EmailMfaConfiguration"></a>
Shows configuration for user pool email message MFA and sign-in with one-time passwords (OTPs). Includes the subject and body of the email message template for sign-in and MFA messages. To activate this setting, your user pool must be in the [ Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.
Type: [EmailMfaConfigType](API_EmailMfaConfigType.md) object

 ** [MfaConfiguration](#API_GetUserPoolMfaConfig_ResponseSyntax) **   <a name="CognitoUserPools-GetUserPoolMfaConfig-response-MfaConfiguration"></a>
Displays the state of multi-factor authentication (MFA) as on, off, or optional. When `ON`, all users must set up MFA before they can sign in. When `OPTIONAL`, your application must make a client-side determination of whether a user wants to register an MFA device. For user pools with adaptive authentication with threat protection, choose `OPTIONAL`.
When `MfaConfiguration` is `OPTIONAL`, managed login doesn't automatically prompt users to set up MFA. Amazon Cognito generates MFA prompts in API responses and in managed login for users who have chosen and configured a preferred MFA factor.
Type: String
Valid Values: `OFF | ON | OPTIONAL`

 ** [SmsMfaConfiguration](#API_GetUserPoolMfaConfig_ResponseSyntax) **   <a name="CognitoUserPools-GetUserPoolMfaConfig-response-SmsMfaConfiguration"></a>
Shows user pool configuration for SMS message MFA. Includes the message template and the SMS message sending configuration for Amazon SNS.
Type: [SmsMfaConfigType](API_SmsMfaConfigType.md) object

 ** [SoftwareTokenMfaConfiguration](#API_GetUserPoolMfaConfig_ResponseSyntax) **   <a name="CognitoUserPools-GetUserPoolMfaConfig-response-SoftwareTokenMfaConfiguration"></a>
Shows user pool configuration for time-based one-time password (TOTP) MFA. Includes TOTP enabled or disabled state.
Type: [SoftwareTokenMfaConfigType](API_SoftwareTokenMfaConfigType.md) object

 ** [WebAuthnConfiguration](#API_GetUserPoolMfaConfig_ResponseSyntax) **   <a name="CognitoUserPools-GetUserPoolMfaConfig-response-WebAuthnConfiguration"></a>
Shows user pool configuration for sign-in with passkey authenticators such as biometric devices and security keys. Includes relying-party configuration, user-verification requirements, and whether passkeys can satisfy MFA requirements.
Type: [WebAuthnConfigurationType](API_WebAuthnConfigurationType.md) object

## Errors
<a name="API_GetUserPoolMfaConfig_Errors"></a>

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
<a name="API_GetUserPoolMfaConfig_Examples"></a>

### Example
<a name="API_GetUserPoolMfaConfig_Example_1"></a>

The following example request returns the MFA and WebAuthn configuration for the requested user pool.

#### Sample Request
<a name="API_GetUserPoolMfaConfig_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.GetUserPoolMfaConfig
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
   "UserPoolId": "us-west-2_EXAMPLE"
}
```

#### Sample Response
<a name="API_GetUserPoolMfaConfig_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{
    "EmailMfaConfiguration": {
        "Message": "Complete your sign-in: use {####}",
        "Subject": "Your sign-in code"
    },
    "MfaConfiguration": "OPTIONAL",
    "SmsMfaConfiguration": {
        "SmsAuthenticationMessage": "Do not share this code with anyone. Your code is {####}.",
        "SmsConfiguration": {
            "ExternalId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "SnsCallerArn": "arn:aws:iam::123456789012:role/service-role/cognito-SMS-Role",
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
<a name="API_GetUserPoolMfaConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/GetUserPoolMfaConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/GetUserPoolMfaConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/GetUserPoolMfaConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/GetUserPoolMfaConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/GetUserPoolMfaConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/GetUserPoolMfaConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/GetUserPoolMfaConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/GetUserPoolMfaConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/GetUserPoolMfaConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/GetUserPoolMfaConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
