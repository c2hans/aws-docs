---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-logging.html
---

# Logging with AWS CloudTrail for S3 Tables
<a name="s3-tables-logging"></a>

 Amazon S3 is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service. CloudTrail captures all API calls for Amazon S3 as events. Using the information collected by CloudTrail, you can determine the request that was made to Amazon S3, the IP address from which the request was made, when it was made, and additional details. When a supported event activity occurs in Amazon S3, that activity is recorded in a CloudTrail event. You can use AWS CloudTrail trail to log management events and data events for S3 Tables. For more information, see [Amazon S3 CloudTrail events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) and [What is AWS CloudTrail? ](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) in the *AWS CloudTrailUser Guide*.

## CloudTrail management events for S3 Tables
<a name="s3-tables-management-events"></a>

Management events provide information about management operations that are performed on resources in your AWS account.

By default, CloudTrail logs management events for S3 Tables. The `eventsource` for CloudTrail management events for S3 Tables is ` s3tables.amazonaws.com`. When you set up your AWS account, CloudTrail management events are enabled by default. The following API actions are tracked by CloudTrail and logged as management events.
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_CreateNamespace.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_CreateNamespace.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_CreateTable.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_CreateTable.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_CreateTableBucket.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_CreateTableBucket.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_DeleteNamespace.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_DeleteNamespace.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_DeleteTable.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_DeleteTable.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_DeleteTableBucket.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_DeleteTableBucket.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_DeleteTableBucketPolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_DeleteTableBucketPolicy.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_DeleteTablePolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_DeleteTablePolicy.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_GetNamespace.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_GetNamespace.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_GetTable.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_GetTable.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_GetTableBucket.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_GetTableBucket.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_GetTableBucketMaintenanceConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_GetTableBucketMaintenanceConfiguration.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_GetTableBucketPolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_GetTableBucketPolicy.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_GetTableMaintenanceConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_GetTableMaintenanceConfiguration.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_GetTableMaintenanceJobStatus.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_GetTableMaintenanceJobStatus.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_GetTableMetadataLocation.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_GetTableMetadataLocation.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_GetTablePolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_GetTablePolicy.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_ListNamespaces.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_ListNamespaces.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_ListTableBuckets.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_ListTableBuckets.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_ListTables.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_ListTables.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_PutTableBucketMaintenanceConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_PutTableBucketMaintenanceConfiguration.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_PutTableMaintenanceConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_PutTableMaintenanceConfiguration.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_PutBucketPolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_PutBucketPolicy.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_PutTablePolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_PutTablePolicy.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_RenameTable.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_RenameTable.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_UpdateTableMetadataLocation.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3TableBuckets_UpdateTableMetadataLocation.html)

For more information on CloudTrail management events, see [Logging management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html) in the *AWS CloudTrail User Guide*.

## CloudTrail management events for S3 Tables maintenance
<a name="s3-tables-maintenance-events"></a>

S3 logs automatic maintenance operations as `TablesMaintenanceEvent` management events in CloudTrail. These events occur during operations like compaction and snapshot expiration. For more information about S3 table maintenance, see [Maintenance for tables](s3-tables-maintenance.md).

### How to identify maintenance events
<a name="identify-maintenance-event"></a>

You can identify S3 Tables maintenance events in CloudTrail logs by these attribute values:
+ `eventSource: s3tables.amazonaws.com`
+ `eventType: AwsServiceEvent`
+ `eventName: TablesMaintenanceEvent`
+ `userAgent: maintenance.s3tables.amazonaws.com`
+ `activityType:`
  + `IcebergCompaction` (for compaction)
  + `IcebergSnapshotManagement` (for snapshot expiration)

For an example of a compaction maintenance event, see [Example – CloudTrail log file for a table maintenance management event](s3-tables-log-files.md#example-ct-log-s3tables-3).

## CloudTrail data events for S3 Tables
<a name="s3-tables-data-events"></a>

Data events provide information about the resource operations performed on or in a resource.By default, CloudTrail trails don't log data events, but you can configure trails to log data events.

When you log data events for a trail in CloudTrail, you will choose or specify the resource type. S3 Tables has two resources types, `AWS::S3Tables::Table` and `AWS::S3Tables::TableBucket`.

The following data events are logged to CloudTrail.
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html)

For more information on CloudTrail data events, see [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) in the *AWS CloudTrail User Guide*.

For additional information about CloudTrail events for S3 Tables, see the following topics:

**Topics**
+ [CloudTrail management events for S3 Tables](#s3-tables-management-events)
+ [CloudTrail management events for S3 Tables maintenance](#s3-tables-maintenance-events)
+ [CloudTrail data events for S3 Tables](#s3-tables-data-events)
+ [AWS CloudTrail data event log file examples for S3 Tables](s3-tables-log-files.md)
