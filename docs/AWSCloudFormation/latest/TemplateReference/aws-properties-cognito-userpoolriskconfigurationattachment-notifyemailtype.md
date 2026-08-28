---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpoolriskconfigurationattachment-notifyemailtype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPoolRiskConfigurationAttachment NotifyEmailType
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-notifyemailtype"></a>

The template for email messages that advanced security features sends to a user when your threat protection automated response has a *Notify* action.

## Syntax
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-notifyemailtype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-notifyemailtype-syntax.json"></a>

```
{
  "[HtmlBody](#cfn-cognito-userpoolriskconfigurationattachment-notifyemailtype-htmlbody)" : {{String}},
  "[Subject](#cfn-cognito-userpoolriskconfigurationattachment-notifyemailtype-subject)" : {{String}},
  "[TextBody](#cfn-cognito-userpoolriskconfigurationattachment-notifyemailtype-textbody)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-notifyemailtype-syntax.yaml"></a>

```
  [HtmlBody](#cfn-cognito-userpoolriskconfigurationattachment-notifyemailtype-htmlbody): {{String}}
  [Subject](#cfn-cognito-userpoolriskconfigurationattachment-notifyemailtype-subject): {{String}}
  [TextBody](#cfn-cognito-userpoolriskconfigurationattachment-notifyemailtype-textbody): {{String}}
```

## Properties
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-notifyemailtype-properties"></a>

`HtmlBody`  <a name="cfn-cognito-userpoolriskconfigurationattachment-notifyemailtype-htmlbody"></a>
The body of an email notification formatted in HTML. Choose an `HtmlBody` or a `TextBody` to send an HTML-formatted or plaintext message, respectively.
*Required*: No
*Type*: String
*Pattern*: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]+`
*Minimum*: `6`
*Maximum*: `20000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subject`  <a name="cfn-cognito-userpoolriskconfigurationattachment-notifyemailtype-subject"></a>
The subject of the threat protection email notification.
*Required*: Yes
*Type*: String
*Pattern*: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s]+`
*Minimum*: `1`
*Maximum*: `140`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextBody`  <a name="cfn-cognito-userpoolriskconfigurationattachment-notifyemailtype-textbody"></a>
The body of an email notification formatted in plaintext. Choose an `HtmlBody` or a `TextBody` to send an HTML-formatted or plaintext message, respectively.
*Required*: No
*Type*: String
*Pattern*: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]+`
*Minimum*: `6`
*Maximum*: `20000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
