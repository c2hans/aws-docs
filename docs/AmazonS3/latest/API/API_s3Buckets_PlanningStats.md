---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PlanningStats.html
---

# PlanningStats
<a name="API_s3Buckets_PlanningStats"></a>

Statistics about the source and the partitions in a migration.

## Contents
<a name="API_s3Buckets_PlanningStats_Contents"></a>

 ** objectsPlanned **   <a name="AmazonS3-Type-s3Buckets_PlanningStats-objectsPlanned"></a>
The number of source objects in the migration. For a start, these are the data files in the AWS Glue table's partitions, or under the table's location if the table isn't partitioned. For a sync, these are all the data files of the table after the sync, including files that earlier migrations migrated.
Type: Long
Required: No

 ** objectsScanned **   <a name="AmazonS3-Type-s3Buckets_PlanningStats-objectsScanned"></a>
The number of source objects that the migration found under the source table's location, whether or not it migrates them. The object compatibility report has one row for each.
Type: Long
Required: No

 ** partitionCount **   <a name="AmazonS3-Type-s3Buckets_PlanningStats-partitionCount"></a>
The number of partitions in the destination table after this migration, or 0 if the source table isn't partitioned. This value is returned when planning produces a valid plan.
Type: Long
Required: No

## See Also
<a name="API_s3Buckets_PlanningStats_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/PlanningStats)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/PlanningStats)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/PlanningStats)
