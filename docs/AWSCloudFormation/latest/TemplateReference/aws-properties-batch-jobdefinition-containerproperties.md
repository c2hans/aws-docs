---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-containerproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition ContainerProperties
<a name="aws-properties-batch-jobdefinition-containerproperties"></a>

Container properties are used for Amazon ECS based job definitions. These properties to describe the container that's launched as part of a job.

## Syntax
<a name="aws-properties-batch-jobdefinition-containerproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-containerproperties-syntax.json"></a>

```
{
  "[Command](#cfn-batch-jobdefinition-containerproperties-command)" : {{[ String, ... ]}},
  "[EnableExecuteCommand](#cfn-batch-jobdefinition-containerproperties-enableexecutecommand)" : {{Boolean}},
  "[Environment](#cfn-batch-jobdefinition-containerproperties-environment)" : {{[ Environment, ... ]}},
  "[EphemeralStorage](#cfn-batch-jobdefinition-containerproperties-ephemeralstorage)" : {{EphemeralStorage}},
  "[ExecutionRoleArn](#cfn-batch-jobdefinition-containerproperties-executionrolearn)" : {{String}},
  "[FargatePlatformConfiguration](#cfn-batch-jobdefinition-containerproperties-fargateplatformconfiguration)" : {{FargatePlatformConfiguration}},
  "[Image](#cfn-batch-jobdefinition-containerproperties-image)" : {{String}},
  "[JobRoleArn](#cfn-batch-jobdefinition-containerproperties-jobrolearn)" : {{String}},
  "[LinuxParameters](#cfn-batch-jobdefinition-containerproperties-linuxparameters)" : {{LinuxParameters}},
  "[LogConfiguration](#cfn-batch-jobdefinition-containerproperties-logconfiguration)" : {{LogConfiguration}},
  "[Memory](#cfn-batch-jobdefinition-containerproperties-memory)" : {{Integer}},
  "[MountPoints](#cfn-batch-jobdefinition-containerproperties-mountpoints)" : {{[ MountPoint, ... ]}},
  "[NetworkConfiguration](#cfn-batch-jobdefinition-containerproperties-networkconfiguration)" : {{NetworkConfiguration}},
  "[Privileged](#cfn-batch-jobdefinition-containerproperties-privileged)" : {{Boolean}},
  "[ReadonlyRootFilesystem](#cfn-batch-jobdefinition-containerproperties-readonlyrootfilesystem)" : {{Boolean}},
  "[RepositoryCredentials](#cfn-batch-jobdefinition-containerproperties-repositorycredentials)" : {{RepositoryCredentials}},
  "[ResourceRequirements](#cfn-batch-jobdefinition-containerproperties-resourcerequirements)" : {{[ ResourceRequirement, ... ]}},
  "[RuntimePlatform](#cfn-batch-jobdefinition-containerproperties-runtimeplatform)" : {{RuntimePlatform}},
  "[Secrets](#cfn-batch-jobdefinition-containerproperties-secrets)" : {{[ Secret, ... ]}},
  "[Ulimits](#cfn-batch-jobdefinition-containerproperties-ulimits)" : {{[ Ulimit, ... ]}},
  "[User](#cfn-batch-jobdefinition-containerproperties-user)" : {{String}},
  "[Vcpus](#cfn-batch-jobdefinition-containerproperties-vcpus)" : {{Integer}},
  "[Volumes](#cfn-batch-jobdefinition-containerproperties-volumes)" : {{[ Volume, ... ]}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-containerproperties-syntax.yaml"></a>

```
  [Command](#cfn-batch-jobdefinition-containerproperties-command): {{
    - String}}
  [EnableExecuteCommand](#cfn-batch-jobdefinition-containerproperties-enableexecutecommand): {{Boolean}}
  [Environment](#cfn-batch-jobdefinition-containerproperties-environment): {{
    - Environment}}
  [EphemeralStorage](#cfn-batch-jobdefinition-containerproperties-ephemeralstorage): {{
    EphemeralStorage}}
  [ExecutionRoleArn](#cfn-batch-jobdefinition-containerproperties-executionrolearn): {{String}}
  [FargatePlatformConfiguration](#cfn-batch-jobdefinition-containerproperties-fargateplatformconfiguration): {{
    FargatePlatformConfiguration}}
  [Image](#cfn-batch-jobdefinition-containerproperties-image): {{String}}
  [JobRoleArn](#cfn-batch-jobdefinition-containerproperties-jobrolearn): {{String}}
  [LinuxParameters](#cfn-batch-jobdefinition-containerproperties-linuxparameters): {{
    LinuxParameters}}
  [LogConfiguration](#cfn-batch-jobdefinition-containerproperties-logconfiguration): {{
    LogConfiguration}}
  [Memory](#cfn-batch-jobdefinition-containerproperties-memory): {{Integer}}
  [MountPoints](#cfn-batch-jobdefinition-containerproperties-mountpoints): {{
    - MountPoint}}
  [NetworkConfiguration](#cfn-batch-jobdefinition-containerproperties-networkconfiguration): {{
    NetworkConfiguration}}
  [Privileged](#cfn-batch-jobdefinition-containerproperties-privileged): {{Boolean}}
  [ReadonlyRootFilesystem](#cfn-batch-jobdefinition-containerproperties-readonlyrootfilesystem): {{Boolean}}
  [RepositoryCredentials](#cfn-batch-jobdefinition-containerproperties-repositorycredentials): {{
    RepositoryCredentials}}
  [ResourceRequirements](#cfn-batch-jobdefinition-containerproperties-resourcerequirements): {{
    - ResourceRequirement}}
  [RuntimePlatform](#cfn-batch-jobdefinition-containerproperties-runtimeplatform): {{
    RuntimePlatform}}
  [Secrets](#cfn-batch-jobdefinition-containerproperties-secrets): {{
    - Secret}}
  [Ulimits](#cfn-batch-jobdefinition-containerproperties-ulimits): {{
    - Ulimit}}
  [User](#cfn-batch-jobdefinition-containerproperties-user): {{String}}
  [Vcpus](#cfn-batch-jobdefinition-containerproperties-vcpus): {{Integer}}
  [Volumes](#cfn-batch-jobdefinition-containerproperties-volumes): {{
    - Volume}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-containerproperties-properties"></a>

`Command`  <a name="cfn-batch-jobdefinition-containerproperties-command"></a>
The command that's passed to the container. This parameter maps to `Cmd` in the [Create a container](https://docs.docker.com/engine/api/latest/#tag/Container/operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/latest/) and the `COMMAND` parameter to [docker run](https://docs.docker.com/engine/reference/run/). For more information, see [https://docs.docker.com/engine/reference/builder/\#cmd](https://docs.docker.com/engine/reference/builder/#cmd).
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableExecuteCommand`  <a name="cfn-batch-jobdefinition-containerproperties-enableexecutecommand"></a>
Determines whether execute command functionality is turned on for this task. If `true`, execute command functionality is turned on all the containers in the task.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Environment`  <a name="cfn-batch-jobdefinition-containerproperties-environment"></a>
The environment variables to pass to a container. This parameter maps to `Env` in the [Create a container](https://docs.docker.com/engine/api/latest/#tag/Container/operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/latest/) and the `--env` option to [docker run](https://docs.docker.com/engine/reference/run/).
We don't recommend using plaintext environment variables for sensitive information, such as credential data.
Environment variables cannot start with "`AWS_BATCH`". This naming convention is reserved for variables that AWS Batch sets.
*Required*: No
*Type*: [Array](aws-properties-batch-jobdefinition-environment.md) of [Environment](aws-properties-batch-jobdefinition-environment.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EphemeralStorage`  <a name="cfn-batch-jobdefinition-containerproperties-ephemeralstorage"></a>
The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on AWS Fargate.
*Required*: No
*Type*: [EphemeralStorage](aws-properties-batch-jobdefinition-ephemeralstorage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRoleArn`  <a name="cfn-batch-jobdefinition-containerproperties-executionrolearn"></a>
The Amazon Resource Name (ARN) of the execution role that AWS Batch can assume. For jobs that run on Fargate resources, you must provide an execution role. For more information, see [AWS Batch execution IAM role](https://docs.aws.amazon.com/batch/latest/userguide/execution-IAM-role.html) in the *AWS Batch User Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FargatePlatformConfiguration`  <a name="cfn-batch-jobdefinition-containerproperties-fargateplatformconfiguration"></a>
The platform configuration for jobs that are running on Fargate resources. Jobs that are running on Amazon EC2 resources must not specify this parameter.
*Required*: No
*Type*: [FargatePlatformConfiguration](aws-properties-batch-jobdefinition-fargateplatformconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Image`  <a name="cfn-batch-jobdefinition-containerproperties-image"></a>
Required. The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with `repository-url/image:tag`. It can be 255 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), underscores (\_), colons (:), periods (.), forward slashes (/), and number signs (\#). This parameter maps to `Image` in the [Create a container](https://docs.docker.com/engine/api/latest/#tag/Container/operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/latest/) and the `IMAGE` parameter of [docker run](https://docs.docker.com/engine/reference/run/).
Docker image architecture must match the processor architecture of the compute resources that they're scheduled on. For example, ARM-based Docker images can only run on ARM-based compute resources.
+ Images in Amazon ECR Public repositories use the full `registry/repository[:tag]` or `registry/repository[@digest]` naming conventions. For example, `public.ecr.aws/registry_alias/my-web-app:latest`.
+ Images in Amazon ECR repositories use the full registry and repository URI (for example, `123456789012.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`).
+ Images in official repositories on Docker Hub use a single name (for example, `ubuntu` or `mongo`).
+ Images in other repositories on Docker Hub are qualified with an organization name (for example, `amazon/amazon-ecs-agent`).
+ Images in other online repositories are qualified further by a domain name (for example, `quay.io/assemblyline/ubuntu`).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JobRoleArn`  <a name="cfn-batch-jobdefinition-containerproperties-jobrolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions. For more information, see [IAM roles for tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LinuxParameters`  <a name="cfn-batch-jobdefinition-containerproperties-linuxparameters"></a>
Linux-specific modifications that are applied to the container, such as details for device mappings.
*Required*: No
*Type*: [LinuxParameters](aws-properties-batch-jobdefinition-linuxparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogConfiguration`  <a name="cfn-batch-jobdefinition-containerproperties-logconfiguration"></a>
The log configuration specification for the container.
This parameter maps to `LogConfig` in the [Create a container](https://docs.docker.com/engine/api/latest/#tag/Container/operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/latest/) and the `--log-driver` option to [docker run](https://docs.docker.com/engine/reference/run/). By default, containers use the same logging driver that the Docker daemon uses. However the container might use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information on the options for different supported log drivers, see [Configure logging drivers](https://docs.docker.com/engine/admin/logging/overview/) in the Docker documentation.
AWS Batch currently supports a subset of the logging drivers available to the Docker daemon (shown in the [LogConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-logconfiguration.html) data type).
This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version | grep "Server API version"`
The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the `ECS_AVAILABLE_LOGGING_DRIVERS` environment variable before containers placed on that instance can use these log configuration options. For more information, see [Amazon ECS container agent configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html) in the *Amazon Elastic Container Service Developer Guide*.
*Required*: No
*Type*: [LogConfiguration](aws-properties-batch-jobdefinition-logconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Memory`  <a name="cfn-batch-jobdefinition-containerproperties-memory"></a>
This parameter is deprecated, use `resourceRequirements` to specify the memory requirements for the job definition. It's not supported for jobs running on Fargate resources. For jobs that run on Amazon EC2 resources, it specifies the memory hard limit (in MiB) for a container. If your container attempts to exceed the specified number, it's terminated. You must specify at least 4 MiB of memory for a job using this parameter. The memory hard limit can be specified in several places. It must be specified for each node at least once.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MountPoints`  <a name="cfn-batch-jobdefinition-containerproperties-mountpoints"></a>
The mount points for data volumes in your container. This parameter maps to `Volumes` in the [Create a container](https://docs.docker.com/engine/api/latest/#tag/Container/operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/latest/) and the `--volume` option to [docker run](https://docs.docker.com/engine/reference/run/).
*Required*: No
*Type*: Array of [MountPoint](aws-properties-batch-jobdefinition-mountpoint.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkConfiguration`  <a name="cfn-batch-jobdefinition-containerproperties-networkconfiguration"></a>
The network configuration for jobs that are running on Fargate resources. Jobs that are running on Amazon EC2 resources must not specify this parameter.
*Required*: No
*Type*: [NetworkConfiguration](aws-properties-batch-jobdefinition-networkconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Privileged`  <a name="cfn-batch-jobdefinition-containerproperties-privileged"></a>
When this parameter is true, the container is given elevated permissions on the host container instance (similar to the `root` user). This parameter maps to `Privileged` in the [Create a container](https://docs.docker.com/engine/api/latest/#tag/Container/operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/latest/) and the `--privileged` option to [docker run](https://docs.docker.com/engine/reference/run/). The default value is false.
This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided, or specified as false.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReadonlyRootFilesystem`  <a name="cfn-batch-jobdefinition-containerproperties-readonlyrootfilesystem"></a>
When this parameter is true, the container is given read-only access to its root file system. This parameter maps to `ReadonlyRootfs` in the [Create a container](https://docs.docker.com/engine/api/latest/#tag/Container/operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/latest/) and the `--read-only` option to `docker run`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RepositoryCredentials`  <a name="cfn-batch-jobdefinition-containerproperties-repositorycredentials"></a>
The private repository authentication credentials to use.
*Required*: No
*Type*: [RepositoryCredentials](aws-properties-batch-jobdefinition-repositorycredentials.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceRequirements`  <a name="cfn-batch-jobdefinition-containerproperties-resourcerequirements"></a>
The type and amount of resources to assign to a container. The supported resources include `GPU`, `MEMORY`, and `VCPU`.
*Required*: No
*Type*: Array of [ResourceRequirement](aws-properties-batch-jobdefinition-resourcerequirement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuntimePlatform`  <a name="cfn-batch-jobdefinition-containerproperties-runtimeplatform"></a>
An object that represents the compute environment architecture for AWS Batch jobs on Fargate.
*Required*: No
*Type*: [RuntimePlatform](aws-properties-batch-jobdefinition-runtimeplatform.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Secrets`  <a name="cfn-batch-jobdefinition-containerproperties-secrets"></a>
The secrets for the container. For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html) in the *AWS Batch User Guide*.
*Required*: No
*Type*: Array of [Secret](aws-properties-batch-jobdefinition-secret.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ulimits`  <a name="cfn-batch-jobdefinition-containerproperties-ulimits"></a>
A list of `ulimits` to set in the container. This parameter maps to `Ulimits` in the [Create a container](https://docs.docker.com/engine/api/latest/#tag/Container/operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/latest/) and the `--ulimit` option to [docker run](https://docs.docker.com/engine/reference/run/).
This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.
*Required*: No
*Type*: Array of [Ulimit](aws-properties-batch-jobdefinition-ulimit.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`User`  <a name="cfn-batch-jobdefinition-containerproperties-user"></a>
The user name to use inside the container. This parameter maps to `User` in the [Create a container](https://docs.docker.com/engine/api/latest/#tag/Container/operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/latest/) and the `--user` option to [docker run](https://docs.docker.com/engine/reference/run/).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Vcpus`  <a name="cfn-batch-jobdefinition-containerproperties-vcpus"></a>
This parameter is deprecated, use `resourceRequirements` to specify the vCPU requirements for the job definition. It's not supported for jobs running on Fargate resources. For jobs running on Amazon EC2 resources, it specifies the number of vCPUs reserved for the job.
Each vCPU is equivalent to 1,024 CPU shares. This parameter maps to `CpuShares` in the [Create a container](https://docs.docker.com/engine/api/latest/#tag/Container/operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/latest/) and the `--cpu-shares` option to [docker run](https://docs.docker.com/engine/reference/run/). The number of vCPUs must be specified but can be specified in several places. You must specify it at least once for each node.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Volumes`  <a name="cfn-batch-jobdefinition-containerproperties-volumes"></a>
A list of data volumes used in a job.
*Required*: No
*Type*: Array of [Volume](aws-properties-batch-jobdefinition-volume.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
