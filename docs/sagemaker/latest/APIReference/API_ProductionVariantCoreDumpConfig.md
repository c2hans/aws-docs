---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariantCoreDumpConfig.html
---

# ProductionVariantCoreDumpConfig
<a name="API_ProductionVariantCoreDumpConfig"></a>

Specifies configuration for a core dump from the model container when the process crashes.

## Contents
<a name="API_ProductionVariantCoreDumpConfig_Contents"></a>

 ** DestinationS3Uri **   <a name="sagemaker-Type-ProductionVariantCoreDumpConfig-DestinationS3Uri"></a>
The Amazon S3 bucket to send the core dump to.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `(https|s3)://([^/])/?(.*)`
Required: Yes

 ** KmsKeyId **   <a name="sagemaker-Type-ProductionVariantCoreDumpConfig-KmsKeyId"></a>
The AWS Key Management Service (AWS KMS) key that SageMaker uses to encrypt the core dump data at rest using Amazon S3 server-side encryption. The `KmsKeyId` can be any of the following formats:
+ // KMS Key ID

   `"1234abcd-12ab-34cd-56ef-1234567890ab"`
+ // Amazon Resource Name (ARN) of a KMS Key

   `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`
+ // KMS Key Alias

   `"alias/ExampleAlias"`
+ // Amazon Resource Name (ARN) of a KMS Key Alias

   `"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"`
If you use a KMS key ID or an alias of your KMS key, the SageMaker execution role must include permissions to call `kms:Encrypt`. If you don't provide a KMS key ID, SageMaker uses the default KMS key for Amazon S3 for your role's account. SageMaker uses server-side encryption with KMS-managed keys for `OutputDataConfig`. If you use a bucket policy with an `s3:PutObject` permission that only allows objects with server-side encryption, set the condition key of `s3:x-amz-server-side-encryption` to `"aws:kms"`. For more information, see [KMS-Managed Encryption Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html) in the *Amazon Simple Storage Service Developer Guide.*
The KMS key policy must grant permission to the IAM role that you specify in your `CreateEndpoint` and `UpdateEndpoint` requests. For more information, see [Using Key Policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the * AWS Key Management Service Developer Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

## See Also
<a name="API_ProductionVariantCoreDumpConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ProductionVariantCoreDumpConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ProductionVariantCoreDumpConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ProductionVariantCoreDumpConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
