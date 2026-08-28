---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoverriskconfigurationtype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPoolRiskConfigurationAttachment AccountTakeoverRiskConfigurationType
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoverriskconfigurationtype"></a>

The settings for automated responses and notification templates for adaptive authentication with advanced security features.

## Syntax
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoverriskconfigurationtype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoverriskconfigurationtype-syntax.json"></a>

```
{
  "[Actions](#cfn-cognito-userpoolriskconfigurationattachment-accounttakeoverriskconfigurationtype-actions)" : {{AccountTakeoverActionsType}},
  "[NotifyConfiguration](#cfn-cognito-userpoolriskconfigurationattachment-accounttakeoverriskconfigurationtype-notifyconfiguration)" : {{NotifyConfigurationType}}
}
```

### YAML
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoverriskconfigurationtype-syntax.yaml"></a>

```
  [Actions](#cfn-cognito-userpoolriskconfigurationattachment-accounttakeoverriskconfigurationtype-actions): {{
    AccountTakeoverActionsType}}
  [NotifyConfiguration](#cfn-cognito-userpoolriskconfigurationattachment-accounttakeoverriskconfigurationtype-notifyconfiguration): {{
    NotifyConfigurationType}}
```

## Properties
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoverriskconfigurationtype-properties"></a>

`Actions`  <a name="cfn-cognito-userpoolriskconfigurationattachment-accounttakeoverriskconfigurationtype-actions"></a>
A list of account-takeover actions for each level of risk that Amazon Cognito might assess with threat protection.
*Required*: Yes
*Type*: [AccountTakeoverActionsType](aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotifyConfiguration`  <a name="cfn-cognito-userpoolriskconfigurationattachment-accounttakeoverriskconfigurationtype-notifyconfiguration"></a>
The settings for composing and sending an email message when threat protection assesses a risk level with adaptive authentication. When you choose to notify users in `AccountTakeoverRiskConfiguration`, Amazon Cognito sends an email message using the method and template that you set with this data type.
*Required*: No
*Type*: [NotifyConfigurationType](aws-properties-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
