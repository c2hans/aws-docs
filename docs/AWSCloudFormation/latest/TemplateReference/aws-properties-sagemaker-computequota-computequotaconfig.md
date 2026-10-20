---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-computequota-computequotaconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ComputeQuota ComputeQuotaConfig
<a name="aws-properties-sagemaker-computequota-computequotaconfig"></a>

Configuration of the compute allocation definition for an entity. This includes the resource sharing option and the setting to preempt low priority tasks.

## Syntax
<a name="aws-properties-sagemaker-computequota-computequotaconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-computequota-computequotaconfig-syntax.json"></a>

```
{
  "[ComputeQuotaResources](#cfn-sagemaker-computequota-computequotaconfig-computequotaresources)" : {{[ ComputeQuotaResourceConfig, ... ]}},
  "[PreemptTeamTasks](#cfn-sagemaker-computequota-computequotaconfig-preemptteamtasks)" : {{String}},
  "[ResourceSharingConfig](#cfn-sagemaker-computequota-computequotaconfig-resourcesharingconfig)" : {{ResourceSharingConfig}}
}
```

### YAML
<a name="aws-properties-sagemaker-computequota-computequotaconfig-syntax.yaml"></a>

```
  [ComputeQuotaResources](#cfn-sagemaker-computequota-computequotaconfig-computequotaresources): {{
    - ComputeQuotaResourceConfig}}
  [PreemptTeamTasks](#cfn-sagemaker-computequota-computequotaconfig-preemptteamtasks): {{String}}
  [ResourceSharingConfig](#cfn-sagemaker-computequota-computequotaconfig-resourcesharingconfig): {{
    ResourceSharingConfig}}
```

## Properties
<a name="aws-properties-sagemaker-computequota-computequotaconfig-properties"></a>

`ComputeQuotaResources`  <a name="cfn-sagemaker-computequota-computequotaconfig-computequotaresources"></a>
Allocate compute resources by instance types.
*Required*: No
*Type*: Array of [ComputeQuotaResourceConfig](aws-properties-sagemaker-computequota-computequotaresourceconfig.md)
*Minimum*: `0`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreemptTeamTasks`  <a name="cfn-sagemaker-computequota-computequotaconfig-preemptteamtasks"></a>
Allows workloads from within an entity to preempt same-team workloads. When set to `LowerPriority`, the entity's lower priority tasks are preempted by their own higher priority tasks.
Default is `LowerPriority`.
*Required*: No
*Type*: String
*Allowed values*: `Never | LowerPriority`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceSharingConfig`  <a name="cfn-sagemaker-computequota-computequotaconfig-resourcesharingconfig"></a>
Resource sharing configuration. This defines how an entity can lend and borrow idle compute with other entities within the cluster.
*Required*: No
*Type*: [ResourceSharingConfig](aws-properties-sagemaker-computequota-resourcesharingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
