---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-multinodeecstaskproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition MultiNodeEcsTaskProperties
<a name="aws-properties-batch-jobdefinition-multinodeecstaskproperties"></a>

The properties for a task definition that describes the container and volume definitions of an Amazon ECS task. You can specify which Docker images to use, the required resources, and other configurations related to launching the task definition through an Amazon ECS service or task.

## Syntax
<a name="aws-properties-batch-jobdefinition-multinodeecstaskproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-multinodeecstaskproperties-syntax.json"></a>

```
{
  "[Containers](#cfn-batch-jobdefinition-multinodeecstaskproperties-containers)" : {{[ TaskContainerProperties, ... ]}},
  "[EnableExecuteCommand](#cfn-batch-jobdefinition-multinodeecstaskproperties-enableexecutecommand)" : {{Boolean}},
  "[ExecutionRoleArn](#cfn-batch-jobdefinition-multinodeecstaskproperties-executionrolearn)" : {{String}},
  "[IpcMode](#cfn-batch-jobdefinition-multinodeecstaskproperties-ipcmode)" : {{String}},
  "[PidMode](#cfn-batch-jobdefinition-multinodeecstaskproperties-pidmode)" : {{String}},
  "[TaskRoleArn](#cfn-batch-jobdefinition-multinodeecstaskproperties-taskrolearn)" : {{String}},
  "[Volumes](#cfn-batch-jobdefinition-multinodeecstaskproperties-volumes)" : {{[ Volume, ... ]}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-multinodeecstaskproperties-syntax.yaml"></a>

```
  [Containers](#cfn-batch-jobdefinition-multinodeecstaskproperties-containers): {{
    - TaskContainerProperties}}
  [EnableExecuteCommand](#cfn-batch-jobdefinition-multinodeecstaskproperties-enableexecutecommand): {{Boolean}}
  [ExecutionRoleArn](#cfn-batch-jobdefinition-multinodeecstaskproperties-executionrolearn): {{String}}
  [IpcMode](#cfn-batch-jobdefinition-multinodeecstaskproperties-ipcmode): {{String}}
  [PidMode](#cfn-batch-jobdefinition-multinodeecstaskproperties-pidmode): {{String}}
  [TaskRoleArn](#cfn-batch-jobdefinition-multinodeecstaskproperties-taskrolearn): {{String}}
  [Volumes](#cfn-batch-jobdefinition-multinodeecstaskproperties-volumes): {{
    - Volume}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-multinodeecstaskproperties-properties"></a>

`Containers`  <a name="cfn-batch-jobdefinition-multinodeecstaskproperties-containers"></a>
This object is a list of containers.
*Required*: No
*Type*: Array of [TaskContainerProperties](aws-properties-batch-jobdefinition-taskcontainerproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableExecuteCommand`  <a name="cfn-batch-jobdefinition-multinodeecstaskproperties-enableexecutecommand"></a>
Determines whether execute command functionality is turned on for this task. If `true`, execute command functionality is turned on all the containers in the task.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRoleArn`  <a name="cfn-batch-jobdefinition-multinodeecstaskproperties-executionrolearn"></a>
The Amazon Resource Name (ARN) of the execution role that AWS Batch can assume. For jobs that run on Fargate resources, you must provide an execution role. For more information, see [AWS Batch execution IAM role](https://docs.aws.amazon.com/batch/latest/userguide/execution-IAM-role.html) in the *AWS Batch User Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpcMode`  <a name="cfn-batch-jobdefinition-multinodeecstaskproperties-ipcmode"></a>
The IPC resource namespace to use for the containers in the task. The valid values are `host`, `task`, or `none`.
If `host` is specified, all containers within the tasks that specified the `host` IPC mode on the same container instance share the same IPC resources with the host Amazon EC2 instance.
If `task` is specified, all containers within the specified `task` share the same IPC resources.
If `none` is specified, the IPC resources within the containers of a task are private, and are not shared with other containers in a task or on the container instance.
If no value is specified, then the IPC resource namespace sharing depends on the Docker daemon setting on the container instance. For more information, see [IPC settings](https://docs.docker.com/engine/reference/run/#ipc-settings---ipc) in the Docker run reference.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PidMode`  <a name="cfn-batch-jobdefinition-multinodeecstaskproperties-pidmode"></a>
The process namespace to use for the containers in the task. The valid values are `host` or `task`. For example, monitoring sidecars might need `pidMode` to access information about other containers running in the same task.
If `host` is specified, all containers within the tasks that specified the `host` PID mode on the same container instance share the process namespace with the host Amazon EC2 instance.
If `task` is specified, all containers within the specified task share the same process namespace.
If no value is specified, the default is a private namespace for each container. For more information, see [PID settings](https://docs.docker.com/engine/reference/run/#pid-settings---pid) in the Docker run reference.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TaskRoleArn`  <a name="cfn-batch-jobdefinition-multinodeecstaskproperties-taskrolearn"></a>
The Amazon Resource Name (ARN) that's associated with the Amazon ECS task.
This is object is comparable to [ContainerProperties:jobRoleArn](https://docs.aws.amazon.com/batch/latest/APIReference/API_ContainerProperties.html).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Volumes`  <a name="cfn-batch-jobdefinition-multinodeecstaskproperties-volumes"></a>
A list of volumes that are associated with the job.
*Required*: No
*Type*: Array of [Volume](aws-properties-batch-jobdefinition-volume.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
