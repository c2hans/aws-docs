---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPoolRiskConfigurationAttachment AccountTakeoverActionsType
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype"></a>

A list of account-takeover actions for each level of risk that Amazon Cognito might assess with advanced security features.

## Syntax
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype-syntax.json"></a>

```
{
  "[HighAction](#cfn-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype-highaction)" : {{AccountTakeoverActionType}},
  "[LowAction](#cfn-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype-lowaction)" : {{AccountTakeoverActionType}},
  "[MediumAction](#cfn-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype-mediumaction)" : {{AccountTakeoverActionType}}
}
```

### YAML
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype-syntax.yaml"></a>

```
  [HighAction](#cfn-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype-highaction): {{
    AccountTakeoverActionType}}
  [LowAction](#cfn-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype-lowaction): {{
    AccountTakeoverActionType}}
  [MediumAction](#cfn-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype-mediumaction): {{
    AccountTakeoverActionType}}
```

## Properties
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype-properties"></a>

`HighAction`  <a name="cfn-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype-highaction"></a>
The action that you assign to a high-risk assessment by threat protection.
*Required*: No
*Type*: [AccountTakeoverActionType](aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractiontype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LowAction`  <a name="cfn-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype-lowaction"></a>
The action that you assign to a low-risk assessment by threat protection.
*Required*: No
*Type*: [AccountTakeoverActionType](aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractiontype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediumAction`  <a name="cfn-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype-mediumaction"></a>
The action that you assign to a medium-risk assessment by threat protection.
*Required*: No
*Type*: [AccountTakeoverActionType](aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractiontype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
