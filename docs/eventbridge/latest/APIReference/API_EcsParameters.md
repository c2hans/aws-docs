---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_EcsParameters.html
---

# EcsParameters
<a name="API_EcsParameters"></a>

The custom parameters to be used when the target is an Amazon ECS task.

## Contents
<a name="API_EcsParameters_Contents"></a>

 ** TaskDefinitionArn **   <a name="eventbridge-Type-EcsParameters-TaskDefinitionArn"></a>
The ARN of the task definition to use if the event target is an Amazon ECS task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: Yes

 ** CapacityProviderStrategy **   <a name="eventbridge-Type-EcsParameters-CapacityProviderStrategy"></a>
The capacity provider strategy to use for the task.
If a `capacityProviderStrategy` is specified, the `launchType` parameter must be omitted. If no `capacityProviderStrategy` or launchType is specified, the `defaultCapacityProviderStrategy` for the cluster is used.
Type: Array of [CapacityProviderStrategyItem](API_CapacityProviderStrategyItem.md) objects
Array Members: Maximum number of 6 items.
Required: No

 ** EnableECSManagedTags **   <a name="eventbridge-Type-EcsParameters-EnableECSManagedTags"></a>
Specifies whether to enable Amazon ECS managed tags for the task. For more information, see [Tagging Your Amazon ECS Resources](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html) in the Amazon Elastic Container Service Developer Guide.
Type: Boolean
Required: No

 ** EnableExecuteCommand **   <a name="eventbridge-Type-EcsParameters-EnableExecuteCommand"></a>
Whether or not to enable the execute command functionality for the containers in this task. If true, this enables execute command functionality on all containers in the task.
Type: Boolean
Required: No

 ** Group **   <a name="eventbridge-Type-EcsParameters-Group"></a>
Specifies an ECS task group for the task. The maximum length is 255 characters.
Type: String
Required: No

 ** LaunchType **   <a name="eventbridge-Type-EcsParameters-LaunchType"></a>
Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. The `FARGATE` value is supported only in the Regions where AWS Fargate with Amazon ECS is supported. For more information, see [AWS Fargate on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS-Fargate.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: String
Valid Values: `EC2 | FARGATE | EXTERNAL`
Required: No

 ** NetworkConfiguration **   <a name="eventbridge-Type-EcsParameters-NetworkConfiguration"></a>
Use this structure if the Amazon ECS task uses the `awsvpc` network mode. This structure specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. This structure is required if `LaunchType` is `FARGATE` because the `awsvpc` mode is required for Fargate tasks.
If you specify `NetworkConfiguration` when the target ECS task does not use the `awsvpc` network mode, the task fails.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object
Required: No

 ** PlacementConstraints **   <a name="eventbridge-Type-EcsParameters-PlacementConstraints"></a>
An array of placement constraint objects to use for the task. You can specify up to 10 constraints per task (including constraints in the task definition and those specified at runtime).
Type: Array of [PlacementConstraint](API_PlacementConstraint.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** PlacementStrategy **   <a name="eventbridge-Type-EcsParameters-PlacementStrategy"></a>
The placement strategy objects to use for the task. You can specify a maximum of five strategy rules per task.
Type: Array of [PlacementStrategy](API_PlacementStrategy.md) objects
Array Members: Maximum number of 5 items.
Required: No

 ** PlatformVersion **   <a name="eventbridge-Type-EcsParameters-PlatformVersion"></a>
Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as `1.1.0`.
This structure is used only if `LaunchType` is `FARGATE`. For more information about valid platform versions, see [AWS Fargate Platform Versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: String
Required: No

 ** PropagateTags **   <a name="eventbridge-Type-EcsParameters-PropagateTags"></a>
Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags are not propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the TagResource API action.
Type: String
Valid Values: `TASK_DEFINITION`
Required: No

 ** ReferenceId **   <a name="eventbridge-Type-EcsParameters-ReferenceId"></a>
The reference ID to use for the task.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** Tags **   <a name="eventbridge-Type-EcsParameters-Tags"></a>
The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. To learn more, see [RunTask](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html#ECS-RunTask-request-tags) in the Amazon ECS API Reference.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** TaskCount **   <a name="eventbridge-Type-EcsParameters-TaskCount"></a>
The number of tasks to create based on `TaskDefinition`. The default is 1.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_EcsParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/EcsParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/EcsParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/EcsParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
