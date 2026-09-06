---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-verifiedpermissions-identitysource-openidconnectidentitytokenconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VerifiedPermissions::IdentitySource OpenIdConnectIdentityTokenConfiguration
<a name="aws-properties-verifiedpermissions-identitysource-openidconnectidentitytokenconfiguration"></a>

The configuration of an OpenID Connect (OIDC) identity source for handling identity (ID) token claims. Contains the claim that you want to identify as the principal in an authorization request, and the values of the `aud` claim, or audiences, that you want to accept.

This data type is part of a [OpenIdConnectTokenSelection](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectTokenSelection.html) structure, which is a parameter of [CreateIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html).

## Syntax
<a name="aws-properties-verifiedpermissions-identitysource-openidconnectidentitytokenconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-verifiedpermissions-identitysource-openidconnectidentitytokenconfiguration-syntax.json"></a>

```
{
  "[ClientIds](#cfn-verifiedpermissions-identitysource-openidconnectidentitytokenconfiguration-clientids)" : {{[ String, ... ]}},
  "[PrincipalIdClaim](#cfn-verifiedpermissions-identitysource-openidconnectidentitytokenconfiguration-principalidclaim)" : {{String}}
}
```

### YAML
<a name="aws-properties-verifiedpermissions-identitysource-openidconnectidentitytokenconfiguration-syntax.yaml"></a>

```
  [ClientIds](#cfn-verifiedpermissions-identitysource-openidconnectidentitytokenconfiguration-clientids): {{
    - String}}
  [PrincipalIdClaim](#cfn-verifiedpermissions-identitysource-openidconnectidentitytokenconfiguration-principalidclaim): {{String}}
```

## Properties
<a name="aws-properties-verifiedpermissions-identitysource-openidconnectidentitytokenconfiguration-properties"></a>

`ClientIds`  <a name="cfn-verifiedpermissions-identitysource-openidconnectidentitytokenconfiguration-clientids"></a>
The ID token audience, or client ID, claim values that you want to accept in your policy store from an OIDC identity provider. For example, `1example23456789, 2example10111213`.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `255 | 1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrincipalIdClaim`  <a name="cfn-verifiedpermissions-identitysource-openidconnectidentitytokenconfiguration-principalidclaim"></a>
The claim that determines the principal in OIDC access tokens. For example, `sub`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
