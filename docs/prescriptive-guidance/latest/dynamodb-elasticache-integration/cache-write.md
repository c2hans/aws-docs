---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-elasticache-integration/cache-write.html
---

# Cache write behavior
<a name="cache-write"></a>

This guide describes a read-through cache where items are cached upon first read. A write-through cache would push entries into the cache during the write operation, but this guide does not suggest doing that, for two reasons:
+ When an item is written, there's no indication that it's going to be read anytime soon, and it's wasteful to write cache entries that aren't used.
+ An item that is cached might be cached multiple times under different signature keys. For example, different projection expressions result in different cache entries. Thus, it's not clear which signature key you should store the entry under before a request comes in. You might consider it more elegant to cache the item only once in its entirety, and, if the request specifies a `ProjectionExpression` parameter, apply the projection live within the caching wrapper. Unfortunately, this adds significant complexity because it requires implementing the non-trivial `ProjectionExpression` grammar. It's easier to keep the caching wrapper very simple so it only caches requests that happened previously, and try to avoid inventing a new response as much as possible. Let the database be the only place that a `ProjectionExpression` ever gets interpreted. That eliminates an easy write-through cache model.

However, write operations can be intelligent, and they can proactively invalidate any item cache entries stored earlier that are relevant to the written item. This keeps the item cache fresh without having to wait for TTL expiry. The cache entry is repopulated on the next read.

**Note**
A key advantage of this DynamoDB integration, compared with a similarly designed relational database cache integration, is that every write to DynamoDB always specifies the primary keys of the items that are being written. A read-through cache can watch the write calls and perform exact, immediate item cache invalidation. When you use a relational database, an `UPDATE` statement doesn't identify the items that might be affected, and there's no passive way to invalidate cached row entries other than through TTL.

Write calls implement this logic flow:
+ Perform the write operation against the database.
+ If the operation is successful, extract the table and primary keys for the write.
+ Invalidate any item cache entries that are relevant to the primary keys.

There's a bit of housekeeping required to make this last step possible. Item cache entries are stored under a hash of their signature, so it's necessary to know which keys to invalidate. You can do that by maintaining within the cache a mapping between item primary keys and the list of stored signatures that are associated with that primary key. It's that list of items that must be invalidated.

Here's the table from earlier:

|
|
| Pseudocode | ElastiCache key calculation | ElastiCache value |
| --- |--- |--- |
| `get_item(t1, k1, p1)` | `hash('get', t1, k1, p1) = 0xad4c812a` | `{ 'Item': … }` |
| `get_item(t1, k1, p2)` | `hash('get', t1, k2, p2) = 0x045deaab` | `{ 'Item': … }` |
| `get_item(t1, k2, p1)` | `hash('get', t1, k2, p1) = 0x9cda78af` | `{ 'Item': … }` |

And the earlier housekeeping table:

|  |  |  |
| --- |--- |--- |
| Operation | ElastiCache key calculation | ElastiCache value |
| Track list of entries for table `t1`, key `k1` | `hash('list', t1, k1)` | ( `0xad4c812a, 0x045deaab` ) |
| --- |--- |--- |
| Track list of entries for table `t1`, key `k2` | `hash('list', t1, k2) ` | ( `0x9cda78af` ) |

Let's assume that there's a write operation on table `t1` and the item has the primary key `k1`. The next step is to invalidate the entries that are relevant to that item.

Here's the full logic:
+ Perform the write operation against the database.
+ If the operation is successful, extract the table and primary key for the write.
+ Pull from the cache the list of stored hash signatures that are associated with that primary key.
+ Invalidate those item cache entries.
+ Delete the housekeeping list for that primary key.

It would be fantastic to have a way to proactively invalidate query cache entries as part of item write operations. However, inventing a design for this is extremely difficult because it's almost impossible to determine, efficiently and reliably, which cached query results would be affected by an updated item. For this reason, query cache entries have no better option than to expire through TTL settings.
