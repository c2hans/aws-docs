---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TargetTrackingScalingPolicyConfiguration.html
---

# TargetTrackingScalingPolicyConfiguration
<a name="API_TargetTrackingScalingPolicyConfiguration"></a>

A target tracking scaling policy. Includes support for predefined or customized metrics.

When using the [PutScalingPolicy](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PutScalingPolicy.html) API, this parameter is required when you are creating a policy with the policy type `TargetTrackingScaling`.

## Contents
<a name="API_TargetTrackingScalingPolicyConfiguration_Contents"></a>

 ** MetricSpecification **   <a name="sagemaker-Type-TargetTrackingScalingPolicyConfiguration-MetricSpecification"></a>
An object containing information about a metric.
Type: [MetricSpecification](API_MetricSpecification.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** TargetValue **   <a name="sagemaker-Type-TargetTrackingScalingPolicyConfiguration-TargetValue"></a>
The recommended target value to specify for the metric when creating a scaling policy.
Type: Double
Required: No

## See Also
<a name="API_TargetTrackingScalingPolicyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TargetTrackingScalingPolicyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TargetTrackingScalingPolicyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TargetTrackingScalingPolicyConfiguration)
