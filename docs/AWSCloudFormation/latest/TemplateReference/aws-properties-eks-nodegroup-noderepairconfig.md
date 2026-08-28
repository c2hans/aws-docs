---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-nodegroup-noderepairconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Nodegroup NodeRepairConfig
<a name="aws-properties-eks-nodegroup-noderepairconfig"></a>

The node auto repair configuration for the node group.

## Syntax
<a name="aws-properties-eks-nodegroup-noderepairconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-nodegroup-noderepairconfig-syntax.json"></a>

```
{
  "[Enabled](#cfn-eks-nodegroup-noderepairconfig-enabled)" : {{Boolean}},
  "[MaxParallelNodesRepairedCount](#cfn-eks-nodegroup-noderepairconfig-maxparallelnodesrepairedcount)" : {{Integer}},
  "[MaxParallelNodesRepairedPercentage](#cfn-eks-nodegroup-noderepairconfig-maxparallelnodesrepairedpercentage)" : {{Integer}},
  "[MaxUnhealthyNodeThresholdCount](#cfn-eks-nodegroup-noderepairconfig-maxunhealthynodethresholdcount)" : {{Integer}},
  "[MaxUnhealthyNodeThresholdPercentage](#cfn-eks-nodegroup-noderepairconfig-maxunhealthynodethresholdpercentage)" : {{Integer}},
  "[NodeRepairConfigOverrides](#cfn-eks-nodegroup-noderepairconfig-noderepairconfigoverrides)" : {{[ NodeRepairConfigOverrides, ... ]}}
}
```

### YAML
<a name="aws-properties-eks-nodegroup-noderepairconfig-syntax.yaml"></a>

```
  [Enabled](#cfn-eks-nodegroup-noderepairconfig-enabled): {{Boolean}}
  [MaxParallelNodesRepairedCount](#cfn-eks-nodegroup-noderepairconfig-maxparallelnodesrepairedcount): {{Integer}}
  [MaxParallelNodesRepairedPercentage](#cfn-eks-nodegroup-noderepairconfig-maxparallelnodesrepairedpercentage): {{Integer}}
  [MaxUnhealthyNodeThresholdCount](#cfn-eks-nodegroup-noderepairconfig-maxunhealthynodethresholdcount): {{Integer}}
  [MaxUnhealthyNodeThresholdPercentage](#cfn-eks-nodegroup-noderepairconfig-maxunhealthynodethresholdpercentage): {{Integer}}
  [NodeRepairConfigOverrides](#cfn-eks-nodegroup-noderepairconfig-noderepairconfigoverrides): {{
    - NodeRepairConfigOverrides}}
```

## Properties
<a name="aws-properties-eks-nodegroup-noderepairconfig-properties"></a>

`Enabled`  <a name="cfn-eks-nodegroup-noderepairconfig-enabled"></a>
Specifies whether to enable node auto repair for the node group. Node auto repair is disabled by default.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxParallelNodesRepairedCount`  <a name="cfn-eks-nodegroup-noderepairconfig-maxparallelnodesrepairedcount"></a>
Specify the maximum number of nodes that can be repaired concurrently or in parallel, expressed as a count of unhealthy nodes. This gives you finer-grained control over the pace of node replacements. When using this, you cannot also set `maxParallelNodesRepairedPercentage` at the same time.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxParallelNodesRepairedPercentage`  <a name="cfn-eks-nodegroup-noderepairconfig-maxparallelnodesrepairedpercentage"></a>
Specify the maximum number of nodes that can be repaired concurrently or in parallel, expressed as a percentage of unhealthy nodes. This gives you finer-grained control over the pace of node replacements. When using this, you cannot also set `maxParallelNodesRepairedCount` at the same time.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxUnhealthyNodeThresholdCount`  <a name="cfn-eks-nodegroup-noderepairconfig-maxunhealthynodethresholdcount"></a>
Specify a count threshold of unhealthy nodes, above which node auto repair actions will stop. When using this, you cannot also set `maxUnhealthyNodeThresholdPercentage` at the same time.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxUnhealthyNodeThresholdPercentage`  <a name="cfn-eks-nodegroup-noderepairconfig-maxunhealthynodethresholdpercentage"></a>
Specify a percentage threshold of unhealthy nodes, above which node auto repair actions will stop. When using this, you cannot also set `maxUnhealthyNodeThresholdCount` at the same time.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NodeRepairConfigOverrides`  <a name="cfn-eks-nodegroup-noderepairconfig-noderepairconfigoverrides"></a>
Specify granular overrides for specific repair actions. These overrides control the repair action and the repair delay time before a node is considered eligible for repair. If you use this, you must specify all the values.
*Required*: No
*Type*: [Array](aws-properties-eks-nodegroup-noderepairconfigoverrides.md) of [NodeRepairConfigOverrides](aws-properties-eks-nodegroup-noderepairconfigoverrides.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
