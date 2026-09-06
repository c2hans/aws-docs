---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_MessageTemplateType.html
---

# MessageTemplateType
<a name="API_MessageTemplateType"></a>

The message template structure.

## Contents
<a name="API_MessageTemplateType_Contents"></a>

 ** EmailMessage **   <a name="CognitoUserPools-Type-MessageTemplateType-EmailMessage"></a>
The message template for email messages. EmailMessage is allowed only if [EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is DEVELOPER.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 20000.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*`
Required: No

 ** EmailSubject **   <a name="CognitoUserPools-Type-MessageTemplateType-EmailSubject"></a>
The subject line for email messages. EmailSubject is allowed only if [EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is DEVELOPER.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s]+`
Required: No

 ** SMSMessage **   <a name="CognitoUserPools-Type-MessageTemplateType-SMSMessage"></a>
The message template for SMS messages.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 140.
Pattern: `(?s).*`
Required: No

## See Also
<a name="API_MessageTemplateType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/MessageTemplateType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/MessageTemplateType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/MessageTemplateType)
