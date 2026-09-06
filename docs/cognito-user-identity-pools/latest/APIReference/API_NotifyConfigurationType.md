---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_NotifyConfigurationType.html
---

# NotifyConfigurationType
<a name="API_NotifyConfigurationType"></a>

The configuration for Amazon SES email messages that threat protection sends to a user when your adaptive authentication automated response has a *Notify* action.

This data type is a request parameter of [SetRiskConfiguration](API_SetRiskConfiguration.md) and a response parameter of [DescribeRiskConfiguration](API_DescribeRiskConfiguration.md).

## Contents
<a name="API_NotifyConfigurationType_Contents"></a>

 ** SourceArn **   <a name="CognitoUserPools-Type-NotifyConfigurationType-SourceArn"></a>
The Amazon Resource Name (ARN) of the identity that is associated with the sending authorization policy. This identity permits Amazon Cognito to send for the email address specified in the `From` parameter.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: Yes

 ** BlockEmail **   <a name="CognitoUserPools-Type-NotifyConfigurationType-BlockEmail"></a>
The template for the email message that your user pool sends when a detected risk event is blocked.
Type: [NotifyEmailType](API_NotifyEmailType.md) object
Required: No

 ** From **   <a name="CognitoUserPools-Type-NotifyConfigurationType-From"></a>
The email address that sends the email message. The address must be either individually verified with Amazon Simple Email Service, or from a domain that has been verified with Amazon SES.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** MfaEmail **   <a name="CognitoUserPools-Type-NotifyConfigurationType-MfaEmail"></a>
The template for the email message that your user pool sends when MFA is challenged in response to a detected risk.
Type: [NotifyEmailType](API_NotifyEmailType.md) object
Required: No

 ** NoActionEmail **   <a name="CognitoUserPools-Type-NotifyConfigurationType-NoActionEmail"></a>
The template for the email message that your user pool sends when no action is taken in response to a detected risk.
Type: [NotifyEmailType](API_NotifyEmailType.md) object
Required: No

 ** ReplyTo **   <a name="CognitoUserPools-Type-NotifyConfigurationType-ReplyTo"></a>
The reply-to email address of an email template. Can be an email address in the format `admin@example.com` or `Administrator <admin@example.com>`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

## See Also
<a name="API_NotifyConfigurationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/NotifyConfigurationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/NotifyConfigurationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/NotifyConfigurationType)
