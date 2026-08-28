---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-computeenvironment-managedinstancesprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::ComputeEnvironment ManagedInstancesProvider
<a name="aws-properties-batch-computeenvironment-managedinstancesprovider"></a>

The configuration for an Amazon ECS Managed Instances capacity provider. This object is required when creating a compute environment with `computeResources.type` set to `ECS_MANAGED_INSTANCES`.

## Syntax
<a name="aws-properties-batch-computeenvironment-managedinstancesprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-computeenvironment-managedinstancesprovider-syntax.json"></a>

```
{
  "[InfrastructureOptimization](#cfn-batch-computeenvironment-managedinstancesprovider-infrastructureoptimization)" : {{InfrastructureOptimization}},
  "[InfrastructureRoleArn](#cfn-batch-computeenvironment-managedinstancesprovider-infrastructurerolearn)" : {{String}},
  "[InstanceLaunchTemplate](#cfn-batch-computeenvironment-managedinstancesprovider-instancelaunchtemplate)" : {{InstanceLaunchTemplate}},
  "[PropagateTags](#cfn-batch-computeenvironment-managedinstancesprovider-propagatetags)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-computeenvironment-managedinstancesprovider-syntax.yaml"></a>

```
  [InfrastructureOptimization](#cfn-batch-computeenvironment-managedinstancesprovider-infrastructureoptimization): {{
    InfrastructureOptimization}}
  [InfrastructureRoleArn](#cfn-batch-computeenvironment-managedinstancesprovider-infrastructurerolearn): {{String}}
  [InstanceLaunchTemplate](#cfn-batch-computeenvironment-managedinstancesprovider-instancelaunchtemplate): {{
    InstanceLaunchTemplate}}
  [PropagateTags](#cfn-batch-computeenvironment-managedinstancesprovider-propagatetags): {{String}}
```

## Properties
<a name="aws-properties-batch-computeenvironment-managedinstancesprovider-properties"></a>

`InfrastructureOptimization`  <a name="cfn-batch-computeenvironment-managedinstancesprovider-infrastructureoptimization"></a>
The infrastructure optimization configuration for the capacity provider. Specifies the idle-instance scale-in behavior.
*Required*: No
*Type*: [InfrastructureOptimization](aws-properties-batch-computeenvironment-infrastructureoptimization.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InfrastructureRoleArn`  <a name="cfn-batch-computeenvironment-managedinstancesprovider-infrastructurerolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that Amazon ECS assumes to manage Amazon EC2 instances on your behalf. This role must have a trust policy for `ecs.amazonaws.com`. You must have the `iam:PassRole` permission for this role with the condition `iam:PassedToService: ecs.amazonaws.com`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceLaunchTemplate`  <a name="cfn-batch-computeenvironment-managedinstancesprovider-instancelaunchtemplate"></a>
The instance launch configuration for the Amazon ECS Managed Instances capacity provider. Contains networking, instance profile, instance requirements, capacity type, storage, and monitoring configuration.
*Required*: Yes
*Type*: [InstanceLaunchTemplate](aws-properties-batch-computeenvironment-instancelaunchtemplate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropagateTags`  <a name="cfn-batch-computeenvironment-managedinstancesprovider-propagatetags"></a>
Specifies whether tags on the capacity provider are propagated to the Amazon EC2 instances it launches. Valid values:
+ `CAPACITY_PROVIDER` — Propagates tags to instances.
+ `NONE` (default) — Does not propagate tags to instances.
*Required*: No
*Type*: String
*Allowed values*: `CAPACITY_PROVIDER | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
