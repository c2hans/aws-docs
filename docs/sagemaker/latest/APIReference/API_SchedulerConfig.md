---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SchedulerConfig.html
---

# SchedulerConfig
<a name="API_SchedulerConfig"></a>

Cluster policy configuration. This policy is used for task prioritization and fair-share allocation. This helps prioritize critical workloads and distributes idle compute across entities.

## Contents
<a name="API_SchedulerConfig_Contents"></a>

 ** FairShare **   <a name="sagemaker-Type-SchedulerConfig-FairShare"></a>
When enabled, entities borrow idle compute based on their assigned `FairShareWeight`.
When disabled, entities borrow idle compute based on a first-come first-serve basis.
Default is `Enabled`.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

 ** IdleResourceSharing **   <a name="sagemaker-Type-SchedulerConfig-IdleResourceSharing"></a>
Configuration for sharing idle compute resources across entities in the cluster. When enabled, unallocated resources are automatically calculated and made available for entities to borrow.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

 ** PriorityClasses **   <a name="sagemaker-Type-SchedulerConfig-PriorityClasses"></a>
List of the priority classes, `PriorityClass`, of the cluster policy. When specified, these class configurations define how tasks are queued.
Type: Array of [PriorityClass](API_PriorityClass.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_SchedulerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/SchedulerConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/SchedulerConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/SchedulerConfig)
