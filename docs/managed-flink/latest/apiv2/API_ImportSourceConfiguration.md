---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ImportSourceConfiguration.html
---

# ImportSourceConfiguration
<a name="API_ImportSourceConfiguration"></a>

Describes the source of the savepoint data to import.

## Contents
<a name="API_ImportSourceConfiguration_Contents"></a>

 ** ImportRoleArn **   <a name="APIReference-Type-ImportSourceConfiguration-ImportRoleArn"></a>
The ARN of the IAM role that Managed Service for Apache Flink assumes to read the savepoint data from the source location. For information about the permissions that this role requires, see [Import and export](https://docs.aws.amazon.com/managed-flink/latest/java/snapshots-import-export.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** SourceS3PrefixLocation **   <a name="APIReference-Type-ImportSourceConfiguration-SourceS3PrefixLocation"></a>
The Amazon S3 bucket and key prefix that contain the savepoint data to import. The bucket must be owned by your account and must be in the same Region as the request.
Type: [S3PrefixLocation](API_S3PrefixLocation.md) object
Required: Yes

 ** SourceType **   <a name="APIReference-Type-ImportSourceConfiguration-SourceType"></a>
The type of the source location. The only supported value is `S3`.
Type: String
Valid Values: `S3`
Required: Yes

 ** SourceEncryptionConfiguration **   <a name="APIReference-Type-ImportSourceConfiguration-SourceEncryptionConfiguration"></a>
The encryption configuration of the savepoint data at the source location. If you don't specify this parameter, Managed Service for Apache Flink uses a key of type `AWS_OWNED_KEY`. If you specify a KMS key, you must specify the key ARN.
Type: [SnapshotEncryptionConfiguration](API_SnapshotEncryptionConfiguration.md) object
Required: No

## See Also
<a name="API_ImportSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ImportSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ImportSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ImportSourceConfiguration)
