---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_KinesisParameters.html
---

# KinesisParameters
<a name="API_KinesisParameters"></a>

This object enables you to specify a JSON path to extract from the event and use as the partition key for the Amazon Kinesis data stream, so that you can control the shard to which the event goes. If you do not include this parameter, the default is to use the `eventId` as the partition key.

## Contents
<a name="API_KinesisParameters_Contents"></a>

 ** PartitionKeyPath **   <a name="eventbridge-Type-KinesisParameters-PartitionKeyPath"></a>
The JSON path to be extracted from the event and used as the partition key. For more information, see [Amazon Kinesis Streams Key Concepts](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html#partition-key) in the *Amazon Kinesis Streams Developer Guide*.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

## See Also
<a name="API_KinesisParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/KinesisParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/KinesisParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/KinesisParameters)
