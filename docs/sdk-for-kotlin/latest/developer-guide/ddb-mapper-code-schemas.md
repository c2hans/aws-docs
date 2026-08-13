---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper-code-schemas.html
---

# Manually define schemas
<a name="ddb-mapper-code-schemas"></a>

Instead of generating schemas from annotations, you can define them directly in code. Manual schemas give you full control over how objects map to items and don’t require the schema-generator plugin. They’re useful when you want explicit control over conversion, when you can’t annotate a type (for example, a class from another library), or when you map polymorphic or document-shaped data.

A schema has two parts:
+ An **item converter** ([`ItemConverter`](#ddb-mapper-code-schemas-item-converters)) that converts between your object and a DynamoDB item.
+ A **key specification** ([`KeySpec`](#ddb-mapper-code-schemas-keyspec)) that identifies primary key fields.

You combine them into an [`ItemSchema`](#ddb-mapper-code-schemas-assemble), then pass that schema to [`getTable`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper/-dynamo-db-mapper/get-table.html). This page builds a schema for the `Product` class (a partition-key-only item) as the worked example.

```
data class Product(
    val sku: String,
    val name: String,
    val category: String,
    val priceCents: Long,
)
```

## Item converters
<a name="ddb-mapper-code-schemas-item-converters"></a>

An `ItemConverter<T>` converts between objects of type `T` and DynamoDB items. It’s a type alias for `Converter<T, Item>` and defines two methods:
+  `convertRight(from: T): Item`: convert your object **to** an item for writes.
+  `convertLeft(from: Item): T`: convert an item **to** your object (for reads).

You may implement [`ItemConverter`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.items/-item-converter/index.html) from scratch or use one of the built-in implementations described in the following sections.

### Build a converter with `SimpleItemConverter`
<a name="ddb-mapper-code-schemas-simple-converter"></a>

 [`SimpleItemConverter`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.items/-simple-item-converter/index.html) builds an item attribute by attribute. It separates the potentially-immutable **object** type `T` from a mutable **builder** type `B` used when reading items back. You provide:
+  `builderFactory`: a function which creates a fresh builder.
+  `build`: a function which finalizes a builder into a `T`.
+ One [`AttributeDescriptor`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.items/-attribute-descriptor/index.html) per attribute, describing its name, how to read it from `T`, how to write it onto the builder, and which [value converter](#ddb-mapper-code-schemas-value-converters) handles its type.

For example, assuming the type `Product` is immutable, define a small builder for it:

```
class ProductBuilder {
    var sku: String? = null
    var name: String? = null
    var category: String? = null
    var priceCents: Long? = null

    fun build() = Product(
        sku = requireNotNull(sku) { "sku is required" },
        name = requireNotNull(name) { "name is required" },
        category = requireNotNull(category) { "category is required" },
        priceCents = requireNotNull(priceCents) { "priceCents is required" },
    )
}
```

Then assemble the converter. Each [`AttributeDescriptor`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.items/-attribute-descriptor/index.html) pairs a property with a built-in value converter (`StringValueConverter` for the `String` attributes and `NumberValueConverters.Long` for the `Long` price):

```
import aws.sdk.kotlin.hll.dynamodbmapper.items.AttributeDescriptor
import aws.sdk.kotlin.hll.dynamodbmapper.items.SimpleItemConverter
import aws.sdk.kotlin.hll.dynamodbmapper.values.scalars.NumberValueConverters
import aws.sdk.kotlin.hll.dynamodbmapper.values.scalars.StringValueConverter

val productConverter = SimpleItemConverter(
    builderFactory = ::ProductBuilder,
    build = ProductBuilder::build,
    AttributeDescriptor(
        name = "sku",
        getter = Product::sku,
        setter = ProductBuilder::sku::set,
        converter = StringValueConverter,
    ),
    AttributeDescriptor(
        name = "name",
        getter = Product::name,
        setter = ProductBuilder::name::set,
        converter = StringValueConverter,
    ),
    AttributeDescriptor(
        name = "category",
        getter = Product::category,
        setter = ProductBuilder::category::set,
        converter = StringValueConverter,
    ),
    AttributeDescriptor(
        name = "priceCents",
        getter = Product::priceCents,
        setter = ProductBuilder::priceCents::set,
        converter = NumberValueConverters.Long,
    ),
)
```

By default, attributes present on a stored item but absent from the descriptors are ignored when reading. Pass `unknownValueHandling` to [`SimpleItemConverter`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.items/-simple-item-converter/index.html) to throw or handle them instead.

## Define keys with `KeySpec`
<a name="ddb-mapper-code-schemas-keyspec"></a>

A [`KeySpec`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.items/-key-spec/index.html) names the key attributes and their types, which DynamoDB Mapper needs in order to build key conditions for [`query`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.operations/index.html) and [`scan`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.operations/index.html). Create a single-attribute spec with one of the [`KeySpec`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.items/-key-spec/index.html) companion functions (in alphabetical order: `byte`, `byteArray`, `int`, `long`, `short`, and `string`):

```
import aws.sdk.kotlin.hll.dynamodbmapper.items.KeySpec

val skuKey = KeySpec.string("sku")   // KeySpec.Key1<String>
```

**Important**
The attribute name you pass must exactly match the key attribute defined on your DynamoDB table or index.

For a composite key, the partition and sort keys are two separate [`KeySpec`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.items/-key-spec/index.html) instances (see [Assemble an `ItemSchema`](#ddb-mapper-code-schemas-assemble)). A single [`KeySpec`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.items/-key-spec/index.html) can also describe up to four attributes by chaining `thenInt`, `thenLong`, `thenString`, and the like. This is used for [multi-attribute index keys](/amazondynamodb/latest/developerguide/GSI.DesignPattern.MultiAttributeKeys.html), not table primary keys.

## Assemble an `ItemSchema`
<a name="ddb-mapper-code-schemas-assemble"></a>

Combine the converter and key spec into an [`ItemSchema`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.items/-item-schema/index.html). For a partition-key-only item like `Product`, pass the converter and a single partition key:

```
import aws.sdk.kotlin.hll.dynamodbmapper.items.ItemSchema

val productSchema = ItemSchema(
    converter = productConverter,
    partitionKey = KeySpec.string("sku"),
)

val productsTable = mapper.getTable("products", productSchema)
```

For a composite-key item, supply both keys:

```
val orderSchema = ItemSchema(
    converter = orderConverter,
    partitionKey = KeySpec.string("customerId"),
    sortKey = KeySpec.string("orderId"),
)
```

Equivalently, call `withKeySpec` on a converter:

```
import aws.sdk.kotlin.hll.dynamodbmapper.items.withKeySpec

val productSchema = productConverter.withKeySpec(KeySpec.string("sku"))
```

## Value converters
<a name="ddb-mapper-code-schemas-value-converters"></a>

A `ValueConverter<V>` converts a single value between your type `V` and a DynamoDB attribute value. Like [`ItemConverter`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.items/-item-converter/index.html), it defines `convertRight` (`V` → attribute value) and `convertLeft` (attribute value → `V`). The SDK ships value converters for the common types, so you usually reference an existing one rather than write your own. The following table lists representative built-in converters, in alphabetical order:

| Converter | Kotlin type | Package |
| --- | --- | --- |
|  `BooleanValueConverter`  |  `Boolean`  |  `…​values.scalars`  |
|  `ByteArrayValueConverter`  |  `ByteArray`  |  `…​values.scalars`  |
|  `DocumentValueConverter`  |  `Document`  |  `…​values.smithytypes`  |
|  `EnumValueConverter`  | enum types |  `…​values.scalars`  |
|  `InstantValueConverter`  |  `Instant`  |  `…​values.smithytypes`  |
|  `ListValueConverter`  |  `List`  |  `…​values.collections`  |
|  `MapValueConverter`  |  `Map`  |  `…​values.collections`  |
|  `NumberValueConverters.{Int, Long, Short, …​}`  | numeric types |  `…​values.scalars`  |
|  `StringValueConverter`  |  `String`  |  `…​values.scalars`  |
|  `UrlValueConverter`  |  `Url`  |  `…​values.smithytypes`  |

The full package prefix is `aws.sdk.kotlin.hll.dynamodbmapper.values`. Set and number-set converters live in `…​values.collections`.

To support a type that has no built-in converter, implement `ValueConverter` yourself. For example, a converter for `kotlin.uuid.Uuid` stored as a DynamoDB string:

```
import aws.sdk.kotlin.hll.dynamodbmapper.values.ValueConverter
import aws.sdk.kotlin.services.dynamodb.model.AttributeValue
import kotlin.uuid.Uuid

object UuidConverter : ValueConverter<Uuid> {
    override fun convertRight(from: Uuid): AttributeValue = AttributeValue.S(from.toString())
    override fun convertLeft(from: AttributeValue): Uuid = Uuid.parse(from.asS())
}
```

You can reference a custom value converter from a [`SimpleItemConverter`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.items/-simple-item-converter/index.html) attribute descriptor, or, when generating schemas from annotations, from [`@DynamoDbAttributeConverter`](ddb-mapper-anno-schema-gen.md).

## Other item converters
<a name="ddb-mapper-code-schemas-other"></a>

Two more built-in [`ItemConverter`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.items/-item-converter/index.html) implementations cover specialized mappings:

### HeterogeneousItemConverter
<a name="_heterogeneousitemconverter"></a>

 `HeterogeneousItemConverter` maps polymorphic or heterogeneous types by using a string discriminator attribute and delegating to per-subtype converters. You provide: \* `typeMapper`: a function which returns the discriminator value for an object \* `typeAttribute`: the item attribute name which stores the discriminator \* `subConverters`: a map from discriminator values to [`ItemConverter`s](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.items/-item-converter/index.html) for each subtype. Each subtype converter is an ordinary [`ItemConverter`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.items/-item-converter/index.html) such as a [`SimpleItemConverter`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.items/-simple-item-converter/index.html) built as shown [earlier in this topic](#ddb-mapper-code-schemas-simple-converter)).

For example:

```
import aws.sdk.kotlin.hll.dynamodbmapper.items.HeterogeneousItemConverter

sealed interface PaymentMethod {
    data class CreditCard(val customerId: String, val methodId: String, val last4: String) : PaymentMethod
    data class BankAccount(val customerId: String, val methodId: String, val routing: String) : PaymentMethod
    data class GiftCard(val customerId: String, val methodId: String, val balanceCents: Long) : PaymentMethod
}

fun paymentType(p: PaymentMethod): String = when (p) {
    is PaymentMethod.CreditCard -> "credit_card"
    is PaymentMethod.BankAccount -> "bank_account"
    is PaymentMethod.GiftCard -> "gift_card"
}

val paymentConverter = HeterogeneousItemConverter(
    typeMapper = ::paymentType,
    typeAttribute = "type",
    subConverters = mapOf(
        "bank_account" to bankAccountConverter,
        "credit_card" to creditCardConverter,
        "gift_card" to giftCardConverter,
    ),
)
```

Each object is stored using only the attributes relevant to its subtype, plus the discriminator.

### DocumentItemConverter
<a name="_documentitemconverter"></a>

 [`DocumentItemConverter`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.items/-document-item-converter/index.html) maps a smithy-kotlin `Document.Map` to and from an item, which is handy for schemaless or dynamically shaped data. Use `DocumentItemConverter.Default` for the standard configuration.

## Related topics
<a name="ddb-mapper-code-schemas-related"></a>
+  [Generate a schema from annotations](ddb-mapper-anno-schema-gen.md): let the plugin generate schemas for you.
+  [DynamoDB Mapper annotations reference](ddb-mapper-anno-index.md): the annotations (such as `@DynamoDbItem` and `@DynamoDbAttributeConverter`) that the schema generator reads.
+  [Operations overview](ddb-mapper-operations.md): use the table you obtained from your schema.
+  [Use secondary indexes with DynamoDB Mapper](ddb-mapper-secondary-indexes.md): multi-attribute index keys with [`KeySpec`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.items/-key-spec/index.html).
