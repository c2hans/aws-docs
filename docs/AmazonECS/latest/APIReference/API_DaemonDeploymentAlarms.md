---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DaemonDeploymentAlarms.html
---

# DaemonDeploymentAlarms
<a name="API_DaemonDeploymentAlarms"></a>

The CloudWatch alarms used to determine a daemon deployment failed.

## Contents
<a name="API_DaemonDeploymentAlarms_Contents"></a>

 ** alarmNames **   <a name="ECS-Type-DaemonDeploymentAlarms-alarmNames"></a>
The name of the CloudWatch alarms that determine when a daemon deployment failed.
Type: Array of strings
Required: No

 ** status **   <a name="ECS-Type-DaemonDeploymentAlarms-status"></a>
The status of the alarms check. Amazon ECS is not using alarms for daemon deployment failures when the status is `DISABLED`.
Type: String
Valid Values: `TRIGGERED | MONITORING | MONITORING_COMPLETE | DISABLED`
Required: No

 ** triggeredAlarmNames **   <a name="ECS-Type-DaemonDeploymentAlarms-triggeredAlarmNames"></a>
One or more CloudWatch alarm names that have been triggered during the daemon deployment.
Type: Array of strings
Required: No

## See Also
<a name="API_DaemonDeploymentAlarms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DaemonDeploymentAlarms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DaemonDeploymentAlarms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DaemonDeploymentAlarms)
