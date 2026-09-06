---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterFsxLustreConfig.html
---

# ClusterFsxLustreConfig
<a name="API_ClusterFsxLustreConfig"></a>

Defines the configuration for attaching an Amazon FSx for Lustre file system to instances in a SageMaker HyperPod cluster instance group.

## Contents
<a name="API_ClusterFsxLustreConfig_Contents"></a>

 ** DnsName **   <a name="sagemaker-Type-ClusterFsxLustreConfig-DnsName"></a>
The DNS name of the Amazon FSx for Lustre file system.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 275.
Pattern: `((fs|fc)i?-[0-9a-f]{8,}\..{4,253})`
Required: Yes

 ** MountName **   <a name="sagemaker-Type-ClusterFsxLustreConfig-MountName"></a>
The mount name of the Amazon FSx for Lustre file system.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8.
Pattern: `([A-Za-z0-9_-]{1,8})`
Required: Yes

 ** MountPath **   <a name="sagemaker-Type-ClusterFsxLustreConfig-MountPath"></a>
The local path where the Amazon FSx for Lustre file system is mounted on instances.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `/[a-zA-Z0-9._/-]+`
Required: No

## See Also
<a name="API_ClusterFsxLustreConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterFsxLustreConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterFsxLustreConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterFsxLustreConfig)
