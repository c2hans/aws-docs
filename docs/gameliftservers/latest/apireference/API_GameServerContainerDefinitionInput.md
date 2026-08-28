---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GameServerContainerDefinitionInput.html
---

# GameServerContainerDefinitionInput
<a name="API_GameServerContainerDefinitionInput"></a>

Describes the configuration for a container that runs your game server executable. This definition includes container configuration, resources, and start instructions. Use this data type when creating or updating a game server container group definition. For properties of a deployed container, see [GameServerContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html). A game server container is automatically considered essential; if an essential container fails, the entire container group restarts.

 **Use with: ** [CreateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html), [UpdateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html)

## Contents
<a name="API_GameServerContainerDefinitionInput_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ContainerName **   <a name="gameliftservers-Type-GameServerContainerDefinitionInput-ContainerName"></a>
A string that uniquely identifies the container definition within a container group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9\-]+$`
Required: Yes

 ** ImageUri **   <a name="gameliftservers-Type-GameServerContainerDefinitionInput-ImageUri"></a>
The location of the container image to deploy to a container fleet. Provide an image in an Amazon Elastic Container Registry public or private repository. The repository must be in the same AWS account and AWS Region where you're creating the container group definition. For limits on image size, see [Amazon GameLift Servers endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/gamelift.html). You can use any of the following image URI formats:
+ Image ID only: `[AWS account].dkr.ecr.[AWS region].amazonaws.com/[repository ID]`
+ Image ID and digest: `[AWS account].dkr.ecr.[AWS region].amazonaws.com/[repository ID]@[digest]`
+ Image ID and tag: `[AWS account].dkr.ecr.[AWS region].amazonaws.com/[repository ID]:[tag]`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9-_\.@\/:]+$`
Required: Yes

 ** PortConfiguration **   <a name="gameliftservers-Type-GameServerContainerDefinitionInput-PortConfiguration"></a>
A set of ports that Amazon GameLift Servers can assign to processes in a container. The container port configuration must have enough ports for each container process that accepts inbound traffic connections. For example, a game server process requires a container port to allow game clients to connect to it. A container port configuration can have can have one or more container port ranges. Each range specifies starting and ending values as well as the supported network protocol.
Container ports aren't directly accessed by inbound traffic. Amazon GameLift Servers maps each container port to an externally accessible connection port (see the container fleet property `ConnectionPortRange`).
Type: [ContainerPortConfiguration](API_ContainerPortConfiguration.md) object
Required: Yes

 ** ServerSdkVersion **   <a name="gameliftservers-Type-GameServerContainerDefinitionInput-ServerSdkVersion"></a>
The Amazon GameLift Servers server SDK version that the game server is integrated with. Only game servers using 5.2.0 or higher are compatible with container fleets.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^\d+\.\d+\.\d+$`
Required: Yes

 ** DependsOn **   <a name="gameliftservers-Type-GameServerContainerDefinitionInput-DependsOn"></a>
Establishes dependencies between this container and the status of other containers in the same container group. A container can have dependencies on multiple different containers.
You can use dependencies to establish a startup/shutdown sequence across the container group. For example, you might specify that *ContainerB* has a `START` dependency on *ContainerA*. This dependency means that *ContainerB* can't start until after *ContainerA* has started. This dependency is reversed on shutdown, which means that *ContainerB* must shut down before *ContainerA* can shut down.
Type: Array of [ContainerDependency](API_ContainerDependency.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** EnvironmentOverride **   <a name="gameliftservers-Type-GameServerContainerDefinitionInput-EnvironmentOverride"></a>
A set of environment variables to pass to the container on startup. See the [ContainerDefinition::environment](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-environment) parameter in the *Amazon Elastic Container Service API Reference*.
Type: Array of [ContainerEnvironment](API_ContainerEnvironment.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** LinuxCapabilities **   <a name="gameliftservers-Type-GameServerContainerDefinitionInput-LinuxCapabilities"></a>
Linux-specific modifications that are applied to the default Docker container configuration, such as Linux capabilities. For more information see [LinuxCapabilities](https://docs.aws.amazon.com/gamelift/latest/apireference/API_LinuxCapabilities.html).
Type: [LinuxCapabilities](API_LinuxCapabilities.md) object
Required: No

 ** MountPoints **   <a name="gameliftservers-Type-GameServerContainerDefinitionInput-MountPoints"></a>
A mount point that binds a path inside the container to a file or directory on the host system and lets it access the file or directory.
Type: Array of [ContainerMountPoint](API_ContainerMountPoint.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_GameServerContainerDefinitionInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/GameServerContainerDefinitionInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/GameServerContainerDefinitionInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/GameServerContainerDefinitionInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
