---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AvailabilityZoneImpairmentPolicy.html
---

# AvailabilityZoneImpairmentPolicy
<a name="API_AvailabilityZoneImpairmentPolicy"></a>

 Describes an Availability Zone impairment policy.

## Contents
<a name="API_AvailabilityZoneImpairmentPolicy_Contents"></a>

 ** ImpairedZoneHealthCheckBehavior **
 Specifies the health check behavior for the impaired Availability Zone in an active zonal shift. If you select `Replace unhealthy`, instances that appear unhealthy will be replaced in all Availability Zones. If you select `Ignore unhealthy`, instances will not be replaced in the Availability Zone with the active zonal shift. For more information, see [Auto Scaling group zonal shift](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-zonal-shift.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: String
Valid Values: `ReplaceUnhealthy | IgnoreUnhealthy`
Required: No

 ** ZonalShiftEnabled **
 If `true`, enable zonal shift for your Auto Scaling group.
Type: Boolean
Required: No

## See Also
<a name="API_AvailabilityZoneImpairmentPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/AvailabilityZoneImpairmentPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/AvailabilityZoneImpairmentPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/AvailabilityZoneImpairmentPolicy)
