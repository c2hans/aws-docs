---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterLifeCycleConfig.html
---

# ClusterLifeCycleConfig
<a name="API_ClusterLifeCycleConfig"></a>

The lifecycle configuration for a SageMaker HyperPod cluster.

## Contents
<a name="API_ClusterLifeCycleConfig_Contents"></a>

 ** OnCreate **   <a name="sagemaker-Type-ClusterLifeCycleConfig-OnCreate"></a>
The file name of the entrypoint script of lifecycle scripts under `SourceS3Uri`. This entrypoint script runs during cluster creation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\S\s]+`
Required: No

 ** OnInitComplete **   <a name="sagemaker-Type-ClusterLifeCycleConfig-OnInitComplete"></a>
The file name of the entrypoint script of lifecycle scripts under `SourceS3Uri`. This script runs on the node after the AMI-based initialization is complete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\S\s]+`
Required: No

 ** SourceS3Uri **   <a name="sagemaker-Type-ClusterLifeCycleConfig-SourceS3Uri"></a>
An Amazon S3 bucket path where your lifecycle scripts are stored.
Make sure that the S3 bucket path starts with `s3://sagemaker-`. The [IAM role for SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.html#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod) has the managed [`AmazonSageMakerClusterInstanceRolePolicy`](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-cluster.html) attached, which allows access to S3 buckets with the specific prefix `sagemaker-`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

## See Also
<a name="API_ClusterLifeCycleConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterLifeCycleConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterLifeCycleConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterLifeCycleConfig)
