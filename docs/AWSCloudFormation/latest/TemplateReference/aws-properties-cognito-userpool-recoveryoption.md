---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpool-recoveryoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPool RecoveryOption
<a name="aws-properties-cognito-userpool-recoveryoption"></a>

A recovery option for a user. The `AccountRecoverySettingType` data type is an array of this object. Each `RecoveryOptionType` has a priority property that determines whether it is a primary or secondary option.

For example, if `verified_email` has a priority of `1` and `verified_phone_number` has a priority of `2`, your user pool sends account-recovery messages to a verified email address but falls back to an SMS message if the user has a verified phone number. The `admin_only` option prevents self-service account recovery.

## Syntax
<a name="aws-properties-cognito-userpool-recoveryoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpool-recoveryoption-syntax.json"></a>

```
{
  "[Name](#cfn-cognito-userpool-recoveryoption-name)" : {{String}},
  "[Priority](#cfn-cognito-userpool-recoveryoption-priority)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-cognito-userpool-recoveryoption-syntax.yaml"></a>

```
  [Name](#cfn-cognito-userpool-recoveryoption-name): {{String}}
  [Priority](#cfn-cognito-userpool-recoveryoption-priority): {{Integer}}
```

## Properties
<a name="aws-properties-cognito-userpool-recoveryoption-properties"></a>

`Name`  <a name="cfn-cognito-userpool-recoveryoption-name"></a>
The recovery method that this object sets a recovery option for.
*Required*: No
*Type*: String
*Allowed values*: `verified_email | verified_phone_number | admin_only`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Priority`  <a name="cfn-cognito-userpool-recoveryoption-priority"></a>
Your priority preference for using the specified attribute in account recovery. The highest priority is `1`.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
