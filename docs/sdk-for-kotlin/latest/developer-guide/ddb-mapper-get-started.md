---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper-get-started.html
---

# Get started with DynamoDB Mapper
<a name="ddb-mapper-get-started"></a>

This tutorial introduces the basic components of DynamoDB Mapper and shows how to use it in your code. The examples use an online store domain whose flagship type is an `Order`.

## Add dependencies
<a name="ddb-mapper-get-started-dependencies"></a>

Add the DynamoDB Mapper dependencies to your project build file. Replace {{X.Y.Z}} with the [latest release of the SDK](https://github.com/aws/aws-sdk-kotlin/releases/latest).

**Example**
To use DynamoDB Mapper with annotation-based schema generation, apply the schema-generator plugin and add the runtime and annotations dependencies to your `build.gradle.kts` file:

```
// build.gradle.kts
val sdkVersion: String = "{{X.Y.Z}}"

plugins {
    id("aws.sdk.kotlin.hll.dynamodbmapper.schema.generator") version sdkVersion
}

dependencies {
    implementation("aws.sdk.kotlin:dynamodb-mapper:$sdkVersion")
    implementation("aws.sdk.kotlin:dynamodb-mapper-annotations:$sdkVersion")
}
```
The annotations dependency and the schema-generator plugin are needed only if you generate schemas from annotated classes (shown in this topic). If you define schemas manually, you need only the `dynamodb-mapper` dependency.
Add the DynamoDB Mapper runtime dependency to the `<dependencies>` section of your `pom.xml` file:

```
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>aws.sdk.kotlin</groupId>
            <artifactId>bom</artifactId>
            <version>{{X.Y.Z}}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>

<dependencies>
    <dependency>
        <groupId>aws.sdk.kotlin</groupId>
        <artifactId>dynamodb-mapper-jvm</artifactId>
    </dependency>
</dependencies>
```
The DynamoDB Mapper schema-generator plugin is available for Gradle only. Maven projects must define schemas manually in code. For instructions, see [Manually define schemas](ddb-mapper-code-schemas.md).

## Create and use a mapper
<a name="ddb-mapper-get-started-create-mapper"></a>

DynamoDB Mapper uses the SDK’s DynamoDB client to interact with DynamoDB. Provide a configured [`DynamoDbClient`](/sdk-for-kotlin/api/latest/dynamodb/aws.sdk.kotlin.services.dynamodb/-dynamo-db-client/index.html) when you create a mapper:

```
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbMapper
import aws.sdk.kotlin.services.dynamodb.DynamoDbClient

val client = DynamoDbClient.fromEnvironment()
val mapper = DynamoDbMapper(client)
```

**Note**
DynamoDB Mapper doesn’t create tables. Use the [`DynamoDbClient`](/sdk-for-kotlin/api/latest/dynamodb/aws.sdk.kotlin.services.dynamodb/-dynamo-db-client/index.html) to create tables and indexes.

## Define a schema with class annotations
<a name="ddb-mapper-get-started-define-schema"></a>

For many Kotlin classes, the SDK can generate a schema at build time using the DynamoDB Mapper schema generator plugin. The plugin inspects your annotated classes and emits the schema, which removes the boilerplate of defining schemas by hand.

Annotate your class with `@DynamoDbItem`, mark the partition key with `@DynamoDbPartitionKey`, and (for a composite key) mark the sort key with `@DynamoDbSortKey`:

```
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbAttribute
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbAttributeConverter
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbIgnore
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbItem
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbPartitionKey
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbSortKey
import aws.smithy.kotlin.runtime.time.Instant
import kotlin.uuid.Uuid

@DynamoDbItem
data class Order(
    @DynamoDbPartitionKey
    val customerId: String,
    @DynamoDbSortKey
    val orderId: String,
    val status: OrderStatus,
    val totalCents: Long,
    val productSkus: List<String>,
    val tags: Set<String>,
    @DynamoDbAttribute("created_at")
    val placedAt: Instant,
    @DynamoDbAttributeConverter(UuidConverter::class)
    val idempotencyKey: Uuid,
) {
    @DynamoDbIgnore
    val isLargeOrder: Boolean get() = totalCents >= 100_00
}

enum class OrderStatus { PENDING, PAID, SHIPPED, DELIVERED, CANCELED }
```

This example previews a few field-level annotations that will be discussed in greater detail later:
+  `@DynamoDbAttribute` renames an attribute
+  `@DynamoDbAttributeConverter` supplies a custom converter for a type the generator doesn’t support on its own (here, `kotlin.uuid.Uuid`)
+  `@DynamoDbIgnore` excludes a property from mapping

See [Generate a schema from annotations](ddb-mapper-anno-schema-gen.md) and the [annotations reference](ddb-mapper-anno-index.md) for the full set.

The custom converter is a small object that implements `convertRight`/`convertLeft`:

```
import aws.sdk.kotlin.hll.dynamodbmapper.values.ValueConverter
import aws.sdk.kotlin.services.dynamodb.model.AttributeValue
import kotlin.uuid.Uuid

object UuidConverter : ValueConverter<Uuid> {
    override fun convertRight(from: Uuid): AttributeValue = AttributeValue.S(from.toString())
    override fun convertLeft(from: AttributeValue): Uuid = Uuid.parse(from.asS())
}
```

After you build the project, the generator produces an `OrderSchema` and a convenience extension function. You can get a table reference with the generated `getOrderTable` extension. Note that the function name contains the class name (`Order`), while the string you pass is your actual table name (`orders`):

```
val ordersTable = mapper.getOrderTable("orders")
```

Equivalently, you can pass the generated schema to [`getTable`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper/-dynamo-db-mapper/get-table.html):

```
import com.example.store.model.dynamodbmapper.generatedschemas.OrderSchema

val ordersTable = mapper.getTable("orders", OrderSchema)
```

## Invoke operations
<a name="ddb-mapper-get-started-invoke-operations"></a>

After you have a table reference, you can perform operations on it. The following sections show a few basics. For the complete operation surface and the different ways to invoke each operation, see the [Operations overview](ddb-mapper-operations.md).

### Put an item
<a name="ddb-mapper-get-started-put-item"></a>

```
import aws.smithy.kotlin.runtime.time.Instant
import kotlin.uuid.Uuid

ordersTable.putItem {
    item = Order(
        customerId = "customer-123",
        orderId = "ORDER#2026-06-25#0042",
        status = OrderStatus.PENDING,
        totalCents = 4_999,
        productSkus = listOf("SKU-1", "SKU-2"),
        tags = setOf("gift"),
        placedAt = Instant.now(),
        idempotencyKey = Uuid.random(),
    )
}
```

### Get an item
<a name="ddb-mapper-get-started-get-item"></a>

 [`getItem`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.model/get-item.html) returns a `GetItemResponse`; read the mapped object from its `item` property (which is `null` if no matching item exists). For a composite-key table, supply both keys, wrapping each key value with `Key(…​)`:

```
import aws.sdk.kotlin.hll.dynamodbmapper.items.Key

val response = ordersTable.getItem {
    partitionKey = Key("customer-123")
    sortKey = Key("ORDER#2026-06-25#0042")
}

println(response.item)   // the Order, or null
```

### Query with paginated results
<a name="ddb-mapper-get-started-query"></a>

 [`query`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.operations/index.html) and [`scan`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.operations/index.html) can match more items than fit in a single response. DynamoDB Mapper provides paginating variants ([`queryPaginated`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.operations/index.html) and [`scanPaginated`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.operations/index.html)) that return a [`Flow`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/) of response pages and transparently fetch subsequent pages as you collect them.

```
import aws.sdk.kotlin.hll.dynamodbmapper.expressions.KeyFilter

val responses = ordersTable.queryPaginated {
    keyCondition = KeyFilter(partitionKey = "customer-123")
}

responses.collect { response ->
    val orders = response.items.orEmpty()
    println("Found a page of ${orders.size} orders")
    orders.forEach { order -> println(order) }
}
```

Often a flow of objects is more convenient than a flow of response pages. Call `items()` to flatten a paginated flow into a `Flow` of your objects (here, a `Flow<Order>` instead of a `Flow<QueryResponse<Order>>`):

```
val orders = ordersTable
    .queryPaginated {
        keyCondition = KeyFilter(partitionKey = "customer-123")
        limit = 20
    }
    .items()

orders.collect { order -> println(order) }
```

## Next steps
<a name="ddb-mapper-get-started-next-steps"></a>
+ Learn the full operation surface in the [Operations overview](ddb-mapper-operations.md).
+ Customize schema generation in [Generate a schema from annotations](ddb-mapper-anno-schema-gen.md).
+ Define schemas by hand in [Manually define schemas](ddb-mapper-code-schemas.md).
