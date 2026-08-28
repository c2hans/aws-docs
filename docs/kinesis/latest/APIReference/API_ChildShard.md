---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ChildShard.html
---

# ChildShard
<a name="API_ChildShard"></a>

Output parameter of the GetRecords API. The existing child shard of the current shard.

## Contents
<a name="API_ChildShard_Contents"></a>

 ** HashKeyRange **   <a name="Streams-Type-ChildShard-HashKeyRange"></a>
The range of possible hash key values for the shard, which is a set of ordered contiguous positive integers.
Type: [HashKeyRange](API_HashKeyRange.md) object
Required: Yes

 ** ParentShards **   <a name="Streams-Type-ChildShard-ParentShards"></a>
The current shard that is the parent of the existing child shard.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** ShardId **   <a name="Streams-Type-ChildShard-ShardId"></a>
The shard ID of the existing child shard of the current shard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## See Also
<a name="API_ChildShard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/ChildShard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/ChildShard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/ChildShard)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
