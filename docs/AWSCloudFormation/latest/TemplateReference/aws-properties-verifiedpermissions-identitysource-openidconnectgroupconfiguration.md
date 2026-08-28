---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-verifiedpermissions-identitysource-openidconnectgroupconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VerifiedPermissions::IdentitySource OpenIdConnectGroupConfiguration
<a name="aws-properties-verifiedpermissions-identitysource-openidconnectgroupconfiguration"></a>

The claim in OIDC identity provider tokens that indicates a user's group membership, and the entity type that you want to map it to. For example, this object can map the contents of a `groups` claim to `MyCorp::UserGroup`.

This data type is part of a [OpenIdConnectConfiguration](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectConfiguration.html) structure, which is a parameter of [CreateIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html).

## Syntax
<a name="aws-properties-verifiedpermissions-identitysource-openidconnectgroupconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-verifiedpermissions-identitysource-openidconnectgroupconfiguration-syntax.json"></a>

```
{
  "[GroupClaim](#cfn-verifiedpermissions-identitysource-openidconnectgroupconfiguration-groupclaim)" : {{String}},
  "[GroupEntityType](#cfn-verifiedpermissions-identitysource-openidconnectgroupconfiguration-groupentitytype)" : {{String}}
}
```

### YAML
<a name="aws-properties-verifiedpermissions-identitysource-openidconnectgroupconfiguration-syntax.yaml"></a>

```
  [GroupClaim](#cfn-verifiedpermissions-identitysource-openidconnectgroupconfiguration-groupclaim): {{String}}
  [GroupEntityType](#cfn-verifiedpermissions-identitysource-openidconnectgroupconfiguration-groupentitytype): {{String}}
```

## Properties
<a name="aws-properties-verifiedpermissions-identitysource-openidconnectgroupconfiguration-properties"></a>

`GroupClaim`  <a name="cfn-verifiedpermissions-identitysource-openidconnectgroupconfiguration-groupclaim"></a>
The token claim that you want Verified Permissions to interpret as group membership. For example, `groups`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupEntityType`  <a name="cfn-verifiedpermissions-identitysource-openidconnectgroupconfiguration-groupentitytype"></a>
The policy store entity type that you want to map your users' group claim to. For example, `MyCorp::UserGroup`. A group entity type is an entity that can have a user entity type as a member.
*Required*: Yes
*Type*: String
*Pattern*: `^([_a-zA-Z][_a-zA-Z0-9]*::)*[_a-zA-Z][_a-zA-Z0-9]*$`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
