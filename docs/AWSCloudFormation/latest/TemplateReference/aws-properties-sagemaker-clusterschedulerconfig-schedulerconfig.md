---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-clusterschedulerconfig-schedulerconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ClusterSchedulerConfig SchedulerConfig
<a name="aws-properties-sagemaker-clusterschedulerconfig-schedulerconfig"></a>

Cluster policy configuration. This policy is used for task prioritization and fair-share allocation. This helps prioritize critical workloads and distributes idle compute across entities.

## Syntax
<a name="aws-properties-sagemaker-clusterschedulerconfig-schedulerconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-clusterschedulerconfig-schedulerconfig-syntax.json"></a>

```
{
  "[FairShare](#cfn-sagemaker-clusterschedulerconfig-schedulerconfig-fairshare)" : {{String}},
  "[IdleResourceSharing](#cfn-sagemaker-clusterschedulerconfig-schedulerconfig-idleresourcesharing)" : {{String}},
  "[PriorityClasses](#cfn-sagemaker-clusterschedulerconfig-schedulerconfig-priorityclasses)" : {{[ PriorityClass, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-clusterschedulerconfig-schedulerconfig-syntax.yaml"></a>

```
  [FairShare](#cfn-sagemaker-clusterschedulerconfig-schedulerconfig-fairshare): {{String}}
  [IdleResourceSharing](#cfn-sagemaker-clusterschedulerconfig-schedulerconfig-idleresourcesharing): {{String}}
  [PriorityClasses](#cfn-sagemaker-clusterschedulerconfig-schedulerconfig-priorityclasses): {{
    - PriorityClass}}
```

## Properties
<a name="aws-properties-sagemaker-clusterschedulerconfig-schedulerconfig-properties"></a>

`FairShare`  <a name="cfn-sagemaker-clusterschedulerconfig-schedulerconfig-fairshare"></a>
When enabled, entities borrow idle compute based on their assigned `FairShareWeight`.
When disabled, entities borrow idle compute based on a first-come first-serve basis.
Default is `Enabled`.
*Required*: No
*Type*: String
*Allowed values*: `Enabled | Disabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdleResourceSharing`  <a name="cfn-sagemaker-clusterschedulerconfig-schedulerconfig-idleresourcesharing"></a>
Configuration for sharing idle compute resources across entities in the cluster. When enabled, unallocated resources are automatically calculated and made available for entities to borrow.
*Required*: No
*Type*: String
*Allowed values*: `Enabled | Disabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PriorityClasses`  <a name="cfn-sagemaker-clusterschedulerconfig-schedulerconfig-priorityclasses"></a>
List of the priority classes, `PriorityClass`, of the cluster policy. When specified, these class configurations define how tasks are queued.
*Required*: No
*Type*: Array of [PriorityClass](aws-properties-sagemaker-clusterschedulerconfig-priorityclass.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
