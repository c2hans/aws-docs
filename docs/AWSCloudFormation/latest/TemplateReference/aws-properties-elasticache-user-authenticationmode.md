---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticache-user-authenticationmode.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElastiCache::User AuthenticationMode
<a name="aws-properties-elasticache-user-authenticationmode"></a>

Specifies the authentication mode to use.

## Syntax
<a name="aws-properties-elasticache-user-authenticationmode-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticache-user-authenticationmode-syntax.json"></a>

```
{
  "[Passwords](#cfn-elasticache-user-authenticationmode-passwords)" : {{[ String, ... ]}},
  "[Type](#cfn-elasticache-user-authenticationmode-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticache-user-authenticationmode-syntax.yaml"></a>

```
  [Passwords](#cfn-elasticache-user-authenticationmode-passwords): {{
    - String}}
  [Type](#cfn-elasticache-user-authenticationmode-type): {{String}}
```

## Properties
<a name="aws-properties-elasticache-user-authenticationmode-properties"></a>

`Passwords`  <a name="cfn-elasticache-user-authenticationmode-passwords"></a>
Specifies the passwords to use for authentication if `Type` is set to `password`.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-elasticache-user-authenticationmode-type"></a>
Specifies the authentication type. Possible options are IAM authentication, password, and no password.
The `no-password-required` type is not supported for users with the Valkey engine. If you use the Valkey engine, specify `iam` or `password` authentication.
*Required*: Yes
*Type*: String
*Allowed values*: `password | no-password-required | iam`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
