---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpool-usernameconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPool UsernameConfiguration
<a name="aws-properties-cognito-userpool-usernameconfiguration"></a>

Case sensitivity of the username input for the selected sign-in option. When case sensitivity is set to `False` (case insensitive), users can sign in with any combination of capital and lowercase letters. For example, `username`, `USERNAME`, or `UserName`, or for email, `email@example.com` or `EMaiL@eXamplE.Com`. For most use cases, set case sensitivity to `False` (case insensitive) as a best practice. When usernames and email addresses are case insensitive, Amazon Cognito treats any variation in case as the same user, and prevents a case variation from being assigned to the same attribute for a different user.

## Syntax
<a name="aws-properties-cognito-userpool-usernameconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpool-usernameconfiguration-syntax.json"></a>

```
{
  "[CaseSensitive](#cfn-cognito-userpool-usernameconfiguration-casesensitive)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cognito-userpool-usernameconfiguration-syntax.yaml"></a>

```
  [CaseSensitive](#cfn-cognito-userpool-usernameconfiguration-casesensitive): {{Boolean}}
```

## Properties
<a name="aws-properties-cognito-userpool-usernameconfiguration-properties"></a>

`CaseSensitive`  <a name="cfn-cognito-userpool-usernameconfiguration-casesensitive"></a>
Specifies whether user name case sensitivity will be applied for all users in the user pool through Amazon Cognito APIs. For most use cases, set case sensitivity to `False` (case insensitive) as a best practice. When usernames and email addresses are case insensitive, users can sign in as the same user when they enter a different capitalization of their user name.
Valid values include:
true
Enables case sensitivity for all username input. When this option is set to `true`, users must sign in using the exact capitalization of their given username, such as “UserName”. This is the default value.
false
Enables case insensitivity for all username input. For example, when this option is set to `false`, users can sign in using `username`, `USERNAME`, or `UserName`. This option also enables both `preferred_username` and `email` alias to be case insensitive, in addition to the `username` attribute.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
