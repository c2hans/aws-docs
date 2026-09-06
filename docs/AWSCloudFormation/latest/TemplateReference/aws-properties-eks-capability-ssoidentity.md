---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-capability-ssoidentity.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Capability SsoIdentity
<a name="aws-properties-eks-capability-ssoidentity"></a>

An IAM Identity CenterIAM; Identity Center identity (user or group) that can be assigned permissions in a capability.

## Syntax
<a name="aws-properties-eks-capability-ssoidentity-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-capability-ssoidentity-syntax.json"></a>

```
{
  "[Id](#cfn-eks-capability-ssoidentity-id)" : {{String}},
  "[Type](#cfn-eks-capability-ssoidentity-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-capability-ssoidentity-syntax.yaml"></a>

```
  [Id](#cfn-eks-capability-ssoidentity-id): {{String}}
  [Type](#cfn-eks-capability-ssoidentity-type): {{String}}
```

## Properties
<a name="aws-properties-eks-capability-ssoidentity-properties"></a>

`Id`  <a name="cfn-eks-capability-ssoidentity-id"></a>
The unique identifier of the IAM Identity CenterIAM; Identity Center user or group.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-eks-capability-ssoidentity-type"></a>
The type of identity. Valid values are `SSO_USER` or `SSO_GROUP`.
*Required*: Yes
*Type*: String
*Allowed values*: `SSO_USER | SSO_GROUP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
