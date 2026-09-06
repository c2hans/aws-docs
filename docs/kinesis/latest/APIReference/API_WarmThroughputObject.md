---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_WarmThroughputObject.html
---

# WarmThroughputObject
<a name="API_WarmThroughputObject"></a>

Represents the warm throughput configuration on the stream. This is only present for On-Demand Kinesis Data Streams in accounts that have `MinimumThroughputBillingCommitment` enabled.

## Contents
<a name="API_WarmThroughputObject_Contents"></a>

 ** CurrentMiBps **   <a name="Streams-Type-WarmThroughputObject-CurrentMiBps"></a>
The current warm throughput value on the stream. This is the write throughput in MiBps that the stream is currently scaled to handle.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** TargetMiBps **   <a name="Streams-Type-WarmThroughputObject-TargetMiBps"></a>
The target warm throughput value on the stream. This indicates that the stream is currently scaling towards this target value.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_WarmThroughputObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/WarmThroughputObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/WarmThroughputObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/WarmThroughputObject)
