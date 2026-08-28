---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterEbsVolumeConfig.html
---

# ClusterEbsVolumeConfig
<a name="API_ClusterEbsVolumeConfig"></a>

Defines the configuration for attaching an additional Amazon Elastic Block Store (EBS) volume to each instance of the SageMaker HyperPod cluster instance group. To learn more, see [SageMaker HyperPod release notes: June 20, 2024](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-release-notes.html#sagemaker-hyperpod-release-notes-20240620).

## Contents
<a name="API_ClusterEbsVolumeConfig_Contents"></a>

 ** RootVolume **   <a name="sagemaker-Type-ClusterEbsVolumeConfig-RootVolume"></a>
Specifies whether the configuration is for the cluster's root or secondary Amazon EBS volume. You can specify two `ClusterEbsVolumeConfig` fields to configure both the root and secondary volumes. Set the value to `True` if you'd like to provide your own customer managed AWS KMS key to encrypt the root volume. When `True`:
+ The configuration is applied to the root volume.
+ You can't specify the `VolumeSizeInGB` field. The size of the root volume is determined for you.
+ You must specify a KMS key ID for `VolumeKmsKeyId` to encrypt the root volume with your own KMS key instead of an AWS owned KMS key.
Otherwise, by default, the value is `False`, and the following applies:
+ The configuration is applied to the secondary volume, while the root volume is encrypted with an AWS owned key.
+ You must specify the `VolumeSizeInGB` field.
+ You can optionally specify the `VolumeKmsKeyId` to encrypt the secondary volume with your own KMS key instead of an AWS owned KMS key.
Type: Boolean
Required: No

 ** VolumeKmsKeyId **   <a name="sagemaker-Type-ClusterEbsVolumeConfig-VolumeKmsKeyId"></a>
The ID of a KMS key to encrypt the Amazon EBS volume.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** VolumeSizeInGB **   <a name="sagemaker-Type-ClusterEbsVolumeConfig-VolumeSizeInGB"></a>
The size in gigabytes (GB) of the additional EBS volume to be attached to the instances in the SageMaker HyperPod cluster instance group. The additional EBS volume is attached to each instance within the SageMaker HyperPod cluster instance group and mounted to `/opt/sagemaker`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 16384.
Required: No

## See Also
<a name="API_ClusterEbsVolumeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterEbsVolumeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterEbsVolumeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterEbsVolumeConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
