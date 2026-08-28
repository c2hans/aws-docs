---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-verifiedpermissions-identitysource-identitysourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VerifiedPermissions::IdentitySource IdentitySourceConfiguration
<a name="aws-properties-verifiedpermissions-identitysource-identitysourceconfiguration"></a>

A structure that contains configuration information used when creating or updating a new identity source.

**Note**
At this time, the only valid member of this structure is a Amazon Cognito user pool configuration.
You must specify a `userPoolArn`, and optionally, a `ClientId`.

## Syntax
<a name="aws-properties-verifiedpermissions-identitysource-identitysourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-verifiedpermissions-identitysource-identitysourceconfiguration-syntax.json"></a>

```
{
  "[CognitoUserPoolConfiguration](#cfn-verifiedpermissions-identitysource-identitysourceconfiguration-cognitouserpoolconfiguration)" : {{CognitoUserPoolConfiguration}},
  "[OpenIdConnectConfiguration](#cfn-verifiedpermissions-identitysource-identitysourceconfiguration-openidconnectconfiguration)" : {{OpenIdConnectConfiguration}}
}
```

### YAML
<a name="aws-properties-verifiedpermissions-identitysource-identitysourceconfiguration-syntax.yaml"></a>

```
  [CognitoUserPoolConfiguration](#cfn-verifiedpermissions-identitysource-identitysourceconfiguration-cognitouserpoolconfiguration): {{
    CognitoUserPoolConfiguration}}
  [OpenIdConnectConfiguration](#cfn-verifiedpermissions-identitysource-identitysourceconfiguration-openidconnectconfiguration): {{
    OpenIdConnectConfiguration}}
```

## Properties
<a name="aws-properties-verifiedpermissions-identitysource-identitysourceconfiguration-properties"></a>

`CognitoUserPoolConfiguration`  <a name="cfn-verifiedpermissions-identitysource-identitysourceconfiguration-cognitouserpoolconfiguration"></a>
A structure that contains configuration information used when creating or updating an identity source that represents a connection to an Amazon Cognito user pool used as an identity provider for Verified Permissions.
*Required*: No
*Type*: [CognitoUserPoolConfiguration](aws-properties-verifiedpermissions-identitysource-cognitouserpoolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OpenIdConnectConfiguration`  <a name="cfn-verifiedpermissions-identitysource-identitysourceconfiguration-openidconnectconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [OpenIdConnectConfiguration](aws-properties-verifiedpermissions-identitysource-openidconnectconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
