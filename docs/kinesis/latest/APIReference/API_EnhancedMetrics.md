---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_EnhancedMetrics.html
---

# EnhancedMetrics
<a name="API_EnhancedMetrics"></a>

Represents enhanced metrics types.

## Contents
<a name="API_EnhancedMetrics_Contents"></a>

 ** ShardLevelMetrics **   <a name="Streams-Type-EnhancedMetrics-ShardLevelMetrics"></a>
List of shard-level metrics.
The following are the valid shard-level metrics. The value "`ALL`" enhances every metric.
+  `IncomingBytes`
+  `IncomingRecords`
+  `OutgoingBytes`
+  `OutgoingRecords`
+  `WriteProvisionedThroughputExceeded`
+  `ReadProvisionedThroughputExceeded`
+  `IteratorAgeMilliseconds`
+  `ALL`
For more information, see [Monitoring the Amazon Kinesis Data Streams Service with Amazon CloudWatch](https://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-cloudwatch.html) in the *Amazon Kinesis Data Streams Developer Guide*.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 7 items.
Valid Values: `IncomingBytes | IncomingRecords | OutgoingBytes | OutgoingRecords | WriteProvisionedThroughputExceeded | ReadProvisionedThroughputExceeded | IteratorAgeMilliseconds | ALL`
Required: No

## See Also
<a name="API_EnhancedMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/EnhancedMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/EnhancedMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/EnhancedMetrics)
