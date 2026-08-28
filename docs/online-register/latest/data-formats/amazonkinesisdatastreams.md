---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/amazonkinesisdatastreams.html
---

# Data retrieval APIs for Amazon Kinesis Data Streams
<a name="amazonkinesisdatastreams"></a>

Amazon Kinesis Data Streams provides the following APIs for data retrieval.

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="kinesis-DescribeAccountSettings"></a>[DescribeAccountSettings](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeAccountSettings.html) | Describe the account-level settings for Amazon Kinesis Data Streams | Read |
| <a name="kinesis-DescribeLimits"></a>[DescribeLimits](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeLimits.html) | Describe the shard limits and usage for the account | Read |
| <a name="kinesis-DescribeStream"></a>[DescribeStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStream.html) | Describe the specified stream | Read |
| <a name="kinesis-DescribeStreamConsumer"></a>[DescribeStreamConsumer](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStreamConsumer.html) | Get the description of a registered stream consumer | Read |
| <a name="kinesis-DescribeStreamSummary"></a>[DescribeStreamSummary](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStreamSummary.html) | Provide a summarized description of the specified Kinesis data stream without the shard list | Read |
| <a name="kinesis-GetRecords"></a>[GetRecords](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetRecords.html) | Get data records from a shard | Read |
| <a name="kinesis-GetResourcePolicy"></a>[GetResourcePolicy](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetResourcePolicy.html) | Get a resource policy associated with a specified stream or consumer | Read |
| <a name="kinesis-GetShardIterator"></a>[GetShardIterator](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html) | Get a shard iterator. A shard iterator expires five minutes after it is returned to the requester | Read |
| <a name="kinesis-ListShards"></a>[ListShards](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListShards.html) | List the shards in a stream and provides information about each shard | List |
| <a name="kinesis-ListStreamConsumers"></a>[ListStreamConsumers](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListStreamConsumers.html) | List the stream consumers registered to receive data from a Kinesis stream using enhanced fan-out, and provides information about each consumer | List |
| <a name="kinesis-ListStreams"></a>[ListStreams](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListStreams.html) | List your streams | List |
| <a name="kinesis-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListTagsForResource.html) | List the tags for the specified Amazon Kinesis resource | Read |
| <a name="kinesis-ListTagsForStream"></a>[ListTagsForStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListTagsForStream.html) | List the tags for the specified Amazon Kinesis stream | Read |
| <a name="kinesis-SubscribeToShard"></a>[SubscribeToShard](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_SubscribeToShard.html) | Listen to a specific shard with enhanced fan-out | Read |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for none. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query online-register` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
