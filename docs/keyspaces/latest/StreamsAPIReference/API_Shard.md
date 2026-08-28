---
source_url: https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_Shard.html
---

# Shard
<a name="API_Shard"></a>

Represents a uniquely identified group of change records within a change data capture stream for Amazon Keyspaces.

## Contents
<a name="API_Shard_Contents"></a>

 ** parentShardIds **   <a name="keyspaces-Type-Shard-parentShardIds"></a>
The identifiers of parent shards that this shard evolved from, if this shard was created through resharding.
Type: Array of strings
Length Constraints: Minimum length of 28. Maximum length of 65.
Required: No

 ** sequenceNumberRange **   <a name="keyspaces-Type-Shard-sequenceNumberRange"></a>
The range of sequence numbers contained within this shard.
Type: [SequenceNumberRange](API_SequenceNumberRange.md) object
Required: No

 ** shardId **   <a name="keyspaces-Type-Shard-shardId"></a>
A unique identifier for this shard within the stream.
Type: String
Length Constraints: Minimum length of 28. Maximum length of 65.
Required: No

## See Also
<a name="API_Shard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspacesstreams-2024-09-09/Shard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspacesstreams-2024-09-09/Shard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspacesstreams-2024-09-09/Shard)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
