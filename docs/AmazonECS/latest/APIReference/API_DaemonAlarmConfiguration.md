---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DaemonAlarmConfiguration.html
---

# DaemonAlarmConfiguration
<a name="API_DaemonAlarmConfiguration"></a>

The CloudWatch alarm configuration for a daemon. When enabled, CloudWatch alarms determine whether a daemon deployment has failed.

## Contents
<a name="API_DaemonAlarmConfiguration_Contents"></a>

 ** alarmNames **   <a name="ECS-Type-DaemonAlarmConfiguration-alarmNames"></a>
The CloudWatch alarm names to monitor during a daemon deployment.
Type: Array of strings
Required: No

 ** enable **   <a name="ECS-Type-DaemonAlarmConfiguration-enable"></a>
Determines whether to use the CloudWatch alarm option in the daemon deployment process. The default value is `false`.
Type: Boolean
Required: No

## See Also
<a name="API_DaemonAlarmConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DaemonAlarmConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DaemonAlarmConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DaemonAlarmConfiguration)
