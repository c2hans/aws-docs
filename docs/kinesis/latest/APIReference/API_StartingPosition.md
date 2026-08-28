---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_StartingPosition.html
---

# StartingPosition
<a name="API_StartingPosition"></a>

The starting position in the data stream from which to start streaming.

## Contents
<a name="API_StartingPosition_Contents"></a>

 ** Type **   <a name="Streams-Type-StartingPosition-Type"></a>
You can set the starting position to one of the following values:
 `AT_SEQUENCE_NUMBER`: Start streaming from the position denoted by the sequence number specified in the `SequenceNumber` field.
 `AFTER_SEQUENCE_NUMBER`: Start streaming right after the position denoted by the sequence number specified in the `SequenceNumber` field.
 `AT_TIMESTAMP`: Start streaming from the position denoted by the time stamp specified in the `Timestamp` field.
 `TRIM_HORIZON`: Start streaming at the last untrimmed record in the shard, which is the oldest data record in the shard.
 `LATEST`: Start streaming just after the most recent record in the shard, so that you always read the most recent data in the shard.
Type: String
Valid Values: `AT_SEQUENCE_NUMBER | AFTER_SEQUENCE_NUMBER | TRIM_HORIZON | LATEST | AT_TIMESTAMP`
Required: Yes

 ** SequenceNumber **   <a name="Streams-Type-StartingPosition-SequenceNumber"></a>
The sequence number of the data record in the shard from which to start streaming. To specify a sequence number, set `StartingPosition` to `AT_SEQUENCE_NUMBER` or `AFTER_SEQUENCE_NUMBER`.
Type: String
Pattern: `0|([1-9]\d{0,128})`
Required: No

 ** Timestamp **   <a name="Streams-Type-StartingPosition-Timestamp"></a>
The time stamp of the data record from which to start reading. To specify a time stamp, set `StartingPosition` to `Type AT_TIMESTAMP`. A time stamp is the Unix epoch date with precision in milliseconds. For example, `2016-04-04T19:58:46.480-00:00` or `1459799926.480`. If a record with this exact time stamp does not exist, records will be streamed from the next (later) record. If the time stamp is older than the current trim horizon, records will be streamed from the oldest untrimmed data record (`TRIM_HORIZON`).
Type: Timestamp
Required: No

## See Also
<a name="API_StartingPosition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/StartingPosition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/StartingPosition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/StartingPosition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
