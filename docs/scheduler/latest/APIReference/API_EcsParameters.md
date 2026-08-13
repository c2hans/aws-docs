---
source_url: https://docs.aws.amazon.com/scheduler/latest/APIReference/API_EcsParameters.html
---

# EcsParameters
<a name="API_EcsParameters"></a>

The templated target type for the Amazon ECS [`RunTask`](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html) API operation.

## Contents
<a name="API_EcsParameters_Contents"></a>

 ** TaskDefinitionArn **   <a name="scheduler-Type-EcsParameters-TaskDefinitionArn"></a>
The Amazon Resource Name (ARN) of the task definition to use if the event target is an Amazon ECS task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: Yes

 ** CapacityProviderStrategy **   <a name="scheduler-Type-EcsParameters-CapacityProviderStrategy"></a>
The capacity provider strategy to use for the task.
Type: Array of [CapacityProviderStrategyItem](API_CapacityProviderStrategyItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 6 items.
Required: No

 ** EnableECSManagedTags **   <a name="scheduler-Type-EcsParameters-EnableECSManagedTags"></a>
Specifies whether to enable Amazon ECS managed tags for the task. For more information, see [Tagging Your Amazon ECS Resources](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html) in the *Amazon ECS Developer Guide*.
Type: Boolean
Required: No

 ** EnableExecuteCommand **   <a name="scheduler-Type-EcsParameters-EnableExecuteCommand"></a>
Whether or not to enable the execute command functionality for the containers in this task. If true, this enables execute command functionality on all containers in the task.
Type: Boolean
Required: No

 ** Group **   <a name="scheduler-Type-EcsParameters-Group"></a>
Specifies an ECS task group for the task. The maximum length is 255 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** LaunchType **   <a name="scheduler-Type-EcsParameters-LaunchType"></a>
Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. The `FARGATE` value is supported only in the Regions where Fargate with Amazon ECS is supported. For more information, see [AWS Fargate on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) in the *Amazon ECS Developer Guide*.
Type: String
Valid Values: `EC2 | FARGATE | EXTERNAL`
Required: No

 ** NetworkConfiguration **   <a name="scheduler-Type-EcsParameters-NetworkConfiguration"></a>
This structure specifies the network configuration for an ECS task.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object
Required: No

 ** PlacementConstraints **   <a name="scheduler-Type-EcsParameters-PlacementConstraints"></a>
An array of placement constraint objects to use for the task. You can specify up to 10 constraints per task (including constraints in the task definition and those specified at runtime).
Type: Array of [PlacementConstraint](API_PlacementConstraint.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** PlacementStrategy **   <a name="scheduler-Type-EcsParameters-PlacementStrategy"></a>
The task placement strategy for a task or service.
Type: Array of [PlacementStrategy](API_PlacementStrategy.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** PlatformVersion **   <a name="scheduler-Type-EcsParameters-PlatformVersion"></a>
Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as `1.1.0`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** PropagateTags **   <a name="scheduler-Type-EcsParameters-PropagateTags"></a>
Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags are not propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use Amazon ECS's [`TagResource`](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html) API action.
Type: String
Valid Values: `TASK_DEFINITION`
Required: No

 ** ReferenceId **   <a name="scheduler-Type-EcsParameters-ReferenceId"></a>
The reference ID to use for the task.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** Tags **   <a name="scheduler-Type-EcsParameters-Tags"></a>
The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. For more information, see [`RunTask`](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html) in the *Amazon ECS API Reference*.
Type: Array of string to string maps
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** TaskCount **   <a name="scheduler-Type-EcsParameters-TaskCount"></a>
The number of tasks to create based on `TaskDefinition`. The default is `1`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

## See Also
<a name="API_EcsParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/scheduler-2021-06-30/EcsParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/EcsParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/scheduler-2021-06-30/EcsParameters)
