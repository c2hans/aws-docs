---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-containergroupdefinition-containerenvironment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::ContainerGroupDefinition ContainerEnvironment
<a name="aws-properties-gamelift-containergroupdefinition-containerenvironment"></a>

An environment variable to set inside a container, in the form of a key-value pair.

**Part of:**[GameServerContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html), [GameServerContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html), [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html), [SupportContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html)

## Syntax
<a name="aws-properties-gamelift-containergroupdefinition-containerenvironment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-containergroupdefinition-containerenvironment-syntax.json"></a>

```
{
  "[Name](#cfn-gamelift-containergroupdefinition-containerenvironment-name)" : {{String}},
  "[Value](#cfn-gamelift-containergroupdefinition-containerenvironment-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-gamelift-containergroupdefinition-containerenvironment-syntax.yaml"></a>

```
  [Name](#cfn-gamelift-containergroupdefinition-containerenvironment-name): {{String}}
  [Value](#cfn-gamelift-containergroupdefinition-containerenvironment-value): {{String}}
```

## Properties
<a name="aws-properties-gamelift-containergroupdefinition-containerenvironment-properties"></a>

`Name`  <a name="cfn-gamelift-containergroupdefinition-containerenvironment-name"></a>
The environment variable name.
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-gamelift-containergroupdefinition-containerenvironment-value"></a>
The environment variable value.
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
