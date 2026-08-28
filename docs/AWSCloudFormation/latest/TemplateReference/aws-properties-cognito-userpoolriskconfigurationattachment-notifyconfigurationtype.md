---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPoolRiskConfigurationAttachment NotifyConfigurationType
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype"></a>

The configuration for Amazon SES email messages that advanced security features sends to a user when your adaptive authentication automated response has a *Notify* action.

## Syntax
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-syntax.json"></a>

```
{
  "[BlockEmail](#cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-blockemail)" : {{NotifyEmailType}},
  "[From](#cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-from)" : {{String}},
  "[MfaEmail](#cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-mfaemail)" : {{NotifyEmailType}},
  "[NoActionEmail](#cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-noactionemail)" : {{NotifyEmailType}},
  "[ReplyTo](#cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-replyto)" : {{String}},
  "[SourceArn](#cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-sourcearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-syntax.yaml"></a>

```
  [BlockEmail](#cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-blockemail): {{
    NotifyEmailType}}
  [From](#cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-from): {{String}}
  [MfaEmail](#cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-mfaemail): {{
    NotifyEmailType}}
  [NoActionEmail](#cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-noactionemail): {{
    NotifyEmailType}}
  [ReplyTo](#cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-replyto): {{String}}
  [SourceArn](#cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-sourcearn): {{String}}
```

## Properties
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-properties"></a>

`BlockEmail`  <a name="cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-blockemail"></a>
The template for the email message that your user pool sends when a detected risk event is blocked.
*Required*: No
*Type*: [NotifyEmailType](aws-properties-cognito-userpoolriskconfigurationattachment-notifyemailtype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`From`  <a name="cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-from"></a>
The email address that sends the email message. The address must be either individually verified with Amazon Simple Email Service, or from a domain that has been verified with Amazon SES.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `131072`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MfaEmail`  <a name="cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-mfaemail"></a>
The template for the email message that your user pool sends when MFA is challenged in response to a detected risk.
*Required*: No
*Type*: [NotifyEmailType](aws-properties-cognito-userpoolriskconfigurationattachment-notifyemailtype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NoActionEmail`  <a name="cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-noactionemail"></a>
The template for the email message that your user pool sends when no action is taken in response to a detected risk.
*Required*: No
*Type*: [NotifyEmailType](aws-properties-cognito-userpoolriskconfigurationattachment-notifyemailtype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReplyTo`  <a name="cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-replyto"></a>
The reply-to email address of an email template. Can be an email address in the format `admin@example.com` or `Administrator <admin@example.com>`.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `131072`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceArn`  <a name="cfn-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype-sourcearn"></a>
The Amazon Resource Name (ARN) of the identity that is associated with the sending authorization policy. This identity permits Amazon Cognito to send for the email address specified in the `From` parameter.
*Required*: Yes
*Type*: String
*Pattern*: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
