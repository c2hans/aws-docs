---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-daemontaskdefinition-daemoncontainerdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::DaemonTaskDefinition DaemonContainerDefinition
<a name="aws-properties-ecs-daemontaskdefinition-daemoncontainerdefinition"></a>

A container definition for a daemon task. Daemon container definitions describe the containers that run as part of a daemon task on container instances managed by capacity providers.

## Syntax
<a name="aws-properties-ecs-daemontaskdefinition-daemoncontainerdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-daemontaskdefinition-daemoncontainerdefinition-syntax.json"></a>

```
{
  "[Command](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-command)" : {{[ String, ... ]}},
  "[Cpu](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-cpu)" : {{Integer}},
  "[DependsOn](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-dependson)" : {{[ ContainerDependency, ... ]}},
  "[EntryPoint](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-entrypoint)" : {{[ String, ... ]}},
  "[Environment](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-environment)" : {{[ KeyValuePair, ... ]}},
  "[EnvironmentFiles](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-environmentfiles)" : {{[ EnvironmentFile, ... ]}},
  "[Essential](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-essential)" : {{Boolean}},
  "[FirelensConfiguration](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-firelensconfiguration)" : {{FirelensConfiguration}},
  "[HealthCheck](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-healthcheck)" : {{HealthCheck}},
  "[Image](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-image)" : {{String}},
  "[Interactive](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-interactive)" : {{Boolean}},
  "[LinuxParameters](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-linuxparameters)" : {{LinuxParameters}},
  "[LogConfiguration](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-logconfiguration)" : {{LogConfiguration}},
  "[Memory](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-memory)" : {{Integer}},
  "[MemoryReservation](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-memoryreservation)" : {{Integer}},
  "[MountPoints](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-mountpoints)" : {{[ MountPoint, ... ]}},
  "[Name](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-name)" : {{String}},
  "[Privileged](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-privileged)" : {{Boolean}},
  "[PseudoTerminal](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-pseudoterminal)" : {{Boolean}},
  "[ReadonlyRootFilesystem](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-readonlyrootfilesystem)" : {{Boolean}},
  "[RepositoryCredentials](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-repositorycredentials)" : {{RepositoryCredentials}},
  "[RestartPolicy](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-restartpolicy)" : {{RestartPolicy}},
  "[Secrets](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-secrets)" : {{[ Secret, ... ]}},
  "[StartTimeout](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-starttimeout)" : {{Integer}},
  "[StopTimeout](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-stoptimeout)" : {{Integer}},
  "[SystemControls](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-systemcontrols)" : {{[ SystemControl, ... ]}},
  "[Ulimits](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-ulimits)" : {{[ Ulimit, ... ]}},
  "[User](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-user)" : {{String}},
  "[WorkingDirectory](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-workingdirectory)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-daemontaskdefinition-daemoncontainerdefinition-syntax.yaml"></a>

```
  [Command](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-command): {{
    - String}}
  [Cpu](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-cpu): {{Integer}}
  [DependsOn](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-dependson): {{
    - ContainerDependency}}
  [EntryPoint](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-entrypoint): {{
    - String}}
  [Environment](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-environment): {{
    - KeyValuePair}}
  [EnvironmentFiles](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-environmentfiles): {{
    - EnvironmentFile}}
  [Essential](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-essential): {{Boolean}}
  [FirelensConfiguration](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-firelensconfiguration): {{
    FirelensConfiguration}}
  [HealthCheck](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-healthcheck): {{
    HealthCheck}}
  [Image](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-image): {{String}}
  [Interactive](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-interactive): {{Boolean}}
  [LinuxParameters](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-linuxparameters): {{
    LinuxParameters}}
  [LogConfiguration](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-logconfiguration): {{
    LogConfiguration}}
  [Memory](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-memory): {{Integer}}
  [MemoryReservation](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-memoryreservation): {{Integer}}
  [MountPoints](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-mountpoints): {{
    - MountPoint}}
  [Name](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-name): {{String}}
  [Privileged](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-privileged): {{Boolean}}
  [PseudoTerminal](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-pseudoterminal): {{Boolean}}
  [ReadonlyRootFilesystem](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-readonlyrootfilesystem): {{Boolean}}
  [RepositoryCredentials](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-repositorycredentials): {{
    RepositoryCredentials}}
  [RestartPolicy](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-restartpolicy): {{
    RestartPolicy}}
  [Secrets](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-secrets): {{
    - Secret}}
  [StartTimeout](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-starttimeout): {{Integer}}
  [StopTimeout](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-stoptimeout): {{Integer}}
  [SystemControls](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-systemcontrols): {{
    - SystemControl}}
  [Ulimits](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-ulimits): {{
    - Ulimit}}
  [User](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-user): {{String}}
  [WorkingDirectory](#cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-workingdirectory): {{String}}
```

## Properties
<a name="aws-properties-ecs-daemontaskdefinition-daemoncontainerdefinition-properties"></a>

`Command`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-command"></a>
The command that's passed to the container.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Cpu`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-cpu"></a>
The number of `cpu` units reserved for the container.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DependsOn`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-dependson"></a>
The dependencies defined for container startup and shutdown. A container can contain multiple dependencies on other containers in a task definition.
*Required*: No
*Type*: Array of [ContainerDependency](aws-properties-ecs-daemontaskdefinition-containerdependency.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EntryPoint`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-entrypoint"></a>
The entry point that's passed to the container.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Environment`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-environment"></a>
The environment variables to pass to a container.
*Required*: No
*Type*: Array of [KeyValuePair](aws-properties-ecs-daemontaskdefinition-keyvaluepair.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnvironmentFiles`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-environmentfiles"></a>
A list of files containing the environment variables to pass to a container.
*Required*: No
*Type*: Array of [EnvironmentFile](aws-properties-ecs-daemontaskdefinition-environmentfile.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Essential`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-essential"></a>
If the `essential` parameter of a container is marked as `true`, and that container fails or stops for any reason, all other containers that are part of the task are stopped.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FirelensConfiguration`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-firelensconfiguration"></a>
The FireLens configuration for the container. This is used to specify and configure a log router for container logs.
*Required*: No
*Type*: [FirelensConfiguration](aws-properties-ecs-daemontaskdefinition-firelensconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HealthCheck`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-healthcheck"></a>
The container health check command and associated configuration parameters for the container.
*Required*: No
*Type*: [HealthCheck](aws-properties-ecs-daemontaskdefinition-healthcheck.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Image`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-image"></a>
The image used to start the container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with either `repository-url/image:tag` or `repository-url/image@digest`.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Interactive`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-interactive"></a>
When this parameter is `true`, you can deploy containerized applications that require `stdin` or a `tty` to be allocated.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LinuxParameters`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-linuxparameters"></a>
Linux-specific modifications that are applied to the container configuration, such as Linux kernel capabilities.
*Required*: No
*Type*: [LinuxParameters](aws-properties-ecs-daemontaskdefinition-linuxparameters.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LogConfiguration`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-logconfiguration"></a>
The log configuration specification for the container.
*Required*: No
*Type*: [LogConfiguration](aws-properties-ecs-daemontaskdefinition-logconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Memory`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-memory"></a>
The amount (in MiB) of memory to present to the container. If the container attempts to exceed the memory specified here, the container is killed.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MemoryReservation`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-memoryreservation"></a>
The soft limit (in MiB) of memory to reserve for the container.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MountPoints`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-mountpoints"></a>
The mount points for data volumes in your container.
*Required*: No
*Type*: Array of [MountPoint](aws-properties-ecs-daemontaskdefinition-mountpoint.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-name"></a>
The name of the container. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Privileged`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-privileged"></a>
When this parameter is true, the container is given elevated privileges on the host container instance (similar to the `root` user).
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PseudoTerminal`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-pseudoterminal"></a>
When this parameter is `true`, a TTY is allocated.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReadonlyRootFilesystem`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-readonlyrootfilesystem"></a>
When this parameter is true, the container is given read-only access to its root file system.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RepositoryCredentials`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-repositorycredentials"></a>
The private repository authentication credentials to use.
*Required*: No
*Type*: [RepositoryCredentials](aws-properties-ecs-daemontaskdefinition-repositorycredentials.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RestartPolicy`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-restartpolicy"></a>
The restart policy for the container. When you set up a restart policy, Amazon ECS can restart the container without needing to replace the task.
*Required*: No
*Type*: [RestartPolicy](aws-properties-ecs-daemontaskdefinition-restartpolicy.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Secrets`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-secrets"></a>
The secrets to pass to the container.
*Required*: No
*Type*: Array of [Secret](aws-properties-ecs-daemontaskdefinition-secret.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StartTimeout`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-starttimeout"></a>
Time duration (in seconds) to wait before giving up on resolving dependencies for a container.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StopTimeout`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-stoptimeout"></a>
Time duration (in seconds) to wait before the container is forcefully killed if it doesn't exit normally on its own.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SystemControls`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-systemcontrols"></a>
A list of namespaced kernel parameters to set in the container.
*Required*: No
*Type*: Array of [SystemControl](aws-properties-ecs-daemontaskdefinition-systemcontrol.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ulimits`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-ulimits"></a>
A list of `ulimits` to set in the container.
*Required*: No
*Type*: Array of [Ulimit](aws-properties-ecs-daemontaskdefinition-ulimit.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`User`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-user"></a>
The user to use inside the container.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WorkingDirectory`  <a name="cfn-ecs-daemontaskdefinition-daemoncontainerdefinition-workingdirectory"></a>
The working directory to run commands inside the container in.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
