---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-containergroupdefinition-portconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::ContainerGroupDefinition PortConfiguration
<a name="aws-properties-gamelift-containergroupdefinition-portconfiguration"></a>

A set of port ranges that can be opened on the container. A process that's running in the container can bind to a port number, making it accessible to inbound traffic when it's mapped to a container fleet's connection port.

Each container port range specifies a network protocol. When the configuration supports more than one protocol, we recommend that you use a different range for each protocol. If your ranges have overlapping port numbers, Amazon GameLift Servers maps a duplicated container port number to different connection ports. For example, if you include 1935 in port ranges for both TCP and UDP, it might result in the following mappings:
+ container port 1935 (tcp) => connection port 2001
+ container port 1935 (udp) => connection port 2002

**Part of:**[GameServerContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html), [GameServerContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html), [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html), [SupportContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html)

## Syntax
<a name="aws-properties-gamelift-containergroupdefinition-portconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-containergroupdefinition-portconfiguration-syntax.json"></a>

```
{
  "[ContainerPortRanges](#cfn-gamelift-containergroupdefinition-portconfiguration-containerportranges)" : {{[ ContainerPortRange, ... ]}}
}
```

### YAML
<a name="aws-properties-gamelift-containergroupdefinition-portconfiguration-syntax.yaml"></a>

```
  [ContainerPortRanges](#cfn-gamelift-containergroupdefinition-portconfiguration-containerportranges): {{
    - ContainerPortRange}}
```

## Properties
<a name="aws-properties-gamelift-containergroupdefinition-portconfiguration-properties"></a>

`ContainerPortRanges`  <a name="cfn-gamelift-containergroupdefinition-portconfiguration-containerportranges"></a>
A set of one or more container port number ranges. The ranges can't overlap if the ranges' network protocols are the same. Overlapping ranges with different protocols is allowed but not recommended.
*Required*: Yes
*Type*: Array of [ContainerPortRange](aws-properties-gamelift-containergroupdefinition-containerportrange.md)
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
