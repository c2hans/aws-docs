---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_PartitionedPrefix.html
---

# PartitionedPrefix
<a name="API_PartitionedPrefix"></a>

Amazon S3 keys for log objects are partitioned in the following format:

 `[DestinationPrefix][SourceAccountId]/[SourceRegion]/[SourceBucket]/[YYYY]/[MM]/[DD]/[YYYY]-[MM]-[DD]-[hh]-[mm]-[ss]-[UniqueString]`

PartitionedPrefix defaults to EventTime delivery when server access logs are delivered.

## Contents
<a name="API_PartitionedPrefix_Contents"></a>

 ** PartitionDateSource **   <a name="AmazonS3-Type-PartitionedPrefix-PartitionDateSource"></a>
Specifies the partition date source for the partitioned prefix. `PartitionDateSource` can be `EventTime` or `DeliveryTime`.
For `DeliveryTime`, the time in the log file names corresponds to the delivery time for the log files.
 For `EventTime`, The logs delivered are for a specific day only. The year, month, and day correspond to the day on which the event occurred, and the hour, minutes and seconds are set to 00 in the key.
Type: String
Valid Values: `EventTime | DeliveryTime`
Required: No

## See Also
<a name="API_PartitionedPrefix_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PartitionedPrefix)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PartitionedPrefix)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PartitionedPrefix)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
