---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails.html
---

# AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails
<a name="API_AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails"></a>

Information about the instances distribution.

## Contents
<a name="API_AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails_Contents"></a>

 ** OnDemandAllocationStrategy **   <a name="securityhub-Type-AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails-OnDemandAllocationStrategy"></a>
How to allocate instance types to fulfill On-Demand capacity. The valid value is `prioritized`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** OnDemandBaseCapacity **   <a name="securityhub-Type-AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails-OnDemandBaseCapacity"></a>
The minimum amount of the Auto Scaling group's capacity that must be fulfilled by On-Demand Instances.
Type: Integer
Required: No

 ** OnDemandPercentageAboveBaseCapacity **   <a name="securityhub-Type-AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails-OnDemandPercentageAboveBaseCapacity"></a>
The percentage of On-Demand Instances and Spot Instances for additional capacity beyond `OnDemandBaseCapacity`.
Type: Integer
Required: No

 ** SpotAllocationStrategy **   <a name="securityhub-Type-AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails-SpotAllocationStrategy"></a>
How to allocate instances across Spot Instance pools. Valid values are as follows:
+  `lowest-price`
+  `capacity-optimized`
+  `capacity-optimized-prioritized`
Type: String
Pattern: `.*\S.*`
Required: No

 ** SpotInstancePools **   <a name="securityhub-Type-AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails-SpotInstancePools"></a>
The number of Spot Instance pools across which to allocate your Spot Instances.
Type: Integer
Required: No

 ** SpotMaxPrice **   <a name="securityhub-Type-AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails-SpotMaxPrice"></a>
The maximum price per unit hour that you are willing to pay for a Spot Instance.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails)
