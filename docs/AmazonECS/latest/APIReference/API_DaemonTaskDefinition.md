---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DaemonTaskDefinition.html
---

# DaemonTaskDefinition
<a name="API_DaemonTaskDefinition"></a>

The details of a daemon task definition. A daemon task definition is a template that describes the containers that form a daemon. Daemons deploy cross-cutting software agents independently across your Amazon ECS infrastructure.

## Contents
<a name="API_DaemonTaskDefinition_Contents"></a>

 ** containerDefinitions **   <a name="ECS-Type-DaemonTaskDefinition-containerDefinitions"></a>
A list of container definitions in JSON format that describe the containers that make up the daemon task.
Type: Array of [DaemonContainerDefinition](API_DaemonContainerDefinition.md) objects
Required: No

 ** cpu **   <a name="ECS-Type-DaemonTaskDefinition-cpu"></a>
The number of CPU units used by the daemon task.
Type: String
Required: No

 ** daemonTaskDefinitionArn **   <a name="ECS-Type-DaemonTaskDefinition-daemonTaskDefinitionArn"></a>
The full Amazon Resource Name (ARN) of the daemon task definition.
Type: String
Required: No

 ** deleteRequestedAt **   <a name="ECS-Type-DaemonTaskDefinition-deleteRequestedAt"></a>
The Unix timestamp for the time when the daemon task definition delete was requested.
Type: Timestamp
Required: No

 ** executionRoleArn **   <a name="ECS-Type-DaemonTaskDefinition-executionRoleArn"></a>
The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make Amazon Web Services API calls on your behalf.
Type: String
Required: No

 ** family **   <a name="ECS-Type-DaemonTaskDefinition-family"></a>
The name of a family that this daemon task definition is registered to.
Type: String
Required: No

 ** ipcMode **   <a name="ECS-Type-DaemonTaskDefinition-ipcMode"></a>
The IPC namespace mode for the daemon. The valid values are `none` and `shared`. The default is `none`.
If `none` is specified or no value is provided, the daemon runs with its own IPC namespace, isolated from other tasks. If `shared` is specified, the daemon joins the host IPC namespace, making it accessible to non-daemon tasks that use `ipcMode: "host"` or other daemons that use `ipcMode: "shared"`.
Type: String
Valid Values: `none | shared`
Required: No

 ** memory **   <a name="ECS-Type-DaemonTaskDefinition-memory"></a>
The amount of memory (in MiB) used by the daemon task.
Type: String
Required: No

 ** pidMode **   <a name="ECS-Type-DaemonTaskDefinition-pidMode"></a>
The PID namespace mode for the daemon. The valid values are `none` and `shared`. The default is `none`.
If `none` is specified or no value is provided, the daemon runs with its own PID namespace, isolated from other tasks. If `shared` is specified, the daemon joins the host PID namespace, making it accessible to non-daemon tasks that use `pidMode: "host"` or other daemons that use `pidMode: "shared"`.
Type: String
Valid Values: `none | shared`
Required: No

 ** registeredAt **   <a name="ECS-Type-DaemonTaskDefinition-registeredAt"></a>
The Unix timestamp for the time when the daemon task definition was registered.
Type: Timestamp
Required: No

 ** registeredBy **   <a name="ECS-Type-DaemonTaskDefinition-registeredBy"></a>
The principal that registered the daemon task definition.
Type: String
Required: No

 ** revision **   <a name="ECS-Type-DaemonTaskDefinition-revision"></a>
The revision of the daemon task in a particular family. The revision is a version number of a daemon task definition in a family. When you register a daemon task definition for the first time, the revision is `1`. Each time that you register a new revision of a daemon task definition in the same family, the revision value always increases by one.
Type: Integer
Required: No

 ** status **   <a name="ECS-Type-DaemonTaskDefinition-status"></a>
The status of the daemon task definition. The valid values are `ACTIVE`, `DELETE_IN_PROGRESS`, and `DELETED`.
Type: String
Valid Values: `ACTIVE | DELETE_IN_PROGRESS | DELETED`
Required: No

 ** taskRoleArn **   <a name="ECS-Type-DaemonTaskDefinition-taskRoleArn"></a>
The short name or full Amazon Resource Name (ARN) of the IAM role that grants containers in the daemon task permission to call Amazon Web Services APIs on your behalf.
Type: String
Required: No

 ** volumes **   <a name="ECS-Type-DaemonTaskDefinition-volumes"></a>
The list of data volume definitions for the daemon task.
Type: Array of [DaemonVolume](API_DaemonVolume.md) objects
Required: No

## See Also
<a name="API_DaemonTaskDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DaemonTaskDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DaemonTaskDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DaemonTaskDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
