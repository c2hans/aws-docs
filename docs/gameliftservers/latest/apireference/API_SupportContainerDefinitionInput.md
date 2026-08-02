---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_SupportContainerDefinitionInput.html
---

# SupportContainerDefinitionInput
<a name="API_SupportContainerDefinitionInput"></a>

Describes a support container in a container group. You can define a support container in either a game server container group or a per-instance container group. Support containers don't run game server processes.

This definition includes container configuration, resources, and start instructions. Use this data type when creating or updating a container group definition. For properties of a deployed support container, see [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html).

 **Use with: ** [CreateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html), [UpdateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html)

## Contents
<a name="API_SupportContainerDefinitionInput_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ContainerName **   <a name="gameliftservers-Type-SupportContainerDefinitionInput-ContainerName"></a>
A string that uniquely identifies the container definition within a container group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9\-]+$`
Required: Yes

 ** ImageUri **   <a name="gameliftservers-Type-SupportContainerDefinitionInput-ImageUri"></a>
The location of the container image to deploy to a container fleet. Provide an image in an Amazon Elastic Container Registry public or private repository. The repository must be in the same AWS account and AWS Region where you're creating the container group definition. For limits on image size, see [Amazon GameLift Servers endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/gamelift.html). You can use any of the following image URI formats:
+ Image ID only: `[AWS account].dkr.ecr.[AWS region].amazonaws.com/[repository ID]`
+ Image ID and digest: `[AWS account].dkr.ecr.[AWS region].amazonaws.com/[repository ID]@[digest]`
+ Image ID and tag: `[AWS account].dkr.ecr.[AWS region].amazonaws.com/[repository ID]:[tag]`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9-_\.@\/:]+$`
Required: Yes

 ** DependsOn **   <a name="gameliftservers-Type-SupportContainerDefinitionInput-DependsOn"></a>
Establishes dependencies between this container and the status of other containers in the same container group. A container can have dependencies on multiple different containers.
.
You can use dependencies to establish a startup/shutdown sequence across the container group. For example, you might specify that *ContainerB* has a `START` dependency on *ContainerA*. This dependency means that *ContainerB* can't start until after *ContainerA* has started. This dependency is reversed on shutdown, which means that *ContainerB* must shut down before *ContainerA* can shut down.
Type: Array of [ContainerDependency](API_ContainerDependency.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** EnvironmentOverride **   <a name="gameliftservers-Type-SupportContainerDefinitionInput-EnvironmentOverride"></a>
A set of environment variables to pass to the container on startup. See the [ContainerDefinition::environment](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-environment) parameter in the *Amazon Elastic Container Service API Reference*.
Type: Array of [ContainerEnvironment](API_ContainerEnvironment.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** Essential **   <a name="gameliftservers-Type-SupportContainerDefinitionInput-Essential"></a>
Flags the container as vital for the container group to function properly. If an essential container fails, the entire container group restarts. At least one support container in a per-instance container group must be essential. When flagging a container as essential, also configure a health check so that the container can signal that it's healthy.
Type: Boolean
Required: No

 ** HealthCheck **   <a name="gameliftservers-Type-SupportContainerDefinitionInput-HealthCheck"></a>
Configuration for a non-terminal health check. A container automatically restarts if it stops functioning. With a health check, you can define additional reasons to flag a container as unhealthy and restart it. If an essential container fails a health check, the entire container group restarts.
Type: [ContainerHealthCheck](API_ContainerHealthCheck.md) object
Required: No

 ** LinuxCapabilities **   <a name="gameliftservers-Type-SupportContainerDefinitionInput-LinuxCapabilities"></a>
Linux-specific modifications that are applied to the default Docker container configuration, such as Linux capabilities. For more information see [LinuxCapabilities](https://docs.aws.amazon.com/gamelift/latest/apireference/API_LinuxCapabilities.html).
Type: [LinuxCapabilities](API_LinuxCapabilities.md) object
Required: No

 ** MemoryHardLimitMebibytes **   <a name="gameliftservers-Type-SupportContainerDefinitionInput-MemoryHardLimitMebibytes"></a>
A specified amount of memory (in MiB) to reserve for this container. If you don't specify a container-specific memory limit, the container shares the container group's total memory allocation.
 **Related data type: ** [ContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html)TotalMemoryLimitMebibytes``
Type: Integer
Valid Range: Minimum value of 4. Maximum value of 1024000.
Required: No

 ** MountPoints **   <a name="gameliftservers-Type-SupportContainerDefinitionInput-MountPoints"></a>
A mount point that binds a path inside the container to a file or directory on the host system and lets it access the file or directory.
Type: Array of [ContainerMountPoint](API_ContainerMountPoint.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** PortConfiguration **   <a name="gameliftservers-Type-SupportContainerDefinitionInput-PortConfiguration"></a>
A set of ports that Amazon GameLift Servers can assign to processes in a container. The container port configuration must have enough ports for each container process that accepts inbound traffic connections. A container port configuration can have can have one or more container port ranges. Each range specifies starting and ending values as well as the supported network protocol.
Container ports aren't directly accessed by inbound traffic. Amazon GameLift Servers maps each container port to an externally accessible connection port (see the container fleet property `ConnectionPortRange`).
Type: [ContainerPortConfiguration](API_ContainerPortConfiguration.md) object
Required: No

 ** Vcpu **   <a name="gameliftservers-Type-SupportContainerDefinitionInput-Vcpu"></a>
The number of vCPU units to reserve for this container. The container can use more resources when needed, if available. If you don't reserve CPU units for this container, it shares the container group's total vCPU limit.
 **Related data type: ** [ContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html) TotalCpuLimit
Type: Double
Valid Range: Minimum value of 0.125. Maximum value of 10.
Required: No

## See Also
<a name="API_SupportContainerDefinitionInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/SupportContainerDefinitionInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/SupportContainerDefinitionInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/SupportContainerDefinitionInput)
