---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpool-verificationmessagetemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPool VerificationMessageTemplate
<a name="aws-properties-cognito-userpool-verificationmessagetemplate"></a>

The template for the verification message that your user pool delivers to users who set an email address or phone number attribute.

## Syntax
<a name="aws-properties-cognito-userpool-verificationmessagetemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpool-verificationmessagetemplate-syntax.json"></a>

```
{
  "[DefaultEmailOption](#cfn-cognito-userpool-verificationmessagetemplate-defaultemailoption)" : {{String}},
  "[EmailMessage](#cfn-cognito-userpool-verificationmessagetemplate-emailmessage)" : {{String}},
  "[EmailMessageByLink](#cfn-cognito-userpool-verificationmessagetemplate-emailmessagebylink)" : {{String}},
  "[EmailSubject](#cfn-cognito-userpool-verificationmessagetemplate-emailsubject)" : {{String}},
  "[EmailSubjectByLink](#cfn-cognito-userpool-verificationmessagetemplate-emailsubjectbylink)" : {{String}},
  "[SmsMessage](#cfn-cognito-userpool-verificationmessagetemplate-smsmessage)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-userpool-verificationmessagetemplate-syntax.yaml"></a>

```
  [DefaultEmailOption](#cfn-cognito-userpool-verificationmessagetemplate-defaultemailoption): {{String}}
  [EmailMessage](#cfn-cognito-userpool-verificationmessagetemplate-emailmessage): {{String}}
  [EmailMessageByLink](#cfn-cognito-userpool-verificationmessagetemplate-emailmessagebylink): {{String}}
  [EmailSubject](#cfn-cognito-userpool-verificationmessagetemplate-emailsubject): {{String}}
  [EmailSubjectByLink](#cfn-cognito-userpool-verificationmessagetemplate-emailsubjectbylink): {{String}}
  [SmsMessage](#cfn-cognito-userpool-verificationmessagetemplate-smsmessage): {{String}}
```

## Properties
<a name="aws-properties-cognito-userpool-verificationmessagetemplate-properties"></a>

`DefaultEmailOption`  <a name="cfn-cognito-userpool-verificationmessagetemplate-defaultemailoption"></a>
The configuration of verification emails to contain a clickable link or a verification code.
For link, your template body must contain link text in the format `{##Click here##}`. "Click here" in the example is a customizable string. For code, your template body must contain a code placeholder in the format `{####}`.
*Required*: No
*Type*: String
*Allowed values*: `CONFIRM_WITH_LINK | CONFIRM_WITH_CODE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmailMessage`  <a name="cfn-cognito-userpool-verificationmessagetemplate-emailmessage"></a>
The template for email messages that Amazon Cognito sends to your users. You can set an `EmailMessage` template only if the value of [ EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER`. When your [EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER`, your user pool sends email messages with your own Amazon SES configuration.
*Required*: No
*Type*: String
*Pattern*: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*\{####\}[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*`
*Minimum*: `6`
*Maximum*: `20000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmailMessageByLink`  <a name="cfn-cognito-userpool-verificationmessagetemplate-emailmessagebylink"></a>
The email message template for sending a confirmation link to the user. You can set an `EmailMessageByLink` template only if the value of [ EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER`. When your [EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER`, your user pool sends email messages with your own Amazon SES configuration.
*Required*: No
*Type*: String
*Pattern*: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*\{##[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*##\}[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*`
*Minimum*: `6`
*Maximum*: `20000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmailSubject`  <a name="cfn-cognito-userpool-verificationmessagetemplate-emailsubject"></a>
The subject line for the email message template. You can set an `EmailSubject` template only if the value of [ EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER`. When your [EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER`, your user pool sends email messages with your own Amazon SES configuration.
*Required*: No
*Type*: String
*Pattern*: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s]+`
*Minimum*: `1`
*Maximum*: `140`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmailSubjectByLink`  <a name="cfn-cognito-userpool-verificationmessagetemplate-emailsubjectbylink"></a>
The subject line for the email message template for sending a confirmation link to the user. You can set an `EmailSubjectByLink` template only if the value of [ EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER`. When your [EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER`, your user pool sends email messages with your own Amazon SES configuration.
*Required*: No
*Type*: String
*Pattern*: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s]+`
*Minimum*: `1`
*Maximum*: `140`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SmsMessage`  <a name="cfn-cognito-userpool-verificationmessagetemplate-smsmessage"></a>
The template for SMS messages that Amazon Cognito sends to your users.
*Required*: No
*Type*: String
*Pattern*: `.*\{####\}.*`
*Minimum*: `6`
*Maximum*: `140`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
