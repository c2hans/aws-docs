---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_Record.html
---

# Record
<a name="API_Record"></a>

The unit of data of the Kinesis data stream, which is composed of a sequence number, a partition key, and a data blob.

## Contents
<a name="API_Record_Contents"></a>

 ** Data **   <a name="Streams-Type-Record-Data"></a>
The data blob. The data in the blob is both opaque and immutable to Kinesis Data Streams, which does not inspect, interpret, or change the data in the blob in any way. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (10 MiB).
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 0. Maximum length of 10485760.
Required: Yes

 ** SequenceNumber **   <a name="Streams-Type-Record-SequenceNumber"></a>
The unique identifier of the record within its shard.
Type: String
Pattern: `^(0|([1-9]\d{0,128}))$`
Required: Yes

 ** ApproximateArrivalTimestamp **   <a name="Streams-Type-Record-ApproximateArrivalTimestamp"></a>
The approximate time that the record was inserted into the stream.
Type: Timestamp
Required: No

 ** EncryptionType **   <a name="Streams-Type-Record-EncryptionType"></a>
The encryption type used on the record. This parameter can be one of the following values:
+  `NONE`: Do not encrypt the records in the stream.
+  `KMS`: Use server-side encryption on the records in the stream using a customer-managed AWS KMS key.
Type: String
Valid Values: `NONE | KMS`
Required: No

 ** PartitionKey **   <a name="Streams-Type-Record-PartitionKey"></a>
Identifies which shard in the stream the data record is assigned to.
For a stream that uses the `AUTO` record distribution strategy, this value is not returned if the producer did not provide a partition key when writing the record. If the producer provided a partition key, the original value is returned even though it was not used to determine shard placement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_Record_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/Record)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/Record)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/Record)
