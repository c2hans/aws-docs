---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_S3StorageConfig.html
---

# S3StorageConfig
<a name="API_S3StorageConfig"></a>

The Amazon Simple Storage (Amazon S3) location and security configuration for `OfflineStore`.

## Contents
<a name="API_S3StorageConfig_Contents"></a>

 ** S3Uri **   <a name="sagemaker-Type-S3StorageConfig-S3Uri"></a>
The S3 URI, or location in Amazon S3, of `OfflineStore`.
S3 URIs have a format similar to the following: `s3://example-bucket/prefix/`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** KmsKeyId **   <a name="sagemaker-Type-S3StorageConfig-KmsKeyId"></a>
The AWS Key Management Service (KMS) key ARN of the key used to encrypt any objects written into the `OfflineStore` S3 location.
The IAM `roleARN` that is passed as a parameter to `CreateFeatureGroup` must have below permissions to the `KmsKeyId`:
+  `"kms:GenerateDataKey"`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** ResolvedOutputS3Uri **   <a name="sagemaker-Type-S3StorageConfig-ResolvedOutputS3Uri"></a>
The S3 path where offline records are written.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

## See Also
<a name="API_S3StorageConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/S3StorageConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/S3StorageConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/S3StorageConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
