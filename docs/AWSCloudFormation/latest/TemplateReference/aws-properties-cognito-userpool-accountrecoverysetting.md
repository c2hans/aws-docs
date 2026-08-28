---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpool-accountrecoverysetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPool AccountRecoverySetting
<a name="aws-properties-cognito-userpool-accountrecoverysetting"></a>

The available verified method a user can use to recover their password when they call `ForgotPassword`. You can use this setting to define a preferred method when a user has more than one method available. With this setting, SMS doesn't qualify for a valid password recovery mechanism if the user also has SMS multi-factor authentication (MFA) activated. In the absence of this setting, Amazon Cognito uses the legacy behavior to determine the recovery method where SMS is preferred through email.

## Syntax
<a name="aws-properties-cognito-userpool-accountrecoverysetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpool-accountrecoverysetting-syntax.json"></a>

```
{
  "[RecoveryMechanisms](#cfn-cognito-userpool-accountrecoverysetting-recoverymechanisms)" : {{[ RecoveryOption, ... ]}}
}
```

### YAML
<a name="aws-properties-cognito-userpool-accountrecoverysetting-syntax.yaml"></a>

```
  [RecoveryMechanisms](#cfn-cognito-userpool-accountrecoverysetting-recoverymechanisms): {{
    - RecoveryOption}}
```

## Properties
<a name="aws-properties-cognito-userpool-accountrecoverysetting-properties"></a>

`RecoveryMechanisms`  <a name="cfn-cognito-userpool-accountrecoverysetting-recoverymechanisms"></a>
The list of options and priorities for user message delivery in forgot-password operations. Sets or displays user pool preferences for email or SMS message priority, whether users should fall back to a second delivery method, and whether passwords should only be reset by administrators.
*Required*: No
*Type*: Array of [RecoveryOption](aws-properties-cognito-userpool-recoveryoption.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
