---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-verifiedpermissions-policystore-deletionprotection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VerifiedPermissions::PolicyStore DeletionProtection
<a name="aws-properties-verifiedpermissions-policystore-deletionprotection"></a>

Specifies whether the policy store can be deleted.

## Syntax
<a name="aws-properties-verifiedpermissions-policystore-deletionprotection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-verifiedpermissions-policystore-deletionprotection-syntax.json"></a>

```
{
  "[Mode](#cfn-verifiedpermissions-policystore-deletionprotection-mode)" : {{String}}
}
```

### YAML
<a name="aws-properties-verifiedpermissions-policystore-deletionprotection-syntax.yaml"></a>

```
  [Mode](#cfn-verifiedpermissions-policystore-deletionprotection-mode): {{String}}
```

## Properties
<a name="aws-properties-verifiedpermissions-policystore-deletionprotection-properties"></a>

`Mode`  <a name="cfn-verifiedpermissions-policystore-deletionprotection-mode"></a>
Specifies whether the policy store can be deleted. If enabled, the policy store can't be deleted.
The default state is `DISABLED`.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
