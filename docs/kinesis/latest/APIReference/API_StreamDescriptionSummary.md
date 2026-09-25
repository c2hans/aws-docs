---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_StreamDescriptionSummary.html
---

# StreamDescriptionSummary
<a name="API_StreamDescriptionSummary"></a>

Represents the output for [DescribeStreamSummary](API_DescribeStreamSummary.md)

## Contents
<a name="API_StreamDescriptionSummary_Contents"></a>

 ** EnhancedMonitoring **   <a name="Streams-Type-StreamDescriptionSummary-EnhancedMonitoring"></a>
Represents the current enhanced monitoring settings of the stream.
Type: Array of [EnhancedMetrics](API_EnhancedMetrics.md) objects
Required: Yes

 ** OpenShardCount **   <a name="Streams-Type-StreamDescriptionSummary-OpenShardCount"></a>
The number of open shards in the stream.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000000.
Required: Yes

 ** RetentionPeriodHours **   <a name="Streams-Type-StreamDescriptionSummary-RetentionPeriodHours"></a>
The current retention period, in hours.
Type: Integer
Required: Yes

 ** StreamARN **   <a name="Streams-Type-StreamDescriptionSummary-StreamARN"></a>
The Amazon Resource Name (ARN) for the stream being described.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: Yes

 ** StreamCreationTimestamp **   <a name="Streams-Type-StreamDescriptionSummary-StreamCreationTimestamp"></a>
The approximate time that the stream was created.
Type: Timestamp
Required: Yes

 ** StreamName **   <a name="Streams-Type-StreamDescriptionSummary-StreamName"></a>
The name of the stream being described.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** StreamStatus **   <a name="Streams-Type-StreamDescriptionSummary-StreamStatus"></a>
The current status of the stream being described. The stream status is one of the following states:
+  `CREATING` - The stream is being created. Kinesis Data Streams immediately returns and sets `StreamStatus` to `CREATING`.
+  `DELETING` - The stream is being deleted. The specified stream is in the `DELETING` state until Kinesis Data Streams completes the deletion.
+  `ACTIVE` - The stream exists and is ready for read and write operations or deletion. You should perform read and write operations only on an `ACTIVE` stream.
+  `UPDATING` - Shards in the stream are being merged or split. Read and write operations continue to work while the stream is in the `UPDATING` state.
Type: String
Valid Values: `CREATING | DELETING | ACTIVE | UPDATING`
Required: Yes

 ** ChannelCount **   <a name="Streams-Type-StreamDescriptionSummary-ChannelCount"></a>
The number of channels associated with the stream.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000000.
Required: No

 ** ConsumerCount **   <a name="Streams-Type-StreamDescriptionSummary-ConsumerCount"></a>
The number of enhanced fan-out consumers registered with the stream.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000000.
Required: No

 ** EncryptionType **   <a name="Streams-Type-StreamDescriptionSummary-EncryptionType"></a>
The encryption type used. This value is one of the following:
+  `KMS`
+  `NONE`
Type: String
Valid Values: `NONE | KMS`
Required: No

 ** KeyId **   <a name="Streams-Type-StreamDescriptionSummary-KeyId"></a>
The GUID for the customer-managed AWS KMS key to use for encryption. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by "alias/".You can also use a master key owned by Kinesis Data Streams by specifying the alias `aws/kinesis`.
+ Key ARN example: `arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012`
+ Alias ARN example: ` arn:aws:kms:us-east-1:123456789012:alias/MyAliasName`
+ Globally unique key ID example: `12345678-1234-1234-1234-123456789012`
+ Alias name example: `alias/MyAliasName`
+ Master key owned by Kinesis Data Streams: `alias/aws/kinesis`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** MaxRecordSizeInKiB **   <a name="Streams-Type-StreamDescriptionSummary-MaxRecordSizeInKiB"></a>
The maximum record size of a single record in kibibyte (KiB) that you can write to, and read from a stream.
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 10240.
Required: No

 ** RecordDistributionStrategy **   <a name="Streams-Type-StreamDescriptionSummary-RecordDistributionStrategy"></a>
The record distribution strategy that the stream currently uses. A value of `AUTO` indicates that Amazon Kinesis Data Streams distributes records across shards using service-managed algorithms. A value of `USER_PARTITION_KEY` indicates that shard placement is determined by the partition key that producers supply. This field is only present for streams that use the on-demand capacity mode.
Type: String
Valid Values: `AUTO | USER_PARTITION_KEY`
Required: No

 ** StreamId **   <a name="Streams-Type-StreamDescriptionSummary-StreamId"></a>
Not Implemented. Reserved for future use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `[a-z0-9]{20}-[a-z0-9]{3}`
Required: No

 ** StreamModeDetails **   <a name="Streams-Type-StreamDescriptionSummary-StreamModeDetails"></a>
 Specifies the capacity mode to which you want to set your data stream. Currently, in Kinesis Data Streams, you can choose between an **on-demand** ycapacity mode and a **provisioned** capacity mode for your data streams.
Type: [StreamModeDetails](API_StreamModeDetails.md) object
Required: No

 ** WarmThroughput **   <a name="Streams-Type-StreamDescriptionSummary-WarmThroughput"></a>
The warm throughput in MB/s for the stream. This represents the throughput capacity that will be immediately available for write operations.
Type: [WarmThroughputObject](API_WarmThroughputObject.md) object
Required: No

## See Also
<a name="API_StreamDescriptionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/StreamDescriptionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/StreamDescriptionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/StreamDescriptionSummary)
