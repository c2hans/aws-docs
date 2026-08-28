---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Deployment.html
---

# Deployment
<a name="API_Deployment"></a>

The details of an Amazon ECS service deployment. This is used only when a service uses the `ECS` deployment controller type.

## Contents
<a name="API_Deployment_Contents"></a>

 ** capacityProviderStrategy **   <a name="ECS-Type-Deployment-capacityProviderStrategy"></a>
The capacity provider strategy that the deployment is using.
Type: Array of [CapacityProviderStrategyItem](API_CapacityProviderStrategyItem.md) objects
Required: No

 ** createdAt **   <a name="ECS-Type-Deployment-createdAt"></a>
The Unix timestamp for the time when the service deployment was created.
Type: Timestamp
Required: No

 ** desiredCount **   <a name="ECS-Type-Deployment-desiredCount"></a>
The most recent desired count of tasks that was specified for the service to deploy or maintain.
Type: Integer
Required: No

 ** failedTasks **   <a name="ECS-Type-Deployment-failedTasks"></a>
The number of consecutively failed tasks in the deployment. A task is considered a failure if the service scheduler can't launch the task, the task doesn't transition to a `RUNNING` state, or if it fails any of its defined health checks and is stopped.
Once a service deployment has one or more successfully running tasks, the failed task count resets to zero and stops being evaluated.
Type: Integer
Required: No

 ** fargateEphemeralStorage **   <a name="ECS-Type-Deployment-fargateEphemeralStorage"></a>
The Fargate ephemeral storage settings for the deployment.
Type: [DeploymentEphemeralStorage](API_DeploymentEphemeralStorage.md) object
Required: No

 ** id **   <a name="ECS-Type-Deployment-id"></a>
The ID of the deployment.
Type: String
Required: No

 ** launchType **   <a name="ECS-Type-Deployment-launchType"></a>
The launch type the tasks in the service are using. For more information, see [Amazon ECS Launch Types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: String
Valid Values: `EC2 | FARGATE | EXTERNAL | MANAGED_INSTANCES`
Required: No

 ** networkConfiguration **   <a name="ECS-Type-Deployment-networkConfiguration"></a>
The VPC subnet and security group configuration for tasks that receive their own elastic network interface by using the `awsvpc` networking mode.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object
Required: No

 ** pendingCount **   <a name="ECS-Type-Deployment-pendingCount"></a>
The number of tasks in the deployment that are in the `PENDING` status.
Type: Integer
Required: No

 ** platformFamily **   <a name="ECS-Type-Deployment-platformFamily"></a>
The operating system that your tasks in the service, or tasks are running on. A platform family is specified only for tasks using the Fargate launch type.
 All tasks that run as part of this service must use the same `platformFamily` value as the service, for example, ` LINUX.`.
Type: String
Required: No

 ** platformVersion **   <a name="ECS-Type-Deployment-platformVersion"></a>
The platform version that your tasks in the service run on. A platform version is only specified for tasks using the Fargate launch type. If one isn't specified, the `LATEST` platform version is used. For more information, see [AWS Fargate Platform Versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: String
Required: No

 ** rolloutState **   <a name="ECS-Type-Deployment-rolloutState"></a>
The `rolloutState` of a service is only returned for services that use the rolling update (`ECS`) deployment type that aren't behind a Classic Load Balancer.
The rollout state of the deployment. When a service deployment is started, it begins in an `IN_PROGRESS` state. When the service reaches a steady state, the deployment transitions to a `COMPLETED` state. If the service fails to reach a steady state and circuit breaker is turned on, the deployment transitions to a `FAILED` state. A deployment in `FAILED` state doesn't launch any new tasks. For more information, see [DeploymentCircuitBreaker](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeploymentCircuitBreaker.html).
Type: String
Valid Values: `COMPLETED | FAILED | IN_PROGRESS`
Required: No

 ** rolloutStateReason **   <a name="ECS-Type-Deployment-rolloutStateReason"></a>
A description of the rollout state of a deployment.
Type: String
Required: No

 ** runningCount **   <a name="ECS-Type-Deployment-runningCount"></a>
The number of tasks in the deployment that are in the `RUNNING` status.
Type: Integer
Required: No

 ** serviceConnectConfiguration **   <a name="ECS-Type-Deployment-serviceConnectConfiguration"></a>
The details of the Service Connect configuration that's used by this deployment. Compare the configuration between multiple deployments when troubleshooting issues with new deployments.
The configuration for this service to discover and connect to services, and be discovered by, and connected from, other services within a namespace.
Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see [Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: [ServiceConnectConfiguration](API_ServiceConnectConfiguration.md) object
Required: No

 ** serviceConnectResources **   <a name="ECS-Type-Deployment-serviceConnectResources"></a>
The list of Service Connect resources that are associated with this deployment. Each list entry maps a discovery name to a AWS Cloud Map service name.
Type: Array of [ServiceConnectServiceResource](API_ServiceConnectServiceResource.md) objects
Required: No

 ** status **   <a name="ECS-Type-Deployment-status"></a>
The status of the deployment. The following describes each state.
PRIMARY
The most recent deployment of a service.
ACTIVE
A service deployment that still has running tasks, but are in the process of being replaced with a new `PRIMARY` deployment.
INACTIVE
A deployment that has been completely replaced.
Type: String
Required: No

 ** taskDefinition **   <a name="ECS-Type-Deployment-taskDefinition"></a>
The most recent task definition that was specified for the tasks in the service to use.
Type: String
Required: No

 ** updatedAt **   <a name="ECS-Type-Deployment-updatedAt"></a>
The Unix timestamp for the time when the service deployment was last updated.
Type: Timestamp
Required: No

 ** volumeConfigurations **   <a name="ECS-Type-Deployment-volumeConfigurations"></a>
The details of the volume that was `configuredAtLaunch`. You can configure different settings like the size, throughput, volumeType, and ecryption in [ServiceManagedEBSVolumeConfiguration](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceManagedEBSVolumeConfiguration.html). The `name` of the volume must match the `name` from the task definition.
Type: Array of [ServiceVolumeConfiguration](API_ServiceVolumeConfiguration.md) objects
Required: No

 ** vpcLatticeConfigurations **   <a name="ECS-Type-Deployment-vpcLatticeConfigurations"></a>
The VPC Lattice configuration for the service deployment.
Type: Array of [VpcLatticeConfiguration](API_VpcLatticeConfiguration.md) objects
Required: No

## See Also
<a name="API_Deployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/Deployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/Deployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/Deployment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
