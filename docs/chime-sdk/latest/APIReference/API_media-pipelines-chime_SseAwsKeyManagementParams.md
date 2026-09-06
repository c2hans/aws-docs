---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_SseAwsKeyManagementParams.html
---

# SseAwsKeyManagementParams
<a name="API_media-pipelines-chime_SseAwsKeyManagementParams"></a>

Contains server side encryption parameters to be used by media capture pipeline. The parameters can also be used by media concatenation pipeline taking media capture pipeline as a media source.

## Contents
<a name="API_media-pipelines-chime_SseAwsKeyManagementParams_Contents"></a>

 ** AwsKmsKeyId **   <a name="chimesdk-Type-media-pipelines-chime_SseAwsKeyManagementParams-AwsKmsKeyId"></a>
The AWS KMS key you want to use to encrypt your media pipeline output. Decryption is required for concatenation pipeline. If using a key located in the current AWS account, you can specify your AWS KMS key in one of four ways:
+ Use the AWS KMS key ID itself. For example, `1234abcd-12ab-34cd-56ef-1234567890ab`.
+ Use an alias for the AWS KMS key ID. For example, `alias/ExampleAlias`.
+ Use the Amazon Resource Name (ARN) for the AWS KMS key ID. For example, `arn:aws:kms:region:account-ID:key/1234abcd-12ab-34cd-56ef-1234567890ab`.
+ Use the ARN for the AWS KMS key alias. For example, `arn:aws:kms:region:account-ID:alias/ExampleAlias`.
If using a key located in a different AWS account than the current AWS account, you can specify your AWS KMS key in one of two ways:
+ Use the ARN for the AWS KMS key ID. For example, `arn:aws:kms:region:account-ID:key/1234abcd-12ab-34cd-56ef-1234567890ab`.
+ Use the ARN for the AWS KMS key alias. For example, `arn:aws:kms:region:account-ID:alias/ExampleAlias`.
If you don't specify an encryption key, your output is encrypted with the default Amazon S3 key (SSE-S3).
Note that the role specified in the `SinkIamRoleArn` request parameter must have permission to use the specified KMS key.
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `.*`
Required: Yes

 ** AwsKmsEncryptionContext **   <a name="chimesdk-Type-media-pipelines-chime_SseAwsKeyManagementParams-AwsKmsEncryptionContext"></a>
Base64-encoded string of a UTF-8 encoded JSON, which contains the encryption context as non-secret key-value pair known as encryption context pairs, that provides an added layer of security for your data. For more information, see [AWS KMS encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html) and [Asymmetric keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the * AWS Key Management Service Developer Guide*.
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `.*`
Required: No

## See Also
<a name="API_media-pipelines-chime_SseAwsKeyManagementParams_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/SseAwsKeyManagementParams)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/SseAwsKeyManagementParams)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/SseAwsKeyManagementParams)
