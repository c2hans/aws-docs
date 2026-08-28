---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Service.html
---

# Service
<a name="API_Service"></a>

Details on a service within a cluster.

## Contents
<a name="API_Service_Contents"></a>

 ** availabilityZoneRebalancing **   <a name="ECS-Type-Service-availabilityZoneRebalancing"></a>
Indicates whether to use Availability Zone rebalancing for the service.
For more information, see [Balancing an Amazon ECS service across Availability Zones](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-rebalancing.html) in the * *Amazon Elastic Container Service Developer Guide* *.
The default behavior of `AvailabilityZoneRebalancing` differs between create and update requests:
+ For create service requests, when no value is specified for `AvailabilityZoneRebalancing`, Amazon ECS defaults the value to `ENABLED`.
+ For update service requests, when no value is specified for `AvailabilityZoneRebalancing`, Amazon ECS defaults to the existing service’s `AvailabilityZoneRebalancing` value. If the service never had an `AvailabilityZoneRebalancing` value set, Amazon ECS treats this as `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** capacityProviderStrategy **   <a name="ECS-Type-Service-capacityProviderStrategy"></a>
The capacity provider strategy the service uses. When using the DescribeServices API, this field is omitted if the service was created using a launch type.
Type: Array of [CapacityProviderStrategyItem](API_CapacityProviderStrategyItem.md) objects
Required: No

 ** clusterArn **   <a name="ECS-Type-Service-clusterArn"></a>
The Amazon Resource Name (ARN) of the cluster that hosts the service.
Type: String
Required: No

 ** createdAt **   <a name="ECS-Type-Service-createdAt"></a>
The Unix timestamp for the time when the service was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="ECS-Type-Service-createdBy"></a>
The principal that created the service.
Type: String
Required: No

 ** currentServiceDeployment **   <a name="ECS-Type-Service-currentServiceDeployment"></a>
The ARN of the current service deployment.
Type: String
Required: No

 ** currentServiceRevisions **   <a name="ECS-Type-Service-currentServiceRevisions"></a>
The list of the service revisions.
Type: Array of [ServiceCurrentRevisionSummary](API_ServiceCurrentRevisionSummary.md) objects
Required: No

 ** deploymentConfiguration **   <a name="ECS-Type-Service-deploymentConfiguration"></a>
Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.
Type: [DeploymentConfiguration](API_DeploymentConfiguration.md) object
Required: No

 ** deploymentController **   <a name="ECS-Type-Service-deploymentController"></a>
The deployment controller type the service is using.
Type: [DeploymentController](API_DeploymentController.md) object
Required: No

 ** deployments **   <a name="ECS-Type-Service-deployments"></a>
The current state of deployments for the service.
Type: Array of [Deployment](API_Deployment.md) objects
Required: No

 ** desiredCount **   <a name="ECS-Type-Service-desiredCount"></a>
The desired number of instantiations of the task definition to keep running on the service. This value is specified when the service is created with [CreateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html) , and it can be modified with [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html).
Type: Integer
Required: No

 ** enableECSManagedTags **   <a name="ECS-Type-Service-enableECSManagedTags"></a>
Determines whether to use Amazon ECS managed tags for the tasks in the service. For more information, see [Tagging Your Amazon ECS Resources](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: Boolean
Required: No

 ** enableExecuteCommand **   <a name="ECS-Type-Service-enableExecuteCommand"></a>
Determines whether the execute command functionality is turned on for the service. If `true`, the execute command functionality is turned on for all containers in tasks as part of the service.
Type: Boolean
Required: No

 ** events **   <a name="ECS-Type-Service-events"></a>
The event stream for your service. A maximum of 100 of the latest events are displayed.
Type: Array of [ServiceEvent](API_ServiceEvent.md) objects
Required: No

 ** healthCheckGracePeriodSeconds **   <a name="ECS-Type-Service-healthCheckGracePeriodSeconds"></a>
The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing, VPC Lattice, and container health checks after a task has first started.
If your service has more running tasks than desired, unhealthy tasks in the grace period might be stopped to reach the desired count.
Type: Integer
Required: No

 ** launchType **   <a name="ECS-Type-Service-launchType"></a>
The launch type the service is using. When using the DescribeServices API, this field is omitted if the service was created using a capacity provider strategy.
Type: String
Valid Values: `EC2 | FARGATE | EXTERNAL | MANAGED_INSTANCES`
Required: No

 ** loadBalancers **   <a name="ECS-Type-Service-loadBalancers"></a>
A list of Elastic Load Balancing load balancer objects. It contains the load balancer name, the container name, and the container port to access from the load balancer. The container name is as it appears in a container definition.
Type: Array of [LoadBalancer](API_LoadBalancer.md) objects
Required: No

 ** networkConfiguration **   <a name="ECS-Type-Service-networkConfiguration"></a>
The VPC subnet and security group configuration for tasks that receive their own elastic network interface by using the `awsvpc` networking mode.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object
Required: No

 ** pendingCount **   <a name="ECS-Type-Service-pendingCount"></a>
The number of tasks in the cluster that are in the `PENDING` state.
Type: Integer
Required: No

 ** placementConstraints **   <a name="ECS-Type-Service-placementConstraints"></a>
The placement constraints for the tasks in the service.
Type: Array of [PlacementConstraint](API_PlacementConstraint.md) objects
Required: No

 ** placementStrategy **   <a name="ECS-Type-Service-placementStrategy"></a>
The placement strategy that determines how tasks for the service are placed.
Type: Array of [PlacementStrategy](API_PlacementStrategy.md) objects
Required: No

 ** platformFamily **   <a name="ECS-Type-Service-platformFamily"></a>
The operating system that your tasks in the service run on. A platform family is specified only for tasks using the Fargate launch type.
 All tasks that run as part of this service must use the same `platformFamily` value as the service (for example, `LINUX`).
Type: String
Required: No

 ** platformVersion **   <a name="ECS-Type-Service-platformVersion"></a>
The platform version to run your service on. A platform version is only specified for tasks that are hosted on AWS Fargate. If one isn't specified, the `LATEST` platform version is used. For more information, see [AWS Fargate Platform Versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: String
Required: No

 ** propagateTags **   <a name="ECS-Type-Service-propagateTags"></a>
Determines whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags aren't propagated.
Type: String
Valid Values: `TASK_DEFINITION | SERVICE | NONE`
Required: No

 ** resourceManagementType **   <a name="ECS-Type-Service-resourceManagementType"></a>
Identifies whether an ECS Service is an Express Service managed by ECS, or managed by the customer. The valid values are `ECS` and `CUSTOMER`
Type: String
Valid Values: `CUSTOMER | ECS`
Required: No

 ** roleArn **   <a name="ECS-Type-Service-roleArn"></a>
The ARN of the IAM role that's associated with the service. It allows the Amazon ECS container agent to register container instances with an Elastic Load Balancing load balancer.
Type: String
Required: No

 ** runningCount **   <a name="ECS-Type-Service-runningCount"></a>
The number of tasks in the cluster that are in the `RUNNING` state.
Type: Integer
Required: No

 ** schedulingStrategy **   <a name="ECS-Type-Service-schedulingStrategy"></a>
The scheduling strategy to use for the service. For more information, see [Services](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html).
There are two service scheduler strategies available.
+  `REPLICA`-The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions.
+  `DAEMON`-The daemon scheduling strategy deploys exactly one task on each active container instance. This task meets all of the task placement constraints that you specify in your cluster. The service scheduler also evaluates the task placement constraints for running tasks. It stop tasks that don't meet the placement constraints.
**Note**
Fargate tasks don't support the `DAEMON` scheduling strategy.
Type: String
Valid Values: `REPLICA | DAEMON`
Required: No

 ** serviceArn **   <a name="ECS-Type-Service-serviceArn"></a>
The ARN that identifies the service. For more information about the ARN format, see [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids) in the *Amazon ECS Developer Guide*.
Type: String
Required: No

 ** serviceName **   <a name="ECS-Type-Service-serviceName"></a>
The name of your service. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed. Service names must be unique within a cluster. However, you can have similarly named services in multiple clusters within a Region or across multiple Regions.
Type: String
Required: No

 ** serviceRegistries **   <a name="ECS-Type-Service-serviceRegistries"></a>
The details for the service discovery registries to assign to this service. For more information, see [Service Discovery](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html).
Type: Array of [ServiceRegistry](API_ServiceRegistry.md) objects
Required: No

 ** status **   <a name="ECS-Type-Service-status"></a>
The status of the service. The valid values are `ACTIVE`, `DRAINING`, or `INACTIVE`.
Type: String
Required: No

 ** tags **   <a name="ECS-Type-Service-tags"></a>
The metadata that you apply to the service to help you categorize and organize them. Each tag consists of a key and an optional value. You define bot the key and value.
The following basic restrictions apply to tags:
+ Maximum number of tags per resource - 50
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length - 128 Unicode characters in UTF-8
+ Maximum value length - 256 Unicode characters in UTF-8
+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case-sensitive.
+ Do not use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** taskDefinition **   <a name="ECS-Type-Service-taskDefinition"></a>
The task definition to use for tasks in the service. This value is specified when the service is created with [CreateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html), and it can be modified with [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html).
Type: String
Required: No

 ** taskSets **   <a name="ECS-Type-Service-taskSets"></a>
Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an `EXTERNAL` deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic.
Type: Array of [TaskSet](API_TaskSet.md) objects
Required: No

## See Also
<a name="API_Service_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/Service)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/Service)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/Service)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
