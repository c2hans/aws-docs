---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ManagedAutoScaling.html
---

# ManagedAutoScaling
<a name="API_ManagedAutoScaling"></a>

The auto scaling configuration created by Amazon ECS for an Express service.

## Contents
<a name="API_ManagedAutoScaling_Contents"></a>

 ** applicationAutoScalingPolicies **   <a name="ECS-Type-ManagedAutoScaling-applicationAutoScalingPolicies"></a>
The policy used for auto scaling.
Type: Array of [ManagedApplicationAutoScalingPolicy](API_ManagedApplicationAutoScalingPolicy.md) objects
Required: No

 ** scalableTarget **   <a name="ECS-Type-ManagedAutoScaling-scalableTarget"></a>
Represents a scalable target.
Type: [ManagedScalableTarget](API_ManagedScalableTarget.md) object
Required: No

## See Also
<a name="API_ManagedAutoScaling_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ManagedAutoScaling)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ManagedAutoScaling)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ManagedAutoScaling)
