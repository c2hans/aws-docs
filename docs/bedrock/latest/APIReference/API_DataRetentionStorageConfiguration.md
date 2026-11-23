---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DataRetentionStorageConfiguration.html
---

# DataRetentionStorageConfiguration

You provide the Amazon S3 destination and AWS Key Management Service (AWS KMS) key for retained data.

Before saving a customer-managed destination, Amazon Bedrock validates that you can use the bucket and key and that their resource policies permit the required Amazon Bedrock access. If validation fails, Amazon Bedrock rejects the configuration without saving it.

You need `s3:PutObject`, `s3:GetObject`, `kms:GenerateDataKey`, and `kms:Decrypt` permissions. The Amazon S3 bucket policy must allow the Amazon Bedrock service principal, `bedrock.amazonaws.com`, to put, get, and delete objects with conditions appropriate to the configuration scope.

Use `aws:SourceAccount` for account scope, `aws:SourceOrgID` for organization scope, and both `aws:SourceAccount` and the project's `aws:SourceArn` for project scope. Validation rejects resource policies that allow the service principal to access the destination without the required scope conditions.

The key policy must permit `kms:GenerateDataKey` and `kms:Decrypt` for both uses of the key: direct use by Amazon Bedrock with the scope conditions, and use through Amazon S3 with a `kms:ViaService` condition for the bucket's Region and `kms:EncryptionContext:aws:s3:arn` scoped to the bucket.

## Contents
<a name="API_DataRetentionStorageConfiguration_Contents"></a>

 ** kmsKeyArn **   <a name="bedrock-Type-DataRetentionStorageConfiguration-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the customer managed AWS Key Management Service (AWS KMS) key you use to encrypt retained data. Specify an enabled symmetric encryption key in the AWS Region where you register the configuration. You cannot specify a key alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`
Required: Yes

 ** s3BucketArn **   <a name="bedrock-Type-DataRetentionStorageConfiguration-s3BucketArn"></a>
The Amazon Resource Name (ARN) of the Amazon S3 bucket that receives retained data. The bucket must be in the AWS Region where you register the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:s3:::[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]`
Required: Yes

 ** s3BucketOwner **   <a name="bedrock-Type-DataRetentionStorageConfiguration-s3BucketOwner"></a>
The AWS account ID of the destination bucket's owner. You must specify the owner, even when the bucket belongs to another account. Amazon Bedrock uses this ID to verify bucket ownership for each delivery request.
Type: String
Pattern: `[0-9]{12}`
Required: Yes

## See Also
<a name="API_DataRetentionStorageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/DataRetentionStorageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/DataRetentionStorageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/DataRetentionStorageConfiguration)
