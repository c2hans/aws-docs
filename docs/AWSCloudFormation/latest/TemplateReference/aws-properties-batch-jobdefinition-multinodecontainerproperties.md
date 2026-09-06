---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-multinodecontainerproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition MultiNodeContainerProperties
<a name="aws-properties-batch-jobdefinition-multinodecontainerproperties"></a>

Container properties are used for Amazon ECS based job definitions. These properties to describe the container that's launched as part of a job.

## Syntax
<a name="aws-properties-batch-jobdefinition-multinodecontainerproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-multinodecontainerproperties-syntax.json"></a>

```
{
  "[Command](#cfn-batch-jobdefinition-multinodecontainerproperties-command)" : {{[ String, ... ]}},
  "[EnableExecuteCommand](#cfn-batch-jobdefinition-multinodecontainerproperties-enableexecutecommand)" : {{Boolean}},
  "[Environment](#cfn-batch-jobdefinition-multinodecontainerproperties-environment)" : {{[ Environment, ... ]}},
  "[EphemeralStorage](#cfn-batch-jobdefinition-multinodecontainerproperties-ephemeralstorage)" : {{EphemeralStorage}},
  "[ExecutionRoleArn](#cfn-batch-jobdefinition-multinodecontainerproperties-executionrolearn)" : {{String}},
  "[Image](#cfn-batch-jobdefinition-multinodecontainerproperties-image)" : {{String}},
  "[InstanceType](#cfn-batch-jobdefinition-multinodecontainerproperties-instancetype)" : {{String}},
  "[JobRoleArn](#cfn-batch-jobdefinition-multinodecontainerproperties-jobrolearn)" : {{String}},
  "[LinuxParameters](#cfn-batch-jobdefinition-multinodecontainerproperties-linuxparameters)" : {{LinuxParameters}},
  "[LogConfiguration](#cfn-batch-jobdefinition-multinodecontainerproperties-logconfiguration)" : {{LogConfiguration}},
  "[Memory](#cfn-batch-jobdefinition-multinodecontainerproperties-memory)" : {{Integer}},
  "[MountPoints](#cfn-batch-jobdefinition-multinodecontainerproperties-mountpoints)" : {{[ MountPoint, ... ]}},
  "[Privileged](#cfn-batch-jobdefinition-multinodecontainerproperties-privileged)" : {{Boolean}},
  "[ReadonlyRootFilesystem](#cfn-batch-jobdefinition-multinodecontainerproperties-readonlyrootfilesystem)" : {{Boolean}},
  "[RepositoryCredentials](#cfn-batch-jobdefinition-multinodecontainerproperties-repositorycredentials)" : {{RepositoryCredentials}},
  "[ResourceRequirements](#cfn-batch-jobdefinition-multinodecontainerproperties-resourcerequirements)" : {{[ ResourceRequirement, ... ]}},
  "[RuntimePlatform](#cfn-batch-jobdefinition-multinodecontainerproperties-runtimeplatform)" : {{RuntimePlatform}},
  "[Secrets](#cfn-batch-jobdefinition-multinodecontainerproperties-secrets)" : {{[ Secret, ... ]}},
  "[Ulimits](#cfn-batch-jobdefinition-multinodecontainerproperties-ulimits)" : {{[ Ulimit, ... ]}},
  "[User](#cfn-batch-jobdefinition-multinodecontainerproperties-user)" : {{String}},
  "[Vcpus](#cfn-batch-jobdefinition-multinodecontainerproperties-vcpus)" : {{Integer}},
  "[Volumes](#cfn-batch-jobdefinition-multinodecontainerproperties-volumes)" : {{[ Volume, ... ]}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-multinodecontainerproperties-syntax.yaml"></a>

```
  [Command](#cfn-batch-jobdefinition-multinodecontainerproperties-command): {{
    - String}}
  [EnableExecuteCommand](#cfn-batch-jobdefinition-multinodecontainerproperties-enableexecutecommand): {{Boolean}}
  [Environment](#cfn-batch-jobdefinition-multinodecontainerproperties-environment): {{
    - Environment}}
  [EphemeralStorage](#cfn-batch-jobdefinition-multinodecontainerproperties-ephemeralstorage): {{
    EphemeralStorage}}
  [ExecutionRoleArn](#cfn-batch-jobdefinition-multinodecontainerproperties-executionrolearn): {{String}}
  [Image](#cfn-batch-jobdefinition-multinodecontainerproperties-image): {{String}}
  [InstanceType](#cfn-batch-jobdefinition-multinodecontainerproperties-instancetype): {{String}}
  [JobRoleArn](#cfn-batch-jobdefinition-multinodecontainerproperties-jobrolearn): {{String}}
  [LinuxParameters](#cfn-batch-jobdefinition-multinodecontainerproperties-linuxparameters): {{
    LinuxParameters}}
  [LogConfiguration](#cfn-batch-jobdefinition-multinodecontainerproperties-logconfiguration): {{
    LogConfiguration}}
  [Memory](#cfn-batch-jobdefinition-multinodecontainerproperties-memory): {{Integer}}
  [MountPoints](#cfn-batch-jobdefinition-multinodecontainerproperties-mountpoints): {{
    - MountPoint}}
  [Privileged](#cfn-batch-jobdefinition-multinodecontainerproperties-privileged): {{Boolean}}
  [ReadonlyRootFilesystem](#cfn-batch-jobdefinition-multinodecontainerproperties-readonlyrootfilesystem): {{Boolean}}
  [RepositoryCredentials](#cfn-batch-jobdefinition-multinodecontainerproperties-repositorycredentials): {{
    RepositoryCredentials}}
  [ResourceRequirements](#cfn-batch-jobdefinition-multinodecontainerproperties-resourcerequirements): {{
    - ResourceRequirement}}
  [RuntimePlatform](#cfn-batch-jobdefinition-multinodecontainerproperties-runtimeplatform): {{
    RuntimePlatform}}
  [Secrets](#cfn-batch-jobdefinition-multinodecontainerproperties-secrets): {{
    - Secret}}
  [Ulimits](#cfn-batch-jobdefinition-multinodecontainerproperties-ulimits): {{
    - Ulimit}}
  [User](#cfn-batch-jobdefinition-multinodecontainerproperties-user): {{String}}
  [Vcpus](#cfn-batch-jobdefinition-multinodecontainerproperties-vcpus): {{Integer}}
  [Volumes](#cfn-batch-jobdefinition-multinodecontainerproperties-volumes): {{
    - Volume}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-multinodecontainerproperties-properties"></a>

`Command`  <a name="cfn-batch-jobdefinition-multinodecontainerproperties-command"></a>
The command that's passed to the container. This parameter maps to `Cmd` in the [Create a container](https://docs.docker.com/engine/api/latest/#tag/Container/operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/latest/) and the `COMMAND` parameter to [docker run](https://docs.docker.com/engine/reference/run/). For more information, see [https://docs.docker.com/engine/reference/builder/\#cmd](https://docs.docker.com/engine/reference/builder/#cmd).
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableExecuteCommand`  <a name="cfn-batch-jobdefinition-multinodecontainerproperties-enableexecutecommand"></a>
Determines whether execute command functionality is turned on for this task. If `true`, execute command functionality is turned on all the containers in the task.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Environment`  <a name="cfn-batch-jobdefinition-multinodecontainerproperties-environment"></a>
The environment variables to pass to a container. This parameter maps to `Env` in the [Create a container](https://docs.docker.com/engine/api/latest/#tag/Container/operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/latest/) and the `--env` option to [docker run](https://docs.docker.com/engine/reference/run/).
We don't recommend using plaintext environment variables for sensitive information, such as credential data.
Environment variables cannot start with "`AWS_BATCH`". This naming convention is reserved for variables that AWS Batch sets.
*Required*: No
*Type*: [Array](aws-properties-batch-jobdefinition-environment.md) of [Environment](aws-properties-batch-jobdefinition-environment.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EphemeralStorage`  <a name="cfn-batch-jobdefinition-multinodecontainerproperties-ephemeralstorage"></a>
The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on AWS Fargate.
*Required*: No
*Type*: [EphemeralStorage](aws-properties-batch-jobdefinition-ephemeralstorage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRoleArn`  <a name="cfn-batch-jobdefinition-multinodecontainerproperties-executionrolearn"></a>
The Amazon Resource Name (ARN) of the execution role that AWS Batch can assume. For jobs that run on Fargate resources, you must provide an execution role. For more information, see [AWS Batch execution IAM role](https://docs.aws.amazon.com/batch/latest/userguide/execution-IAM-role.html) in the *AWS Batch User Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Image`  <a name="cfn-batch-jobdefinition-multinodecontainerproperties-image"></a>
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

`InstanceType`  <a name="cfn-batch-jobdefinition-multinodecontainerproperties-instancetype"></a>
The instance type to use for a multi-node parallel job. All node groups in a multi-node parallel job must use the same instance type.
This parameter isn't applicable to single-node container jobs or jobs that run on Fargate resources, and shouldn't be provided.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JobRoleArn`  <a name="cfn-batch-jobdefinition-multinodecontainerproperties-jobrolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions. For more information, see [IAM roles for tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LinuxParameters`  <a name="cfn-batch-jobdefinition-multinodecontainerproperties-linuxparameters"></a>
Linux-specific modifications that are applied to the container, such as details for device mappings.
*Required*: No
*Type*: [LinuxParameters](aws-properties-batch-jobdefinition-linuxparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogConfiguration`  <a name="cfn-batch-jobdefinition-multinodecontainerproperties-logconfiguration"></a>
The log configuration specification for the container.
This parameter maps to `LogConfig` in the [Create a container](https://docs.docker.com/engine/api/latest/#tag/Container/operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/latest/) and the `--log-driver` option to [docker run](https://docs.docker.com/engine/reference/run/). By default, containers use the same logging driver that the Docker daemon uses. However the container might use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information on the options for different supported log drivers, see [Configure logging drivers](https://docs.docker.com/engine/admin/logging/overview/) in the Docker documentation.
AWS Batch currently supports a subset of the logging drivers available to the Docker daemon (shown in the [LogConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-logconfiguration.html) data type).
This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version | grep "Server API version"`
The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the `ECS_AVAILABLE_LOGGING_DRIVERS` environment variable before containers placed on that instance can use these log configuration options. For more information, see [Amazon ECS container agent configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html) in the *Amazon Elastic Container Service Developer Guide*.
*Required*: No
*Type*: [LogConfiguration](aws-properties-batch-jobdefinition-logconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Memory`  <a name="cfn-batch-jobdefinition-multinodecontainerproperties-memory"></a>
This parameter is deprecated, use `resourceRequirements` to specify the memory requirements for the job definition. It's not supported for jobs running on Fargate resources. For jobs that run on Amazon EC2 resources, it specifies the memory hard limit (in MiB) for a container. If your container attempts to exceed the specified number, it's terminated. You must specify at least 4 MiB of memory for a job using this parameter. The memory hard limit can be specified in several places. It must be specified for each node at least once.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MountPoints`  <a name="cfn-batch-jobdefinition-multinodecontainerproperties-mountpoints"></a>
The mount points for data volumes in your container.
This parameter maps to `Volumes` in the [Create a container](https://docs.docker.com/engine/api/latest/#tag/Container/operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/latest/) and the [--volume]() option to [docker run](https://docs.docker.com/engine/reference/run/#security-configuration).
Windows containers can mount whole directories on the same drive as `$env:ProgramData`. Windows containers can't mount directories on a different drive, and mount point can't be across drives.
*Required*: No
*Type*: Array of [MountPoint](aws-properties-batch-jobdefinition-mountpoint.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Privileged`  <a name="cfn-batch-jobdefinition-multinodecontainerproperties-privileged"></a>
When this parameter is true, the container is given elevated permissions on the host container instance (similar to the `root` user). This parameter maps to `Privileged` in the [Create a container](https://docs.docker.com/engine/api/latest/#tag/Container/operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/latest/) and the `--privileged` option to [docker run](https://docs.docker.com/engine/reference/run/). The default value is false.
This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided, or specified as false.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReadonlyRootFilesystem`  <a name="cfn-batch-jobdefinition-multinodecontainerproperties-readonlyrootfilesystem"></a>
When this parameter is true, the container is given read-only access to its root file system. This parameter maps to `ReadonlyRootfs` in the [Create a container](https://docs.docker.com/engine/api/latest/#tag/Container/operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/latest/) and the `--read-only` option to `docker run`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RepositoryCredentials`  <a name="cfn-batch-jobdefinition-multinodecontainerproperties-repositorycredentials"></a>
The private repository authentication credentials to use.
*Required*: No
*Type*: [RepositoryCredentials](aws-properties-batch-jobdefinition-repositorycredentials.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceRequirements`  <a name="cfn-batch-jobdefinition-multinodecontainerproperties-resourcerequirements"></a>
The type and amount of resources to assign to a container. The supported resources include `GPU`, `MEMORY`, and `VCPU`.
*Required*: No
*Type*: Array of [ResourceRequirement](aws-properties-batch-jobdefinition-resourcerequirement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuntimePlatform`  <a name="cfn-batch-jobdefinition-multinodecontainerproperties-runtimeplatform"></a>
An object that represents the compute environment architecture for AWS Batch jobs on Fargate.
*Required*: No
*Type*: [RuntimePlatform](aws-properties-batch-jobdefinition-runtimeplatform.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Secrets`  <a name="cfn-batch-jobdefinition-multinodecontainerproperties-secrets"></a>
The secrets for the container. For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html) in the *AWS Batch User Guide*.
*Required*: No
*Type*: Array of [Secret](aws-properties-batch-jobdefinition-secret.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ulimits`  <a name="cfn-batch-jobdefinition-multinodecontainerproperties-ulimits"></a>
A list of `ulimits` to set in the container. This parameter maps to `Ulimits` in the [Create a container](https://docs.docker.com/engine/api/latest/#tag/Container/operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/latest/) and the `--ulimit` option to [docker run](https://docs.docker.com/engine/reference/run/).
This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.
*Required*: No
*Type*: Array of [Ulimit](aws-properties-batch-jobdefinition-ulimit.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`User`  <a name="cfn-batch-jobdefinition-multinodecontainerproperties-user"></a>
The user name to use inside the container. This parameter maps to `User` in the [Create a container](https://docs.docker.com/engine/api/latest/#tag/Container/operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/latest/) and the `--user` option to [docker run](https://docs.docker.com/engine/reference/run/).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Vcpus`  <a name="cfn-batch-jobdefinition-multinodecontainerproperties-vcpus"></a>
This parameter is deprecated, use `resourceRequirements` to specify the vCPU requirements for the job definition. It's not supported for jobs running on Fargate resources. For jobs running on Amazon EC2 resources, it specifies the number of vCPUs reserved for the job.
Each vCPU is equivalent to 1,024 CPU shares. This parameter maps to `CpuShares` in the [Create a container](https://docs.docker.com/engine/api/latest/#tag/Container/operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/latest/) and the `--cpu-shares` option to [docker run](https://docs.docker.com/engine/reference/run/). The number of vCPUs must be specified but can be specified in several places. You must specify it at least once for each node.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Volumes`  <a name="cfn-batch-jobdefinition-multinodecontainerproperties-volumes"></a>
A list of data volumes used in a job.
*Required*: No
*Type*: Array of [Volume](aws-properties-batch-jobdefinition-volume.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
