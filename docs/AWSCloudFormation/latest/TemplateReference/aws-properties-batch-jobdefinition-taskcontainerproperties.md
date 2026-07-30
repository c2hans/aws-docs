---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-taskcontainerproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition TaskContainerProperties
<a name="aws-properties-batch-jobdefinition-taskcontainerproperties"></a>

Container properties are used for Amazon ECS-based job definitions. These properties to describe the container that's launched as part of a job.

## Syntax
<a name="aws-properties-batch-jobdefinition-taskcontainerproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-taskcontainerproperties-syntax.json"></a>

```
{
  "[Command](#cfn-batch-jobdefinition-taskcontainerproperties-command)" : {{[ String, ... ]}},
  "[DependsOn](#cfn-batch-jobdefinition-taskcontainerproperties-dependson)" : {{[ TaskContainerDependency, ... ]}},
  "[Environment](#cfn-batch-jobdefinition-taskcontainerproperties-environment)" : {{[ Environment, ... ]}},
  "[Essential](#cfn-batch-jobdefinition-taskcontainerproperties-essential)" : {{Boolean}},
  "[FirelensConfiguration](#cfn-batch-jobdefinition-taskcontainerproperties-firelensconfiguration)" : {{FirelensConfiguration}},
  "[Image](#cfn-batch-jobdefinition-taskcontainerproperties-image)" : {{String}},
  "[LinuxParameters](#cfn-batch-jobdefinition-taskcontainerproperties-linuxparameters)" : {{LinuxParameters}},
  "[LogConfiguration](#cfn-batch-jobdefinition-taskcontainerproperties-logconfiguration)" : {{LogConfiguration}},
  "[MountPoints](#cfn-batch-jobdefinition-taskcontainerproperties-mountpoints)" : {{[ MountPoint, ... ]}},
  "[Name](#cfn-batch-jobdefinition-taskcontainerproperties-name)" : {{String}},
  "[Privileged](#cfn-batch-jobdefinition-taskcontainerproperties-privileged)" : {{Boolean}},
  "[ReadonlyRootFilesystem](#cfn-batch-jobdefinition-taskcontainerproperties-readonlyrootfilesystem)" : {{Boolean}},
  "[RepositoryCredentials](#cfn-batch-jobdefinition-taskcontainerproperties-repositorycredentials)" : {{RepositoryCredentials}},
  "[ResourceRequirements](#cfn-batch-jobdefinition-taskcontainerproperties-resourcerequirements)" : {{[ ResourceRequirement, ... ]}},
  "[Secrets](#cfn-batch-jobdefinition-taskcontainerproperties-secrets)" : {{[ Secret, ... ]}},
  "[StartTimeout](#cfn-batch-jobdefinition-taskcontainerproperties-starttimeout)" : {{Integer}},
  "[StopTimeout](#cfn-batch-jobdefinition-taskcontainerproperties-stoptimeout)" : {{Integer}},
  "[Ulimits](#cfn-batch-jobdefinition-taskcontainerproperties-ulimits)" : {{[ Ulimit, ... ]}},
  "[User](#cfn-batch-jobdefinition-taskcontainerproperties-user)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-taskcontainerproperties-syntax.yaml"></a>

```
  [Command](#cfn-batch-jobdefinition-taskcontainerproperties-command): {{
    - String}}
  [DependsOn](#cfn-batch-jobdefinition-taskcontainerproperties-dependson): {{
    - TaskContainerDependency}}
  [Environment](#cfn-batch-jobdefinition-taskcontainerproperties-environment): {{
    - Environment}}
  [Essential](#cfn-batch-jobdefinition-taskcontainerproperties-essential): {{Boolean}}
  [FirelensConfiguration](#cfn-batch-jobdefinition-taskcontainerproperties-firelensconfiguration): {{
    FirelensConfiguration}}
  [Image](#cfn-batch-jobdefinition-taskcontainerproperties-image): {{String}}
  [LinuxParameters](#cfn-batch-jobdefinition-taskcontainerproperties-linuxparameters): {{
    LinuxParameters}}
  [LogConfiguration](#cfn-batch-jobdefinition-taskcontainerproperties-logconfiguration): {{
    LogConfiguration}}
  [MountPoints](#cfn-batch-jobdefinition-taskcontainerproperties-mountpoints): {{
    - MountPoint}}
  [Name](#cfn-batch-jobdefinition-taskcontainerproperties-name): {{String}}
  [Privileged](#cfn-batch-jobdefinition-taskcontainerproperties-privileged): {{Boolean}}
  [ReadonlyRootFilesystem](#cfn-batch-jobdefinition-taskcontainerproperties-readonlyrootfilesystem): {{Boolean}}
  [RepositoryCredentials](#cfn-batch-jobdefinition-taskcontainerproperties-repositorycredentials): {{
    RepositoryCredentials}}
  [ResourceRequirements](#cfn-batch-jobdefinition-taskcontainerproperties-resourcerequirements): {{
    - ResourceRequirement}}
  [Secrets](#cfn-batch-jobdefinition-taskcontainerproperties-secrets): {{
    - Secret}}
  [StartTimeout](#cfn-batch-jobdefinition-taskcontainerproperties-starttimeout): {{Integer}}
  [StopTimeout](#cfn-batch-jobdefinition-taskcontainerproperties-stoptimeout): {{Integer}}
  [Ulimits](#cfn-batch-jobdefinition-taskcontainerproperties-ulimits): {{
    - Ulimit}}
  [User](#cfn-batch-jobdefinition-taskcontainerproperties-user): {{String}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-taskcontainerproperties-properties"></a>

`Command`  <a name="cfn-batch-jobdefinition-taskcontainerproperties-command"></a>
The command that's passed to the container. This parameter maps to `Cmd` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `COMMAND` parameter to [docker run](https://docs.docker.com/engine/reference/run/). For more information, see [Dockerfile reference: CMD](https://docs.docker.com/engine/reference/builder/#cmd).
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DependsOn`  <a name="cfn-batch-jobdefinition-taskcontainerproperties-dependson"></a>
A list of containers that this container depends on.
*Required*: No
*Type*: Array of [TaskContainerDependency](aws-properties-batch-jobdefinition-taskcontainerdependency.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Environment`  <a name="cfn-batch-jobdefinition-taskcontainerproperties-environment"></a>
The environment variables to pass to a container. This parameter maps to Env in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--env` parameter to [docker run](https://docs.docker.com/engine/reference/run/).
We don't recommend using plaintext environment variables for sensitive information, such as credential data.
Environment variables cannot start with `AWS_BATCH`. This naming convention is reserved for variables that AWS Batch sets.
*Required*: No
*Type*: [Array](aws-properties-batch-jobdefinition-environment.md) of [Environment](aws-properties-batch-jobdefinition-environment.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Essential`  <a name="cfn-batch-jobdefinition-taskcontainerproperties-essential"></a>
If the essential parameter of a container is marked as `true`, and that container fails or stops for any reason, all other containers that are part of the task are stopped. If the `essential` parameter of a container is marked as false, its failure doesn't affect the rest of the containers in a task. If this parameter is omitted, a container is assumed to be essential.
All jobs must have at least one essential container. If you have an application that's composed of multiple containers, group containers that are used for a common purpose into components, and separate the different components into multiple task definitions. For more information, see [Application Architecture](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/application_architecture.html) in the *Amazon Elastic Container Service Developer Guide*.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirelensConfiguration`  <a name="cfn-batch-jobdefinition-taskcontainerproperties-firelensconfiguration"></a>
The FireLens configuration for the container. This is used to specify and configure a log router for container logs. For more information, see [Custom log](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html) routing in the *Amazon Elastic Container Service Developer Guide*.
*Required*: No
*Type*: [FirelensConfiguration](aws-properties-batch-jobdefinition-firelensconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Image`  <a name="cfn-batch-jobdefinition-taskcontainerproperties-image"></a>
The image used to start a container. This string is passed directly to the Docker daemon. By default, images in the Docker Hub registry are available. Other repositories are specified with either `repository-url/image:tag` or `repository-url/image@digest`. Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to `Image` in the [Create a container](https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.35/) and the `IMAGE` parameter of the [https://docs.docker.com/engine/reference/run/#security-configuration](https://docs.docker.com/engine/reference/run/#security-configuration).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LinuxParameters`  <a name="cfn-batch-jobdefinition-taskcontainerproperties-linuxparameters"></a>
Linux-specific modifications that are applied to the container, such as Linux kernel capabilities. For more information, see [KernelCapabilities](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_KernelCapabilities.html).
*Required*: No
*Type*: [LinuxParameters](aws-properties-batch-jobdefinition-linuxparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogConfiguration`  <a name="cfn-batch-jobdefinition-taskcontainerproperties-logconfiguration"></a>
The log configuration specification for the container.
This parameter maps to `LogConfig` in the [Create a container](https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.35/) and the `--log-driver` option to [docker run](https://docs.docker.com/engine/reference/run/#security-configuration).
By default, containers use the same logging driver that the Docker daemon uses. However the container can use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information about the options for different supported log drivers, see [Configure logging drivers ](https://docs.docker.com/engine/admin/logging/overview/) in the *Docker documentation*.
Amazon ECS currently supports a subset of the logging drivers available to the Docker daemon (shown in the `LogConfiguration` data type). Additional log drivers may be available in future releases of the Amazon ECS container agent.
This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: sudo docker version `--format '{{.Server.APIVersion}}'`
The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the `ECS_AVAILABLE_LOGGING_DRIVERS` environment variable before containers placed on that instance can use these log configuration options. For more information, see [Amazon ECS container agent configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html) in the *Amazon Elastic Container Service Developer Guide*.
*Required*: No
*Type*: [LogConfiguration](aws-properties-batch-jobdefinition-logconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MountPoints`  <a name="cfn-batch-jobdefinition-taskcontainerproperties-mountpoints"></a>
The mount points for data volumes in your container.
This parameter maps to `Volumes` in the [Create a container](https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.35/) and the [--volume]() option to [docker run](https://docs.docker.com/engine/reference/run/#security-configuration).
Windows containers can mount whole directories on the same drive as `$env:ProgramData`. Windows containers can't mount directories on a different drive, and mount point can't be across drives.
*Required*: No
*Type*: Array of [MountPoint](aws-properties-batch-jobdefinition-mountpoint.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-batch-jobdefinition-taskcontainerproperties-name"></a>
The name of a container. The name can be used as a unique identifier to target your `dependsOn` and `Overrides` objects.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Privileged`  <a name="cfn-batch-jobdefinition-taskcontainerproperties-privileged"></a>
When this parameter is `true`, the container is given elevated privileges on the host container instance (similar to the `root` user). This parameter maps to `Privileged` in the [Create a container](https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.35/) and the `--privileged` option to [docker run](https://docs.docker.com/engine/reference/run/#security-configuration).
This parameter is not supported for Windows containers or tasks run on Fargate.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReadonlyRootFilesystem`  <a name="cfn-batch-jobdefinition-taskcontainerproperties-readonlyrootfilesystem"></a>
When this parameter is true, the container is given read-only access to its root file system. This parameter maps to `ReadonlyRootfs` in the [Create a container](https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.35/) and the `--read-only` option to [docker run](https://docs.docker.com/engine/reference/run/#security-configuration).
This parameter is not supported for Windows containers.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RepositoryCredentials`  <a name="cfn-batch-jobdefinition-taskcontainerproperties-repositorycredentials"></a>
The private repository authentication credentials to use.
*Required*: No
*Type*: [RepositoryCredentials](aws-properties-batch-jobdefinition-repositorycredentials.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceRequirements`  <a name="cfn-batch-jobdefinition-taskcontainerproperties-resourcerequirements"></a>
The type and amount of a resource to assign to a container. The only supported resource is a GPU.
*Required*: No
*Type*: Array of [ResourceRequirement](aws-properties-batch-jobdefinition-resourcerequirement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Secrets`  <a name="cfn-batch-jobdefinition-taskcontainerproperties-secrets"></a>
The secrets to pass to the container. For more information, see [Specifying Sensitive Data](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html) in the Amazon Elastic Container Service Developer Guide.
*Required*: No
*Type*: Array of [Secret](aws-properties-batch-jobdefinition-secret.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartTimeout`  <a name="cfn-batch-jobdefinition-taskcontainerproperties-starttimeout"></a>
Time duration (in seconds) to wait before giving up on resolving dependencies for a container. The minimum value is 2 seconds and the maximum value for Fargate is 120 seconds.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StopTimeout`  <a name="cfn-batch-jobdefinition-taskcontainerproperties-stoptimeout"></a>
Time duration (in seconds) to wait before the container is forcefully killed if it doesn't exit normally on its own. The minimum value is 2 seconds and the maximum value for Fargate is 120 seconds. If the parameter is not specified, the default value of 30 seconds is used. For tasks that use the EC2 launch type, if the `stopTimeout` parameter isn't specified, the value set for the Amazon ECS container agent configuration variable `ECS_CONTAINER_STOP_TIMEOUT` is used. If neither the `stopTimeout` parameter nor the `ECS_CONTAINER_STOP_TIMEOUT` agent configuration variable are set, then the default value of 30 seconds is used.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ulimits`  <a name="cfn-batch-jobdefinition-taskcontainerproperties-ulimits"></a>
A list of `ulimits` to set in the container. If a `ulimit` value is specified in a task definition, it overrides the default values set by Docker. This parameter maps to `Ulimits` in the [Create a container](https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.35/) and the `--ulimit` option to [docker run](https://docs.docker.com/engine/reference/run/#security-configuration).
Amazon ECS tasks hosted on Fargate use the default resource limit values set by the operating system with the exception of the nofile resource limit parameter which Fargate overrides. The `nofile` resource limit sets a restriction on the number of open files that a container can use. The default `nofile` soft limit is `1024` and the default hard limit is `65535`.
This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: sudo docker version `--format '{{.Server.APIVersion}}'`
This parameter is not supported for Windows containers.
*Required*: No
*Type*: Array of [Ulimit](aws-properties-batch-jobdefinition-ulimit.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`User`  <a name="cfn-batch-jobdefinition-taskcontainerproperties-user"></a>
The user to use inside the container. This parameter maps to User in the Create a container section of the Docker Remote API and the --user option to docker run.
When running tasks using the `host` network mode, don't run containers using the `root user (UID 0)`. We recommend using a non-root user for better security.
You can specify the `user` using the following formats. If specifying a UID or GID, you must specify it as a positive integer.
+  `user`
+  `user:group`
+  `uid`
+  `uid:gid`
+  `user:gi`
+  `uid:group`
This parameter is not supported for Windows containers.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
