---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_VerificationMessageTemplateType.html
---

# VerificationMessageTemplateType
<a name="API_VerificationMessageTemplateType"></a>

The template for the verification message that your user pool delivers to users who set an email address or phone number attribute.

This data type is a request and response parameter of [CreateUserPool](API_CreateUserPool.md) and [UpdateUserPool](API_UpdateUserPool.md), and a response parameter of [DescribeUserPool](API_DescribeUserPool.md).

## Contents
<a name="API_VerificationMessageTemplateType_Contents"></a>

 ** DefaultEmailOption **   <a name="CognitoUserPools-Type-VerificationMessageTemplateType-DefaultEmailOption"></a>
The configuration of verification emails to contain a clickable link or a verification code.
For link, your template body must contain link text in the format `{##Click here##}`. "Click here" in the example is a customizable string. For code, your template body must contain a code placeholder in the format `{####}`.
Type: String
Valid Values: `CONFIRM_WITH_LINK | CONFIRM_WITH_CODE`
Required: No

 ** EmailMessage **   <a name="CognitoUserPools-Type-VerificationMessageTemplateType-EmailMessage"></a>
The template for email messages that Amazon Cognito sends to your users. You can set an `EmailMessage` template only if the value of [ EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER`. When your [EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER`, your user pool sends email messages with your own Amazon SES configuration.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 20000.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*\{####\}[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*`
Required: No

 ** EmailMessageByLink **   <a name="CognitoUserPools-Type-VerificationMessageTemplateType-EmailMessageByLink"></a>
The email message template for sending a confirmation link to the user. You can set an `EmailMessageByLink` template only if the value of [ EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER`. When your [EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER`, your user pool sends email messages with your own Amazon SES configuration.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 20000.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*\{##[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*##\}[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*`
Required: No

 ** EmailSubject **   <a name="CognitoUserPools-Type-VerificationMessageTemplateType-EmailSubject"></a>
The subject line for the email message template. You can set an `EmailSubject` template only if the value of [ EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER`. When your [EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER`, your user pool sends email messages with your own Amazon SES configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s]+`
Required: No

 ** EmailSubjectByLink **   <a name="CognitoUserPools-Type-VerificationMessageTemplateType-EmailSubjectByLink"></a>
The subject line for the email message template for sending a confirmation link to the user. You can set an `EmailSubjectByLink` template only if the value of [ EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER`. When your [EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER`, your user pool sends email messages with your own Amazon SES configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s]+`
Required: No

 ** SmsMessage **   <a name="CognitoUserPools-Type-VerificationMessageTemplateType-SmsMessage"></a>
The template for SMS messages that Amazon Cognito sends to your users.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 140.
Pattern: `.*\{####\}.*`
Required: No

## See Also
<a name="API_VerificationMessageTemplateType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/VerificationMessageTemplateType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/VerificationMessageTemplateType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/VerificationMessageTemplateType)
