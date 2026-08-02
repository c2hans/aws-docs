---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-verifiedpermissions-identitysource-openidconnectconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VerifiedPermissions::IdentitySource OpenIdConnectConfiguration
<a name="aws-properties-verifiedpermissions-identitysource-openidconnectconfiguration"></a>

Contains configuration details of an OpenID Connect (OIDC) identity provider, or identity source, that Verified Permissions can use to generate entities from authenticated identities. It specifies the issuer URL, token type that you want to use, and policy store entity details.

This data type is part of a [Configuration](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_Configuration.html) structure, which is a parameter to [CreateIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html).

## Syntax
<a name="aws-properties-verifiedpermissions-identitysource-openidconnectconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-verifiedpermissions-identitysource-openidconnectconfiguration-syntax.json"></a>

```
{
  "[EntityIdPrefix](#cfn-verifiedpermissions-identitysource-openidconnectconfiguration-entityidprefix)" : {{String}},
  "[GroupConfiguration](#cfn-verifiedpermissions-identitysource-openidconnectconfiguration-groupconfiguration)" : {{OpenIdConnectGroupConfiguration}},
  "[Issuer](#cfn-verifiedpermissions-identitysource-openidconnectconfiguration-issuer)" : {{String}},
  "[TokenSelection](#cfn-verifiedpermissions-identitysource-openidconnectconfiguration-tokenselection)" : {{OpenIdConnectTokenSelection}}
}
```

### YAML
<a name="aws-properties-verifiedpermissions-identitysource-openidconnectconfiguration-syntax.yaml"></a>

```
  [EntityIdPrefix](#cfn-verifiedpermissions-identitysource-openidconnectconfiguration-entityidprefix): {{String}}
  [GroupConfiguration](#cfn-verifiedpermissions-identitysource-openidconnectconfiguration-groupconfiguration): {{
    OpenIdConnectGroupConfiguration}}
  [Issuer](#cfn-verifiedpermissions-identitysource-openidconnectconfiguration-issuer): {{String}}
  [TokenSelection](#cfn-verifiedpermissions-identitysource-openidconnectconfiguration-tokenselection): {{
    OpenIdConnectTokenSelection}}
```

## Properties
<a name="aws-properties-verifiedpermissions-identitysource-openidconnectconfiguration-properties"></a>

`EntityIdPrefix`  <a name="cfn-verifiedpermissions-identitysource-openidconnectconfiguration-entityidprefix"></a>
A descriptive string that you want to prefix to user entities from your OIDC identity provider. For example, if you set an `entityIdPrefix` of `MyOIDCProvider`, you can reference principals in your policies in the format `MyCorp::User::MyOIDCProvider|Carlos`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupConfiguration`  <a name="cfn-verifiedpermissions-identitysource-openidconnectconfiguration-groupconfiguration"></a>
The claim in OIDC identity provider tokens that indicates a user's group membership, and the entity type that you want to map it to. For example, this object can map the contents of a `groups` claim to `MyCorp::UserGroup`.
*Required*: No
*Type*: [OpenIdConnectGroupConfiguration](aws-properties-verifiedpermissions-identitysource-openidconnectgroupconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Issuer`  <a name="cfn-verifiedpermissions-identitysource-openidconnectconfiguration-issuer"></a>
The issuer URL of an OIDC identity provider. This URL must have an OIDC discovery endpoint at the path `.well-known/openid-configuration`.
*Required*: Yes
*Type*: String
*Pattern*: `^https://.*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenSelection`  <a name="cfn-verifiedpermissions-identitysource-openidconnectconfiguration-tokenselection"></a>
The token type that you want to process from your OIDC identity provider. Your policy store can process either identity (ID) or access tokens from a given OIDC identity source.
*Required*: Yes
*Type*: [OpenIdConnectTokenSelection](aws-properties-verifiedpermissions-identitysource-openidconnecttokenselection.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
