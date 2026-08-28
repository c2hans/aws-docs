---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DaemonContainerDefinition.html
---

# DaemonContainerDefinition
<a name="API_DaemonContainerDefinition"></a>

A container definition for a daemon task. Daemon container definitions describe the containers that run as part of a daemon task on container instances managed by capacity providers.

## Contents
<a name="API_DaemonContainerDefinition_Contents"></a>

 ** image **   <a name="ECS-Type-DaemonContainerDefinition-image"></a>
The image used to start the container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with either ` repository-url/image:tag ` or ` repository-url/image@digest `.
Type: String
Required: Yes

 ** command **   <a name="ECS-Type-DaemonContainerDefinition-command"></a>
The command that's passed to the container.
Type: Array of strings
Required: No

 ** cpu **   <a name="ECS-Type-DaemonContainerDefinition-cpu"></a>
The number of `cpu` units reserved for the container.
Type: Integer
Required: No

 ** dependsOn **   <a name="ECS-Type-DaemonContainerDefinition-dependsOn"></a>
The dependencies defined for container startup and shutdown. A container can contain multiple dependencies on other containers in a task definition.
Type: Array of [ContainerDependency](API_ContainerDependency.md) objects
Required: No

 ** entryPoint **   <a name="ECS-Type-DaemonContainerDefinition-entryPoint"></a>
The entry point that's passed to the container.
Type: Array of strings
Required: No

 ** environment **   <a name="ECS-Type-DaemonContainerDefinition-environment"></a>
The environment variables to pass to a container.
Type: Array of [KeyValuePair](API_KeyValuePair.md) objects
Required: No

 ** environmentFiles **   <a name="ECS-Type-DaemonContainerDefinition-environmentFiles"></a>
A list of files containing the environment variables to pass to a container.
Type: Array of [EnvironmentFile](API_EnvironmentFile.md) objects
Required: No

 ** essential **   <a name="ECS-Type-DaemonContainerDefinition-essential"></a>
If the `essential` parameter of a container is marked as `true`, and that container fails or stops for any reason, all other containers that are part of the task are stopped.
Type: Boolean
Required: No

 ** firelensConfiguration **   <a name="ECS-Type-DaemonContainerDefinition-firelensConfiguration"></a>
The FireLens configuration for the container. This is used to specify and configure a log router for container logs.
Type: [FirelensConfiguration](API_FirelensConfiguration.md) object
Required: No

 ** healthCheck **   <a name="ECS-Type-DaemonContainerDefinition-healthCheck"></a>
The container health check command and associated configuration parameters for the container.
Type: [HealthCheck](API_HealthCheck.md) object
Required: No

 ** interactive **   <a name="ECS-Type-DaemonContainerDefinition-interactive"></a>
When this parameter is `true`, you can deploy containerized applications that require `stdin` or a `tty` to be allocated.
Type: Boolean
Required: No

 ** linuxParameters **   <a name="ECS-Type-DaemonContainerDefinition-linuxParameters"></a>
Linux-specific modifications that are applied to the container configuration, such as Linux kernel capabilities.
Type: [DaemonLinuxParameters](API_DaemonLinuxParameters.md) object
Required: No

 ** logConfiguration **   <a name="ECS-Type-DaemonContainerDefinition-logConfiguration"></a>
The log configuration specification for the container.
Type: [LogConfiguration](API_LogConfiguration.md) object
Required: No

 ** memory **   <a name="ECS-Type-DaemonContainerDefinition-memory"></a>
The amount (in MiB) of memory to present to the container. If the container attempts to exceed the memory specified here, the container is killed.
Type: Integer
Required: No

 ** memoryReservation **   <a name="ECS-Type-DaemonContainerDefinition-memoryReservation"></a>
The soft limit (in MiB) of memory to reserve for the container.
Type: Integer
Required: No

 ** mountPoints **   <a name="ECS-Type-DaemonContainerDefinition-mountPoints"></a>
The mount points for data volumes in your container.
Type: Array of [MountPoint](API_MountPoint.md) objects
Required: No

 ** name **   <a name="ECS-Type-DaemonContainerDefinition-name"></a>
The name of the container. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.
Type: String
Required: No

 ** privileged **   <a name="ECS-Type-DaemonContainerDefinition-privileged"></a>
When this parameter is true, the container is given elevated privileges on the host container instance (similar to the `root` user).
Type: Boolean
Required: No

 ** pseudoTerminal **   <a name="ECS-Type-DaemonContainerDefinition-pseudoTerminal"></a>
When this parameter is `true`, a TTY is allocated.
Type: Boolean
Required: No

 ** readonlyRootFilesystem **   <a name="ECS-Type-DaemonContainerDefinition-readonlyRootFilesystem"></a>
When this parameter is true, the container is given read-only access to its root file system.
Type: Boolean
Required: No

 ** repositoryCredentials **   <a name="ECS-Type-DaemonContainerDefinition-repositoryCredentials"></a>
The private repository authentication credentials to use.
Type: [RepositoryCredentials](API_RepositoryCredentials.md) object
Required: No

 ** restartPolicy **   <a name="ECS-Type-DaemonContainerDefinition-restartPolicy"></a>
The restart policy for the container. When you set up a restart policy, Amazon ECS can restart the container without needing to replace the task.
Type: [ContainerRestartPolicy](API_ContainerRestartPolicy.md) object
Required: No

 ** secrets **   <a name="ECS-Type-DaemonContainerDefinition-secrets"></a>
The secrets to pass to the container.
Type: Array of [Secret](API_Secret.md) objects
Required: No

 ** startTimeout **   <a name="ECS-Type-DaemonContainerDefinition-startTimeout"></a>
Time duration (in seconds) to wait before giving up on resolving dependencies for a container.
Type: Integer
Required: No

 ** stopTimeout **   <a name="ECS-Type-DaemonContainerDefinition-stopTimeout"></a>
Time duration (in seconds) to wait before the container is forcefully killed if it doesn't exit normally on its own.
Type: Integer
Required: No

 ** systemControls **   <a name="ECS-Type-DaemonContainerDefinition-systemControls"></a>
A list of namespaced kernel parameters to set in the container.
Type: Array of [SystemControl](API_SystemControl.md) objects
Required: No

 ** ulimits **   <a name="ECS-Type-DaemonContainerDefinition-ulimits"></a>
A list of `ulimits` to set in the container.
Type: Array of [Ulimit](API_Ulimit.md) objects
Required: No

 ** user **   <a name="ECS-Type-DaemonContainerDefinition-user"></a>
The user to use inside the container.
Type: String
Required: No

 ** workingDirectory **   <a name="ECS-Type-DaemonContainerDefinition-workingDirectory"></a>
The working directory to run commands inside the container in.
Type: String
Required: No

## See Also
<a name="API_DaemonContainerDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DaemonContainerDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DaemonContainerDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DaemonContainerDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
