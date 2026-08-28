---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_SupportContainerDefinition.html
---

# SupportContainerDefinition
<a name="API_SupportContainerDefinition"></a>

Describes a support container in a container group. A support container might be in a game server container group or a per-instance container group. Support containers don't run game server processes.

You can update a support container definition and deploy the updates to an existing fleet. When creating or updating a game server container group definition, use the property [GameServerContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html).

 **Part of:** [ContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html)

 **Returned by:** [CreateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html), [DescribeContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeContainerGroupDefinition.html), [ListContainerGroupDefinitions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListContainerGroupDefinitions.html), [ListContainerGroupDefinitionVersions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListContainerGroupDefinitionVersions.html), [UpdateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html)

## Contents
<a name="API_SupportContainerDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ContainerName **   <a name="gameliftservers-Type-SupportContainerDefinition-ContainerName"></a>
The container definition identifier. Container names are unique within a container group definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9\-]+$`
Required: No

 ** DependsOn **   <a name="gameliftservers-Type-SupportContainerDefinition-DependsOn"></a>
Indicates that the container relies on the status of other containers in the same container group during its startup and shutdown sequences. A container might have dependencies on multiple containers.
Type: Array of [ContainerDependency](API_ContainerDependency.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** EnvironmentOverride **   <a name="gameliftservers-Type-SupportContainerDefinition-EnvironmentOverride"></a>
A set of environment variables that's passed to the container on startup. See the [ContainerDefinition::environment](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-environment) parameter in the *Amazon Elastic Container Service API Reference*.
Type: Array of [ContainerEnvironment](API_ContainerEnvironment.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** Essential **   <a name="gameliftservers-Type-SupportContainerDefinition-Essential"></a>
Indicates whether the container is vital to the container group. If an essential container fails, the entire container group restarts.
Type: Boolean
Required: No

 ** HealthCheck **   <a name="gameliftservers-Type-SupportContainerDefinition-HealthCheck"></a>
A configuration for a non-terminal health check. A support container automatically restarts if it stops functioning or if it fails this health check.
Type: [ContainerHealthCheck](API_ContainerHealthCheck.md) object
Required: No

 ** ImageUri **   <a name="gameliftservers-Type-SupportContainerDefinition-ImageUri"></a>
The URI to the image that Amazon GameLift Servers deploys to a container fleet. For a more specific identifier, see `ResolvedImageDigest`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9-_\.@\/:]+$`
Required: No

 ** LinuxCapabilities **   <a name="gameliftservers-Type-SupportContainerDefinition-LinuxCapabilities"></a>
Linux-specific modifications that are applied to the default Docker container configuration, such as Linux capabilities. For more information see [LinuxCapabilities](https://docs.aws.amazon.com/gamelift/latest/apireference/API_LinuxCapabilities.html).
Type: [LinuxCapabilities](API_LinuxCapabilities.md) object
Required: No

 ** MemoryHardLimitMebibytes **   <a name="gameliftservers-Type-SupportContainerDefinition-MemoryHardLimitMebibytes"></a>
The amount of memory that Amazon GameLift Servers makes available to the container. If memory limits aren't set for an individual container, the container shares the container group's total memory allocation.
 **Related data type: ** [ContainerGroupDefinition TotalMemoryLimitMebibytes](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html)
Type: Integer
Valid Range: Minimum value of 4. Maximum value of 1024000.
Required: No

 ** MountPoints **   <a name="gameliftservers-Type-SupportContainerDefinition-MountPoints"></a>
A mount point that binds a path inside the container to a file or directory on the host system and lets it access the file or directory.
Type: Array of [ContainerMountPoint](API_ContainerMountPoint.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** PortConfiguration **   <a name="gameliftservers-Type-SupportContainerDefinition-PortConfiguration"></a>
A set of ports that allow access to the container from external users. Processes running in the container can bind to a one of these ports. Container ports aren't directly accessed by inbound traffic. Amazon GameLift Servers maps these container ports to externally accessible connection ports, which are assigned as needed from the container fleet's `ConnectionPortRange`.
Type: [ContainerPortConfiguration](API_ContainerPortConfiguration.md) object
Required: No

 ** ResolvedImageDigest **   <a name="gameliftservers-Type-SupportContainerDefinition-ResolvedImageDigest"></a>
A unique and immutable identifier for the container image. The digest is a SHA 256 hash of the container image manifest.
Type: String
Pattern: `^sha256:[a-fA-F0-9]{64}$`
Required: No

 ** Vcpu **   <a name="gameliftservers-Type-SupportContainerDefinition-Vcpu"></a>
The number of vCPU units that are reserved for the container. If no resources are reserved, the container shares the total vCPU limit for the container group.
 **Related data type: ** [ContainerGroupDefinition TotalVcpuLimit](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html)
Type: Double
Valid Range: Minimum value of 0.125. Maximum value of 10.
Required: No

## See Also
<a name="API_SupportContainerDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/SupportContainerDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/SupportContainerDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/SupportContainerDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
