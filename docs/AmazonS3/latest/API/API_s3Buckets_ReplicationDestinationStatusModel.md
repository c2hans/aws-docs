---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_ReplicationDestinationStatusModel.html
---

# ReplicationDestinationStatusModel
<a name="API_s3Buckets_ReplicationDestinationStatusModel"></a>

Contains status information for a replication destination, including the current replication state, last successful update, and any error messages.

## Contents
<a name="API_s3Buckets_ReplicationDestinationStatusModel_Contents"></a>

 ** destinationTableBucketArn **   <a name="AmazonS3-Type-s3Buckets_ReplicationDestinationStatusModel-destinationTableBucketArn"></a>
The Amazon Resource Name (ARN) of the destination table bucket.
Type: String
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`
Required: Yes

 ** replicationStatus **   <a name="AmazonS3-Type-s3Buckets_ReplicationDestinationStatusModel-replicationStatus"></a>
The current status of replication to this destination.
Type: String
Valid Values: `pending | completed | failed`
Required: Yes

 ** destinationTableArn **   <a name="AmazonS3-Type-s3Buckets_ReplicationDestinationStatusModel-destinationTableArn"></a>
The Amazon Resource Name (ARN) of the destination table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`
Required: No

 ** failureMessage **   <a name="AmazonS3-Type-s3Buckets_ReplicationDestinationStatusModel-failureMessage"></a>
If replication has failed, this field contains an error message describing the failure reason.
Type: String
Required: No

 ** lastSuccessfulReplicatedUpdate **   <a name="AmazonS3-Type-s3Buckets_ReplicationDestinationStatusModel-lastSuccessfulReplicatedUpdate"></a>
Information about the most recent successful replication update to this destination.
Type: [LastSuccessfulReplicatedUpdate](API_s3Buckets_LastSuccessfulReplicatedUpdate.md) object
Required: No

## See Also
<a name="API_s3Buckets_ReplicationDestinationStatusModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/ReplicationDestinationStatusModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/ReplicationDestinationStatusModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/ReplicationDestinationStatusModel)
