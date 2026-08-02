---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-systemcontrol.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::TaskDefinition SystemControl
<a name="aws-properties-ecs-taskdefinition-systemcontrol"></a>

A list of namespaced kernel parameters to set in the container. This parameter maps to `Sysctls` in the docker container create command and the `--sysctl` option to docker run. For example, you can configure `net.ipv4.tcp_keepalive_time` setting to maintain longer lived connections.

We don't recommend that you specify network-related `systemControls` parameters for multiple containers in a single task that also uses either the `awsvpc` or `host` network mode. Doing this has the following disadvantages:
+ For tasks that use the `awsvpc` network mode including Fargate, if you set `systemControls` for any container, it applies to all containers in the task. If you set different `systemControls` for multiple containers in a single task, the container that's started last determines which `systemControls` take effect.
+ For tasks that use the `host` network mode, the network namespace `systemControls` aren't supported.

If you're setting an IPC resource namespace to use for the containers in the task, the following conditions apply to your system controls. For more information, see [IPC mode](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#task_definition_ipcmode).
+ For tasks that use the `host` IPC mode, IPC namespace `systemControls` aren't supported.
+ For tasks that use the `task` IPC mode, IPC namespace `systemControls` values apply to all containers within a task.

**Note**
This parameter is not supported for Windows containers.

**Note**
This parameter is only supported for tasks that are hosted on AWS Fargate if the tasks are using platform version `1.4.0` or later (Linux). This isn't supported for Windows containers on Fargate.

## Syntax
<a name="aws-properties-ecs-taskdefinition-systemcontrol-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-taskdefinition-systemcontrol-syntax.json"></a>

```
{
  "[Namespace](#cfn-ecs-taskdefinition-systemcontrol-namespace)" : {{String}},
  "[Value](#cfn-ecs-taskdefinition-systemcontrol-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-taskdefinition-systemcontrol-syntax.yaml"></a>

```
  [Namespace](#cfn-ecs-taskdefinition-systemcontrol-namespace): {{String}}
  [Value](#cfn-ecs-taskdefinition-systemcontrol-value): {{String}}
```

## Properties
<a name="aws-properties-ecs-taskdefinition-systemcontrol-properties"></a>

`Namespace`  <a name="cfn-ecs-taskdefinition-systemcontrol-namespace"></a>
The namespaced kernel parameter to set a `value` for.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-ecs-taskdefinition-systemcontrol-value"></a>
The namespaced kernel parameter to set a `value` for.
Valid IPC namespace values: `"kernel.msgmax" | "kernel.msgmnb" | "kernel.msgmni" | "kernel.sem" | "kernel.shmall" | "kernel.shmmax" | "kernel.shmmni" | "kernel.shm_rmid_forced"`, and `Sysctls` that start with `"fs.mqueue.*"`
Valid network namespace values: `Sysctls` that start with `"net.*"`. Only namespaced `Sysctls` that exist within the container starting with "net.\* are accepted.
All of these values are supported by Fargate.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
