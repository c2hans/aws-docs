---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ManagedInstancesProvider.html
---

# ManagedInstancesProvider
<a name="API_ManagedInstancesProvider"></a>

The configuration for a Amazon ECS Managed Instances provider. Amazon ECS uses this configuration to automatically launch, manage, and terminate Amazon EC2 instances on your behalf. Managed instances provide access to the full range of Amazon EC2 instance types and features while offloading infrastructure management to AWS.

## Contents
<a name="API_ManagedInstancesProvider_Contents"></a>

 ** autoRepairConfiguration **   <a name="ECS-Type-ManagedInstancesProvider-autoRepairConfiguration"></a>
The auto repair configuration for the Amazon ECS Managed Instances capacity provider. Indicates whether Amazon ECS automatically replaces container instances that are detected as unhealthy.
Type: [AutoRepairConfiguration](API_AutoRepairConfiguration.md) object
Required: No

 ** infrastructureOptimization **   <a name="ECS-Type-ManagedInstancesProvider-infrastructureOptimization"></a>
Defines how Amazon ECS Managed Instances optimizes the infrastastructure in your capacity provider. Configure it to turn on or off the infrastructure optimization in your capacity provider, and to control the idle or underutilized EC2 instances optimization delay.
Type: [InfrastructureOptimization](API_InfrastructureOptimization.md) object
Required: No

 ** infrastructureRoleArn **   <a name="ECS-Type-ManagedInstancesProvider-infrastructureRoleArn"></a>
The Amazon Resource Name (ARN) of the infrastructure role that Amazon ECS assumes to manage instances. This role must include permissions for Amazon EC2 instance lifecycle management, networking, and any additional AWS services required for your workloads.
For more information, see [Amazon ECS infrastructure IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/infrastructure_IAM_role.html) in the *Amazon ECS Developer Guide*.
Type: String
Required: No

 ** instanceLaunchTemplate **   <a name="ECS-Type-ManagedInstancesProvider-instanceLaunchTemplate"></a>
The launch template that defines how Amazon ECS launches Amazon ECS Managed Instances. This includes the instance profile for your tasks, network and storage configuration, and instance requirements that determine which Amazon EC2 instance types can be used.
For more information, see [Store instance launch parameters in Amazon EC2 launch templates](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) in the *Amazon EC2 User Guide*.
Type: [InstanceLaunchTemplate](API_InstanceLaunchTemplate.md) object
Required: No

 ** propagateTags **   <a name="ECS-Type-ManagedInstancesProvider-propagateTags"></a>
Determines whether tags from the capacity provider are automatically applied to Amazon ECS Managed Instances. This helps with cost allocation and resource management by ensuring consistent tagging across your infrastructure.
Type: String
Valid Values: `CAPACITY_PROVIDER | NONE`
Required: No

## See Also
<a name="API_ManagedInstancesProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ManagedInstancesProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ManagedInstancesProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ManagedInstancesProvider)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
