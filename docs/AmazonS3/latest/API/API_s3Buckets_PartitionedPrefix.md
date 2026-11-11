---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PartitionedPrefix.html
---

# PartitionedPrefix
<a name="API_s3Buckets_PartitionedPrefix"></a>

Amazon S3 keys for log objects are partitioned in the following format: `[targetPrefix][SourceAccountId]/[SourceRegion]/[SourceTableBucket]/[YYYY]/[MM]/[DD]/[YYYY]-[MM]-[DD]-[hh]-[mm]-[ss]-[UniqueString]`

## Contents
<a name="API_s3Buckets_PartitionedPrefix_Contents"></a>

 ** partitionDateSource **   <a name="AmazonS3-Type-s3Buckets_PartitionedPrefix-partitionDateSource"></a>
The date to use for the log object key partitions. Valid values are `EventTime`, the time that the requests in the log were made, and `DeliveryTime`, the time that the log was delivered.
Type: String
Valid Values: `EventTime | DeliveryTime`
Required: Yes

## See Also
<a name="API_s3Buckets_PartitionedPrefix_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/PartitionedPrefix)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/PartitionedPrefix)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/PartitionedPrefix)
