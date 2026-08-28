---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-containergroupdefinition-gameservercontainerdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::ContainerGroupDefinition GameServerContainerDefinition
<a name="aws-properties-gamelift-containergroupdefinition-gameservercontainerdefinition"></a>

Describes the game server container in an existing game server container group. A game server container identifies a container image with your game server build. A game server container is automatically considered essential; if an essential container fails, the entire container group restarts.

You can update a container definition and deploy the updates to an existing fleet. When creating or updating a game server container group definition, use the property [https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput).

 **Part of:** [ContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html)

**Returned by:**[CreateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html), [DescribeContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeContainerGroupDefinition.html), [ListContainerGroupDefinitions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListContainerGroupDefinitions.html), [ListContainerGroupDefinitionVersions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListContainerGroupDefinitionVersions.html), [UpdateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html)

## Syntax
<a name="aws-properties-gamelift-containergroupdefinition-gameservercontainerdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-containergroupdefinition-gameservercontainerdefinition-syntax.json"></a>

```
{
  "[ContainerName](#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-containername)" : {{String}},
  "[DependsOn](#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-dependson)" : {{[ ContainerDependency, ... ]}},
  "[EnvironmentOverride](#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-environmentoverride)" : {{[ ContainerEnvironment, ... ]}},
  "[ImageUri](#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-imageuri)" : {{String}},
  "[LinuxCapabilities](#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-linuxcapabilities)" : {{LinuxCapabilities}},
  "[MountPoints](#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-mountpoints)" : {{[ ContainerMountPoint, ... ]}},
  "[PortConfiguration](#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-portconfiguration)" : {{PortConfiguration}},
  "[ResolvedImageDigest](#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-resolvedimagedigest)" : {{String}},
  "[ServerSdkVersion](#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-serversdkversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-gamelift-containergroupdefinition-gameservercontainerdefinition-syntax.yaml"></a>

```
  [ContainerName](#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-containername): {{String}}
  [DependsOn](#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-dependson): {{
    - ContainerDependency}}
  [EnvironmentOverride](#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-environmentoverride): {{
    - ContainerEnvironment}}
  [ImageUri](#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-imageuri): {{String}}
  [LinuxCapabilities](#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-linuxcapabilities): {{
    LinuxCapabilities}}
  [MountPoints](#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-mountpoints): {{
    - ContainerMountPoint}}
  [PortConfiguration](#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-portconfiguration): {{
    PortConfiguration}}
  [ResolvedImageDigest](#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-resolvedimagedigest): {{String}}
  [ServerSdkVersion](#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-serversdkversion): {{String}}
```

## Properties
<a name="aws-properties-gamelift-containergroupdefinition-gameservercontainerdefinition-properties"></a>

`ContainerName`  <a name="cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-containername"></a>
The container definition identifier. Container names are unique within a container group definition.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DependsOn`  <a name="cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-dependson"></a>
Indicates that the container relies on the status of other containers in the same container group during startup and shutdown sequences. A container might have dependencies on multiple containers.
*Required*: No
*Type*: Array of [ContainerDependency](aws-properties-gamelift-containergroupdefinition-containerdependency.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentOverride`  <a name="cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-environmentoverride"></a>
A set of environment variables that's passed to the container on startup. See the [ContainerDefinition::environment](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-environment) parameter in the *Amazon Elastic Container Service API Reference*.
*Required*: No
*Type*: Array of [ContainerEnvironment](aws-properties-gamelift-containergroupdefinition-containerenvironment.md)
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageUri`  <a name="cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-imageuri"></a>
The URI to the image that Amazon GameLift Servers uses when deploying this container to a container fleet. For a more specific identifier, see `ResolvedImageDigest`.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_\.@\/:]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LinuxCapabilities`  <a name="cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-linuxcapabilities"></a>
Linux-specific modifications that are applied to the default Docker container configuration, such as Linux capabilities. For more information see [LinuxCapabilities](https://docs.aws.amazon.com/gamelift/latest/apireference/API_LinuxCapabilities.html).
*Required*: No
*Type*: [LinuxCapabilities](aws-properties-gamelift-containergroupdefinition-linuxcapabilities.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MountPoints`  <a name="cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-mountpoints"></a>
A mount point that binds a path inside the container to a file or directory on the host system and lets it access the file or directory.
*Required*: No
*Type*: Array of [ContainerMountPoint](aws-properties-gamelift-containergroupdefinition-containermountpoint.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PortConfiguration`  <a name="cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-portconfiguration"></a>
The set of ports that are available to bind to processes in the container. For example, a game server process requires a container port to allow game clients to connect to it. Container ports aren't directly accessed by inbound traffic. Amazon GameLift Servers maps these container ports to externally accessible connection ports, which are assigned as needed from the container fleet's `ConnectionPortRange`.
*Required*: No
*Type*: [PortConfiguration](aws-properties-gamelift-containergroupdefinition-portconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResolvedImageDigest`  <a name="cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-resolvedimagedigest"></a>
A unique and immutable identifier for the container image. The digest is a SHA 256 hash of the container image manifest.
*Required*: No
*Type*: String
*Pattern*: `^sha256:[a-fA-F0-9]{64}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerSdkVersion`  <a name="cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-serversdkversion"></a>
The Amazon GameLift Servers server SDK version that the game server is integrated with. Only game servers using 5.2.0 or higher are compatible with container fleets.
*Required*: Yes
*Type*: String
*Pattern*: `^\d+\.\d+\.\d+$`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
