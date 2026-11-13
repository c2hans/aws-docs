---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_SnapshotOperationS3PrefixLocation.html
---

# SnapshotOperationS3PrefixLocation
<a name="API_SnapshotOperationS3PrefixLocation"></a>

Describes an Amazon S3 bucket and key prefix for a snapshot operation.

## Contents
<a name="API_SnapshotOperationS3PrefixLocation_Contents"></a>

 ** BucketARN **   <a name="APIReference-Type-SnapshotOperationS3PrefixLocation-BucketARN"></a>
The ARN of the Amazon S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** KeyPrefix **   <a name="APIReference-Type-SnapshotOperationS3PrefixLocation-KeyPrefix"></a>
The key prefix in the Amazon S3 bucket that you specified in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** ExportedPrefix **   <a name="APIReference-Type-SnapshotOperationS3PrefixLocation-ExportedPrefix"></a>
The full key prefix that the exported snapshot data was written to. This value includes the unique prefix that Managed Service for Apache Flink appends to `KeyPrefix`. This field is present only after an `ExportSnapshot` operation completes successfully.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

## See Also
<a name="API_SnapshotOperationS3PrefixLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/SnapshotOperationS3PrefixLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/SnapshotOperationS3PrefixLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/SnapshotOperationS3PrefixLocation)
