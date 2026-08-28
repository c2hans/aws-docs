---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TaskOverride.html
---

# TaskOverride
<a name="API_TaskOverride"></a>

The overrides that are associated with a task.

## Contents
<a name="API_TaskOverride_Contents"></a>

 ** containerOverrides **   <a name="ECS-Type-TaskOverride-containerOverrides"></a>
One or more container overrides that are sent to a task.
Type: Array of [ContainerOverride](API_ContainerOverride.md) objects
Required: No

 ** cpu **   <a name="ECS-Type-TaskOverride-cpu"></a>
The CPU override for the task.
Type: String
Required: No

 ** ephemeralStorage **   <a name="ECS-Type-TaskOverride-ephemeralStorage"></a>
The ephemeral storage setting override for the task.
This parameter is only supported for tasks hosted on Fargate that use the following platform versions:
+ Linux platform version `1.4.0` or later.
+ Windows platform version `1.0.0` or later.
Type: [EphemeralStorage](API_EphemeralStorage.md) object
Required: No

 ** executionRoleArn **   <a name="ECS-Type-TaskOverride-executionRoleArn"></a>
The Amazon Resource Name (ARN) of the task execution role override for the task. For more information, see [Amazon ECS task execution IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: String
Required: No

 ** inferenceAcceleratorOverrides **   <a name="ECS-Type-TaskOverride-inferenceAcceleratorOverrides"></a>
 *This member has been deprecated.*
The Elastic Inference accelerator override for the task.
Type: Array of [InferenceAcceleratorOverride](API_InferenceAcceleratorOverride.md) objects
Required: No

 ** memory **   <a name="ECS-Type-TaskOverride-memory"></a>
The memory override for the task.
Type: String
Required: No

 ** taskRoleArn **   <a name="ECS-Type-TaskOverride-taskRoleArn"></a>
The Amazon Resource Name (ARN) of the role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role. For more information, see [IAM Role for Tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: String
Required: No

## See Also
<a name="API_TaskOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/TaskOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/TaskOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/TaskOverride)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
