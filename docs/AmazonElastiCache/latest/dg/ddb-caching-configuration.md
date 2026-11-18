---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ddb-caching-configuration.html
---

# Configuring DynamoDB caching
<a name="ddb-caching-configuration"></a>

You configure Amazon DynamoDB caching through the Amazon ElastiCache integration client in your application. Connection settings control how the client connects to the serverless cache, and caching behavior settings control which data is cached and how long cache entries live.

## Connection configuration
<a name="ddb-caching-configuration.connection"></a>

The following settings are used to configure the ElastiCache integration client's connection to the serverless cache.

**DynamoDB caching connection settings**

| Setting | Required | Default | Description |
| --- | --- | --- | --- |
| `cache_name` | Yes | None | The name specified when the serverless cache was created. This is distinct from the endpoint hostname. |
| `endpoint` | Yes | None | The serverless endpoint to connect to. |
| `fallback_duration` | No | unlimited | How long requests route directly to DynamoDB after fallback behavior is triggered. A value of zero disables fallback; a negative or null value means unlimited. |
| `integration_request_timeout` | No | 5 seconds | The maximum time to wait for a DynamoDB caching request. This is separate from the AWS SDK HTTP read timeout. |
| `reconnect_timeout` | No | 2 seconds | The period since the last successful connection after which requests fall back directly to DynamoDB. |
| `region_name` | No | Configured in SDK | The AWS Region to connect to. |
| `user_id` | No | `default.iam-user` | The IAM user authenticated upon connection. |

## Configuring caching behavior
<a name="ddb-caching-configuration.behavior"></a>

You can control caching behavior at a global or per-table scope with the following settings. Settings are applied for each connection, so two different workloads can configure different values for the same setting on different connections.

**DynamoDB caching behavior settings**

| Setting | Required | Default value | Valid values | Valid scopes | Description |
| --- | --- | --- | --- | --- | --- |
| `cached_tables` | No | All tables | list | cache | Which DynamoDB tables to cache. Defining this setting limits caching to the tables specified. |
| `cached_operations` | No | All operations | list | cache | Which DynamoDB operations to cache (must be in the list of supported operations). Defining this setting limits caching to the operations specified. |
| `item_enable_negative_caching` | No | true | false, true | cache, table | Whether to cache negative results for item operations. |
| `item_populate_full_item` | No | false | false, true | cache, table | Whether to populate the cache with the complete item as a projection upon a successful PutItem operation. |
| `item_populate_on_write` | No | false | false, true | cache, table | Whether to populate the cache with projections for an item on write operations. |
| `query_enable_negative_caching` | No | true | false, true | cache, table | Whether to cache negative results for query operations. |
| `scan_enable_negative_caching` | No | true | false, true | cache, table | Whether to cache negative results for scan operations. |
| `negative_ttl` | No | 60 | 0-86400 | operation, cache, table | Sets the time to live value in seconds for negative cache entries globally. A zero value means negative caching is disabled. |
| `ttl` | No | 300 | 1-86400 | operation, cache, table | Sets the time to live value in seconds for cache entries. The default is 300 seconds (5 minutes). |

For more information about configuration for your preferred language, see [elasticache-integration-client](https://github.com/awslabs/elasticache-integration-client) on the GitHub website.
