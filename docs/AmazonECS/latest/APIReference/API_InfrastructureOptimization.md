---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_InfrastructureOptimization.html
---

# InfrastructureOptimization
<a name="API_InfrastructureOptimization"></a>

The configuration that controls how Amazon ECS optimizes your infrastructure.

## Contents
<a name="API_InfrastructureOptimization_Contents"></a>

 ** scaleInAfter **   <a name="ECS-Type-InfrastructureOptimization-scaleInAfter"></a>
This parameter defines the number of seconds Amazon ECS Managed Instances waits before optimizing EC2 instances that have become idle or underutilized. A longer delay increases the likelihood of placing new tasks on idle or underutilized instances instances, reducing startup time. A shorter delay helps reduce infrastructure costs by optimizing idle or underutilized instances,instances more quickly.
Valid values are:
+  `null` - Uses the default optimization behavior.
+  `-1` - Disables automatic infrastructure optimization.
+ A value between `0` and `3600` (inclusive) - Specifies the number of seconds to wait before optimizing instances.
Type: Integer
Required: No

## See Also
<a name="API_InfrastructureOptimization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/InfrastructureOptimization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/InfrastructureOptimization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/InfrastructureOptimization)
