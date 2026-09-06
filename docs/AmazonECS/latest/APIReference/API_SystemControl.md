---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_SystemControl.html
---

# SystemControl
<a name="API_SystemControl"></a>

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

## Contents
<a name="API_SystemControl_Contents"></a>

 ** namespace **   <a name="ECS-Type-SystemControl-namespace"></a>
The namespaced kernel parameter to set a `value` for.
Type: String
Required: No

 ** value **   <a name="ECS-Type-SystemControl-value"></a>
The namespaced kernel parameter to set a `value` for.
Valid IPC namespace values: `"kernel.msgmax" | "kernel.msgmnb" | "kernel.msgmni" | "kernel.sem" | "kernel.shmall" | "kernel.shmmax" | "kernel.shmmni" | "kernel.shm_rmid_forced"`, and `Sysctls` that start with `"fs.mqueue.*"`
Valid network namespace values: `Sysctls` that start with `"net.*"`. Only namespaced `Sysctls` that exist within the container starting with "net.\* are accepted.
All of these values are supported by Fargate.
Type: String
Required: No

## See Also
<a name="API_SystemControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/SystemControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/SystemControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/SystemControl)
