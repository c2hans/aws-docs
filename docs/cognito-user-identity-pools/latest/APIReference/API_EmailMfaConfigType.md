---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailMfaConfigType.html
---

# EmailMfaConfigType
<a name="API_EmailMfaConfigType"></a>

Sets or shows configuration for user pool email message MFA and sign-in with one-time passwords (OTPs). Includes the subject and body of the email message template for sign-in and MFA messages. To activate this setting, your user pool must be in the [ Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.

This data type is a request parameter of [SetUserPoolMfaConfig](API_SetUserPoolMfaConfig.md) and a response parameter of [GetUserPoolMfaConfig](API_GetUserPoolMfaConfig.md).

## Contents
<a name="API_EmailMfaConfigType_Contents"></a>

 ** Message **   <a name="CognitoUserPools-Type-EmailMfaConfigType-Message"></a>
The template for the email messages that your user pool sends to users with codes for MFA and sign-in with email OTPs. The message must contain the `{####}` placeholder. In the message, Amazon Cognito replaces this placeholder with the code. If you don't provide this parameter, Amazon Cognito sends messages in the default format.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 20000.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*\{####\}[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*`
Required: No

 ** Subject **   <a name="CognitoUserPools-Type-EmailMfaConfigType-Subject"></a>
The subject of the email messages that your user pool sends to users with codes for MFA and email OTP sign-in.
Type: String
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s]+`
Required: No

## See Also
<a name="API_EmailMfaConfigType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/EmailMfaConfigType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/EmailMfaConfigType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/EmailMfaConfigType)
