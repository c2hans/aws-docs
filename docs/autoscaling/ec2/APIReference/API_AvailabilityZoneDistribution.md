---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AvailabilityZoneDistribution.html
---

# AvailabilityZoneDistribution
<a name="API_AvailabilityZoneDistribution"></a>

 Describes an Availability Zone distribution.

## Contents
<a name="API_AvailabilityZoneDistribution_Contents"></a>

 ** CapacityDistributionStrategy **
 If launches fail in an Availability Zone, the following strategies are available. The default is `balanced-best-effort`.
+  `balanced-only` - If launches fail in an Availability Zone, Auto Scaling will continue to attempt to launch in the unhealthy zone to preserve a balanced distribution.
+  `balanced-best-effort` - If launches fail in an Availability Zone, Auto Scaling will attempt to launch in another healthy Availability Zone instead.
+  `reservations-then-balanced` - Auto Scaling will first attempt to launch into your Capacity Reservations, and then balance any remaining capacity across healthy Availability Zones.
Type: String
Valid Values: `balanced-only | balanced-best-effort | reservations-then-balanced`
Required: No

## See Also
<a name="API_AvailabilityZoneDistribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/AvailabilityZoneDistribution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/AvailabilityZoneDistribution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/AvailabilityZoneDistribution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
