---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterFsxOpenZfsConfig.html
---

# ClusterFsxOpenZfsConfig
<a name="API_ClusterFsxOpenZfsConfig"></a>

Defines the configuration for attaching an Amazon FSx for OpenZFS file system to instances in a SageMaker HyperPod cluster instance group.

## Contents
<a name="API_ClusterFsxOpenZfsConfig_Contents"></a>

 ** DnsName **   <a name="sagemaker-Type-ClusterFsxOpenZfsConfig-DnsName"></a>
The DNS name of the Amazon FSx for OpenZFS file system.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 275.
Pattern: `((fs|fc)i?-[0-9a-f]{8,}\..{4,253})`
Required: Yes

 ** MountPath **   <a name="sagemaker-Type-ClusterFsxOpenZfsConfig-MountPath"></a>
The local path where the Amazon FSx for OpenZFS file system is mounted on instances.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `/[a-zA-Z0-9._/-]+`
Required: No

## See Also
<a name="API_ClusterFsxOpenZfsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterFsxOpenZfsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterFsxOpenZfsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterFsxOpenZfsConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
