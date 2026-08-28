---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper-builtins.html
---

# Built-in features (TTL, atomic counters)
<a name="ddb-mapper-builtins"></a>

DynamoDB Mapper ships with two convenience features that you enable by annotating a property: **time-to-live (TTL)** and **atomic counters**. Both are annotation-driven and implemented by [interceptors](ddb-mapper-configuration.md) (`TtlInterceptor` and `CounterInterceptor`) that the mapper **registers by default**. You don’t wire anything up; annotating the property is enough.

**Note**
Because these features rely on the default interceptors, replacing the mapper’s `interceptors` list outright disables them. Add your own interceptors with `+=` to keep them. See [Configure DynamoDB Mapper](ddb-mapper-configuration.md).

## Time-to-live (TTL)
<a name="ddb-mapper-builtins-ttl"></a>

 [DynamoDB TTL](/amazondynamodb/latest/developerguide/TTL.html) deletes items automatically after an expiration timestamp. Mark a numeric property with `@DynamoDbTtlSeconds`, passing the item’s `lifetime` in seconds. Whenever the item is written, the mapper sets that property to the current time plus the lifetime (as an epoch-seconds timestamp):

```
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbItem
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbPartitionKey
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbTtlSeconds

@DynamoDbItem
data class ShoppingCart(
    @DynamoDbPartitionKey
    val sessionId: String,
    val productSkus: List<String>,
    @DynamoDbTtlSeconds(lifetime = 86_400)
    var expiresAt: Long,   // expires 24 hours after each write
)
```

With this annotation, you don’t compute `expiresAt` yourself; the mapper populates it on every put, update, batch write, and transactional write.

**Note**
The annotation makes the mapper *write* the expiration timestamp, but DynamoDB only *deletes* expired items if TTL is enabled for that attribute on the table. Enable TTL on the table’s attribute using the [`DynamoDbClient`](/sdk-for-kotlin/api/latest/dynamodb/aws.sdk.kotlin.services.dynamodb/-dynamo-db-client/index.html) or the console, as described in [Enabling Time to Live](/amazondynamodb/latest/developerguide/time-to-live-ttl-how-to.html). TTL deletions typically occur within a few days of expiration, not immediately.

## Atomic counters
<a name="ddb-mapper-builtins-counters"></a>

An atomic counter is a numeric attribute the mapper increments automatically each time the item is persisted. Mark a numeric property with `@DynamoDbCounter`:

```
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbCounter
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbItem
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbPartitionKey

@DynamoDbItem
data class Product(
    @DynamoDbPartitionKey
    val sku: String,
    val name: String,
    val category: String,
    val priceCents: Long,
    @DynamoDbCounter
    var viewCount: Long = 0,
    var inventory: Long = 0,
)
```

On each mutating operation the mapper increments every counter field by one. For [`updateItem`](ddb-mapper-operations.md), it adds an `if_not_exists(field, 0) + 1` clause to the update expression, so a counter starts at zero even if the attribute doesn’t exist yet.

Keep these caveats in mind:
+ The counter advances by one on **every** persist of the item, so it reflects how many times the item has been written, not a value you set. Let the mapper manage it rather than assigning it yourself.
+ Counters increment by a fixed step of one; for arbitrary increments or decrements, use an [update expression](ddb-mapper-expressions.md) (`add { attr["…​"] += n }`) instead.

## Related topics
<a name="ddb-mapper-builtins-related"></a>
+  [Configure DynamoDB Mapper](ddb-mapper-configuration.md): how interceptors (including these defaults) are registered.
+  [DynamoDB Mapper annotations reference](ddb-mapper-anno-index.md): `@DynamoDbCounter` and `@DynamoDbTtlSeconds`.
+  [Generate a schema from annotations](ddb-mapper-anno-schema-gen.md): applying these annotations to your classes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
