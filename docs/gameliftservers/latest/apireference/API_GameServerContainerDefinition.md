---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GameServerContainerDefinition.html
---

# GameServerContainerDefinition
<a name="API_GameServerContainerDefinition"></a>

Describes the game server container in an existing game server container group. A game server container identifies a container image with your game server build. A game server container is automatically considered essential; if an essential container fails, the entire container group restarts.

You can update a container definition and deploy the updates to an existing fleet. When creating or updating a game server container group definition, use the property [https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput).

 **Part of:** [ContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html)

 **Returned by:** [CreateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html), [DescribeContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeContainerGroupDefinition.html), [ListContainerGroupDefinitions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListContainerGroupDefinitions.html), [ListContainerGroupDefinitionVersions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListContainerGroupDefinitionVersions.html), [UpdateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html)

## Contents
<a name="API_GameServerContainerDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ContainerName **   <a name="gameliftservers-Type-GameServerContainerDefinition-ContainerName"></a>
The container definition identifier. Container names are unique within a container group definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9\-]+$`
Required: No

 ** DependsOn **   <a name="gameliftservers-Type-GameServerContainerDefinition-DependsOn"></a>
Indicates that the container relies on the status of other containers in the same container group during startup and shutdown sequences. A container might have dependencies on multiple containers.
Type: Array of [ContainerDependency](API_ContainerDependency.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** EnvironmentOverride **   <a name="gameliftservers-Type-GameServerContainerDefinition-EnvironmentOverride"></a>
A set of environment variables that's passed to the container on startup. See the [ContainerDefinition::environment](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-environment) parameter in the *Amazon Elastic Container Service API Reference*.
Type: Array of [ContainerEnvironment](API_ContainerEnvironment.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** ImageUri **   <a name="gameliftservers-Type-GameServerContainerDefinition-ImageUri"></a>
The URI to the image that Amazon GameLift Servers uses when deploying this container to a container fleet. For a more specific identifier, see `ResolvedImageDigest`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9-_\.@\/:]+$`
Required: No

 ** LinuxCapabilities **   <a name="gameliftservers-Type-GameServerContainerDefinition-LinuxCapabilities"></a>
Linux-specific modifications that are applied to the default Docker container configuration, such as Linux capabilities. For more information see [LinuxCapabilities](https://docs.aws.amazon.com/gamelift/latest/apireference/API_LinuxCapabilities.html).
Type: [LinuxCapabilities](API_LinuxCapabilities.md) object
Required: No

 ** MountPoints **   <a name="gameliftservers-Type-GameServerContainerDefinition-MountPoints"></a>
A mount point that binds a path inside the container to a file or directory on the host system and lets it access the file or directory.
Type: Array of [ContainerMountPoint](API_ContainerMountPoint.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** PortConfiguration **   <a name="gameliftservers-Type-GameServerContainerDefinition-PortConfiguration"></a>
The set of ports that are available to bind to processes in the container. For example, a game server process requires a container port to allow game clients to connect to it. Container ports aren't directly accessed by inbound traffic. Amazon GameLift Servers maps these container ports to externally accessible connection ports, which are assigned as needed from the container fleet's `ConnectionPortRange`.
Type: [ContainerPortConfiguration](API_ContainerPortConfiguration.md) object
Required: No

 ** ResolvedImageDigest **   <a name="gameliftservers-Type-GameServerContainerDefinition-ResolvedImageDigest"></a>
A unique and immutable identifier for the container image. The digest is a SHA 256 hash of the container image manifest.
Type: String
Pattern: `^sha256:[a-fA-F0-9]{64}$`
Required: No

 ** ServerSdkVersion **   <a name="gameliftservers-Type-GameServerContainerDefinition-ServerSdkVersion"></a>
The Amazon GameLift Servers server SDK version that the game server is integrated with. Only game servers using 5.2.0 or higher are compatible with container fleets.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^\d+\.\d+\.\d+$`
Required: No

## See Also
<a name="API_GameServerContainerDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/GameServerContainerDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/GameServerContainerDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/GameServerContainerDefinition)
