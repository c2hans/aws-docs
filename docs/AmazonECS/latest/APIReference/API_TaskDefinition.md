---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TaskDefinition.html
---

# TaskDefinition
<a name="API_TaskDefinition"></a>

The details of a task definition which describes the container and volume definitions of an Amazon Elastic Container Service task. You can specify which Docker images to use, the required resources, and other configurations related to launching the task definition through an Amazon ECS service or task.

## Contents
<a name="API_TaskDefinition_Contents"></a>

 ** compatibilities **   <a name="ECS-Type-TaskDefinition-compatibilities"></a>
Amazon ECS validates the task definition parameters with those supported by the launch type. For more information, see [Amazon ECS launch types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: Array of strings
Valid Values: `EC2 | FARGATE | EXTERNAL | MANAGED_INSTANCES`
Required: No

 ** containerDefinitions **   <a name="ECS-Type-TaskDefinition-containerDefinitions"></a>
A list of container definitions in JSON format that describe the different containers that make up your task. For more information about container definition parameters and defaults, see [Amazon ECS Task Definitions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: Array of [ContainerDefinition](API_ContainerDefinition.md) objects
Required: No

 ** cpu **   <a name="ECS-Type-TaskDefinition-cpu"></a>
The number of `cpu` units used by the task. If you use the EC2 launch type, this field is optional. Any value can be used. If you use the Fargate launch type, this field is required. You must use one of the following values. The value that you choose determines your range of valid values for the `memory` parameter.
If you're using the EC2 launch type or the external launch type, this field is optional. Supported values are between `128` CPU units (`0.125` vCPUs) and `196608` CPU units (`192` vCPUs).
This field is required for Fargate. For information about the valid values, see [Task size](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#task_size) in the *Amazon Elastic Container Service Developer Guide*.
Type: String
Required: No

 ** deleteRequestedAt **   <a name="ECS-Type-TaskDefinition-deleteRequestedAt"></a>
The Unix timestamp for the time when the task definition delete was requested.
Type: Timestamp
Required: No

 ** deregisteredAt **   <a name="ECS-Type-TaskDefinition-deregisteredAt"></a>
The Unix timestamp for the time when the task definition was deregistered.
Type: Timestamp
Required: No

 ** enableFaultInjection **   <a name="ECS-Type-TaskDefinition-enableFaultInjection"></a>
Enables fault injection and allows for fault injection requests to be accepted from the task's containers. The default value is `false`.
Type: Boolean
Required: No

 ** ephemeralStorage **   <a name="ECS-Type-TaskDefinition-ephemeralStorage"></a>
The ephemeral storage settings to use for tasks run with the task definition.
Type: [EphemeralStorage](API_EphemeralStorage.md) object
Required: No

 ** executionRoleArn **   <a name="ECS-Type-TaskDefinition-executionRoleArn"></a>
The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make AWS API calls on your behalf. For informationabout the required IAM roles for Amazon ECS, see [IAM roles for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-ecs-iam-role-overview.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: String
Required: No

 ** family **   <a name="ECS-Type-TaskDefinition-family"></a>
The name of a family that this task definition is registered to. Up to 255 characters are allowed. Letters (both uppercase and lowercase letters), numbers, hyphens (-), and underscores (\_) are allowed.
A family groups multiple versions of a task definition. Amazon ECS gives the first task definition that you registered to a family a revision number of 1. Amazon ECS gives sequential revision numbers to each task definition that you add.
Type: String
Required: No

 ** inferenceAccelerators **   <a name="ECS-Type-TaskDefinition-inferenceAccelerators"></a>
 *This member has been deprecated.*
The Elastic Inference accelerator that's associated with the task.
Type: Array of [InferenceAccelerator](API_InferenceAccelerator.md) objects
Required: No

 ** ipcMode **   <a name="ECS-Type-TaskDefinition-ipcMode"></a>
The IPC resource namespace to use for the containers in the task. The valid values are `host`, `task`, or `none`. If `host` is specified, then all containers within the tasks that specified the `host` IPC mode on the same container instance share the same IPC resources with the host Amazon EC2 instance. If `task` is specified, all containers within the specified task share the same IPC resources. If `none` is specified, then IPC resources within the containers of a task are private and not shared with other containers in a task or on the container instance. If no value is specified, then the IPC resource namespace sharing depends on the Docker daemon setting on the container instance.
If the `host` IPC mode is used, be aware that there is a heightened risk of undesired IPC namespace expose.
If you are setting namespaced kernel parameters using `systemControls` for the containers in the task, the following will apply to your IPC resource namespace. For more information, see [System Controls](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html) in the *Amazon Elastic Container Service Developer Guide*.
+ For tasks that use the `host` IPC mode, IPC namespace related `systemControls` are not supported.
+ For tasks that use the `task` IPC mode, IPC namespace related `systemControls` will apply to all containers within a task.
This parameter is not supported for Windows containers or tasks run on AWS Fargate.
Type: String
Valid Values: `host | task | none`
Required: No

 ** memory **   <a name="ECS-Type-TaskDefinition-memory"></a>
The amount (in MiB) of memory used by the task.
If your tasks runs on Amazon EC2 instances, you must specify either a task-level memory value or a container-level memory value. This field is optional and any value can be used. If a task-level memory value is specified, the container-level memory value is optional. For more information regarding container-level memory and memory reservation, see [ContainerDefinition](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html).
If your tasks runs on AWS Fargate, this field is required. You must use one of the following values. The value you choose determines your range of valid values for the `cpu` parameter.
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

 ** networkMode **   <a name="ECS-Type-TaskDefinition-networkMode"></a>
The Docker networking mode to use for the containers in the task. The valid values are `none`, `bridge`, `awsvpc`, and `host`. If no network mode is specified, the default is `bridge`.
For Amazon ECS tasks on Fargate, the `awsvpc` network mode is required. For Amazon ECS tasks on Amazon EC2 Linux instances, any network mode can be used. For Amazon ECS tasks on Amazon EC2 Windows instances, `<default>` or `awsvpc` can be used. If the network mode is set to `none`, you cannot specify port mappings in your container definitions, and the tasks containers do not have external connectivity. The `host` and `awsvpc` network modes offer the highest networking performance for containers because they use the EC2 network stack instead of the virtualized network stack provided by the `bridge` mode.
With the `host` and `awsvpc` network modes, exposed container ports are mapped directly to the corresponding host port (for the `host` network mode) or the attached elastic network interface port (for the `awsvpc` network mode), so you cannot take advantage of dynamic host port mappings.
When using the `host` network mode, you should not run containers using the root user (UID 0). It is considered best practice to use a non-root user.
If the network mode is `awsvpc`, the task is allocated an elastic network interface, and you must specify a [NetworkConfiguration](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_NetworkConfiguration.html) value when you create a service or run a task with the task definition. For more information, see [Task Networking](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html) in the *Amazon Elastic Container Service Developer Guide*.
If the network mode is `host`, you cannot run multiple instantiations of the same task on a single container instance when port mappings are used.
Type: String
Valid Values: `bridge | host | awsvpc | none`
Required: No

 ** pidMode **   <a name="ECS-Type-TaskDefinition-pidMode"></a>
The process namespace to use for the containers in the task. The valid values are `host` or `task`. On Fargate for Linux containers, the only valid value is `task`. For example, monitoring sidecars might need `pidMode` to access information about other containers running in the same task.
If `host` is specified, all containers within the tasks that specified the `host` PID mode on the same container instance share the same process namespace with the host Amazon EC2 instance.
If `task` is specified, all containers within the specified task share the same process namespace.
If no value is specified, the The default is a private namespace for each container.
If the `host` PID mode is used, there's a heightened risk of undesired process namespace exposure.
This parameter is not supported for Windows containers.
This parameter is only supported for tasks that are hosted on AWS Fargate if the tasks are using platform version `1.4.0` or later (Linux). This isn't supported for Windows containers on Fargate.
Type: String
Valid Values: `host | task`
Required: No

 ** placementConstraints **   <a name="ECS-Type-TaskDefinition-placementConstraints"></a>
An array of placement constraint objects to use for tasks.
This parameter isn't supported for tasks run on AWS Fargate.
Type: Array of [TaskDefinitionPlacementConstraint](API_TaskDefinitionPlacementConstraint.md) objects
Required: No

 ** proxyConfiguration **   <a name="ECS-Type-TaskDefinition-proxyConfiguration"></a>
The configuration details for the App Mesh proxy.
Your Amazon ECS container instances require at least version 1.26.0 of the container agent and at least version 1.26.0-1 of the `ecs-init` package to use a proxy configuration. If your container instances are launched from the Amazon ECS optimized AMI version `20190301` or later, they contain the required versions of the container agent and `ecs-init`. For more information, see [Amazon ECS-optimized Linux AMI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: [ProxyConfiguration](API_ProxyConfiguration.md) object
Required: No

 ** registeredAt **   <a name="ECS-Type-TaskDefinition-registeredAt"></a>
The Unix timestamp for the time when the task definition was registered.
Type: Timestamp
Required: No

 ** registeredBy **   <a name="ECS-Type-TaskDefinition-registeredBy"></a>
The principal that registered the task definition.
Type: String
Required: No

 ** requiresAttributes **   <a name="ECS-Type-TaskDefinition-requiresAttributes"></a>
The container instance attributes required by your task. When an Amazon EC2 instance is registered to your cluster, the Amazon ECS container agent assigns some standard attributes to the instance. You can apply custom attributes. These are specified as key-value pairs using the Amazon ECS console or the [PutAttributes](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAttributes.html) API. These attributes are used when determining task placement for tasks hosted on Amazon EC2 instances. For more information, see [Attributes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes) in the *Amazon Elastic Container Service Developer Guide*.
This parameter isn't supported for tasks run on AWS Fargate.
Type: Array of [Attribute](API_Attribute.md) objects
Required: No

 ** requiresCompatibilities **   <a name="ECS-Type-TaskDefinition-requiresCompatibilities"></a>
The task launch types the task definition was validated against. The valid values are `MANAGED_INSTANCES`, `EC2`, `FARGATE`, and `EXTERNAL`. For more information, see [Amazon ECS launch types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: Array of strings
Valid Values: `EC2 | FARGATE | EXTERNAL | MANAGED_INSTANCES`
Required: No

 ** revision **   <a name="ECS-Type-TaskDefinition-revision"></a>
The revision of the task in a particular family. The revision is a version number of a task definition in a family. When you register a task definition for the first time, the revision is `1`. Each time that you register a new revision of a task definition in the same family, the revision value always increases by one. This is even if you deregistered previous revisions in this family.
Type: Integer
Required: No

 ** runtimePlatform **   <a name="ECS-Type-TaskDefinition-runtimePlatform"></a>
The operating system that your task definitions are running on. A platform family is specified only for tasks using the Fargate launch type.
When you specify a task in a service, this value must match the `runtimePlatform` value of the service.
Type: [RuntimePlatform](API_RuntimePlatform.md) object
Required: No

 ** status **   <a name="ECS-Type-TaskDefinition-status"></a>
The status of the task definition.
Type: String
Valid Values: `ACTIVE | INACTIVE | DELETE_IN_PROGRESS`
Required: No

 ** taskDefinitionArn **   <a name="ECS-Type-TaskDefinition-taskDefinitionArn"></a>
The full Amazon Resource Name (ARN) of the task definition.
Type: String
Required: No

 ** taskRoleArn **   <a name="ECS-Type-TaskDefinition-taskRoleArn"></a>
The short name or full Amazon Resource Name (ARN) of the AWS Identity and Access Management role that grants containers in the task permission to call AWS APIs on your behalf. For informationabout the required IAM roles for Amazon ECS, see [IAM roles for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-ecs-iam-role-overview.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: String
Required: No

 ** volumes **   <a name="ECS-Type-TaskDefinition-volumes"></a>
The list of data volume definitions for the task. For more information, see [Using data volumes in tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_data_volumes.html) in the *Amazon Elastic Container Service Developer Guide*.
The `host` and `sourcePath` parameters aren't supported for tasks run on AWS Fargate.
Type: Array of [Volume](API_Volume.md) objects
Required: No

## See Also
<a name="API_TaskDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/TaskDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/TaskDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/TaskDefinition)
