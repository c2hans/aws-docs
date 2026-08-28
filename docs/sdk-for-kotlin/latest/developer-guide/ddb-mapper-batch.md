---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper-batch.html
---

# Perform batch operations
<a name="ddb-mapper-batch"></a>

Batch operations read or write many items across one or more tables in a single call. DynamoDB Mapper exposes two batch operations on the **mapper** itself (not on a table):
+  [`batchGetItem`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper/-dynamo-db-mapper/index.html): retrieve many items by key.
+  [`batchWriteItem`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper/-dynamo-db-mapper/index.html): put and/or delete many items.

**Important**
Batch operations are **not transactional**. The individual puts, deletes, and gets succeed or fail independently, and DynamoDB might return some as *unprocessed* (see [Handle unprocessed items](#ddb-mapper-batch-unprocessed)). If you need all-or-nothing semantics, use [transactional operations](ddb-mapper-transactions.md) instead. DynamoDB also limits how much a single batch can carry; see [BatchGetItem](/amazondynamodb/latest/developerguide/WorkingWithItems.html#WorkingWithItems.BatchOperations) and [BatchWriteItem](/amazondynamodb/latest/APIReference/API_BatchWriteItem.html) in the *Amazon DynamoDB Developer Guide* for the current limits.

Each batch request groups its work by table: inside the request block, call `table(…​)` once per table and describe that table’s items in the nested block.

## Write items in a batch
<a name="ddb-mapper-batch-write"></a>

Use [`batchWriteItem`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper/-dynamo-db-mapper/index.html) to seed or update a catalog. Within each table’s block, add puts with [`putItem`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.model/put-item.html) (or `putItems`) and deletes with `deleteKey` (or `deleteKeys`):

```
import aws.sdk.kotlin.hll.dynamodbmapper.items.Key

val productsTable = mapper.getProductTable("products")

mapper.batchWriteItem {
    table(productsTable) {
        putItem(Product(sku = "SKU-1", name = "Wireless mouse", category = "Electronics", priceCents = 2_999))
        putItem(Product(sku = "SKU-2", name = "USB-C cable", category = "Electronics", priceCents = 1_299))
        deleteKey(Key("SKU-OLD"))
    }
}
```

## Read items in a batch
<a name="ddb-mapper-batch-read"></a>

Use [`batchGetItem`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper/-dynamo-db-mapper/index.html) to fetch many items by key. Supply keys with `key`, `keys`, or by assigning the `keys` list; read the mapped objects from the response’s per-table `items`:

```
val response = mapper.batchGetItem {
    table(productsTable) {
        key(Key("SKU-1"))
        key(Key("SKU-2"))
    }
}

val products: List<Product> = response.table(productsTable).items
```

 `response.table(…​)` returns the results for that specific table. For a multi-table batch, call it once per table you included in the request.

## Handle unprocessed items
<a name="ddb-mapper-batch-unprocessed"></a>

DynamoDB might not process every item in a batch. For example, a request might exceed the per-call size or item-count limits, or a table might be throttled. The mapper surfaces what wasn’t processed so you can retry it:
+  [`batchGetItem`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper/-dynamo-db-mapper/index.html): the per-table response exposes `unprocessedKeys`, the keys that weren’t read.
+  [`batchWriteItem`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper/-dynamo-db-mapper/index.html): the per-table response exposes `unprocessedItems` (puts that weren’t written) and `unprocessedKeys` (deletes that weren’t performed).

```
val response = mapper.batchGetItem {
    table(productsTable) { keys = skus.map(::Key) }
}

val productResults = response.table(productsTable)
val fetched = productResults.items
val notFetched = productResults.unprocessedKeys   // retry these, typically with backoff
```

A non-empty unprocessed collection is normal, not an error. Resubmit the unprocessed keys or items in a follow-up batch, ideally with exponential backoff. See [Batch operations and error handling](/amazondynamodb/latest/developerguide/Programming.Errors.html#Programming.Errors.BatchOperations) in the *Amazon DynamoDB Developer Guide*.

## Related topics
<a name="ddb-mapper-batch-related"></a>
+  [Perform transactional operations](ddb-mapper-transactions.md): all-or-nothing reads and writes across tables.
+  [Operations overview](ddb-mapper-operations.md): single-item operations and where each operation lives.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
