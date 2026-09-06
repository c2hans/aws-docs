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
