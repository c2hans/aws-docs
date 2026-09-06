---
source_url: https://docs.aws.amazon.com/scheduler/latest/APIReference/API_KinesisParameters.html
---

# KinesisParameters
<a name="API_KinesisParameters"></a>

The templated target type for the Amazon Kinesis [`PutRecord`](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html) API operation.

## Contents
<a name="API_KinesisParameters_Contents"></a>

 ** PartitionKey **   <a name="scheduler-Type-KinesisParameters-PartitionKey"></a>
Specifies the shard to which EventBridge Scheduler sends the event. For more information, see [Amazon Kinesis Data Streams terminology and concepts](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html) in the *Amazon Kinesis Streams Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_KinesisParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/scheduler-2021-06-30/KinesisParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/KinesisParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/scheduler-2021-06-30/KinesisParameters)
