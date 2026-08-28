---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-elasticache-integration/design.html
---

# Design considerations
<a name="design"></a>

Other design points to consider:
+ **Error handling**: If the cache becomes unavailable for any reason, the application should proceed as if all items are cache misses. The existence of the cache layer should not add fragility to an application.
+ **TTL**: It's possible to configure a single TTL value for all cache entries or to use different TTL values depending on the entry (for example, `get_item`, `query`, or `scan` cache). It's also possible to have a different TTL value for negative cache entries (requests that returned no items).
+ **Consumed capacity**: When you return a cached response, we recommend that you adjust the `ConsumedCapacity` metrics in the response to indicate zero read consumption.
+ **Removal of response metadata**: You should also remove the `ResponseMetadata` section in the response. This avoids the risk that someone will see a `RequestId` and think that it's current when it was actually from hours earlier.
+ **Addition of cache metadata**: It's helpful to add a `CacheMetadata` section to the response. This section can report the time the value was stored (useful to measure staleness) and the client library and version that stored the value (which might be useful when performing a seamless upgrade from one version to another where the format changes).
+ **Determining the table schema**: To determine the primary key from a write operation for cache invalidation, you must know the table's schema. You can get this information by using a `describe_table` call and long-term cache in ElastiCache on first use (only once) for each table.
+ **Accepting instead of constructing the clients**: An advantage to accepting the DynamoDB and Redis client instances in the constructor (instead of building them within the shim based on passed-in parameters) is that it lets the caller of the constructor determine details, such as whether `read_from_replicas=True` should be set.
+ **Namespace feature**: It can be convenient to support an optional namespace in the constructor that isolates all your cache reads and writes to that namespace. Using a namespace is ideal for testing, because each run with a different namespace appears to start with an empty cache and has no side effects from previous runs. You could also simulate emptying the full cache in production by just changing the namespace. This can be implemented by automatically adding a prefix to each lookup key.
+ **Scan caching**: It's difficult to know whether `scan` calls should be cached. When performing a one-time full table scan, you don't want to fill the cache with large pages of scanned data that won't be read a second time. On the other hand, many workloads do repeated scans, especially against smaller tables, to provide the latest full table data to multiple downstream consumers. One compromise would be to implement a system where it takes two calls, and each call has the same signature (within the TTL time period), for the resulting scan response to be cached. This avoids filling the cache during a one-time full table scan while enabling tight scan loops to get the benefit of caching. The first scan puts a small placeholder in the cache to mark the request as having been made once. The second scan replaces the token value with the actual payload, which can be as large as 1 MB.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
