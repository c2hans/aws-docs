---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpool-passwordpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPool PasswordPolicy
<a name="aws-properties-cognito-userpool-passwordpolicy"></a>

The password policy settings for a user pool, including complexity, history, and length requirements.

## Syntax
<a name="aws-properties-cognito-userpool-passwordpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpool-passwordpolicy-syntax.json"></a>

```
{
  "[MinimumLength](#cfn-cognito-userpool-passwordpolicy-minimumlength)" : {{Integer}},
  "[PasswordHistorySize](#cfn-cognito-userpool-passwordpolicy-passwordhistorysize)" : {{Integer}},
  "[RequireLowercase](#cfn-cognito-userpool-passwordpolicy-requirelowercase)" : {{Boolean}},
  "[RequireNumbers](#cfn-cognito-userpool-passwordpolicy-requirenumbers)" : {{Boolean}},
  "[RequireSymbols](#cfn-cognito-userpool-passwordpolicy-requiresymbols)" : {{Boolean}},
  "[RequireUppercase](#cfn-cognito-userpool-passwordpolicy-requireuppercase)" : {{Boolean}},
  "[TemporaryPasswordValidityDays](#cfn-cognito-userpool-passwordpolicy-temporarypasswordvaliditydays)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-cognito-userpool-passwordpolicy-syntax.yaml"></a>

```
  [MinimumLength](#cfn-cognito-userpool-passwordpolicy-minimumlength): {{Integer}}
  [PasswordHistorySize](#cfn-cognito-userpool-passwordpolicy-passwordhistorysize): {{Integer}}
  [RequireLowercase](#cfn-cognito-userpool-passwordpolicy-requirelowercase): {{Boolean}}
  [RequireNumbers](#cfn-cognito-userpool-passwordpolicy-requirenumbers): {{Boolean}}
  [RequireSymbols](#cfn-cognito-userpool-passwordpolicy-requiresymbols): {{Boolean}}
  [RequireUppercase](#cfn-cognito-userpool-passwordpolicy-requireuppercase): {{Boolean}}
  [TemporaryPasswordValidityDays](#cfn-cognito-userpool-passwordpolicy-temporarypasswordvaliditydays): {{Integer}}
```

## Properties
<a name="aws-properties-cognito-userpool-passwordpolicy-properties"></a>

`MinimumLength`  <a name="cfn-cognito-userpool-passwordpolicy-minimumlength"></a>
The minimum length of the password in the policy that you have set. This value can't be less than 6.
*Required*: No
*Type*: Integer
*Minimum*: `6`
*Maximum*: `99`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PasswordHistorySize`  <a name="cfn-cognito-userpool-passwordpolicy-passwordhistorysize"></a>
The number of previous passwords that you want Amazon Cognito to restrict each user from reusing. Users can't set a password that matches any of `n` previous passwords, where `n` is the value of `PasswordHistorySize`.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `24`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RequireLowercase`  <a name="cfn-cognito-userpool-passwordpolicy-requirelowercase"></a>
The requirement in a password policy that users must include at least one lowercase letter in their password.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RequireNumbers`  <a name="cfn-cognito-userpool-passwordpolicy-requirenumbers"></a>
The requirement in a password policy that users must include at least one number in their password.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RequireSymbols`  <a name="cfn-cognito-userpool-passwordpolicy-requiresymbols"></a>
The requirement in a password policy that users must include at least one symbol in their password.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RequireUppercase`  <a name="cfn-cognito-userpool-passwordpolicy-requireuppercase"></a>
The requirement in a password policy that users must include at least one uppercase letter in their password.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemporaryPasswordValidityDays`  <a name="cfn-cognito-userpool-passwordpolicy-temporarypasswordvaliditydays"></a>
The number of days a temporary password is valid in the password policy. If the user doesn't sign in during this time, an administrator must reset their password. Defaults to `7`. If you submit a value of `0`, Amazon Cognito treats it as a null value and sets `TemporaryPasswordValidityDays` to its default value.
When you set `TemporaryPasswordValidityDays` for a user pool, you can no longer set a value for the legacy `UnusedAccountValidityDays` parameter in that user pool.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `365`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
