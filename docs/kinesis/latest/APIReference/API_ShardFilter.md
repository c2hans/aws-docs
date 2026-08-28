---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ShardFilter.html
---

# ShardFilter
<a name="API_ShardFilter"></a>

The request parameter used to filter out the response of the `ListShards` API.

## Contents
<a name="API_ShardFilter_Contents"></a>

 ** Type **   <a name="Streams-Type-ShardFilter-Type"></a>
The shard type specified in the `ShardFilter` parameter. This is a required property of the `ShardFilter` parameter.
You can specify the following valid values:
+  `AFTER_SHARD_ID` - the response includes all the shards, starting with the shard whose ID immediately follows the `ShardId` that you provided.
+  `AT_TRIM_HORIZON` - the response includes all the shards that were open at `TRIM_HORIZON`.
+  `FROM_TRIM_HORIZON` - (default), the response includes all the shards within the retention period of the data stream (trim to tip).
+  `AT_LATEST` - the response includes only the currently open shards of the data stream.
+  `AT_TIMESTAMP` - the response includes all shards whose start timestamp is less than or equal to the given timestamp and end timestamp is greater than or equal to the given timestamp or still open.
+  `FROM_TIMESTAMP` - the response incldues all closed shards whose end timestamp is greater than or equal to the given timestamp and also all open shards. Corrected to `TRIM_HORIZON` of the data stream if `FROM_TIMESTAMP` is less than the `TRIM_HORIZON` value.
Type: String
Valid Values: `AFTER_SHARD_ID | AT_TRIM_HORIZON | FROM_TRIM_HORIZON | AT_LATEST | AT_TIMESTAMP | FROM_TIMESTAMP`
Required: Yes

 ** ShardId **   <a name="Streams-Type-ShardFilter-ShardId"></a>
The exclusive start `shardID` speified in the `ShardFilter` parameter. This property can only be used if the `AFTER_SHARD_ID` shard type is specified.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** Timestamp **   <a name="Streams-Type-ShardFilter-Timestamp"></a>
The timestamps specified in the `ShardFilter` parameter. A timestamp is a Unix epoch date with precision in milliseconds. For example, 2016-04-04T19:58:46.480-00:00 or 1459799926.480. This property can only be used if `FROM_TIMESTAMP` or `AT_TIMESTAMP` shard types are specified.
Type: Timestamp
Required: No

## See Also
<a name="API_ShardFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/ShardFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/ShardFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/ShardFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
