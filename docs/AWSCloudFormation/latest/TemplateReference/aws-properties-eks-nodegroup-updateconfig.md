---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-nodegroup-updateconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Nodegroup UpdateConfig
<a name="aws-properties-eks-nodegroup-updateconfig"></a>

The update configuration for the node group.

## Syntax
<a name="aws-properties-eks-nodegroup-updateconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-nodegroup-updateconfig-syntax.json"></a>

```
{
  "[MaxUnavailable](#cfn-eks-nodegroup-updateconfig-maxunavailable)" : {{Number}},
  "[MaxUnavailablePercentage](#cfn-eks-nodegroup-updateconfig-maxunavailablepercentage)" : {{Number}},
  "[UpdateStrategy](#cfn-eks-nodegroup-updateconfig-updatestrategy)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-nodegroup-updateconfig-syntax.yaml"></a>

```
  [MaxUnavailable](#cfn-eks-nodegroup-updateconfig-maxunavailable): {{Number}}
  [MaxUnavailablePercentage](#cfn-eks-nodegroup-updateconfig-maxunavailablepercentage): {{Number}}
  [UpdateStrategy](#cfn-eks-nodegroup-updateconfig-updatestrategy): {{String}}
```

## Properties
<a name="aws-properties-eks-nodegroup-updateconfig-properties"></a>

`MaxUnavailable`  <a name="cfn-eks-nodegroup-updateconfig-maxunavailable"></a>
The maximum number of nodes unavailable at once during a version update. Nodes are updated in parallel. This value or `maxUnavailablePercentage` is required to have a value.The maximum number is 100.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxUnavailablePercentage`  <a name="cfn-eks-nodegroup-updateconfig-maxunavailablepercentage"></a>
The maximum percentage of nodes unavailable during a version update. This percentage of nodes are updated in parallel, up to 100 nodes at once. This value or `maxUnavailable` is required to have a value.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateStrategy`  <a name="cfn-eks-nodegroup-updateconfig-updatestrategy"></a>
The configuration for the behavior to follow during a node group version update of this managed node group. You choose between two possible strategies for replacing nodes during an [https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateNodegroupVersion.html](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateNodegroupVersion.html) action.
An Amazon EKS managed node group updates by replacing nodes with new nodes of newer AMI versions in parallel. The *update strategy* changes the managed node update behavior of the managed node group for each quantity. The *default* strategy has guardrails to protect you from misconfiguration and launches the new instances first, before terminating the old instances. The *minimal* strategy removes the guardrails and terminates the old instances before launching the new instances. This minimal strategy is useful in scenarios where you are constrained to resources or costs (for example, with hardware accelerators such as GPUs).
*Required*: No
*Type*: String
*Allowed values*: `DEFAULT | MINIMAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
