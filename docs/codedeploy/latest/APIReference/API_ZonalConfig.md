---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ZonalConfig.html
---

# ZonalConfig
<a name="API_ZonalConfig"></a>

Configure the `ZonalConfig` object if you want AWS CodeDeploy to deploy your application to one [Availability Zone](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones) at a time, within an AWS Region. By deploying to one Availability Zone at a time, you can expose your deployment to a progressively larger audience as confidence in the deployment's performance and viability grows. If you don't configure the `ZonalConfig` object, CodeDeploy deploys your application to a random selection of hosts across a Region.

For more information about the zonal configuration feature, see [zonal configuration](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations-create.html#zonal-config) in the *CodeDeploy User Guide*.

## Contents
<a name="API_ZonalConfig_Contents"></a>

 ** firstZoneMonitorDurationInSeconds **   <a name="CodeDeploy-Type-ZonalConfig-firstZoneMonitorDurationInSeconds"></a>
The period of time, in seconds, that CodeDeploy must wait after completing a deployment to the *first* Availability Zone. CodeDeploy will wait this amount of time before starting a deployment to the second Availability Zone. You might set this option if you want to allow extra bake time for the first Availability Zone. If you don't specify a value for `firstZoneMonitorDurationInSeconds`, then CodeDeploy uses the `monitorDurationInSeconds` value for the first Availability Zone.
For more information about the zonal configuration feature, see [zonal configuration](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations-create.html#zonal-config) in the *CodeDeploy User Guide*.
Type: Long
Required: No

 ** minimumHealthyHostsPerZone **   <a name="CodeDeploy-Type-ZonalConfig-minimumHealthyHostsPerZone"></a>
The number or percentage of instances that must remain available per Availability Zone during a deployment. This option works in conjunction with the `MinimumHealthyHosts` option. For more information, see [About the minimum number of healthy hosts per Availability Zone](https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-health.html#minimum-healthy-hosts-az) in the *CodeDeploy User Guide*.
If you don't specify the `minimumHealthyHostsPerZone` option, then CodeDeploy uses a default value of `0` percent.
For more information about the zonal configuration feature, see [zonal configuration](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations-create.html#zonal-config) in the *CodeDeploy User Guide*.
Type: [MinimumHealthyHostsPerZone](API_MinimumHealthyHostsPerZone.md) object
Required: No

 ** monitorDurationInSeconds **   <a name="CodeDeploy-Type-ZonalConfig-monitorDurationInSeconds"></a>
The period of time, in seconds, that CodeDeploy must wait after completing a deployment to an Availability Zone. CodeDeploy will wait this amount of time before starting a deployment to the next Availability Zone. Consider adding a monitor duration to give the deployment some time to prove itself (or 'bake') in one Availability Zone before it is released in the next zone. If you don't specify a `monitorDurationInSeconds`, CodeDeploy starts deploying to the next Availability Zone immediately.
For more information about the zonal configuration feature, see [zonal configuration](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations-create.html#zonal-config) in the *CodeDeploy User Guide*.
Type: Long
Required: No

## See Also
<a name="API_ZonalConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/ZonalConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/ZonalConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/ZonalConfig)
