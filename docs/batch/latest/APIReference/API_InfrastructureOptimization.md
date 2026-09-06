---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_InfrastructureOptimization.html
---

# InfrastructureOptimization
<a name="API_InfrastructureOptimization"></a>

The infrastructure optimization configuration for an Amazon ECS Managed Instances capacity provider. Specifies the idle-instance scale-in behavior.

## Contents
<a name="API_InfrastructureOptimization_Contents"></a>

 ** scaleInAfter **   <a name="Batch-Type-InfrastructureOptimization-scaleInAfter"></a>
The number of seconds an instance can remain idle before it is terminated. Valid values are `-1` or `0` to `3600`. Use `-1` as a special value to disable scale-in (instances are never terminated for being idle). If not specified, a default value applies.
Type: Integer
Required: No

## See Also
<a name="API_InfrastructureOptimization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/InfrastructureOptimization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/InfrastructureOptimization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/InfrastructureOptimization)
