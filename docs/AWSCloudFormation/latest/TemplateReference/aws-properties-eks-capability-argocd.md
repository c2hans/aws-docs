---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-capability-argocd.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Capability ArgoCd
<a name="aws-properties-eks-capability-argocd"></a>

<a name="aws-properties-eks-capability-argocd-description"></a>The `ArgoCd` property type specifies Property description not available. for an [AWS::EKS::Capability](aws-resource-eks-capability.md).

## Syntax
<a name="aws-properties-eks-capability-argocd-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-capability-argocd-syntax.json"></a>

```
{
  "[AwsIdc](#cfn-eks-capability-argocd-awsidc)" : {{AwsIdc}},
  "[Namespace](#cfn-eks-capability-argocd-namespace)" : {{String}},
  "[NetworkAccess](#cfn-eks-capability-argocd-networkaccess)" : {{NetworkAccess}},
  "[RbacRoleMappings](#cfn-eks-capability-argocd-rbacrolemappings)" : {{[ ArgoCdRoleMapping, ... ]}},
  "[ServerUrl](#cfn-eks-capability-argocd-serverurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-capability-argocd-syntax.yaml"></a>

```
  [AwsIdc](#cfn-eks-capability-argocd-awsidc): {{
    AwsIdc}}
  [Namespace](#cfn-eks-capability-argocd-namespace): {{String}}
  [NetworkAccess](#cfn-eks-capability-argocd-networkaccess): {{
    NetworkAccess}}
  [RbacRoleMappings](#cfn-eks-capability-argocd-rbacrolemappings): {{
    - ArgoCdRoleMapping}}
  [ServerUrl](#cfn-eks-capability-argocd-serverurl): {{String}}
```

## Properties
<a name="aws-properties-eks-capability-argocd-properties"></a>

`AwsIdc`  <a name="cfn-eks-capability-argocd-awsidc"></a>
Property description not available.
*Required*: Yes
*Type*: [AwsIdc](aws-properties-eks-capability-awsidc.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Namespace`  <a name="cfn-eks-capability-argocd-namespace"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkAccess`  <a name="cfn-eks-capability-argocd-networkaccess"></a>
Property description not available.
*Required*: No
*Type*: [NetworkAccess](aws-properties-eks-capability-networkaccess.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RbacRoleMappings`  <a name="cfn-eks-capability-argocd-rbacrolemappings"></a>
Property description not available.
*Required*: No
*Type*: Array of [ArgoCdRoleMapping](aws-properties-eks-capability-argocdrolemapping.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerUrl`  <a name="cfn-eks-capability-argocd-serverurl"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
