---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AcceleratorPartitionLayout.html
---

# AcceleratorPartitionLayout
<a name="API_AcceleratorPartitionLayout"></a>

A layout of accelerator partitions for a production variant. On NVIDIA GPUs, the partitions are Multi-Instance GPU (MIG) instances. SageMaker applies the layout to every accelerator on the variant's instance type. You can't change the layout of a running endpoint. To use a different layout, create a new endpoint.

## Contents
<a name="API_AcceleratorPartitionLayout_Contents"></a>

 ** AcceleratorPartitionTypes **   <a name="sagemaker-Type-AcceleratorPartitionLayout-AcceleratorPartitionTypes"></a>
The list of partition profiles to carve on each accelerator that this layout applies to. On NVIDIA GPUs these are Multi-Instance GPU (MIG) profiles, for example `["mig-3g.40gb", "mig-4g.40gb"]`. The order of the profiles doesn't change how the accelerator is partitioned. However, when you update an endpoint, a layout with the same profiles in a different order counts as a different layout, and the update is rejected. Repeat a profile to request more than one partition of that size: for example, `["mig-3g.40gb", "mig-3g.40gb"]` requests two `mig-3g.40gb` partitions.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `mig-[0-9]+g\.[0-9]+gb([+-][a-z0-9.]+)*`
Required: No

## See Also
<a name="API_AcceleratorPartitionLayout_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AcceleratorPartitionLayout)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AcceleratorPartitionLayout)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AcceleratorPartitionLayout)
