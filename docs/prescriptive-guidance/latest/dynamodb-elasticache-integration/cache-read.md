---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-elasticache-integration/cache-read.html
---

# Cache read behavior
<a name="cache-read"></a>

The shim should cache only eventually consistent read calls made to DynamoDB. This includes `get-item`, `batch-get-item`, `query`, and `scan`. It should not cache strongly consistent reads calls or transactional read calls, because those calls inherently don't want to see a cached version of the data.

The cache entries must understand the signature of the request to identify follow-on, equivalent requests. The signature of each call consists of all the parameters of the request that affect the result. For a `get_item` call, the signature includes the `TableName`, `Key`, `ProjectionExpression`, and `ExpressionAttributeNames` parameters. For a query call, it includes the `TableName`, `IndexName`, `KeyConditions`, `FilterExpression`, `ScanIndexForward`, and `Limit` parameters. If two calls to the same function have the same signature, that's a possible cache hit.

Here is a sample logic flow for a `get_item` call:
+ Check if `ConsistentRead=true`. If so, directly call the database and return the result. Strongly consistent calls shouldn't use a cache.
+ Calculate the signature of the call. Hash together the `TableName`, `Key`, `ProjectionExpression`, and `ExpressionAttributeNames` parameters to get a single string signature value.
+ See if a cache entry exists with this signature key. If so, it's a cache hit, so return it.
+ If not, pass the call to the database, retrieve the result, populate the cache entry for this signature, and return the result. When you store the item, specify a time to live (TTL) expiry time.

For example, assume that you have this code:

```
cache_client.get_item(
  TableName='test',
  Key={ 'PK': { 'S': '123' } },
  ProjectionExpression='#attr1, #attr2',
  ExpressionAttributeNames={
    '#attr1': 'agent',
    '#attr2': 'count'
  },
  ConsistentRead=False
)
```

Inside `cache_client`, the code calculates the hash signature of the call. The signature is derived from hashing the concatenation of the `TableName`, `Key`, `ProjectionExpression`, and `ExpressionAttributeNames` parameters. Any hash system can be used as long as it's deterministic and produces a single string value. In this case, let's assume that it hashes down to `0xad4c812a`. This hash identifies this set of parameters.

What if another call is made that's the same, except that `#attr1` is renamed `#attribute1`? Should that call be considered to have the same signature? Ideally yes, because it's semantically identical, but the overhead of figuring out semantic equivalence on each and every call just isn't practical. It's much faster to hash parameter values blindly and require exact matches. The rule is: Calls are eligible for a cache hit if they're *actually* the same call, but not if they're *basically* the same call.

Inside `cache_client`, the code then looks to ElastiCache for an entry in the item cache that's stored under `0xad4c812a`. If the entry exists, that's a cache hit. If not, the value is fetched from the database and stored in ElastiCache for a later cache hit.

Here's what the cache looks like for three `get_item` calls that have three different sets of table, key, and projection parameters.

|
|
| Pseudocode | ElastiCache key calculation | ElastiCache value |
| --- |--- |--- |
| `get_item(t1, k1, p1)` | `hash('get', t1, k1, p1) = 0xad4c812a` | `{ 'Item': … }` |
| `get_item(t1, k1, p2)` | `hash('get', t1, k2, p2) = 0x045deaab` | `{ 'Item': … }` |
| `get_item(t1, k2, p1)` | `hash('get', t1, k2, p1) = 0x9cda78af` | `{ 'Item': … }` |

Other calls, such as `query` and `scan`, work the same way, but different parameters make up their signatures.

This design might remind you of how an HTTP caching proxy works. If it sees the same request again, it can return the response from the earlier request. The definition of *same request* in HTTP is based mostly on the query string. With DynamoDB, the call type and the set of parameters that are passed to the function influence its results.

There's one more step. It's important for item caching to keep a mapping between each item's primary key and the list of hashes actively used to cache that item. This will come into play during write operations, as described in the next section. So in addition to the previous keys and values, there will be extra cache entries such as these:

|  |  |  |
| --- |--- |--- |
| Operation | ElastiCache key  | ElastiCache value |
| Track list of entries for table `t1`, key `k1` | `hash('list', t1, k1)` | ( `0xad4c812a, 0x045deaab` ) |
| --- |--- |--- |
| Track list of entries for table `t1`, key `k2` | `hash('list', t1, k2) ` | ( `0x9cda78af` ) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
