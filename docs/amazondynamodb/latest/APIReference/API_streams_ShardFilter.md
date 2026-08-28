---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_ShardFilter.html
---

# ShardFilter
<a name="API_streams_ShardFilter"></a>

This optional field contains the filter definition for the `DescribeStream` API.

## Contents
<a name="API_streams_ShardFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ShardId **   <a name="DDB-Type-streams_ShardFilter-ShardId"></a>
Contains the `shardId` of the parent shard for which you are requesting child shards.
 *Sample request:*
Type: String
Length Constraints: Minimum length of 28. Maximum length of 65.
Required: No

 ** Type **   <a name="DDB-Type-streams_ShardFilter-Type"></a>
Contains the type of filter to be applied on the `DescribeStream` API. Currently, the only value this parameter accepts is `CHILD_SHARDS`.
Type: String
Valid Values: `CHILD_SHARDS`
Required: No

## See Also
<a name="API_streams_ShardFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/streams-dynamodb-2012-08-10/ShardFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/streams-dynamodb-2012-08-10/ShardFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/streams-dynamodb-2012-08-10/ShardFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
