---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DaemonDeployment.html
---

# DaemonDeployment
<a name="API_DaemonDeployment"></a>

Information about a daemon deployment. A daemon deployment orchestrates the progressive rollout of daemon task updates across container instances.

## Contents
<a name="API_DaemonDeployment_Contents"></a>

 ** alarms **   <a name="ECS-Type-DaemonDeployment-alarms"></a>
The CloudWatch alarms that determine when a daemon deployment fails.
Type: [DaemonDeploymentAlarms](API_DaemonDeploymentAlarms.md) object
Required: No

 ** circuitBreaker **   <a name="ECS-Type-DaemonDeployment-circuitBreaker"></a>
The circuit breaker configuration that determines when a daemon deployment has failed.
Type: [DaemonCircuitBreaker](API_DaemonCircuitBreaker.md) object
Required: No

 ** clusterArn **   <a name="ECS-Type-DaemonDeployment-clusterArn"></a>
The Amazon Resource Name (ARN) of the cluster that hosts the daemon.
Type: String
Required: No

 ** createdAt **   <a name="ECS-Type-DaemonDeployment-createdAt"></a>
The time the daemon deployment was created. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.
Type: Timestamp
Required: No

 ** daemonDeploymentArn **   <a name="ECS-Type-DaemonDeployment-daemonDeploymentArn"></a>
The Amazon Resource Name (ARN) of the daemon deployment.
Type: String
Required: No

 ** deploymentConfiguration **   <a name="ECS-Type-DaemonDeployment-deploymentConfiguration"></a>
The deployment configuration used for this daemon deployment.
Type: [DaemonDeploymentConfiguration](API_DaemonDeploymentConfiguration.md) object
Required: No

 ** finishedAt **   <a name="ECS-Type-DaemonDeployment-finishedAt"></a>
The time the daemon deployment finished. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.
Type: Timestamp
Required: No

 ** rollback **   <a name="ECS-Type-DaemonDeployment-rollback"></a>
The rollback options for the daemon deployment.
Type: [DaemonRollback](API_DaemonRollback.md) object
Required: No

 ** sourceDaemonRevisions **   <a name="ECS-Type-DaemonDeployment-sourceDaemonRevisions"></a>
The currently deployed daemon revisions that are being replaced.
Type: Array of [DaemonDeploymentRevisionDetail](API_DaemonDeploymentRevisionDetail.md) objects
Required: No

 ** startedAt **   <a name="ECS-Type-DaemonDeployment-startedAt"></a>
The time the daemon deployment started. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.
Type: Timestamp
Required: No

 ** status **   <a name="ECS-Type-DaemonDeployment-status"></a>
The status of the daemon deployment.
Type: String
Valid Values: `PENDING | SUCCESSFUL | STOPPED | STOP_REQUESTED | IN_PROGRESS | ROLLBACK_IN_PROGRESS | ROLLBACK_SUCCESSFUL | ROLLBACK_FAILED`
Required: No

 ** statusReason **   <a name="ECS-Type-DaemonDeployment-statusReason"></a>
Information about why the daemon deployment is in the current status.
Type: String
Required: No

 ** stoppedAt **   <a name="ECS-Type-DaemonDeployment-stoppedAt"></a>
The time the daemon deployment stopped. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.
Type: Timestamp
Required: No

 ** targetDaemonRevision **   <a name="ECS-Type-DaemonDeployment-targetDaemonRevision"></a>
The daemon revision being deployed.
Type: [DaemonDeploymentRevisionDetail](API_DaemonDeploymentRevisionDetail.md) object
Required: No

## See Also
<a name="API_DaemonDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DaemonDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DaemonDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DaemonDeployment)
