---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterInstanceStorageConfig.html
---

# ClusterInstanceStorageConfig
<a name="API_ClusterInstanceStorageConfig"></a>

Defines the configuration for attaching additional storage to the instances in the SageMaker HyperPod cluster instance group. To learn more, see [SageMaker HyperPod release notes: June 20, 2024](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-release-notes.html#sagemaker-hyperpod-release-notes-20240620).

## Contents
<a name="API_ClusterInstanceStorageConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** EbsVolumeConfig **   <a name="sagemaker-Type-ClusterInstanceStorageConfig-EbsVolumeConfig"></a>
Defines the configuration for attaching additional Amazon Elastic Block Store (EBS) volumes to the instances in the SageMaker HyperPod cluster instance group. The additional EBS volume is attached to each instance within the SageMaker HyperPod cluster instance group and mounted to `/opt/sagemaker`.
Type: [ClusterEbsVolumeConfig](API_ClusterEbsVolumeConfig.md) object
Required: No

 ** FsxLustreConfig **   <a name="sagemaker-Type-ClusterInstanceStorageConfig-FsxLustreConfig"></a>
Defines the configuration for attaching an Amazon FSx for Lustre file system to the instances in the SageMaker HyperPod cluster instance group.
Type: [ClusterFsxLustreConfig](API_ClusterFsxLustreConfig.md) object
Required: No

 ** FsxOpenZfsConfig **   <a name="sagemaker-Type-ClusterInstanceStorageConfig-FsxOpenZfsConfig"></a>
Defines the configuration for attaching an Amazon FSx for OpenZFS file system to the instances in the SageMaker HyperPod cluster instance group.
Type: [ClusterFsxOpenZfsConfig](API_ClusterFsxOpenZfsConfig.md) object
Required: No

## See Also
<a name="API_ClusterInstanceStorageConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterInstanceStorageConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterInstanceStorageConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterInstanceStorageConfig)
