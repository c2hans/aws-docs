---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpool-invitemessagetemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPool InviteMessageTemplate
<a name="aws-properties-cognito-userpool-invitemessagetemplate"></a>

The template for the welcome message to new users. This template must include the `{####}` temporary password placeholder if you are creating users with passwords. If your users don't have passwords, you can omit the placeholder.

See also [Customizing User Invitation Messages](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-message-customizations.html#cognito-user-pool-settings-user-invitation-message-customization).

## Syntax
<a name="aws-properties-cognito-userpool-invitemessagetemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpool-invitemessagetemplate-syntax.json"></a>

```
{
  "[EmailMessage](#cfn-cognito-userpool-invitemessagetemplate-emailmessage)" : {{String}},
  "[EmailSubject](#cfn-cognito-userpool-invitemessagetemplate-emailsubject)" : {{String}},
  "[SMSMessage](#cfn-cognito-userpool-invitemessagetemplate-smsmessage)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-userpool-invitemessagetemplate-syntax.yaml"></a>

```
  [EmailMessage](#cfn-cognito-userpool-invitemessagetemplate-emailmessage): {{String}}
  [EmailSubject](#cfn-cognito-userpool-invitemessagetemplate-emailsubject): {{String}}
  [SMSMessage](#cfn-cognito-userpool-invitemessagetemplate-smsmessage): {{String}}
```

## Properties
<a name="aws-properties-cognito-userpool-invitemessagetemplate-properties"></a>

`EmailMessage`  <a name="cfn-cognito-userpool-invitemessagetemplate-emailmessage"></a>
The message template for email messages. EmailMessage is allowed only if [EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is DEVELOPER.
*Required*: No
*Type*: String
*Pattern*: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*`
*Minimum*: `6`
*Maximum*: `20000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmailSubject`  <a name="cfn-cognito-userpool-invitemessagetemplate-emailsubject"></a>
The subject line for email messages. EmailSubject is allowed only if [EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is DEVELOPER.
*Required*: No
*Type*: String
*Pattern*: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s]+`
*Minimum*: `1`
*Maximum*: `140`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SMSMessage`  <a name="cfn-cognito-userpool-invitemessagetemplate-smsmessage"></a>
The message template for SMS messages.
*Required*: No
*Type*: String
*Pattern*: `(?s).*`
*Minimum*: `6`
*Maximum*: `140`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
