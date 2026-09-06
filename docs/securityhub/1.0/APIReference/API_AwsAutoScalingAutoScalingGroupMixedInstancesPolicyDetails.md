---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails.html
---

# AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails
<a name="API_AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails"></a>

The mixed instances policy for the automatic scaling group.

## Contents
<a name="API_AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails_Contents"></a>

 ** InstancesDistribution **   <a name="securityhub-Type-AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails-InstancesDistribution"></a>
The instances distribution. The instances distribution specifies the distribution of On-Demand Instances and Spot Instances, the maximum price to pay for Spot Instances, and how the Auto Scaling group allocates instance types to fulfill On-Demand and Spot capacity.
Type: [AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails](API_AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails.md) object
Required: No

 ** LaunchTemplate **   <a name="securityhub-Type-AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails-LaunchTemplate"></a>
The launch template to use and the instance types (overrides) to use to provision EC2 instances to fulfill On-Demand and Spot capacities.
Type: [AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetails](API_AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetails.md) object
Required: No

## See Also
<a name="API_AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails)
