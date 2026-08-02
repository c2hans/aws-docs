---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceDeploymentAlarms.html
---

# ServiceDeploymentAlarms
<a name="API_ServiceDeploymentAlarms"></a>

The CloudWatch alarms used to determine a service deployment failed.

Amazon ECS considers the service deployment as failed when any of the alarms move to the `ALARM` state. For more information, see [How CloudWatch alarms detect Amazon ECS deployment failures](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-alarm-failure.html) in the Amazon ECS Developer Guide.

## Contents
<a name="API_ServiceDeploymentAlarms_Contents"></a>

 ** alarmNames **   <a name="ECS-Type-ServiceDeploymentAlarms-alarmNames"></a>
The name of the CloudWatch alarms that determine when a service deployment failed. A "," separates the alarms.
Type: Array of strings
Required: No

 ** status **   <a name="ECS-Type-ServiceDeploymentAlarms-status"></a>
The status of the alarms check. Amazon ECS is not using alarms for service deployment failures when the status is `DISABLED`.
Type: String
Valid Values: `TRIGGERED | MONITORING | MONITORING_COMPLETE | DISABLED`
Required: No

 ** triggeredAlarmNames **   <a name="ECS-Type-ServiceDeploymentAlarms-triggeredAlarmNames"></a>
One or more CloudWatch alarm names that have been triggered during the service deployment. A "," separates the alarm names.
Type: Array of strings
Required: No

## See Also
<a name="API_ServiceDeploymentAlarms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ServiceDeploymentAlarms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ServiceDeploymentAlarms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ServiceDeploymentAlarms)
