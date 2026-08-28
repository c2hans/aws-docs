---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-verifiedpermissions-identitysource-openidconnectaccesstokenconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VerifiedPermissions::IdentitySource OpenIdConnectAccessTokenConfiguration
<a name="aws-properties-verifiedpermissions-identitysource-openidconnectaccesstokenconfiguration"></a>

The configuration of an OpenID Connect (OIDC) identity source for handling access token claims. Contains the claim that you want to identify as the principal in an authorization request, and the values of the `aud` claim, or audiences, that you want to accept.

This data type is part of a [OpenIdConnectTokenSelection](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectTokenSelection.html) structure, which is a parameter of [CreateIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html).

## Syntax
<a name="aws-properties-verifiedpermissions-identitysource-openidconnectaccesstokenconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-verifiedpermissions-identitysource-openidconnectaccesstokenconfiguration-syntax.json"></a>

```
{
  "[Audiences](#cfn-verifiedpermissions-identitysource-openidconnectaccesstokenconfiguration-audiences)" : {{[ String, ... ]}},
  "[PrincipalIdClaim](#cfn-verifiedpermissions-identitysource-openidconnectaccesstokenconfiguration-principalidclaim)" : {{String}}
}
```

### YAML
<a name="aws-properties-verifiedpermissions-identitysource-openidconnectaccesstokenconfiguration-syntax.yaml"></a>

```
  [Audiences](#cfn-verifiedpermissions-identitysource-openidconnectaccesstokenconfiguration-audiences): {{
    - String}}
  [PrincipalIdClaim](#cfn-verifiedpermissions-identitysource-openidconnectaccesstokenconfiguration-principalidclaim): {{String}}
```

## Properties
<a name="aws-properties-verifiedpermissions-identitysource-openidconnectaccesstokenconfiguration-properties"></a>

`Audiences`  <a name="cfn-verifiedpermissions-identitysource-openidconnectaccesstokenconfiguration-audiences"></a>
The access token `aud` claim values that you want to accept in your policy store. For example, `https://myapp.example.com, https://myapp2.example.com`.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `255 | 255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrincipalIdClaim`  <a name="cfn-verifiedpermissions-identitysource-openidconnectaccesstokenconfiguration-principalidclaim"></a>
The claim that determines the principal in OIDC access tokens. For example, `sub`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
