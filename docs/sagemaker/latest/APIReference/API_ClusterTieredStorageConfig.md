---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterTieredStorageConfig.html
---

# ClusterTieredStorageConfig
<a name="API_ClusterTieredStorageConfig"></a>

Defines the configuration for managed tier checkpointing in a HyperPod cluster. Managed tier checkpointing uses multiple storage tiers, including cluster CPU memory, to provide faster checkpoint operations and improved fault tolerance for large-scale model training. The system automatically saves checkpoints at high frequency to memory and periodically persists them to durable storage, like Amazon S3.

## Contents
<a name="API_ClusterTieredStorageConfig_Contents"></a>

 ** Mode **   <a name="sagemaker-Type-ClusterTieredStorageConfig-Mode"></a>
Specifies whether managed tier checkpointing is enabled or disabled for the HyperPod cluster. When set to `Enable`, the system installs a memory management daemon that provides disaggregated memory as a service for checkpoint storage. When set to `Disable`, the feature is turned off and the memory management daemon is removed from the cluster.
Type: String
Valid Values: `Enable | Disable`
Required: Yes

 ** InstanceMemoryAllocationPercentage **   <a name="sagemaker-Type-ClusterTieredStorageConfig-InstanceMemoryAllocationPercentage"></a>
The percentage (int) of cluster memory to allocate for checkpointing.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## See Also
<a name="API_ClusterTieredStorageConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterTieredStorageConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterTieredStorageConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterTieredStorageConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
