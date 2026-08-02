---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/amazonkinesisdatastreams.html
---

# Data retrieval APIs for Amazon Kinesis Data Streams
<a name="amazonkinesisdatastreams"></a>

Amazon Kinesis Data Streams provides the following APIs for data retrieval.

****

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="kinesis-DescribeAccountSettings"></a>[https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeAccountSettings.html](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeAccountSettings.html) | Describe the account-level settings for Amazon Kinesis Data Streams | Read |
| <a name="kinesis-DescribeLimits"></a>[https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeLimits.html](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeLimits.html) | Describe the shard limits and usage for the account | Read |
| <a name="kinesis-DescribeStream"></a>[https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStream.html](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStream.html) | Describe the specified stream | Read |
| <a name="kinesis-DescribeStreamConsumer"></a>[https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStreamConsumer.html](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStreamConsumer.html) | Get the description of a registered stream consumer | Read |
| <a name="kinesis-DescribeStreamSummary"></a>[https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStreamSummary.html](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStreamSummary.html) | Provide a summarized description of the specified Kinesis data stream without the shard list | Read |
| <a name="kinesis-GetRecords"></a>[https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetRecords.html](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetRecords.html) | Get data records from a shard | Read |
| <a name="kinesis-GetResourcePolicy"></a>[https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetResourcePolicy.html](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetResourcePolicy.html) | Get a resource policy associated with a specified stream or consumer | Read |
| <a name="kinesis-GetShardIterator"></a>[https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html) | Get a shard iterator. A shard iterator expires five minutes after it is returned to the requester | Read |
| <a name="kinesis-ListShards"></a>[https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListShards.html](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListShards.html) | List the shards in a stream and provides information about each shard | List |
| <a name="kinesis-ListStreamConsumers"></a>[https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListStreamConsumers.html](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListStreamConsumers.html) | List the stream consumers registered to receive data from a Kinesis stream using enhanced fan-out, and provides information about each consumer | List |
| <a name="kinesis-ListStreams"></a>[https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListStreams.html](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListStreams.html) | List your streams | List |
| <a name="kinesis-ListTagsForResource"></a>[https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListTagsForResource.html](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListTagsForResource.html) | List the tags for the specified Amazon Kinesis resource | Read |
| <a name="kinesis-ListTagsForStream"></a>[https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListTagsForStream.html](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListTagsForStream.html) | List the tags for the specified Amazon Kinesis stream | Read |
| <a name="kinesis-SubscribeToShard"></a>[https://docs.aws.amazon.com/kinesis/latest/APIReference/API_SubscribeToShard.html](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_SubscribeToShard.html) | Listen to a specific shard with enhanced fan-out | Read |
