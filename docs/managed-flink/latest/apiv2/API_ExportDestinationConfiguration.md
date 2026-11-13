---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ExportDestinationConfiguration.html
---

# ExportDestinationConfiguration
<a name="API_ExportDestinationConfiguration"></a>

Describes the destination of the exported snapshot data.

## Contents
<a name="API_ExportDestinationConfiguration_Contents"></a>

 ** DestinationS3PrefixLocation **   <a name="APIReference-Type-ExportDestinationConfiguration-DestinationS3PrefixLocation"></a>
The Amazon S3 bucket and key prefix to export the snapshot data to. Managed Service for Apache Flink writes the data under a unique prefix that it appends to the key prefix that you specify. After the export completes, use `DescribeSnapshotOperation` to get the full prefix. The bucket must be owned by your account and must be in the same Region as the request.
Type: [S3PrefixLocation](API_S3PrefixLocation.md) object
Required: Yes

 ** DestinationType **   <a name="APIReference-Type-ExportDestinationConfiguration-DestinationType"></a>
The type of the destination location. The only supported value is `S3`.
Type: String
Valid Values: `S3`
Required: Yes

 ** ExportRoleArn **   <a name="APIReference-Type-ExportDestinationConfiguration-ExportRoleArn"></a>
The ARN of the IAM role that Managed Service for Apache Flink assumes to write the snapshot data to the destination location. For information about the permissions that this role requires, see [Import and export](https://docs.aws.amazon.com/managed-flink/latest/java/snapshots-import-export.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** DestinationEncryptionConfiguration **   <a name="APIReference-Type-ExportDestinationConfiguration-DestinationEncryptionConfiguration"></a>
The encryption configuration of the exported snapshot data. If you don't specify this parameter, Managed Service for Apache Flink uses a key of type `AWS_OWNED_KEY`. If you specify a KMS key, you must specify the key ARN.
Type: [SnapshotEncryptionConfiguration](API_SnapshotEncryptionConfiguration.md) object
Required: No

## See Also
<a name="API_ExportDestinationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ExportDestinationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ExportDestinationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ExportDestinationConfiguration)
