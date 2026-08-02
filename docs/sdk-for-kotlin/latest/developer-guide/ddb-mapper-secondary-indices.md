---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper-secondary-indices.html
---

# Use secondary indices with DynamoDB Mapper
<a name="ddb-mapper-secondary-indices"></a>

**Important**
DynamoDB Mapper is a Developer Preview release. It is not feature complete and is subject to change.

## Define a schema for a secondary index
<a name="ddb-mapper-secondary-indices-schema"></a>

DynamoDB tables support secondary indices which provide access to data using different keys from those defined on the base table itself. As with base tables, DynamoDB Mapper interacts with indices by using the `ItemSchema` type.

DynamoDB secondary indices are not required to contain every attribute from the base table. Accordingly, the Kotlin class that maps to an index may differ from the Kotlin class that maps to that index’s base table. When that is the case, a separate schema must be declared for the index class.

The following code manually creates an index schema for the DynamoDB `cars` table.

```
import aws.sdk.kotlin.hll.dynamodbmapper.items.ItemConverter
import aws.sdk.kotlin.hll.dynamodbmapper.items.ItemSchema
import aws.sdk.kotlin.hll.dynamodbmapper.model.itemOf

// This is a data class for modelling the index of the Car table. Note
// that it contains a subset of the fields from the Car class and also
// uses different names for them.
data class Model(val name: String, val manufacturer: String)

// We define an item converter.
val modelConverter = object : ItemConverter<Model> {
    override fun convertTo(from: Model, onlyAttributes: Set<String>?): Item  = itemOf(
        "model" to AttributeValue.S(from.name),
        "make" to AttributeValue.S(from.manufacturer),
    )

    override fun convertFrom(to: Item): Model = Model(
        name = to["model"]?.asSOrNull() ?: error("Invalid attribute `model`"),
        manufacturer = to["make"]?.asSOrNull() ?: error("Invalid attribute `make`"),
    )
}
val modelKey = KeySpec.String("model")
val makeKey = KeySpec.String("make")

val modelSchema = ItemSchema(modelConverter, modelKey, makeKey) // The partition key specification is the second parameter.

/* Note that `Model` index's partition key is `model` and its sort key is `make`,
   whereas the `Car` base table uses `make` as the partition key and `model` as the sort key:

        @DynamoDbItem
        data class Car(
            @DynamoDbPartitionKey
            val make: String,

            @DynamoDbSortKey
            val model: String,

            val initialYear: Int
        )
*/
```

We can now use `Model` instances in operations.

## Use secondary indices in operations
<a name="ddb-mapper-gs-index-ops"></a>

DynamoDB Mapper supports a subset of operations on indices, namely `queryPaginated` and `scanPaginated`. To invoke these operations on an index, you must first obtain a reference to an index from the table object. In the following sample, we use the `modelSchema` that we created previously for the `cars-by-model` index (creation not shown here):

```
val table = mapper.getTable("cars", CarSchema)
val index = table.getIndex("cars-by-model", modelSchema)

val modelFlow = index
    .scanPaginated { }
    .items()

modelFlow.collect { model -> println(model) }
```
