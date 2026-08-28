---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OutputDataConfig.html
---

# OutputDataConfig
<a name="API_OutputDataConfig"></a>

Provides information about how to store model training results (model artifacts).

## Contents
<a name="API_OutputDataConfig_Contents"></a>

 ** S3OutputPath **   <a name="sagemaker-Type-OutputDataConfig-S3OutputPath"></a>
Identifies the S3 path where you want SageMaker to store the model artifacts. For example, `s3://bucket-name/key-name-prefix`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** CompressionType **   <a name="sagemaker-Type-OutputDataConfig-CompressionType"></a>
The model output compression type. Select `None` to output an uncompressed model, recommended for large model outputs. Defaults to gzip.
Type: String
Valid Values: `GZIP | NONE`
Required: No

 ** KmsKeyId **   <a name="sagemaker-Type-OutputDataConfig-KmsKeyId"></a>
The AWS Key Management Service (AWS KMS) key that SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The `KmsKeyId` can be any of the following formats:
+ // KMS Key ID

   `"1234abcd-12ab-34cd-56ef-1234567890ab"`
+ // Amazon Resource Name (ARN) of a KMS Key

   `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`
+ // KMS Key Alias

   `"alias/ExampleAlias"`
+ // Amazon Resource Name (ARN) of a KMS Key Alias

   `"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"`
If you use a KMS key ID or an alias of your KMS key, the SageMaker execution role must include permissions to call `kms:Encrypt`. If you don't provide a KMS key ID, SageMaker uses the default KMS key for Amazon S3 for your role's account. For more information, see [KMS-Managed Encryption Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html) in the *Amazon Simple Storage Service Developer Guide*. If the output data is stored in Amazon S3 Express One Zone, it is encrypted with server-side encryption with Amazon S3 managed keys (SSE-S3). KMS key is not supported for Amazon S3 Express One Zone
The KMS key policy must grant permission to the IAM role that you specify in your `CreateTrainingJob`, `CreateTransformJob`, or `CreateHyperParameterTuningJob` requests. For more information, see [Using Key Policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the * AWS Key Management Service Developer Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

## See Also
<a name="API_OutputDataConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/OutputDataConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/OutputDataConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/OutputDataConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
