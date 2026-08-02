---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DaemonDeploymentSummary.html
---

# DaemonDeploymentSummary
<a name="API_DaemonDeploymentSummary"></a>

A summary of a daemon deployment.

## Contents
<a name="API_DaemonDeploymentSummary_Contents"></a>

 ** clusterArn **   <a name="ECS-Type-DaemonDeploymentSummary-clusterArn"></a>
The Amazon Resource Name (ARN) of the cluster that hosts the daemon.
Type: String
Required: No

 ** createdAt **   <a name="ECS-Type-DaemonDeploymentSummary-createdAt"></a>
The time the daemon deployment was created.
Type: Timestamp
Required: No

 ** daemonArn **   <a name="ECS-Type-DaemonDeploymentSummary-daemonArn"></a>
The Amazon Resource Name (ARN) of the daemon.
Type: String
Required: No

 ** daemonDeploymentArn **   <a name="ECS-Type-DaemonDeploymentSummary-daemonDeploymentArn"></a>
The Amazon Resource Name (ARN) of the daemon deployment.
Type: String
Required: No

 ** finishedAt **   <a name="ECS-Type-DaemonDeploymentSummary-finishedAt"></a>
The time the daemon deployment finished.
Type: Timestamp
Required: No

 ** startedAt **   <a name="ECS-Type-DaemonDeploymentSummary-startedAt"></a>
The time the daemon deployment started.
Type: Timestamp
Required: No

 ** status **   <a name="ECS-Type-DaemonDeploymentSummary-status"></a>
The status of the daemon deployment.
Type: String
Valid Values: `PENDING | SUCCESSFUL | STOPPED | STOP_REQUESTED | IN_PROGRESS | ROLLBACK_IN_PROGRESS | ROLLBACK_SUCCESSFUL | ROLLBACK_FAILED`
Required: No

 ** statusReason **   <a name="ECS-Type-DaemonDeploymentSummary-statusReason"></a>
Information about why the daemon deployment is in the current status.
Type: String
Required: No

 ** stoppedAt **   <a name="ECS-Type-DaemonDeploymentSummary-stoppedAt"></a>
The time the daemon deployment stopped.
Type: Timestamp
Required: No

 ** targetDaemonRevisionArn **   <a name="ECS-Type-DaemonDeploymentSummary-targetDaemonRevisionArn"></a>
The ARN of the daemon revision being deployed.
Type: String
Required: No

## See Also
<a name="API_DaemonDeploymentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DaemonDeploymentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DaemonDeploymentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DaemonDeploymentSummary)
