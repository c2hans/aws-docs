---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-nodegroup-warmpoolconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Nodegroup WarmPoolConfig
<a name="aws-properties-eks-nodegroup-warmpoolconfig"></a>

The configuration for an Amazon EC2 Auto Scaling warm pool attached to an Amazon EKS managed node group. Warm pools maintain pre-initialized EC2 instances alongside your Auto Scaling group that have already completed the bootup initialization process and can be kept in a `Stopped`, `Running`, or `Hibernated` state.

## Syntax
<a name="aws-properties-eks-nodegroup-warmpoolconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-nodegroup-warmpoolconfig-syntax.json"></a>

```
{
  "[Enabled](#cfn-eks-nodegroup-warmpoolconfig-enabled)" : {{Boolean}},
  "[MaxGroupPreparedCapacity](#cfn-eks-nodegroup-warmpoolconfig-maxgrouppreparedcapacity)" : {{Integer}},
  "[MinSize](#cfn-eks-nodegroup-warmpoolconfig-minsize)" : {{Integer}},
  "[PoolState](#cfn-eks-nodegroup-warmpoolconfig-poolstate)" : {{String}},
  "[ReuseOnScaleIn](#cfn-eks-nodegroup-warmpoolconfig-reuseonscalein)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-eks-nodegroup-warmpoolconfig-syntax.yaml"></a>

```
  [Enabled](#cfn-eks-nodegroup-warmpoolconfig-enabled): {{Boolean}}
  [MaxGroupPreparedCapacity](#cfn-eks-nodegroup-warmpoolconfig-maxgrouppreparedcapacity): {{Integer}}
  [MinSize](#cfn-eks-nodegroup-warmpoolconfig-minsize): {{Integer}}
  [PoolState](#cfn-eks-nodegroup-warmpoolconfig-poolstate): {{String}}
  [ReuseOnScaleIn](#cfn-eks-nodegroup-warmpoolconfig-reuseonscalein): {{Boolean}}
```

## Properties
<a name="aws-properties-eks-nodegroup-warmpoolconfig-properties"></a>

`Enabled`  <a name="cfn-eks-nodegroup-warmpoolconfig-enabled"></a>
Specifies whether to attach warm pools on the managed node group. Set to `true` to enable the warm pool, or `false` to disable and remove it. If not specified during an update, the current value is preserved.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxGroupPreparedCapacity`  <a name="cfn-eks-nodegroup-warmpoolconfig-maxgrouppreparedcapacity"></a>
The maximum total number of instances across the warm pool and Auto Scaling group combined. This value controls the total prepared capacity available for your node group.
*Required*: No
*Type*: Integer
*Minimum*: `-1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinSize`  <a name="cfn-eks-nodegroup-warmpoolconfig-minsize"></a>
The minimum number of instances to maintain in the warm pool. Default: `0`. Size your warm pool based on scaling patterns to balance cost and availability. Start with 10-20% of expected peak capacity.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PoolState`  <a name="cfn-eks-nodegroup-warmpoolconfig-poolstate"></a>
The desired state for warm pool instances. Default: `Stopped`. Valid values are `Stopped` (most cost-effective with EBS storage costs only), `Running` (fastest transition time with full EC2 costs), and `Hibernated` (balance between cost and speed, only supported on specific instance types). Warm pool instances in the `Hibernated` state are not supported with Bottlerocket AMIs.
*Required*: No
*Type*: String
*Allowed values*: `STOPPED | RUNNING | HIBERNATED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReuseOnScaleIn`  <a name="cfn-eks-nodegroup-warmpoolconfig-reuseonscalein"></a>
Indicates whether instances should return to the warm pool during scale-in events instead of being terminated. Default: `false`. Enable this to reduce costs by reusing instances. This feature is not supported for Bottlerocket AMIs.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
