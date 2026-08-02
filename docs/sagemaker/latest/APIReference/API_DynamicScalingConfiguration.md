---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DynamicScalingConfiguration.html
---

# DynamicScalingConfiguration
<a name="API_DynamicScalingConfiguration"></a>

An object with the recommended values for you to specify when creating an autoscaling policy.

## Contents
<a name="API_DynamicScalingConfiguration_Contents"></a>

 ** MaxCapacity **   <a name="sagemaker-Type-DynamicScalingConfiguration-MaxCapacity"></a>
The recommended maximum capacity to specify for your autoscaling policy.
Type: Integer
Required: No

 ** MinCapacity **   <a name="sagemaker-Type-DynamicScalingConfiguration-MinCapacity"></a>
The recommended minimum capacity to specify for your autoscaling policy.
Type: Integer
Required: No

 ** ScaleInCooldown **   <a name="sagemaker-Type-DynamicScalingConfiguration-ScaleInCooldown"></a>
The recommended scale in cooldown time for your autoscaling policy.
Type: Integer
Required: No

 ** ScaleOutCooldown **   <a name="sagemaker-Type-DynamicScalingConfiguration-ScaleOutCooldown"></a>
The recommended scale out cooldown time for your autoscaling policy.
Type: Integer
Required: No

 ** ScalingPolicies **   <a name="sagemaker-Type-DynamicScalingConfiguration-ScalingPolicies"></a>
An object of the scaling policies for each metric.
Type: Array of [ScalingPolicy](API_ScalingPolicy.md) objects
Required: No

## See Also
<a name="API_DynamicScalingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DynamicScalingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DynamicScalingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DynamicScalingConfiguration)
