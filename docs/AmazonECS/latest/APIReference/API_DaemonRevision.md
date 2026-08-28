---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DaemonRevision.html
---

# DaemonRevision
<a name="API_DaemonRevision"></a>

Information about a daemon revision. A daemon revision is a snapshot of the daemon's configuration at the time a deployment was initiated.

## Contents
<a name="API_DaemonRevision_Contents"></a>

 ** clusterArn **   <a name="ECS-Type-DaemonRevision-clusterArn"></a>
The Amazon Resource Name (ARN) of the cluster that hosts the daemon.
Type: String
Required: No

 ** containerImages **   <a name="ECS-Type-DaemonRevision-containerImages"></a>
The container images used by the daemon revision.
Type: Array of [DaemonContainerImage](API_DaemonContainerImage.md) objects
Required: No

 ** createdAt **   <a name="ECS-Type-DaemonRevision-createdAt"></a>
The Unix timestamp for the time when the daemon revision was created.
Type: Timestamp
Required: No

 ** daemonArn **   <a name="ECS-Type-DaemonRevision-daemonArn"></a>
The Amazon Resource Name (ARN) of the daemon for this revision.
Type: String
Required: No

 ** daemonRevisionArn **   <a name="ECS-Type-DaemonRevision-daemonRevisionArn"></a>
The Amazon Resource Name (ARN) of the daemon revision.
Type: String
Required: No

 ** daemonTaskDefinitionArn **   <a name="ECS-Type-DaemonRevision-daemonTaskDefinitionArn"></a>
The Amazon Resource Name (ARN) of the daemon task definition used by this revision.
Type: String
Required: No

 ** enableECSManagedTags **   <a name="ECS-Type-DaemonRevision-enableECSManagedTags"></a>
Specifies whether Amazon ECS managed tags are turned on for the daemon tasks.
Type: Boolean
Required: No

 ** enableExecuteCommand **   <a name="ECS-Type-DaemonRevision-enableExecuteCommand"></a>
Specifies whether the execute command functionality is turned on for the daemon tasks.
Type: Boolean
Required: No

 ** propagateTags **   <a name="ECS-Type-DaemonRevision-propagateTags"></a>
Specifies whether tags are propagated from the daemon to the daemon tasks.
Type: String
Valid Values: `DAEMON | NONE`
Required: No

## See Also
<a name="API_DaemonRevision_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DaemonRevision)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DaemonRevision)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DaemonRevision)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
