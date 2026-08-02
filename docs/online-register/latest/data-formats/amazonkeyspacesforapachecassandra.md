---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/amazonkeyspacesforapachecassandra.html
---

# Data retrieval APIs for Amazon Keyspaces (for Apache Cassandra)
<a name="amazonkeyspacesforapachecassandra"></a>

Amazon Keyspaces (for Apache Cassandra) provides the following APIs for data retrieval.

****

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="cassandra-GetRecords"></a>[https://docs.aws.amazon.com/keyspaces/latest/devguide/](https://docs.aws.amazon.com/keyspaces/latest/devguide/) | Retrieve the CDC stream records from a given shard | Read |
| <a name="cassandra-GetShardIterator"></a>[https://docs.aws.amazon.com/keyspaces/latest/devguide/](https://docs.aws.amazon.com/keyspaces/latest/devguide/) | Return a shard iterator | Read |
| <a name="cassandra-GetStream"></a>[https://docs.aws.amazon.com/keyspaces/latest/devguide/](https://docs.aws.amazon.com/keyspaces/latest/devguide/) | Return information about a CDC stream, including the composition of its shards | Read |
| <a name="cassandra-ListStreams"></a>[https://docs.aws.amazon.com/keyspaces/latest/devguide/](https://docs.aws.amazon.com/keyspaces/latest/devguide/) | Return an array of CDC stream ARNs associated with the current account and endpoint | List |
| <a name="cassandra-Select"></a>[https://docs.aws.amazon.com/keyspaces/latest/devguide/](https://docs.aws.amazon.com/keyspaces/latest/devguide/) | SELECT data from a table | Read |
| <a name="cassandra-SelectMultiRegionResource"></a>[https://docs.aws.amazon.com/keyspaces/latest/devguide/](https://docs.aws.amazon.com/keyspaces/latest/devguide/) | SELECT data from a multiregion table | Read |
