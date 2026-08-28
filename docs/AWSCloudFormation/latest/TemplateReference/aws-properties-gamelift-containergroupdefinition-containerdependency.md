---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-containergroupdefinition-containerdependency.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::ContainerGroupDefinition ContainerDependency
<a name="aws-properties-gamelift-containergroupdefinition-containerdependency"></a>

A container's dependency on another container in the same container group. The dependency impacts how the dependent container is able to start or shut down based the status of the other container.

For example, *ContainerA* is configured with the following dependency: a `START` dependency on *ContainerB*. This means that *ContainerA* can't start until *ContainerB* has started. It also means that *ContainerA* must shut down before *ContainerB*.

**Part of:**[GameServerContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html), [GameServerContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html), [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html), [SupportContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html)

## Syntax
<a name="aws-properties-gamelift-containergroupdefinition-containerdependency-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-containergroupdefinition-containerdependency-syntax.json"></a>

```
{
  "[Condition](#cfn-gamelift-containergroupdefinition-containerdependency-condition)" : {{String}},
  "[ContainerName](#cfn-gamelift-containergroupdefinition-containerdependency-containername)" : {{String}}
}
```

### YAML
<a name="aws-properties-gamelift-containergroupdefinition-containerdependency-syntax.yaml"></a>

```
  [Condition](#cfn-gamelift-containergroupdefinition-containerdependency-condition): {{String}}
  [ContainerName](#cfn-gamelift-containergroupdefinition-containerdependency-containername): {{String}}
```

## Properties
<a name="aws-properties-gamelift-containergroupdefinition-containerdependency-properties"></a>

`Condition`  <a name="cfn-gamelift-containergroupdefinition-containerdependency-condition"></a>
The condition that the dependency container must reach before the dependent container can start. Valid conditions include:
+ START - The dependency container must have started.
+ COMPLETE - The dependency container has run to completion (exits). Use this condition with nonessential containers, such as those that run a script and then exit. The dependency container can't be an essential container.
+ SUCCESS - The dependency container has run to completion and exited with a zero status. The dependency container can't be an essential container.
+ HEALTHY - The dependency container has passed its Docker health check. Use this condition with dependency containers that have health checks configured. This condition is confirmed at container group startup only.
*Required*: Yes
*Type*: String
*Allowed values*: `START | COMPLETE | SUCCESS | HEALTHY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContainerName`  <a name="cfn-gamelift-containergroupdefinition-containerdependency-containername"></a>
A descriptive label for the container definition that this container depends on.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
