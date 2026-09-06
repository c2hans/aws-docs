---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ComputeQuotaConfig.html
---

# ComputeQuotaConfig
<a name="API_ComputeQuotaConfig"></a>

Configuration of the compute allocation definition for an entity. This includes the resource sharing option and the setting to preempt low priority tasks.

## Contents
<a name="API_ComputeQuotaConfig_Contents"></a>

 ** ComputeQuotaResources **   <a name="sagemaker-Type-ComputeQuotaConfig-ComputeQuotaResources"></a>
Allocate compute resources by instance types.
Type: Array of [ComputeQuotaResourceConfig](API_ComputeQuotaResourceConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 15 items.
Required: No

 ** PreemptTeamTasks **   <a name="sagemaker-Type-ComputeQuotaConfig-PreemptTeamTasks"></a>
Allows workloads from within an entity to preempt same-team workloads. When set to `LowerPriority`, the entity's lower priority tasks are preempted by their own higher priority tasks.
Default is `LowerPriority`.
Type: String
Valid Values: `Never | LowerPriority`
Required: No

 ** ResourceSharingConfig **   <a name="sagemaker-Type-ComputeQuotaConfig-ResourceSharingConfig"></a>
Resource sharing configuration. This defines how an entity can lend and borrow idle compute with other entities within the cluster.
Type: [ResourceSharingConfig](API_ResourceSharingConfig.md) object
Required: No

## See Also
<a name="API_ComputeQuotaConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ComputeQuotaConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ComputeQuotaConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ComputeQuotaConfig)
