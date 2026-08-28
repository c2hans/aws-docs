---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper-transactions.html
---

# Perform transactional operations
<a name="ddb-mapper-transactions"></a>

Transactional operations group multiple reads or multiple writes into a single **all-or-nothing** unit across one or more tables. Like batch operations, they’re invoked on the **mapper**:
+  [`transactGetItems`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper/-dynamo-db-mapper/index.html): atomically read items.
+  [`transactWriteItems`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper/-dynamo-db-mapper/index.html): atomically put, update, delete, and condition-check items.

If any part of a transactional write fails (for example, a condition isn’t met or another request conflicts), DynamoDB cancels the **entire** transaction and no changes are applied. Note this is in contrast to [batch operations](ddb-mapper-batch.md), which process items independently. For the ACID guarantees, limits, and cancellation reasons, see [Amazon DynamoDB transactions](/amazondynamodb/latest/developerguide/transactions.html) in the *Amazon DynamoDB Developer Guide*.

As with batches, each request groups work by table: call `table(…​)` once per table and describe that table’s actions in the nested block.

## Write items in a transaction
<a name="ddb-mapper-transactions-write"></a>

A [`transactWriteItems`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper/-dynamo-db-mapper/index.html) block supports four kinds of action, each optionally guarded by a `condition`. In alphabetical order:
+  `conditionCheck(key) { condition { …​ } }`: assert a condition on an item without modifying it.
+  `delete(key) { …​ }`: delete an item.
+  `put(item) { …​ }`: create or replace an item.
+  `update(key) { update { …​ } }`: modify an item with an [update expression](ddb-mapper-expressions.md).

The following transaction places an order atomically: it creates the `Order`, decrements the ordered `Product`'s inventory only if stock remains, and debits the `Customer`'s balance only if they have sufficient funds. If any condition fails, none of the three writes happen.

```
import aws.sdk.kotlin.hll.dynamodbmapper.items.Key

val ordersTable = mapper.getOrderTable("orders")
val productsTable = mapper.getProductTable("products")
val customersTable = mapper.getCustomerTable("customers")

mapper.transactWriteItems {
    table(ordersTable) {
        put(newOrder) {
            condition { attr["orderId"].notExists() }   // don't overwrite an existing order
        }
    }
    table(productsTable) {
        update(Key("SKU-1")) {
            condition { attr["inventory"] gte 1L }       // only if in stock
            update {
                set { attr["inventory"] = attr["inventory"] - 1L }
            }
        }
    }
    table(customersTable) {
        update(Key("customer-123")) {
            condition { attr["balanceCents"] gte 4_999L } // only if funds suffice
            update {
                set { attr["balanceCents"] = attr["balanceCents"] - 4_999L }
            }
        }
    }
}
```

The key value passed to `update`, `delete`, and `conditionCheck` is wrapped with `Key(…​)`. For a composite-key table, pass both: `update(Key(partition), Key(sort)) { …​ }`. A `put` takes the object directly because its keys come from the item.

## Read items in a transaction
<a name="ddb-mapper-transactions-read"></a>

 [`transactGetItems`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper/-dynamo-db-mapper/index.html) reads items across tables in one atomic, consistent snapshot. Supply keys with `key` (or `keys`) and read each table’s results from the response:

```
val response = mapper.transactGetItems {
    table(ordersTable) {
        key(Key("customer-123"), Key("ORDER#2026-06-25#0042"))
    }
    table(customersTable) {
        key(Key("customer-123"))
    }
}

val order = response.table(ordersTable).items.firstOrNull()
val customer = response.table(customersTable).items.firstOrNull()
```

## Related topics
<a name="ddb-mapper-transactions-related"></a>
+  [Perform batch operations](ddb-mapper-batch.md): high-throughput, non-atomic reads and writes.
+  [Use expressions](ddb-mapper-expressions.md): the `condition` and `update` expressions used by transaction actions.
+  [Operations overview](ddb-mapper-operations.md): single-item operations and operation scope.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
