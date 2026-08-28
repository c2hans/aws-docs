---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-containergroupdefinition-containermountpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::ContainerGroupDefinition ContainerMountPoint
<a name="aws-properties-gamelift-containergroupdefinition-containermountpoint"></a>

A mount point that binds a container to a file or directory on the host system.

**Part of:**[GameServerContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html), [https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html), [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html), [https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html)

## Syntax
<a name="aws-properties-gamelift-containergroupdefinition-containermountpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-containergroupdefinition-containermountpoint-syntax.json"></a>

```
{
  "[AccessLevel](#cfn-gamelift-containergroupdefinition-containermountpoint-accesslevel)" : {{String}},
  "[ContainerPath](#cfn-gamelift-containergroupdefinition-containermountpoint-containerpath)" : {{String}},
  "[InstancePath](#cfn-gamelift-containergroupdefinition-containermountpoint-instancepath)" : {{String}}
}
```

### YAML
<a name="aws-properties-gamelift-containergroupdefinition-containermountpoint-syntax.yaml"></a>

```
  [AccessLevel](#cfn-gamelift-containergroupdefinition-containermountpoint-accesslevel): {{String}}
  [ContainerPath](#cfn-gamelift-containergroupdefinition-containermountpoint-containerpath): {{String}}
  [InstancePath](#cfn-gamelift-containergroupdefinition-containermountpoint-instancepath): {{String}}
```

## Properties
<a name="aws-properties-gamelift-containergroupdefinition-containermountpoint-properties"></a>

`AccessLevel`  <a name="cfn-gamelift-containergroupdefinition-containermountpoint-accesslevel"></a>
The type of access for the container.
*Required*: No
*Type*: String
*Allowed values*: `READ_ONLY | READ_AND_WRITE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContainerPath`  <a name="cfn-gamelift-containergroupdefinition-containermountpoint-containerpath"></a>
The mount path on the container. If this property isn't set, the instance path is used.
*Required*: No
*Type*: String
*Pattern*: `^(\/+[^\/]+\/*)+$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstancePath`  <a name="cfn-gamelift-containergroupdefinition-containermountpoint-instancepath"></a>
The path to the source file or directory.
*Required*: Yes
*Type*: String
*Pattern*: `^\/[\s\S]*$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
