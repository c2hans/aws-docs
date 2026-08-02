---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Task.html
---

# Task
<a name="API_Task"></a>

Details on a task in a cluster.

## Contents
<a name="API_Task_Contents"></a>

 ** attachments **   <a name="ECS-Type-Task-attachments"></a>
The Elastic Network Adapter that's associated with the task if the task uses the `awsvpc` network mode.
Type: Array of [Attachment](API_Attachment.md) objects
Required: No

 ** attributes **   <a name="ECS-Type-Task-attributes"></a>
The attributes of the task
Type: Array of [Attribute](API_Attribute.md) objects
Required: No

 ** availabilityZone **   <a name="ECS-Type-Task-availabilityZone"></a>
The Availability Zone for the task.
Type: String
Required: No

 ** capacityProviderName **   <a name="ECS-Type-Task-capacityProviderName"></a>
The capacity provider that's associated with the task.
Type: String
Required: No

 ** clusterArn **   <a name="ECS-Type-Task-clusterArn"></a>
The ARN of the cluster that hosts the task.
Type: String
Required: No

 ** connectivity **   <a name="ECS-Type-Task-connectivity"></a>
The connectivity status of a task.
Type: String
Valid Values: `CONNECTED | DISCONNECTED`
Required: No

 ** connectivityAt **   <a name="ECS-Type-Task-connectivityAt"></a>
The Unix timestamp for the time when the task last went into `CONNECTED` status.
Type: Timestamp
Required: No

 ** containerInstanceArn **   <a name="ECS-Type-Task-containerInstanceArn"></a>
The ARN of the container instances that host the task.
Type: String
Required: No

 ** containers **   <a name="ECS-Type-Task-containers"></a>
The containers that's associated with the task.
Type: Array of [Container](API_Container.md) objects
Required: No

 ** cpu **   <a name="ECS-Type-Task-cpu"></a>
The number of CPU units used by the task as expressed in a task definition. It can be expressed as an integer using CPU units (for example, `1024`). It can also be expressed as a string using vCPUs (for example, `1 vCPU` or `1 vcpu`). String values are converted to an integer that indicates the CPU units when the task definition is registered.
If you're using the EC2 launch type or the external launch type, this field is optional. Supported values are between `128` CPU units (`0.125` vCPUs) and `196608` CPU units (`192` vCPUs). If you do not specify a value, the parameter is ignored.
This field is required for Fargate. For information about the valid values, see [Task size](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#task_size) in the *Amazon Elastic Container Service Developer Guide*.
Type: String
Required: No

 ** createdAt **   <a name="ECS-Type-Task-createdAt"></a>
The Unix timestamp for the time when the task was created. More specifically, it's for the time when the task entered the `PENDING` state.
Type: Timestamp
Required: No

 ** desiredStatus **   <a name="ECS-Type-Task-desiredStatus"></a>
The desired status of the task. For more information, see [Task Lifecycle](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-lifecycle.html).
Type: String
Required: No

 ** enableExecuteCommand **   <a name="ECS-Type-Task-enableExecuteCommand"></a>
Determines whether execute command functionality is turned on for this task. If `true`, execute command functionality is turned on all the containers in the task.
Type: Boolean
Required: No

 ** ephemeralStorage **   <a name="ECS-Type-Task-ephemeralStorage"></a>
The ephemeral storage settings for the task.
Type: [EphemeralStorage](API_EphemeralStorage.md) object
Required: No

 ** executionStoppedAt **   <a name="ECS-Type-Task-executionStoppedAt"></a>
The Unix timestamp for the time when the task execution stopped.
Type: Timestamp
Required: No

 ** fargateEphemeralStorage **   <a name="ECS-Type-Task-fargateEphemeralStorage"></a>
The Fargate ephemeral storage settings for the task.
Type: [TaskEphemeralStorage](API_TaskEphemeralStorage.md) object
Required: No

 ** group **   <a name="ECS-Type-Task-group"></a>
The name of the task group that's associated with the task.
Type: String
Required: No

 ** healthStatus **   <a name="ECS-Type-Task-healthStatus"></a>
The health status for the task. It's determined by the health of the essential containers in the task. If all essential containers in the task are reporting as `HEALTHY`, the task status also reports as `HEALTHY`. If any essential containers in the task are reporting as `UNHEALTHY` or `UNKNOWN`, the task status also reports as `UNHEALTHY` or `UNKNOWN`.
The Amazon ECS container agent doesn't monitor or report on Docker health checks that are embedded in a container image and not specified in the container definition. For example, this includes those specified in a parent image or from the image's Dockerfile. Health check parameters that are specified in a container definition override any Docker health checks that are found in the container image.
Type: String
Valid Values: `HEALTHY | UNHEALTHY | UNKNOWN`
Required: No

 ** inferenceAccelerators **   <a name="ECS-Type-Task-inferenceAccelerators"></a>
 *This member has been deprecated.*
The Elastic Inference accelerator that's associated with the task.
Type: Array of [InferenceAccelerator](API_InferenceAccelerator.md) objects
Required: No

 ** lastStatus **   <a name="ECS-Type-Task-lastStatus"></a>
The last known status for the task. For more information, see [Task Lifecycle](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-lifecycle.html).
Type: String
Required: No

 ** launchType **   <a name="ECS-Type-Task-launchType"></a>
The infrastructure where your task runs on. For more information, see [Amazon ECS launch types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: String
Valid Values: `EC2 | FARGATE | EXTERNAL | MANAGED_INSTANCES`
Required: No

 ** memory **   <a name="ECS-Type-Task-memory"></a>
The amount of memory (in MiB) that the task uses as expressed in a task definition. It can be expressed as an integer using MiB (for example, `1024`). If it's expressed as a string using GB (for example, `1GB` or `1 GB`), it's converted to an integer indicating the MiB when the task definition is registered.
If you use the EC2 launch type, this field is optional.
If you use the Fargate launch type, this field is required. You must use one of the following values. The value that you choose determines the range of supported values for the `cpu` parameter.
+ 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available `cpu` values: 256 (.25 vCPU)
+ 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available `cpu` values: 512 (.5 vCPU)
+ 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available `cpu` values: 1024 (1 vCPU)
+ Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available `cpu` values: 2048 (2 vCPU)
+ Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available `cpu` values: 4096 (4 vCPU)
+ Between 16 GB and 60 GB in 4 GB increments - Available `cpu` values: 8192 (8 vCPU)

  This option requires Linux platform `1.4.0` or later.
+ Between 32GB and 120 GB in 8 GB increments - Available `cpu` values: 16384 (16 vCPU)

  This option requires Linux platform `1.4.0` or later.
Type: String
Required: No

 ** overrides **   <a name="ECS-Type-Task-overrides"></a>
One or more container overrides.
Type: [TaskOverride](API_TaskOverride.md) object
Required: No

 ** platformFamily **   <a name="ECS-Type-Task-platformFamily"></a>
The operating system that your tasks are running on. A platform family is specified only for tasks that use the Fargate launch type.
 All tasks that run as part of this service must use the same `platformFamily` value as the service (for example, `LINUX.`).
Type: String
Required: No

 ** platformVersion **   <a name="ECS-Type-Task-platformVersion"></a>
The platform version where your task runs on. A platform version is only specified for tasks that use the Fargate launch type. If you didn't specify one, the `LATEST` platform version is used. For more information, see [AWS Fargate Platform Versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: String
Required: No

 ** pullStartedAt **   <a name="ECS-Type-Task-pullStartedAt"></a>
The Unix timestamp for the time when the container image pull began.
Type: Timestamp
Required: No

 ** pullStoppedAt **   <a name="ECS-Type-Task-pullStoppedAt"></a>
The Unix timestamp for the time when the container image pull completed.
Type: Timestamp
Required: No

 ** startedAt **   <a name="ECS-Type-Task-startedAt"></a>
The Unix timestamp for the time when the task started. More specifically, it's for the time when the task transitioned from the `PENDING` state to the `RUNNING` state.
Type: Timestamp
Required: No

 ** startedBy **   <a name="ECS-Type-Task-startedBy"></a>
The tag specified when a task is started. If an Amazon ECS service started the task, the `startedBy` parameter contains the deployment ID of that service.
Type: String
Required: No

 ** stopCode **   <a name="ECS-Type-Task-stopCode"></a>
The stop code indicating why a task was stopped. The `stoppedReason` might contain additional details.
For more information about stop code, see [Stopped tasks error codes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/stopped-task-error-codes.html) in the *Amazon ECS Developer Guide*.
Type: String
Valid Values: `TaskFailedToStart | EssentialContainerExited | UserInitiated | ServiceSchedulerInitiated | SpotInterruption | TerminationNotice`
Required: No

 ** stoppedAt **   <a name="ECS-Type-Task-stoppedAt"></a>
The Unix timestamp for the time when the task was stopped. More specifically, it's for the time when the task transitioned from the `RUNNING` state to the `STOPPED` state.
Type: Timestamp
Required: No

 ** stoppedReason **   <a name="ECS-Type-Task-stoppedReason"></a>
The reason that the task was stopped.
Type: String
Required: No

 ** stoppingAt **   <a name="ECS-Type-Task-stoppingAt"></a>
The Unix timestamp for the time when the task stops. More specifically, it's for the time when the task transitions from the `RUNNING` state to `STOPPING`.
Type: Timestamp
Required: No

 ** tags **   <a name="ECS-Type-Task-tags"></a>
The metadata that you apply to the task to help you categorize and organize the task. Each tag consists of a key and an optional value. You define both the key and value.
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

 ** taskArn **   <a name="ECS-Type-Task-taskArn"></a>
The Amazon Resource Name (ARN) of the task.
Type: String
Required: No

 ** taskDefinitionArn **   <a name="ECS-Type-Task-taskDefinitionArn"></a>
The ARN of the task definition that creates the task.
Type: String
Required: No

 ** version **   <a name="ECS-Type-Task-version"></a>
The version counter for the task. Every time a task experiences a change that starts a CloudWatch event, the version counter is incremented. If you replicate your Amazon ECS task state with CloudWatch Events, you can compare the version of a task reported by the Amazon ECS API actions with the version reported in CloudWatch Events for the task (inside the `detail` object) to verify that the version in your event stream is current.
Type: Long
Required: No

## See Also
<a name="API_Task_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/Task)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/Task)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/Task)
