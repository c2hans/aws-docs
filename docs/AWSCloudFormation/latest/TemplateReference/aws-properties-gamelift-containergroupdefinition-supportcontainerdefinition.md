---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-containergroupdefinition-supportcontainerdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::ContainerGroupDefinition SupportContainerDefinition
<a name="aws-properties-gamelift-containergroupdefinition-supportcontainerdefinition"></a>

Describes a support container in a container group. A support container might be in a game server container group or a per-instance container group. Support containers don't run game server processes.

You can update a support container definition and deploy the updates to an existing fleet. When creating or updating a game server container group definition, use the property [GameServerContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html).

 **Part of:** [ContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html)

**Returned by:**[CreateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html), [DescribeContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeContainerGroupDefinition.html), [ListContainerGroupDefinitions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListContainerGroupDefinitions.html), [ListContainerGroupDefinitionVersions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListContainerGroupDefinitionVersions.html), [UpdateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html)

## Syntax
<a name="aws-properties-gamelift-containergroupdefinition-supportcontainerdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-containergroupdefinition-supportcontainerdefinition-syntax.json"></a>

```
{
  "[ContainerName](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-containername)" : {{String}},
  "[DependsOn](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-dependson)" : {{[ ContainerDependency, ... ]}},
  "[EnvironmentOverride](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-environmentoverride)" : {{[ ContainerEnvironment, ... ]}},
  "[Essential](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-essential)" : {{Boolean}},
  "[HealthCheck](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-healthcheck)" : {{ContainerHealthCheck}},
  "[ImageUri](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-imageuri)" : {{String}},
  "[LinuxCapabilities](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-linuxcapabilities)" : {{LinuxCapabilities}},
  "[MemoryHardLimitMebibytes](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-memoryhardlimitmebibytes)" : {{Integer}},
  "[MountPoints](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-mountpoints)" : {{[ ContainerMountPoint, ... ]}},
  "[PortConfiguration](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-portconfiguration)" : {{PortConfiguration}},
  "[ResolvedImageDigest](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-resolvedimagedigest)" : {{String}},
  "[Vcpu](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-vcpu)" : {{Number}}
}
```

### YAML
<a name="aws-properties-gamelift-containergroupdefinition-supportcontainerdefinition-syntax.yaml"></a>

```
  [ContainerName](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-containername): {{String}}
  [DependsOn](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-dependson): {{
    - ContainerDependency}}
  [EnvironmentOverride](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-environmentoverride): {{
    - ContainerEnvironment}}
  [Essential](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-essential): {{Boolean}}
  [HealthCheck](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-healthcheck): {{
    ContainerHealthCheck}}
  [ImageUri](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-imageuri): {{String}}
  [LinuxCapabilities](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-linuxcapabilities): {{
    LinuxCapabilities}}
  [MemoryHardLimitMebibytes](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-memoryhardlimitmebibytes): {{Integer}}
  [MountPoints](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-mountpoints): {{
    - ContainerMountPoint}}
  [PortConfiguration](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-portconfiguration): {{
    PortConfiguration}}
  [ResolvedImageDigest](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-resolvedimagedigest): {{String}}
  [Vcpu](#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-vcpu): {{Number}}
```

## Properties
<a name="aws-properties-gamelift-containergroupdefinition-supportcontainerdefinition-properties"></a>

`ContainerName`  <a name="cfn-gamelift-containergroupdefinition-supportcontainerdefinition-containername"></a>
The container definition identifier. Container names are unique within a container group definition.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DependsOn`  <a name="cfn-gamelift-containergroupdefinition-supportcontainerdefinition-dependson"></a>
Indicates that the container relies on the status of other containers in the same container group during its startup and shutdown sequences. A container might have dependencies on multiple containers.
*Required*: No
*Type*: Array of [ContainerDependency](aws-properties-gamelift-containergroupdefinition-containerdependency.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentOverride`  <a name="cfn-gamelift-containergroupdefinition-supportcontainerdefinition-environmentoverride"></a>
A set of environment variables that's passed to the container on startup. See the [ContainerDefinition::environment](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-environment) parameter in the *Amazon Elastic Container Service API Reference*.
*Required*: No
*Type*: Array of [ContainerEnvironment](aws-properties-gamelift-containergroupdefinition-containerenvironment.md)
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Essential`  <a name="cfn-gamelift-containergroupdefinition-supportcontainerdefinition-essential"></a>
Indicates whether the container is vital to the container group. If an essential container fails, the entire container group restarts.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HealthCheck`  <a name="cfn-gamelift-containergroupdefinition-supportcontainerdefinition-healthcheck"></a>
A configuration for a non-terminal health check. A support container automatically restarts if it stops functioning or if it fails this health check.
*Required*: No
*Type*: [ContainerHealthCheck](aws-properties-gamelift-containergroupdefinition-containerhealthcheck.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageUri`  <a name="cfn-gamelift-containergroupdefinition-supportcontainerdefinition-imageuri"></a>
The URI to the image that Amazon GameLift Servers deploys to a container fleet. For a more specific identifier, see `ResolvedImageDigest`.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_\.@\/:]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LinuxCapabilities`  <a name="cfn-gamelift-containergroupdefinition-supportcontainerdefinition-linuxcapabilities"></a>
Linux-specific modifications that are applied to the default Docker container configuration, such as Linux capabilities. For more information see [LinuxCapabilities](https://docs.aws.amazon.com/gamelift/latest/apireference/API_LinuxCapabilities.html).
*Required*: No
*Type*: [LinuxCapabilities](aws-properties-gamelift-containergroupdefinition-linuxcapabilities.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MemoryHardLimitMebibytes`  <a name="cfn-gamelift-containergroupdefinition-supportcontainerdefinition-memoryhardlimitmebibytes"></a>
The amount of memory that Amazon GameLift Servers makes available to the container. If memory limits aren't set for an individual container, the container shares the container group's total memory allocation.
 **Related data type: ** [ContainerGroupDefinition TotalMemoryLimitMebibytes](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html)
*Required*: No
*Type*: Integer
*Minimum*: `4`
*Maximum*: `1024000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MountPoints`  <a name="cfn-gamelift-containergroupdefinition-supportcontainerdefinition-mountpoints"></a>
A mount point that binds a path inside the container to a file or directory on the host system and lets it access the file or directory.
*Required*: No
*Type*: Array of [ContainerMountPoint](aws-properties-gamelift-containergroupdefinition-containermountpoint.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PortConfiguration`  <a name="cfn-gamelift-containergroupdefinition-supportcontainerdefinition-portconfiguration"></a>
A set of ports that allow access to the container from external users. Processes running in the container can bind to a one of these ports. Container ports aren't directly accessed by inbound traffic. Amazon GameLift Servers maps these container ports to externally accessible connection ports, which are assigned as needed from the container fleet's `ConnectionPortRange`.
*Required*: No
*Type*: [PortConfiguration](aws-properties-gamelift-containergroupdefinition-portconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResolvedImageDigest`  <a name="cfn-gamelift-containergroupdefinition-supportcontainerdefinition-resolvedimagedigest"></a>
A unique and immutable identifier for the container image. The digest is a SHA 256 hash of the container image manifest.
*Required*: No
*Type*: String
*Pattern*: `^sha256:[a-fA-F0-9]{64}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Vcpu`  <a name="cfn-gamelift-containergroupdefinition-supportcontainerdefinition-vcpu"></a>
The number of vCPU units that are reserved for the container. If no resources are reserved, the container shares the total vCPU limit for the container group.
 **Related data type: ** [ContainerGroupDefinition TotalVcpuLimit](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html)
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
