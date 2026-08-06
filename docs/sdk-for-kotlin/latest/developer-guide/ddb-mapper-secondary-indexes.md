---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper-secondary-indexes.html
---

# Use secondary indexes with DynamoDB Mapper
<a name="ddb-mapper-secondary-indexes"></a>

A [secondary index](/amazondynamodb/latest/developerguide/SecondaryIndexes.html) lets you query a table using an alternate key. DynamoDB Mapper models an index as **its own item type**: a class describing the attributes projected into the index, with a schema whose keys are the index’s keys. You obtain an `Index` reference from a table and then run `query` and `scan` operations on it, just as you would on a table.

Indexes are **read-only**: you write through the base table, and DynamoDB propagates the changes to the index. An `Index` reference therefore supports only `query` and `scan`, not item writes.

**Note**
DynamoDB Mapper does not create indexes. Define the secondary index on your table with the `DynamoDbClient` (or another tool), then read from it with the mapper.

## Define an item type for the index
<a name="ddb-mapper-secondary-indexes-define"></a>

Create a class that describes the items as they appear in the index. It’s annotated like any other item type, but its key properties are the **index’s** partition and sort keys, and its other properties are limited to the attributes the index projects.

For example, an online store keeps a `products-by-category` index on the `products` table so it can list products within a category ordered by price. The index partitions on `category` and sorts on `priceCents`, and projects the `sku` and `name` attributes:

```
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbItem
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbPartitionKey
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbSortKey

@DynamoDbItem
data class ProductByCategory(
    @DynamoDbPartitionKey
    val category: String,
    @DynamoDbSortKey
    val priceCents: Long,
    val sku: String,
    val name: String,
)
```

As with any annotated class, the schema generator produces a `ProductByCategorySchema` for this type. Alternatively, you can also [build the schema manually](ddb-mapper-code-schemas.md).

## Get an index reference
<a name="ddb-mapper-secondary-indexes-get"></a>

Call `getIndex` on the base table, passing the index name and the index’s schema. The result is an `Index` typed to the index’s item type:

```
import com.example.store.model.dynamodbmapper.generatedschemas.ProductByCategorySchema

val productsTable = mapper.getProductTable("products")
val byCategory = productsTable.getIndex("products-by-category", ProductByCategorySchema)
```

## Query an index
<a name="ddb-mapper-secondary-indexes-query"></a>

Querying an index works exactly like [querying a table](ddb-mapper-operations.md): supply a `keyCondition` and collect the paginated results. This query finds products in the `Electronics` category priced under $50.00, using a sort-key condition on `priceCents`:

```
import aws.sdk.kotlin.hll.dynamodbmapper.expressions.KeyFilter

val cheapElectronics = byCategory
    .queryPaginated {
        keyCondition = KeyFilter("Electronics", { sortKey lt 5_000L })
    }
    .items()

cheapElectronics.collect { product -> println("${product.name}: ${product.priceCents}") }
```

The `keyCondition` always constrains the partition key and can add a condition on the sort key. See [Use expressions](ddb-mapper-expressions.md) for the full range of key conditions and for filter expressions you can apply with `filter { }`.

## Scan an index
<a name="ddb-mapper-secondary-indexes-scan"></a>

You can also `scan` an index to read every projected item, optionally narrowing the results with a filter expression:

```
val discountable = byCategory
    .scanPaginated {
        filter { attr["priceCents"] gt 10_000L }
    }
    .items()
```

## Related topics
<a name="ddb-mapper-secondary-indexes-related"></a>
+  [Use expressions](ddb-mapper-expressions.md): key conditions, filter expressions, and update expressions.
+  [Operations overview](ddb-mapper-operations.md): the `query`/`scan` operations and pagination.
+  [DynamoDB Mapper annotations reference](ddb-mapper-anno-index.md): the annotations used to define the index item type.
+  [Manually define schemas](ddb-mapper-code-schemas.md): build an index schema in code.
