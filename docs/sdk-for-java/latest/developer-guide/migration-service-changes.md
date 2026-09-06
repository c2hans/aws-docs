---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-service-changes.html
---

# Service-specific changes
<a name="migration-service-changes"></a>

## Amazon S3 changes
<a name="s3-operations-name"></a>

SDK for Java 2.x disables anonymous access by default. As a result, you must enable anonymous access by using the `AnonymousCredentialsProvider`.

### Operation name changes
<a name="s3-op-name-changes"></a>

Many of the operation names for the Amazon S3 client have changed in the AWS SDK for Java 2.x. In version 1.x, the Amazon S3 client is not generated directly from the service API. This results in inconsistency between the SDK operations and the service API. In version 2.x, we now generate the Amazon S3 client to be more consistent with the service API.

The following table shows the operation names in the two versions.

**Amazon S3 Operation names**

| 1.x | 2.x |
| --- | --- |
| abortMultipartUpload | abortMultipartUpload |
| changeObjectStorageClass  | copyObject |
| completeMultipartUpload  | completeMultipartUpload |
| copyObject | copyObject |
| copyPart | uploadPartCopy |
| createBucket | createBucket |
| deleteBucket | deleteBucket |
| deleteBucketAnalyticsConfiguration | deleteBucketAnalyticsConfiguration |
| deleteBucketCrossOriginConfiguration | deleteBucketCors |
| deleteBucketEncryption | deleteBucketEncryption |
| deleteBucketInventoryConfiguration | deleteBucketInventoryConfiguration |
| deleteBucketLifecycleConfiguration | deleteBucketLifecycle |
| deleteBucketMetricsConfiguration | deleteBucketMetricsConfiguration |
| deleteBucketPolicy | deleteBucketPolicy |
| deleteBucketReplicationConfiguration | deleteBucketReplication |
| deleteBucketTaggingConfiguration | deleteBucketTagging |
| deleteBucketWebsiteConfiguration | deleteBucketWebsite |
| deleteObject | deleteObject |
| deleteObjectTagging | deleteObjectTagging |
| deleteObjects | deleteObjects |
| deleteVersion | deleteObject |
| disableRequesterPays | putBucketRequestPayment |
| doesBucketExist | headBucket |
| doesBucketExistV2 | headBucket |
| doesObjectExist | headObject |
| enableRequesterPays | putBucketRequestPayment |
| generatePresignedUrl | [S3Presigner](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/presigner/S3Presigner.html) |
| getBucketAccelerateConfiguration | getBucketAccelerateConfiguration |
| getBucketAcl | getBucketAcl |
| getBucketAnalyticsConfiguration | getBucketAnalyticsConfiguration |
| getBucketCrossOriginConfiguration | getBucketCors |
| getBucketEncryption | getBucketEncryption |
| getBucketInventoryConfiguration | getBucketInventoryConfiguration |
| getBucketLifecycleConfiguration | getBucketLifecycle or getBucketLifecycleConfiguration |
| getBucketLocation | getBucketLocation |
| getBucketLoggingConfiguration | getBucketLogging |
| getBucketMetricsConfiguration | getBucketMetricsConfiguration |
| getBucketNotificationConfiguration | getBucketNotification or getBucketNotificationConfiguration |
| getBucketPolicy | getBucketPolicy |
| getBucketReplicationConfiguration | getBucketReplication |
| getBucketTaggingConfiguration | getBucketTagging |
| getBucketVersioningConfiguration | getBucketVersioning |
| getBucketWebsiteConfiguration | getBucketWebsite |
| getObject | getObject |
| getObjectAcl | getObjectAcl |
| getObjectAsString | getObjectAsBytes().asUtf8String |
| getObjectMetadata | headObject |
| getObjectTagging | getObjectTagging |
| getResourceUrl | [`S3Utilities#getUrl`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3Utilities.html#getUrl(java.util.function.Consumer)) |
| getS3AccountOwner | listBuckets |
| getUrl | [S3Utilities\#getUrl](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3Utilities.html#getUrl(java.util.function.Consumer)) |
| headBucket | headBucket |
| initiateMultipartUpload | createMultipartUpload |
| isRequesterPaysEnabled | getBucketRequestPayment |
| listBucketAnalyticsConfigurations | listBucketAnalyticsConfigurations |
| listBucketInventoryConfigurations | listBucketInventoryConfigurations |
| listBucketMetricsConfigurations | listBucketMetricsConfigurations |
| listBuckets | listBuckets |
| listMultipartUploads | listMultipartUploads |
| listNextBatchOfObjects | listObjectsV2Paginator |
| listNextBatchOfVersions | listObjectVersionsPaginator |
| listObjects | listObjects |
| listObjectsV2 | listObjectsV2 |
| listParts | listParts |
| listVersions | listObjectVersions |
| putObject | putObject |
| restoreObject | restoreObject |
| restoreObjectV2 | restoreObject |
| selectObjectContent | selectObjectContent |
| setBucketAccelerateConfiguration | putBucketAccelerateConfiguration |
| setBucketAcl | putBucketAcl |
| setBucketAnalyticsConfiguration | putBucketAnalyticsConfiguration |
| setBucketCrossOriginConfiguration | putBucketCors |
| setBucketEncryption | putBucketEncryption |
| setBucketInventoryConfiguration | putBucketInventoryConfiguration |
| setBucketLifecycleConfiguration | putBucketLifecycle or putBucketLifecycleConfiguration |
| setBucketLoggingConfiguration | putBucketLogging |
| setBucketMetricsConfiguration | putBucketMetricsConfiguration |
| setBucketNotificationConfiguration | putBucketNotification or putBucketNotificationConfiguration |
| setBucketPolicy | putBucketPolicy |
| setBucketReplicationConfiguration | putBucketReplication |
| setBucketTaggingConfiguration | putBucketTagging |
| setBucketVersioningConfiguration | putBucketVersioning |
| setBucketWebsiteConfiguration | putBucketWebsite |
| setObjectAcl | putObjectAcl |
| setObjectRedirectLocation | copyObject |
| setObjectTagging | putObjectTagging |
| uploadPart | uploadPart |

## Amazon SNS changes
<a name="sns-changes"></a>

By default, an SNS client only sends requests to the Region it's configured for. To target a different Region, use a separate per-Region client.

## Amazon SQS changes
<a name="sqs-changes"></a>

By default, an SQS client only sends requests to the Region it's configured for. To target a different Region, use a separate per-Region client.

## Amazon RDS changes
<a name="rds-changes"></a>

The SDK for Java 2.x uses `RdsUtilities#generateAuthenticationToken` in place of the class `RdsIamAuthTokenGenerator` in 1.x.
