---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-nodegroup-noderepairconfigoverrides.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Nodegroup NodeRepairConfigOverrides
<a name="aws-properties-eks-nodegroup-noderepairconfigoverrides"></a>

Specify granular overrides for specific repair actions. These overrides control the repair action and the repair delay time before a node is considered eligible for repair. If you use this, you must specify all the values.

## Syntax
<a name="aws-properties-eks-nodegroup-noderepairconfigoverrides-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-nodegroup-noderepairconfigoverrides-syntax.json"></a>

```
{
  "[MinRepairWaitTimeMins](#cfn-eks-nodegroup-noderepairconfigoverrides-minrepairwaittimemins)" : {{Integer}},
  "[NodeMonitoringCondition](#cfn-eks-nodegroup-noderepairconfigoverrides-nodemonitoringcondition)" : {{String}},
  "[NodeUnhealthyReason](#cfn-eks-nodegroup-noderepairconfigoverrides-nodeunhealthyreason)" : {{String}},
  "[RepairAction](#cfn-eks-nodegroup-noderepairconfigoverrides-repairaction)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-nodegroup-noderepairconfigoverrides-syntax.yaml"></a>

```
  [MinRepairWaitTimeMins](#cfn-eks-nodegroup-noderepairconfigoverrides-minrepairwaittimemins): {{Integer}}
  [NodeMonitoringCondition](#cfn-eks-nodegroup-noderepairconfigoverrides-nodemonitoringcondition): {{String}}
  [NodeUnhealthyReason](#cfn-eks-nodegroup-noderepairconfigoverrides-nodeunhealthyreason): {{String}}
  [RepairAction](#cfn-eks-nodegroup-noderepairconfigoverrides-repairaction): {{String}}
```

## Properties
<a name="aws-properties-eks-nodegroup-noderepairconfigoverrides-properties"></a>

`MinRepairWaitTimeMins`  <a name="cfn-eks-nodegroup-noderepairconfigoverrides-minrepairwaittimemins"></a>
Specify the minimum time in minutes to wait before attempting to repair a node with this specific `nodeMonitoringCondition` and `nodeUnhealthyReason`.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NodeMonitoringCondition`  <a name="cfn-eks-nodegroup-noderepairconfigoverrides-nodemonitoringcondition"></a>
Specify an unhealthy condition reported by the node monitoring agent that this override would apply to.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NodeUnhealthyReason`  <a name="cfn-eks-nodegroup-noderepairconfigoverrides-nodeunhealthyreason"></a>
Specify a reason reported by the node monitoring agent that this override would apply to.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RepairAction`  <a name="cfn-eks-nodegroup-noderepairconfigoverrides-repairaction"></a>
Specify the repair action to take for nodes when all of the specified conditions are met.
*Required*: No
*Type*: String
*Allowed values*: `Replace | Reboot | NoAction`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
