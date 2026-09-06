---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_MixedInstancesPolicy.html
---

# MixedInstancesPolicy
<a name="API_MixedInstancesPolicy"></a>

Use this structure to launch multiple instance types and configure how capacity is distributed across On-Demand, Spot, and supported Capacity Reservation types within a single Auto Scaling group.

A mixed instances policy contains information that Amazon EC2 Auto Scaling can use to launch instances, prioritize capacity types, and help optimize your costs. For more information, see [Auto Scaling groups with multiple instance types and purchase options](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html) in the *Amazon EC2 Auto Scaling User Guide*. To learn how to prioritize multiple capacity types, see [Use Distribution Segments to target multiple capacity types](https://docs.aws.amazon.com/autoscaling/ec2/userguide/use-distribution-segments.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Contents
<a name="API_MixedInstancesPolicy_Contents"></a>

 ** InstancesDistribution **
The instances distribution.
Type: [InstancesDistribution](API_InstancesDistribution.md) object
Required: No

 ** LaunchTemplate **
One or more launch templates and the instance types (overrides) that are used to launch EC2 instances to fulfill the configured capacities.
Type: [LaunchTemplate](API_LaunchTemplate.md) object
Required: No

## See Also
<a name="API_MixedInstancesPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/MixedInstancesPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/MixedInstancesPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/MixedInstancesPolicy)
