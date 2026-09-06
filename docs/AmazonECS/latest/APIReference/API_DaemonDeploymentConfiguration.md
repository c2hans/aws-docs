---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DaemonDeploymentConfiguration.html
---

# DaemonDeploymentConfiguration
<a name="API_DaemonDeploymentConfiguration"></a>

Optional deployment parameters that control how a daemon rolls out updates across container instances.

## Contents
<a name="API_DaemonDeploymentConfiguration_Contents"></a>

 ** alarms **   <a name="ECS-Type-DaemonDeploymentConfiguration-alarms"></a>
The CloudWatch alarm configuration for the daemon deployment. When alarms are triggered during a deployment, the deployment can be automatically rolled back.
Type: [DaemonAlarmConfiguration](API_DaemonAlarmConfiguration.md) object
Required: No

 ** bakeTimeInMinutes **   <a name="ECS-Type-DaemonDeploymentConfiguration-bakeTimeInMinutes"></a>
The amount of time (in minutes) to wait after a successful deployment step before proceeding. This allows time to monitor for issues before continuing. The default value is 0.
Type: Integer
Required: No

 ** drainPercent **   <a name="ECS-Type-DaemonDeploymentConfiguration-drainPercent"></a>
The percentage of container instances to drain simultaneously during a daemon deployment. Valid values are between 0.0 and 100.0.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 100.0.
Required: No

## See Also
<a name="API_DaemonDeploymentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DaemonDeploymentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DaemonDeploymentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DaemonDeploymentConfiguration)
