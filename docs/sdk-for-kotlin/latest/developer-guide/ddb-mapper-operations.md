---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper-operations.html
---

# Operations overview
<a name="ddb-mapper-operations"></a>

DynamoDB Mapper supports a subset of the operations available on the SDK’s low-level `DynamoDbClient`. Mapper operations are named after their low-level counterparts, but they accept and return your mapped classes instead of raw attribute-value maps. This topic explains which operations exist, where they live, and the different ways you can invoke them.

## Where operations live
<a name="ddb-mapper-operations-where"></a>

Operations belong to one of two scopes:
+  **Item-level operations** act on a single table or index and are invoked on a `Table` or `Index` reference obtained from `mapper.getTable(…​)` or `table.getIndex(…​)`
+  **Multi-table operations** act across one or more tables and are invoked on the `DynamoDbMapper` itself

## Operations at a glance
<a name="ddb-mapper-operations-glance"></a>

| Operation | Scope | Invoked on | Summary |
| --- | --- | --- | --- |
|  `deleteItem`  | item-level |  `Table`  | Delete a single item by its key. |
|  `getItem`  | item-level |  `Table`  | Retrieve a single item by its key; returns the mapped object or `null`. |
|  `putItem`  | item-level |  `Table`  | Create or replace a single item. |
|  `query` / `queryPaginated`  | item-level |  `Table`, `Index`  | Read items sharing a partition key, optionally filtered by a sort-key condition. |
|  `scan` / `scanPaginated`  | item-level |  `Table`, `Index`  | Read every item, optionally filtered. |
|  `updateItem`  | item-level |  `Table`  | Modify attributes of a single item. See [Use expressions](ddb-mapper-expressions.md). |
|  `batchGetItem`  | multi-table |  `DynamoDbMapper`  | Read many items across one or more tables in one call. See [Perform batch operations](ddb-mapper-batch.md). |
|  `batchWriteItem`  | multi-table |  `DynamoDbMapper`  | Put and/or delete many items across one or more tables in one call. See [Perform batch operations](ddb-mapper-batch.md). |
|  `transactGetItems`  | multi-table |  `DynamoDbMapper`  | Atomically read items across one or more tables. See [Perform transactional operations](ddb-mapper-transactions.md). |
|  `transactWriteItems`  | multi-table |  `DynamoDbMapper`  | Atomically put/update/delete/condition-check items across one or more tables. See [Perform transactional operations](ddb-mapper-transactions.md). |

All operations **except** `queryPaginated` and `scanPaginated` are `suspend` functions; call them from a coroutine.

The `queryPaginated` and `scanPaginated` methods are not `suspend` but synchronously return a [https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/). See [Work with paginated responses](#ddb-mapper-operations-paginated) for more details.

## Ways to invoke an operation
<a name="ddb-mapper-operations-invoke"></a>

Operations offer several calling styles. The recommended default is the **DSL lambda**. Operations that identify an item by its primary key also accept **literal key values**, and every operation has a corresponding **request type** you can build explicitly.

 `getItem` illustrates the all three styles. All three of the following calls retrieve the same item from the `orders` table (composite key: `customerId` partition, `orderId` sort). `getItem` returns a `GetItemResponse`, whose `item` property holds the mapped object (or `null`):

 **DSL lambda**: wrap each key value with `Key(…​)`:

```
import aws.sdk.kotlin.hll.dynamodbmapper.items.Key

val order = ordersTable.getItem {
    partitionKey = Key("customer-123")
    sortKey = Key("ORDER#2026-06-25#0042")
}.item
```

 **Literal key values**: pass the partition key, then the sort key:

```
val order = ordersTable.getItem("customer-123", "ORDER#2026-06-25#0042").item
```

 **Explicit request object**: each operation has a corresponding request type (for example `GetItemRequest`, `PutItemRequest`, `QueryRequest`, `ScanRequest`) that you can build once and reuse, or use to set less-common request fields. The key-bearing request types come in `PartitionKey` and `CompositeKey` variants (matching the table’s key shape) and are parameterized by their key type(s). You construct one with the same DSL shown previously and pass it to the matching operation. For instance, a built `QueryRequest` is passed to `queryPaginated(request)`. See the [API reference](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.operations/index.html) for each request type’s exact shape.

```
import aws.sdk.kotlin.hll.dynamodbmapper.operations.GetItemRequest

val request = GetItemRequest.CompositeKey {
    partitionKey = Key("customer-123")
    sortKey = Key("ORDER#2026-06-25#0042")
}

val order = ordersTable.getItem(request).item
```

**Note**
Many mapper request and response members mirror their low-level `DynamoDbClient` counterparts (for example, `consistentRead` and `returnConsumedCapacity`). Some have been renamed, re-typed, or dropped where the high-level mapping makes them unnecessary.

## Work with paginated responses
<a name="ddb-mapper-operations-paginated"></a>

 `query` and `scan` can match more items than fit in a single low-level response. The paginating variants (`queryPaginated` and `scanPaginated`) return a [https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/) of response pages and fetch subsequent pages automatically as you collect them. They do not call DynamoDB until the flow is collected.

```
import aws.sdk.kotlin.hll.dynamodbmapper.operations.scanPaginated

ordersTable.scanPaginated { }.collect { response ->
    val orders = response.items.orEmpty()
    println("Found a page of ${orders.size} orders")
    orders.forEach { order -> println(order) }
}
```

Usually a flow of objects is more useful than a flow of pages. Call `items()` on a paginated flow to flatten it into a `Flow` of your mapped type (for example, a `Flow<Order>` rather than a `Flow<ScanResponse<Order>>`):

```
import aws.sdk.kotlin.hll.dynamodbmapper.operations.items
import aws.sdk.kotlin.hll.dynamodbmapper.operations.scanPaginated

val orders = ordersTable
    .scanPaginated { }
    .items()

orders.collect { order -> println(order) }
```

### Manual pagination
<a name="ddb-mapper-operations-manual-pagination"></a>

DynamoDB Mapper also exposes non-paginating `query` and `scan` operations that return a single response page and a token you would use to request the next page yourself. These are intended for advanced scenarios; in typical code you should prefer the paginated variants.

Because manual pagination is easy to use incorrectly, the non-paginating operations are gated behind the [`@ManualPagination`](ddb-mapper-anno-index.md#ddb-mapper-anno-index-optin) opt-in annotation. To call one, opt in at the call site:

```
import aws.sdk.kotlin.hll.dynamodbmapper.annotations.ManualPagination
import aws.sdk.kotlin.hll.dynamodbmapper.expressions.KeyFilter

suspend fun firstPageOfOrders() {
    @OptIn(ManualPagination::class)
    val response = ordersTable.query {
        keyCondition = KeyFilter(partitionKey = "customer-123")
    }
    // Inspect response.items and the pagination token, and issue another call to continue.
}
```

## Related topics
<a name="ddb-mapper-operations-related"></a>
+  [Perform batch operations](ddb-mapper-batch.md)
+  [Perform transactional operations](ddb-mapper-transactions.md)
+  [Use expressions](ddb-mapper-expressions.md): filter results and build update expressions.
