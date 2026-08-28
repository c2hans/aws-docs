---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-verifiedpermissions-identitysource-cognitouserpoolconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VerifiedPermissions::IdentitySource CognitoUserPoolConfiguration
<a name="aws-properties-verifiedpermissions-identitysource-cognitouserpoolconfiguration"></a>

A structure that contains configuration information used when creating or updating an identity source that represents a connection to an Amazon Cognito user pool used as an identity provider for Verified Permissions.

## Syntax
<a name="aws-properties-verifiedpermissions-identitysource-cognitouserpoolconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-verifiedpermissions-identitysource-cognitouserpoolconfiguration-syntax.json"></a>

```
{
  "[ClientIds](#cfn-verifiedpermissions-identitysource-cognitouserpoolconfiguration-clientids)" : {{[ String, ... ]}},
  "[GroupConfiguration](#cfn-verifiedpermissions-identitysource-cognitouserpoolconfiguration-groupconfiguration)" : {{CognitoGroupConfiguration}},
  "[UserPoolArn](#cfn-verifiedpermissions-identitysource-cognitouserpoolconfiguration-userpoolarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-verifiedpermissions-identitysource-cognitouserpoolconfiguration-syntax.yaml"></a>

```
  [ClientIds](#cfn-verifiedpermissions-identitysource-cognitouserpoolconfiguration-clientids): {{
    - String}}
  [GroupConfiguration](#cfn-verifiedpermissions-identitysource-cognitouserpoolconfiguration-groupconfiguration): {{
    CognitoGroupConfiguration}}
  [UserPoolArn](#cfn-verifiedpermissions-identitysource-cognitouserpoolconfiguration-userpoolarn): {{String}}
```

## Properties
<a name="aws-properties-verifiedpermissions-identitysource-cognitouserpoolconfiguration-properties"></a>

`ClientIds`  <a name="cfn-verifiedpermissions-identitysource-cognitouserpoolconfiguration-clientids"></a>
The unique application client IDs that are associated with the specified Amazon Cognito user pool.
Example: `"ClientIds": ["&ExampleCogClientId;"]`
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `255 | 1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupConfiguration`  <a name="cfn-verifiedpermissions-identitysource-cognitouserpoolconfiguration-groupconfiguration"></a>
The type of entity that a policy store maps to groups from an Amazon Cognito user pool identity source.
*Required*: No
*Type*: [CognitoGroupConfiguration](aws-properties-verifiedpermissions-identitysource-cognitogroupconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPoolArn`  <a name="cfn-verifiedpermissions-identitysource-cognitouserpoolconfiguration-userpoolarn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the Amazon Cognito user pool that contains the identities to be authorized.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-zA-Z0-9-]+:cognito-idp:(([a-zA-Z0-9-]+:\d{12}:userpool/[\w-]+_[0-9a-zA-Z]+))$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
