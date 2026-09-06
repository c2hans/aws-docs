---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-identityproviderconfig-requiredclaim.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::IdentityProviderConfig RequiredClaim
<a name="aws-properties-eks-identityproviderconfig-requiredclaim"></a>

A key-value pair that describes a required claim in the identity token. If set, each claim is verified to be present in the token with a matching value.

## Syntax
<a name="aws-properties-eks-identityproviderconfig-requiredclaim-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-identityproviderconfig-requiredclaim-syntax.json"></a>

```
{
  "[Key](#cfn-eks-identityproviderconfig-requiredclaim-key)" : {{String}},
  "[Value](#cfn-eks-identityproviderconfig-requiredclaim-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-identityproviderconfig-requiredclaim-syntax.yaml"></a>

```
  [Key](#cfn-eks-identityproviderconfig-requiredclaim-key): {{String}}
  [Value](#cfn-eks-identityproviderconfig-requiredclaim-value): {{String}}
```

## Properties
<a name="aws-properties-eks-identityproviderconfig-requiredclaim-properties"></a>

`Key`  <a name="cfn-eks-identityproviderconfig-requiredclaim-key"></a>
The key to match from the token.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-eks-identityproviderconfig-requiredclaim-value"></a>
The value for the key from the token.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `253`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
