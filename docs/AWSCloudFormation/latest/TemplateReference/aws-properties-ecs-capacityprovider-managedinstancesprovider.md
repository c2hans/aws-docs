---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-managedinstancesprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::CapacityProvider ManagedInstancesProvider
<a name="aws-properties-ecs-capacityprovider-managedinstancesprovider"></a>

The configuration for a Amazon ECS Managed Instances provider. Amazon ECS uses this configuration to automatically launch, manage, and terminate Amazon EC2 instances on your behalf. Managed instances provide access to the full range of Amazon EC2 instance types and features while offloading infrastructure management to AWS.

## Syntax
<a name="aws-properties-ecs-capacityprovider-managedinstancesprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-capacityprovider-managedinstancesprovider-syntax.json"></a>

```
{
  "[AutoRepairConfiguration](#cfn-ecs-capacityprovider-managedinstancesprovider-autorepairconfiguration)" : {{AutoRepairConfiguration}},
  "[InfrastructureOptimization](#cfn-ecs-capacityprovider-managedinstancesprovider-infrastructureoptimization)" : {{InfrastructureOptimization}},
  "[InfrastructureRoleArn](#cfn-ecs-capacityprovider-managedinstancesprovider-infrastructurerolearn)" : {{String}},
  "[InstanceLaunchTemplate](#cfn-ecs-capacityprovider-managedinstancesprovider-instancelaunchtemplate)" : {{InstanceLaunchTemplate}},
  "[PropagateTags](#cfn-ecs-capacityprovider-managedinstancesprovider-propagatetags)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-capacityprovider-managedinstancesprovider-syntax.yaml"></a>

```
  [AutoRepairConfiguration](#cfn-ecs-capacityprovider-managedinstancesprovider-autorepairconfiguration): {{
    AutoRepairConfiguration}}
  [InfrastructureOptimization](#cfn-ecs-capacityprovider-managedinstancesprovider-infrastructureoptimization): {{
    InfrastructureOptimization}}
  [InfrastructureRoleArn](#cfn-ecs-capacityprovider-managedinstancesprovider-infrastructurerolearn): {{String}}
  [InstanceLaunchTemplate](#cfn-ecs-capacityprovider-managedinstancesprovider-instancelaunchtemplate): {{
    InstanceLaunchTemplate}}
  [PropagateTags](#cfn-ecs-capacityprovider-managedinstancesprovider-propagatetags): {{String}}
```

## Properties
<a name="aws-properties-ecs-capacityprovider-managedinstancesprovider-properties"></a>

`AutoRepairConfiguration`  <a name="cfn-ecs-capacityprovider-managedinstancesprovider-autorepairconfiguration"></a>
The auto repair configuration for the Amazon ECS Managed Instances capacity provider. Indicates whether Amazon ECS automatically replaces container instances that are detected as unhealthy.
*Required*: No
*Type*: [AutoRepairConfiguration](aws-properties-ecs-capacityprovider-autorepairconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InfrastructureOptimization`  <a name="cfn-ecs-capacityprovider-managedinstancesprovider-infrastructureoptimization"></a>
Defines how Amazon ECS Managed Instances optimizes the infrastastructure in your capacity provider. Configure it to turn on or off the infrastructure optimization in your capacity provider, and to control the idle or underutilized EC2 instances optimization delay.
*Required*: No
*Type*: [InfrastructureOptimization](aws-properties-ecs-capacityprovider-infrastructureoptimization.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InfrastructureRoleArn`  <a name="cfn-ecs-capacityprovider-managedinstancesprovider-infrastructurerolearn"></a>
The Amazon Resource Name (ARN) of the infrastructure role that Amazon ECS assumes to manage instances. This role must include permissions for Amazon EC2 instance lifecycle management, networking, and any additional AWS services required for your workloads.
For more information, see [Amazon ECS infrastructure IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/infrastructure_IAM_role.html) in the *Amazon ECS Developer Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceLaunchTemplate`  <a name="cfn-ecs-capacityprovider-managedinstancesprovider-instancelaunchtemplate"></a>
The launch template that defines how Amazon ECS launches Amazon ECS Managed Instances. This includes the instance profile for your tasks, network and storage configuration, and instance requirements that determine which Amazon EC2 instance types can be used.
For more information, see [Store instance launch parameters in Amazon EC2 launch templates](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) in the *Amazon EC2 User Guide*.
*Required*: Yes
*Type*: [InstanceLaunchTemplate](aws-properties-ecs-capacityprovider-instancelaunchtemplate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropagateTags`  <a name="cfn-ecs-capacityprovider-managedinstancesprovider-propagatetags"></a>
Determines whether tags from the capacity provider are automatically applied to Amazon ECS Managed Instances. This helps with cost allocation and resource management by ensuring consistent tagging across your infrastructure.
*Required*: No
*Type*: String
*Allowed values*: `CAPACITY_PROVIDER | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
