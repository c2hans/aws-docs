---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsServiceDetails.html
---

# AwsEcsServiceDetails
<a name="API_AwsEcsServiceDetails"></a>

Provides details about a service within an ECS cluster.

## Contents
<a name="API_AwsEcsServiceDetails_Contents"></a>

 ** CapacityProviderStrategy **   <a name="securityhub-Type-AwsEcsServiceDetails-CapacityProviderStrategy"></a>
The capacity provider strategy that the service uses.
Type: Array of [AwsEcsServiceCapacityProviderStrategyDetails](API_AwsEcsServiceCapacityProviderStrategyDetails.md) objects
Required: No

 ** Cluster **   <a name="securityhub-Type-AwsEcsServiceDetails-Cluster"></a>
The ARN of the cluster that hosts the service.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DeploymentConfiguration **   <a name="securityhub-Type-AwsEcsServiceDetails-DeploymentConfiguration"></a>
Deployment parameters for the service. Includes the number of tasks that run and the order in which to start and stop tasks.
Type: [AwsEcsServiceDeploymentConfigurationDetails](API_AwsEcsServiceDeploymentConfigurationDetails.md) object
Required: No

 ** DeploymentController **   <a name="securityhub-Type-AwsEcsServiceDetails-DeploymentController"></a>
Contains the deployment controller type that the service uses.
Type: [AwsEcsServiceDeploymentControllerDetails](API_AwsEcsServiceDeploymentControllerDetails.md) object
Required: No

 ** DesiredCount **   <a name="securityhub-Type-AwsEcsServiceDetails-DesiredCount"></a>
The number of instantiations of the task definition to run on the service.
Type: Integer
Required: No

 ** EnableEcsManagedTags **   <a name="securityhub-Type-AwsEcsServiceDetails-EnableEcsManagedTags"></a>
Whether to enable Amazon ECS managed tags for the tasks in the service.
Type: Boolean
Required: No

 ** EnableExecuteCommand **   <a name="securityhub-Type-AwsEcsServiceDetails-EnableExecuteCommand"></a>
Whether the execute command functionality is enabled for the service.
Type: Boolean
Required: No

 ** HealthCheckGracePeriodSeconds **   <a name="securityhub-Type-AwsEcsServiceDetails-HealthCheckGracePeriodSeconds"></a>
After a task starts, the amount of time in seconds that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing target health checks.
Type: Integer
Required: No

 ** LaunchType **   <a name="securityhub-Type-AwsEcsServiceDetails-LaunchType"></a>
The launch type that the service uses.
Valid values: `EC2` \| `FARGATE` \| `EXTERNAL`
Type: String
Pattern: `.*\S.*`
Required: No

 ** LoadBalancers **   <a name="securityhub-Type-AwsEcsServiceDetails-LoadBalancers"></a>
Information about the load balancers that the service uses.
Type: Array of [AwsEcsServiceLoadBalancersDetails](API_AwsEcsServiceLoadBalancersDetails.md) objects
Required: No

 ** Name **   <a name="securityhub-Type-AwsEcsServiceDetails-Name"></a>
The name of the service.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NetworkConfiguration **   <a name="securityhub-Type-AwsEcsServiceDetails-NetworkConfiguration"></a>
For tasks that use the `awsvpc` networking mode, the VPC subnet and security group configuration.
Type: [AwsEcsServiceNetworkConfigurationDetails](API_AwsEcsServiceNetworkConfigurationDetails.md) object
Required: No

 ** PlacementConstraints **   <a name="securityhub-Type-AwsEcsServiceDetails-PlacementConstraints"></a>
The placement constraints for the tasks in the service.
Type: Array of [AwsEcsServicePlacementConstraintsDetails](API_AwsEcsServicePlacementConstraintsDetails.md) objects
Required: No

 ** PlacementStrategies **   <a name="securityhub-Type-AwsEcsServiceDetails-PlacementStrategies"></a>
Information about how tasks for the service are placed.
Type: Array of [AwsEcsServicePlacementStrategiesDetails](API_AwsEcsServicePlacementStrategiesDetails.md) objects
Required: No

 ** PlatformVersion **   <a name="securityhub-Type-AwsEcsServiceDetails-PlatformVersion"></a>
The platform version on which to run the service. Only specified for tasks that are hosted on AWS Fargate. If a platform version is not specified, the `LATEST` platform version is used by default.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PropagateTags **   <a name="securityhub-Type-AwsEcsServiceDetails-PropagateTags"></a>
Indicates whether to propagate the tags from the task definition to the task or from the service to the task. If no value is provided, then tags are not propagated.
Valid values: `TASK_DEFINITION` \| `SERVICE`
Type: String
Pattern: `.*\S.*`
Required: No

 ** Role **   <a name="securityhub-Type-AwsEcsServiceDetails-Role"></a>
The ARN of the IAM role that is associated with the service. The role allows the Amazon ECS container agent to register container instances with an Elastic Load Balancing load balancer.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SchedulingStrategy **   <a name="securityhub-Type-AwsEcsServiceDetails-SchedulingStrategy"></a>
The scheduling strategy to use for the service.
The `REPLICA` scheduling strategy places and maintains the desired number of tasks across the cluster. By default, the service scheduler spreads tasks across Availability Zones. Task placement strategies and constraints are used to customize task placement decisions.
The `DAEMON` scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that are specified in the cluster. The service scheduler also evaluates the task placement constraints for running tasks and stops tasks that don't meet the placement constraints.
Valid values: `REPLICA` \| `DAEMON`
Type: String
Pattern: `.*\S.*`
Required: No

 ** ServiceArn **   <a name="securityhub-Type-AwsEcsServiceDetails-ServiceArn"></a>
The ARN of the service.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ServiceName **   <a name="securityhub-Type-AwsEcsServiceDetails-ServiceName"></a>
The name of the service.
The name can contain up to 255 characters. It can use letters, numbers, underscores, and hyphens.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ServiceRegistries **   <a name="securityhub-Type-AwsEcsServiceDetails-ServiceRegistries"></a>
Information about the service discovery registries to assign to the service.
Type: Array of [AwsEcsServiceServiceRegistriesDetails](API_AwsEcsServiceServiceRegistriesDetails.md) objects
Required: No

 ** TaskDefinition **   <a name="securityhub-Type-AwsEcsServiceDetails-TaskDefinition"></a>
The task definition to use for tasks in the service.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsServiceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsServiceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsServiceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsServiceDetails)
