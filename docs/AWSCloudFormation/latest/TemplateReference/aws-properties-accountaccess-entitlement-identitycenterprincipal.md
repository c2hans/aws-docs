---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-accountaccess-entitlement-identitycenterprincipal.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AccountAccess::Entitlement IdentityCenterPrincipal
<a name="aws-properties-accountaccess-entitlement-identitycenterprincipal"></a>

Identifies a user or group from IAM Identity Center.

## Syntax
<a name="aws-properties-accountaccess-entitlement-identitycenterprincipal-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-accountaccess-entitlement-identitycenterprincipal-syntax.json"></a>

```
{
  "[GroupId](#cfn-accountaccess-entitlement-identitycenterprincipal-groupid)" : {{String}},
  "[UserId](#cfn-accountaccess-entitlement-identitycenterprincipal-userid)" : {{String}}
}
```

### YAML
<a name="aws-properties-accountaccess-entitlement-identitycenterprincipal-syntax.yaml"></a>

```
  [GroupId](#cfn-accountaccess-entitlement-identitycenterprincipal-groupid): {{String}}
  [UserId](#cfn-accountaccess-entitlement-identitycenterprincipal-userid): {{String}}
```

## Properties
<a name="aws-properties-accountaccess-entitlement-identitycenterprincipal-properties"></a>

`GroupId`  <a name="cfn-accountaccess-entitlement-identitycenterprincipal-groupid"></a>
The unique identifier of a group in IAM Identity Center.
*Required*: No
*Type*: String
*Pattern*: `^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$`
*Minimum*: `1`
*Maximum*: `47`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UserId`  <a name="cfn-accountaccess-entitlement-identitycenterprincipal-userid"></a>
The unique identifier of a user in IAM Identity Center.
*Required*: No
*Type*: String
*Pattern*: `^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$`
*Minimum*: `1`
*Maximum*: `47`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
