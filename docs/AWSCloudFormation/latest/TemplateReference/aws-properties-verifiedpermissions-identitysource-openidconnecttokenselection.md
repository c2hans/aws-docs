---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-verifiedpermissions-identitysource-openidconnecttokenselection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VerifiedPermissions::IdentitySource OpenIdConnectTokenSelection
<a name="aws-properties-verifiedpermissions-identitysource-openidconnecttokenselection"></a>

The token type that you want to process from your OIDC identity provider. Your policy store can process either identity (ID) or access tokens from a given OIDC identity source.

This data type is part of a [OpenIdConnectConfiguration](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectConfiguration.html) structure, which is a parameter of [CreateIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html).

## Syntax
<a name="aws-properties-verifiedpermissions-identitysource-openidconnecttokenselection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-verifiedpermissions-identitysource-openidconnecttokenselection-syntax.json"></a>

```
{
  "[AccessTokenOnly](#cfn-verifiedpermissions-identitysource-openidconnecttokenselection-accesstokenonly)" : {{OpenIdConnectAccessTokenConfiguration}},
  "[IdentityTokenOnly](#cfn-verifiedpermissions-identitysource-openidconnecttokenselection-identitytokenonly)" : {{OpenIdConnectIdentityTokenConfiguration}}
}
```

### YAML
<a name="aws-properties-verifiedpermissions-identitysource-openidconnecttokenselection-syntax.yaml"></a>

```
  [AccessTokenOnly](#cfn-verifiedpermissions-identitysource-openidconnecttokenselection-accesstokenonly): {{
    OpenIdConnectAccessTokenConfiguration}}
  [IdentityTokenOnly](#cfn-verifiedpermissions-identitysource-openidconnecttokenselection-identitytokenonly): {{
    OpenIdConnectIdentityTokenConfiguration}}
```

## Properties
<a name="aws-properties-verifiedpermissions-identitysource-openidconnecttokenselection-properties"></a>

`AccessTokenOnly`  <a name="cfn-verifiedpermissions-identitysource-openidconnecttokenselection-accesstokenonly"></a>
The OIDC configuration for processing access tokens. Contains allowed audience claims, for example `https://auth.example.com`, and the claim that you want to map to the principal, for example `sub`.
*Required*: No
*Type*: [OpenIdConnectAccessTokenConfiguration](aws-properties-verifiedpermissions-identitysource-openidconnectaccesstokenconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentityTokenOnly`  <a name="cfn-verifiedpermissions-identitysource-openidconnecttokenselection-identitytokenonly"></a>
The OIDC configuration for processing identity (ID) tokens. Contains allowed client ID claims, for example `1example23456789`, and the claim that you want to map to the principal, for example `sub`.
*Required*: No
*Type*: [OpenIdConnectIdentityTokenConfiguration](aws-properties-verifiedpermissions-identitysource-openidconnectidentitytokenconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
