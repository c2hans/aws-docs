---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_StreamDescription.html
---

# StreamDescription
<a name="API_StreamDescription"></a>

Represents the output for [DescribeStream](API_DescribeStream.md).

## Contents
<a name="API_StreamDescription_Contents"></a>

 ** EnhancedMonitoring **   <a name="Streams-Type-StreamDescription-EnhancedMonitoring"></a>
Represents the current enhanced monitoring settings of the stream.
Type: Array of [EnhancedMetrics](API_EnhancedMetrics.md) objects
Required: Yes

 ** HasMoreShards **   <a name="Streams-Type-StreamDescription-HasMoreShards"></a>
If set to `true`, more shards in the stream are available to describe.
Type: Boolean
Required: Yes

 ** RetentionPeriodHours **   <a name="Streams-Type-StreamDescription-RetentionPeriodHours"></a>
The current retention period, in hours. Minimum value of 24. Maximum value of 168.
Type: Integer
Required: Yes

 ** Shards **   <a name="Streams-Type-StreamDescription-Shards"></a>
The shards that comprise the stream.
Type: Array of [Shard](API_Shard.md) objects
Required: Yes

 ** StreamARN **   <a name="Streams-Type-StreamDescription-StreamARN"></a>
The Amazon Resource Name (ARN) for the stream being described.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: Yes

 ** StreamCreationTimestamp **   <a name="Streams-Type-StreamDescription-StreamCreationTimestamp"></a>
The approximate time that the stream was created.
Type: Timestamp
Required: Yes

 ** StreamName **   <a name="Streams-Type-StreamDescription-StreamName"></a>
The name of the stream being described.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** StreamStatus **   <a name="Streams-Type-StreamDescription-StreamStatus"></a>
The current status of the stream being described. The stream status is one of the following states:
+  `CREATING` - The stream is being created. Kinesis Data Streams immediately returns and sets `StreamStatus` to `CREATING`.
+  `DELETING` - The stream is being deleted. The specified stream is in the `DELETING` state until Kinesis Data Streams completes the deletion.
+  `ACTIVE` - The stream exists and is ready for read and write operations or deletion. You should perform read and write operations only on an `ACTIVE` stream.
+  `UPDATING` - Shards in the stream are being merged or split. Read and write operations continue to work while the stream is in the `UPDATING` state.
Type: String
Valid Values: `CREATING | DELETING | ACTIVE | UPDATING`
Required: Yes

 ** EncryptionType **   <a name="Streams-Type-StreamDescription-EncryptionType"></a>
The server-side encryption type used on the stream. This parameter can be one of the following values:
+  `NONE`: Do not encrypt the records in the stream.
+  `KMS`: Use server-side encryption on the records in the stream using a customer-managed AWS KMS key.
Type: String
Valid Values: `NONE | KMS`
Required: No

 ** KeyId **   <a name="Streams-Type-StreamDescription-KeyId"></a>
The GUID for the customer-managed AWS KMS key to use for encryption. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by "alias/".You can also use a master key owned by Kinesis Data Streams by specifying the alias `aws/kinesis`.
+ Key ARN example: `arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012`
+ Alias ARN example: `arn:aws:kms:us-east-1:123456789012:alias/MyAliasName`
+ Globally unique key ID example: `12345678-1234-1234-1234-123456789012`
+ Alias name example: `alias/MyAliasName`
+ Master key owned by Kinesis Data Streams: `alias/aws/kinesis`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** StreamModeDetails **   <a name="Streams-Type-StreamDescription-StreamModeDetails"></a>
 Specifies the capacity mode to which you want to set your data stream. Currently, in Kinesis Data Streams, you can choose between an **on-demand** capacity mode and a **provisioned** capacity mode for your data streams.
Type: [StreamModeDetails](API_StreamModeDetails.md) object
Required: No

## See Also
<a name="API_StreamDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/StreamDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/StreamDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/StreamDescription)
