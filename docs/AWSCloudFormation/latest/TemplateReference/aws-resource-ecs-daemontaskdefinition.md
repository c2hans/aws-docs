---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-daemontaskdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::DaemonTaskDefinition
<a name="aws-resource-ecs-daemontaskdefinition"></a>

The details of a daemon task definition. A daemon task definition is a template that describes the containers that form a daemon. Daemons deploy cross-cutting software agents independently across your Amazon ECS infrastructure.

## Syntax
<a name="aws-resource-ecs-daemontaskdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ecs-daemontaskdefinition-syntax.json"></a>

```
{
  "Type" : "AWS::ECS::DaemonTaskDefinition",
  "Properties" : {
      "[ContainerDefinitions](#cfn-ecs-daemontaskdefinition-containerdefinitions)" : {{[ DaemonContainerDefinition, ... ]}},
      "[Cpu](#cfn-ecs-daemontaskdefinition-cpu)" : {{String}},
      "[ExecutionRoleArn](#cfn-ecs-daemontaskdefinition-executionrolearn)" : {{String}},
      "[Family](#cfn-ecs-daemontaskdefinition-family)" : {{String}},
      "[IpcMode](#cfn-ecs-daemontaskdefinition-ipcmode)" : {{String}},
      "[Memory](#cfn-ecs-daemontaskdefinition-memory)" : {{String}},
      "[PidMode](#cfn-ecs-daemontaskdefinition-pidmode)" : {{String}},
      "[Tags](#cfn-ecs-daemontaskdefinition-tags)" : {{[ Tag, ... ]}},
      "[TaskRoleArn](#cfn-ecs-daemontaskdefinition-taskrolearn)" : {{String}},
      "[Volumes](#cfn-ecs-daemontaskdefinition-volumes)" : {{[ Volume, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ecs-daemontaskdefinition-syntax.yaml"></a>

```
Type: AWS::ECS::DaemonTaskDefinition
Properties:
  [ContainerDefinitions](#cfn-ecs-daemontaskdefinition-containerdefinitions): {{
    - DaemonContainerDefinition}}
  [Cpu](#cfn-ecs-daemontaskdefinition-cpu): {{String}}
  [ExecutionRoleArn](#cfn-ecs-daemontaskdefinition-executionrolearn): {{String}}
  [Family](#cfn-ecs-daemontaskdefinition-family): {{String}}
  [IpcMode](#cfn-ecs-daemontaskdefinition-ipcmode): {{String}}
  [Memory](#cfn-ecs-daemontaskdefinition-memory): {{String}}
  [PidMode](#cfn-ecs-daemontaskdefinition-pidmode): {{String}}
  [Tags](#cfn-ecs-daemontaskdefinition-tags): {{
    - Tag}}
  [TaskRoleArn](#cfn-ecs-daemontaskdefinition-taskrolearn): {{String}}
  [Volumes](#cfn-ecs-daemontaskdefinition-volumes): {{
    - Volume}}
```

## Properties
<a name="aws-resource-ecs-daemontaskdefinition-properties"></a>

`ContainerDefinitions`  <a name="cfn-ecs-daemontaskdefinition-containerdefinitions"></a>
A list of container definitions in JSON format that describe the containers that make up the daemon task.
*Required*: No
*Type*: Array of [DaemonContainerDefinition](aws-properties-ecs-daemontaskdefinition-daemoncontainerdefinition.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Cpu`  <a name="cfn-ecs-daemontaskdefinition-cpu"></a>
The number of CPU units used by the daemon task.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExecutionRoleArn`  <a name="cfn-ecs-daemontaskdefinition-executionrolearn"></a>
The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make Amazon Web Services API calls on your behalf.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Family`  <a name="cfn-ecs-daemontaskdefinition-family"></a>
The name of a family that this daemon task definition is registered to.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IpcMode`  <a name="cfn-ecs-daemontaskdefinition-ipcmode"></a>
The IPC namespace mode for the daemon. The valid values are `none` and `shared`. The default is `none`.
If `none` is specified or no value is provided, the daemon runs with its own IPC namespace, isolated from other tasks. If `shared` is specified, the daemon joins the host IPC namespace, making it accessible to non-daemon tasks that use `ipcMode: "host"` or other daemons that use `ipcMode: "shared"`.
*Required*: No
*Type*: String
*Allowed values*: `none | shared`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Memory`  <a name="cfn-ecs-daemontaskdefinition-memory"></a>
The amount of memory (in MiB) used by the daemon task.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PidMode`  <a name="cfn-ecs-daemontaskdefinition-pidmode"></a>
The PID namespace mode for the daemon. The valid values are `none` and `shared`. The default is `none`.
If `none` is specified or no value is provided, the daemon runs with its own PID namespace, isolated from other tasks. If `shared` is specified, the daemon joins the host PID namespace, making it accessible to non-daemon tasks that use `pidMode: "host"` or other daemons that use `pidMode: "shared"`.
*Required*: No
*Type*: String
*Allowed values*: `none | shared`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ecs-daemontaskdefinition-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-ecs-daemontaskdefinition-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TaskRoleArn`  <a name="cfn-ecs-daemontaskdefinition-taskrolearn"></a>
The short name or full Amazon Resource Name (ARN) of the IAM role that grants containers in the daemon task permission to call Amazon Web Services APIs on your behalf.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Volumes`  <a name="cfn-ecs-daemontaskdefinition-volumes"></a>
The list of data volume definitions for the daemon task.
*Required*: No
*Type*: Array of [Volume](aws-properties-ecs-daemontaskdefinition-volume.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ecs-daemontaskdefinition-return-values"></a>

### Ref
<a name="aws-resource-ecs-daemontaskdefinition-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ecs-daemontaskdefinition-return-values-fn--getatt"></a>

####
<a name="aws-resource-ecs-daemontaskdefinition-return-values-fn--getatt-fn--getatt"></a>

`DaemonTaskDefinitionArn`  <a name="DaemonTaskDefinitionArn-fn::getatt"></a>
The full Amazon Resource Name (ARN) of the daemon task definition.
