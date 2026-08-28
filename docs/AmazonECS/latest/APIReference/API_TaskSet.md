---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TaskSet.html
---

# TaskSet
<a name="API_TaskSet"></a>

Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an `EXTERNAL` deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic.

## Contents
<a name="API_TaskSet_Contents"></a>

 ** capacityProviderStrategy **   <a name="ECS-Type-TaskSet-capacityProviderStrategy"></a>
The capacity provider strategy that are associated with the task set.
Type: Array of [CapacityProviderStrategyItem](API_CapacityProviderStrategyItem.md) objects
Required: No

 ** clusterArn **   <a name="ECS-Type-TaskSet-clusterArn"></a>
The Amazon Resource Name (ARN) of the cluster that the service that hosts the task set exists in.
Type: String
Required: No

 ** computedDesiredCount **   <a name="ECS-Type-TaskSet-computedDesiredCount"></a>
The computed desired count for the task set. This is calculated by multiplying the service's `desiredCount` by the task set's `scale` percentage. The result is always rounded up. For example, if the computed desired count is 1.2, it rounds up to 2 tasks.
Type: Integer
Required: No

 ** createdAt **   <a name="ECS-Type-TaskSet-createdAt"></a>
The Unix timestamp for the time when the task set was created.
Type: Timestamp
Required: No

 ** externalId **   <a name="ECS-Type-TaskSet-externalId"></a>
The external ID associated with the task set.
If an AWS CodeDeploy deployment created a task set, the `externalId` parameter contains the AWS CodeDeploy deployment ID.
If a task set is created for an external deployment and is associated with a service discovery registry, the `externalId` parameter contains the `ECS_TASK_SET_EXTERNAL_ID` AWS Cloud Map attribute.
Type: String
Required: No

 ** fargateEphemeralStorage **   <a name="ECS-Type-TaskSet-fargateEphemeralStorage"></a>
The Fargate ephemeral storage settings for the task set.
Type: [DeploymentEphemeralStorage](API_DeploymentEphemeralStorage.md) object
Required: No

 ** id **   <a name="ECS-Type-TaskSet-id"></a>
The ID of the task set.
Type: String
Required: No

 ** launchType **   <a name="ECS-Type-TaskSet-launchType"></a>
The launch type the tasks in the task set are using. For more information, see [Amazon ECS launch types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: String
Valid Values: `EC2 | FARGATE | EXTERNAL | MANAGED_INSTANCES`
Required: No

 ** loadBalancers **   <a name="ECS-Type-TaskSet-loadBalancers"></a>
Details on a load balancer that are used with a task set.
Type: Array of [LoadBalancer](API_LoadBalancer.md) objects
Required: No

 ** networkConfiguration **   <a name="ECS-Type-TaskSet-networkConfiguration"></a>
The network configuration for the task set.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object
Required: No

 ** pendingCount **   <a name="ECS-Type-TaskSet-pendingCount"></a>
The number of tasks in the task set that are in the `PENDING` status during a deployment. A task in the `PENDING` state is preparing to enter the `RUNNING` state. A task set enters the `PENDING` status when it launches for the first time or when it's restarted after being in the `STOPPED` state.
Type: Integer
Required: No

 ** platformFamily **   <a name="ECS-Type-TaskSet-platformFamily"></a>
The operating system that your tasks in the set are running on. A platform family is specified only for tasks that use the Fargate launch type.
 All tasks in the set must have the same value.
Type: String
Required: No

 ** platformVersion **   <a name="ECS-Type-TaskSet-platformVersion"></a>
The AWS Fargate platform version where the tasks in the task set are running. A platform version is only specified for tasks run on AWS Fargate. For more information, see [AWS Fargate platform versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: String
Required: No

 ** runningCount **   <a name="ECS-Type-TaskSet-runningCount"></a>
The number of tasks in the task set that are in the `RUNNING` status during a deployment. A task in the `RUNNING` state is running and ready for use.
Type: Integer
Required: No

 ** scale **   <a name="ECS-Type-TaskSet-scale"></a>
A floating-point percentage of your desired number of tasks to place and keep running in the task set.
Type: [Scale](API_Scale.md) object
Required: No

 ** serviceArn **   <a name="ECS-Type-TaskSet-serviceArn"></a>
The Amazon Resource Name (ARN) of the service the task set exists in.
Type: String
Required: No

 ** serviceRegistries **   <a name="ECS-Type-TaskSet-serviceRegistries"></a>
The details for the service discovery registries to assign to this task set. For more information, see [Service discovery](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html).
Type: Array of [ServiceRegistry](API_ServiceRegistry.md) objects
Required: No

 ** stabilityStatus **   <a name="ECS-Type-TaskSet-stabilityStatus"></a>
The stability status. This indicates whether the task set has reached a steady state. If the following conditions are met, the task set are in `STEADY_STATE`:
+ The task `runningCount` is equal to the `computedDesiredCount`.
+ The `pendingCount` is `0`.
+ There are no tasks that are running on container instances in the `DRAINING` status.
+ All tasks are reporting a healthy status from the load balancers, service discovery, and container health checks.
If any of those conditions aren't met, the stability status returns `STABILIZING`.
Type: String
Valid Values: `STEADY_STATE | STABILIZING`
Required: No

 ** stabilityStatusAt **   <a name="ECS-Type-TaskSet-stabilityStatusAt"></a>
The Unix timestamp for the time when the task set stability status was retrieved.
Type: Timestamp
Required: No

 ** startedBy **   <a name="ECS-Type-TaskSet-startedBy"></a>
The tag specified when a task set is started. If an AWS CodeDeploy deployment created the task set, the `startedBy` parameter is `CODE_DEPLOY`. If an external deployment created the task set, the `startedBy` field isn't used.
Type: String
Required: No

 ** status **   <a name="ECS-Type-TaskSet-status"></a>
The status of the task set. The following describes each state.
PRIMARY
The task set is serving production traffic.
ACTIVE
The task set isn't serving production traffic.
DRAINING
The tasks in the task set are being stopped, and their corresponding targets are being deregistered from their target group.
Type: String
Required: No

 ** tags **   <a name="ECS-Type-TaskSet-tags"></a>
The metadata that you apply to the task set to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.
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

 ** taskDefinition **   <a name="ECS-Type-TaskSet-taskDefinition"></a>
The task definition that the task set is using.
Type: String
Required: No

 ** taskSetArn **   <a name="ECS-Type-TaskSet-taskSetArn"></a>
The Amazon Resource Name (ARN) of the task set.
Type: String
Required: No

 ** updatedAt **   <a name="ECS-Type-TaskSet-updatedAt"></a>
The Unix timestamp for the time when the task set was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_TaskSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/TaskSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/TaskSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/TaskSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
