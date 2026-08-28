---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpool-signinpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPool SignInPolicy
<a name="aws-properties-cognito-userpool-signinpolicy"></a>

The policy for allowed types of authentication in a user pool. To activate this setting, your user pool must be in the [ Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.

## Syntax
<a name="aws-properties-cognito-userpool-signinpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpool-signinpolicy-syntax.json"></a>

```
{
  "[AllowedFirstAuthFactors](#cfn-cognito-userpool-signinpolicy-allowedfirstauthfactors)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cognito-userpool-signinpolicy-syntax.yaml"></a>

```
  [AllowedFirstAuthFactors](#cfn-cognito-userpool-signinpolicy-allowedfirstauthfactors): {{
    - String}}
```

## Properties
<a name="aws-properties-cognito-userpool-signinpolicy-properties"></a>

`AllowedFirstAuthFactors`  <a name="cfn-cognito-userpool-signinpolicy-allowedfirstauthfactors"></a>
The sign-in methods that a user pool supports as the first factor. You can permit users to start authentication with a standard username and password, or with other one-time password and hardware factors.
Supports values of `EMAIL_OTP`, `SMS_OTP`, `WEB_AUTHN` and `PASSWORD`,
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
