---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_Destination.html
---

# Destination
<a name="API_Destination"></a>

Specifies information about where to publish analysis or configuration results for an Amazon S3 bucket and S3 Replication Time Control (S3 RTC).

## Contents
<a name="API_Destination_Contents"></a>

 ** Bucket **   <a name="AmazonS3-Type-Destination-Bucket"></a>
 The Amazon Resource Name (ARN) of the bucket where you want Amazon S3 to store the results.
Type: String
Required: Yes

 ** AccessControlTranslation **   <a name="AmazonS3-Type-Destination-AccessControlTranslation"></a>
Specify this only in a cross-account scenario (where source and destination bucket owners are not the same), and you want to change replica ownership to the AWS account that owns the destination bucket. If this is not specified in the replication configuration, the replicas are owned by same AWS account that owns the source object.
Type: [AccessControlTranslation](API_AccessControlTranslation.md) data type
Required: No

 ** Account **   <a name="AmazonS3-Type-Destination-Account"></a>
Destination bucket owner account ID. In a cross-account scenario, if you direct Amazon S3 to change replica ownership to the AWS account that owns the destination bucket by specifying the `AccessControlTranslation` property, this is the account ID of the destination bucket owner. For more information, see [Replication Additional Configuration: Changing the Replica Owner](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-change-owner.html) in the *Amazon S3 User Guide*.
Type: String
Required: No

 ** EncryptionConfiguration **   <a name="AmazonS3-Type-Destination-EncryptionConfiguration"></a>
A container that provides information about encryption. If `SourceSelectionCriteria` is specified, you must specify this element.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) data type
Required: No

 ** Metrics **   <a name="AmazonS3-Type-Destination-Metrics"></a>
 A container specifying replication metrics-related settings enabling replication metrics and events.
Type: [Metrics](API_Metrics.md) data type
Required: No

 ** ReplicationTime **   <a name="AmazonS3-Type-Destination-ReplicationTime"></a>
 A container specifying S3 Replication Time Control (S3 RTC), including whether S3 RTC is enabled and the time when all objects and operations on objects must be replicated. Must be specified together with a `Metrics` block.
Type: [ReplicationTime](API_ReplicationTime.md) data type
Required: No

 ** StorageClass **   <a name="AmazonS3-Type-Destination-StorageClass"></a>
 The storage class to use when replicating objects, such as S3 Standard or reduced redundancy. By default, Amazon S3 uses the storage class of the source object to create the object replica.
For valid values, see the `StorageClass` element of the [PUT Bucket replication](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTreplication.html) action in the *Amazon S3 API Reference*.
 `FSX_OPENZFS` is not an accepted value when replicating objects.
Type: String
Valid Values: `STANDARD | REDUCED_REDUNDANCY | STANDARD_IA | ONEZONE_IA | INTELLIGENT_TIERING | GLACIER | DEEP_ARCHIVE | OUTPOSTS | GLACIER_IR | SNOW | EXPRESS_ONEZONE | FSX_OPENZFS | FSX_ONTAP`
Required: No

## See Also
<a name="API_Destination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Destination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Destination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Destination)
