---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractiontype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPoolRiskConfigurationAttachment AccountTakeoverActionType
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractiontype"></a>

The automated response to a risk level for adaptive authentication in full-function, or `ENFORCED`, mode. You can assign an action to each risk level that advanced security features evaluates.

## Syntax
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractiontype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractiontype-syntax.json"></a>

```
{
  "[EventAction](#cfn-cognito-userpoolriskconfigurationattachment-accounttakeoveractiontype-eventaction)" : {{String}},
  "[Notify](#cfn-cognito-userpoolriskconfigurationattachment-accounttakeoveractiontype-notify)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractiontype-syntax.yaml"></a>

```
  [EventAction](#cfn-cognito-userpoolriskconfigurationattachment-accounttakeoveractiontype-eventaction): {{String}}
  [Notify](#cfn-cognito-userpoolriskconfigurationattachment-accounttakeoveractiontype-notify): {{Boolean}}
```

## Properties
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractiontype-properties"></a>

`EventAction`  <a name="cfn-cognito-userpoolriskconfigurationattachment-accounttakeoveractiontype-eventaction"></a>
The action to take for the attempted account takeover action for the associated risk level. Valid values are as follows:
+ `BLOCK`: Block the request.
+ `MFA_IF_CONFIGURED`: Present an MFA challenge if possible. MFA is possible if the user pool has active MFA methods that the user can set up. For example, if the user pool only supports SMS message MFA but the user doesn't have a phone number attribute, MFA setup isn't possible. If MFA setup isn't possible, allow the request.
+ `MFA_REQUIRED`: Present an MFA challenge if possible. Block the request if a user hasn't set up MFA. To sign in with required MFA, users must have an email address or phone number attribute, or a registered TOTP factor.
+ `NO_ACTION`: Take no action. Permit sign-in.
*Required*: Yes
*Type*: String
*Allowed values*: `BLOCK | MFA_IF_CONFIGURED | MFA_REQUIRED | NO_ACTION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Notify`  <a name="cfn-cognito-userpoolriskconfigurationattachment-accounttakeoveractiontype-notify"></a>
Determines whether Amazon Cognito sends a user a notification message when your user pools assesses a user's session at the associated risk level.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
