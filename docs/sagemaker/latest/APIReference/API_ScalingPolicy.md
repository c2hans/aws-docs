---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ScalingPolicy.html
---

# ScalingPolicy
<a name="API_ScalingPolicy"></a>

An object containing a recommended scaling policy.

## Contents
<a name="API_ScalingPolicy_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** TargetTracking **   <a name="sagemaker-Type-ScalingPolicy-TargetTracking"></a>
A target tracking scaling policy. Includes support for predefined or customized metrics.
Type: [TargetTrackingScalingPolicyConfiguration](API_TargetTrackingScalingPolicyConfiguration.md) object
Required: No

## See Also
<a name="API_ScalingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ScalingPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ScalingPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ScalingPolicy)
