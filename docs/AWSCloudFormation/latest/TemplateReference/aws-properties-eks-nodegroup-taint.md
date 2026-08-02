---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-nodegroup-taint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Nodegroup Taint
<a name="aws-properties-eks-nodegroup-taint"></a>

A property that allows a node to repel a `Pod`. For more information, see [Node taints on managed node groups](https://docs.aws.amazon.com/eks/latest/userguide/node-taints-managed-node-groups.html) in the *Amazon EKS User Guide*.

## Syntax
<a name="aws-properties-eks-nodegroup-taint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-nodegroup-taint-syntax.json"></a>

```
{
  "[Effect](#cfn-eks-nodegroup-taint-effect)" : {{String}},
  "[Key](#cfn-eks-nodegroup-taint-key)" : {{String}},
  "[Value](#cfn-eks-nodegroup-taint-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-nodegroup-taint-syntax.yaml"></a>

```
  [Effect](#cfn-eks-nodegroup-taint-effect): {{String}}
  [Key](#cfn-eks-nodegroup-taint-key): {{String}}
  [Value](#cfn-eks-nodegroup-taint-value): {{String}}
```

## Properties
<a name="aws-properties-eks-nodegroup-taint-properties"></a>

`Effect`  <a name="cfn-eks-nodegroup-taint-effect"></a>
The effect of the taint.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-eks-nodegroup-taint-key"></a>
The key of the taint.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-eks-nodegroup-taint-value"></a>
The value of the taint.
*Required*: No
*Type*: String
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
