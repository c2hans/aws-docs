---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_NotifyEmailType.html
---

# NotifyEmailType
<a name="API_NotifyEmailType"></a>

The template for email messages that threat protection sends to a user when your threat protection automated response has a *Notify* action.

This data type is a request parameter of [SetRiskConfiguration](API_SetRiskConfiguration.md) and a response parameter of [DescribeRiskConfiguration](API_DescribeRiskConfiguration.md).

## Contents
<a name="API_NotifyEmailType_Contents"></a>

 ** Subject **   <a name="CognitoUserPools-Type-NotifyEmailType-Subject"></a>
The subject of the threat protection email notification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s]+`
Required: Yes

 ** HtmlBody **   <a name="CognitoUserPools-Type-NotifyEmailType-HtmlBody"></a>
The body of an email notification formatted in HTML. Choose an `HtmlBody` or a `TextBody` to send an HTML-formatted or plaintext message, respectively.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 20000.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]+`
Required: No

 ** TextBody **   <a name="CognitoUserPools-Type-NotifyEmailType-TextBody"></a>
The body of an email notification formatted in plaintext. Choose an `HtmlBody` or a `TextBody` to send an HTML-formatted or plaintext message, respectively.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 20000.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]+`
Required: No

## See Also
<a name="API_NotifyEmailType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/NotifyEmailType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/NotifyEmailType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/NotifyEmailType)
