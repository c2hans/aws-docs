---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_CapacityProviderScalingConfig.html
---

# CapacityProviderScalingConfig
<a name="API_CapacityProviderScalingConfig"></a>

Configuration that defines how the capacity provider scales compute instances based on demand and policies.

## Contents
<a name="API_CapacityProviderScalingConfig_Contents"></a>

 ** MaxVCpuCount **   <a name="lambda-Type-CapacityProviderScalingConfig-MaxVCpuCount"></a>
The maximum number of vCPUs that the capacity provider can provision across all compute instances.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 15000.
Required: No

 ** ScalingMode **   <a name="lambda-Type-CapacityProviderScalingConfig-ScalingMode"></a>
The scaling mode that determines how the capacity provider responds to changes in demand.
Type: String
Valid Values: `Auto | Manual`
Required: No

 ** ScalingPolicies **   <a name="lambda-Type-CapacityProviderScalingConfig-ScalingPolicies"></a>
A list of scaling policies that define how the capacity provider scales compute instances based on metrics and thresholds.
Type: Array of [TargetTrackingScalingPolicy](API_TargetTrackingScalingPolicy.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_CapacityProviderScalingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/CapacityProviderScalingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/CapacityProviderScalingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/CapacityProviderScalingConfig)
