---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpool-policies.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPool Policies
<a name="aws-properties-cognito-userpool-policies"></a>

A list of user pool policies. Contains the policy that sets password-complexity requirements.

## Syntax
<a name="aws-properties-cognito-userpool-policies-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpool-policies-syntax.json"></a>

```
{
  "[PasswordPolicy](#cfn-cognito-userpool-policies-passwordpolicy)" : {{PasswordPolicy}},
  "[SignInPolicy](#cfn-cognito-userpool-policies-signinpolicy)" : {{SignInPolicy}}
}
```

### YAML
<a name="aws-properties-cognito-userpool-policies-syntax.yaml"></a>

```
  [PasswordPolicy](#cfn-cognito-userpool-policies-passwordpolicy): {{
    PasswordPolicy}}
  [SignInPolicy](#cfn-cognito-userpool-policies-signinpolicy): {{
    SignInPolicy}}
```

## Properties
<a name="aws-properties-cognito-userpool-policies-properties"></a>

`PasswordPolicy`  <a name="cfn-cognito-userpool-policies-passwordpolicy"></a>
The password policy settings for a user pool, including complexity, history, and length requirements.
*Required*: No
*Type*: [PasswordPolicy](aws-properties-cognito-userpool-passwordpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SignInPolicy`  <a name="cfn-cognito-userpool-policies-signinpolicy"></a>
The policy for allowed types of authentication in a user pool. To activate this setting, your user pool must be in the [ Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.
*Required*: No
*Type*: [SignInPolicy](aws-properties-cognito-userpool-signinpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
