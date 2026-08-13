---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper-anno-schema-gen.html
---

# Generate a schema from annotations
<a name="ddb-mapper-anno-schema-gen"></a>

The simplest way to use DynamoDB Mapper is to annotate your Kotlin classes and let the SDK generate their schemas for you at build time. You annotate a class with `@DynamoDbItem`, mark its key properties, and the **schema-generator Gradle plugin** inspects the annotated classes and emits a schema object and a convenience extension function for obtaining a typed table.

This topic covers the plugin setup, the available annotations, custom converters for unsupported types, and how to configure the generator. For the complete list of annotations and their parameters, see the [annotations reference](ddb-mapper-anno-index.md).

**Note**
The schema-generator plugin is available for Gradle only. If you use Maven, see [Manually define schemas](ddb-mapper-code-schemas.md) for how to define schemas in code.

## How annotation-based generation works
<a name="ddb-mapper-anno-schema-gen-how"></a>

1. You apply the schema-generator plugin and annotate your data classes.

1. At build time, the plugin’s symbol processor reads the annotations. For each `@DynamoDbItem` class `Foo`, the plugin generates a `FooSchema` object and a `DynamoDbMapper.getFooTable(…​)` extension function.

1. Your code calls the generated extension or passes the generated schema to [`getTable`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper/-dynamo-db-mapper/get-table.html) to obtain a typed [`Table`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.model/-table/index.html) and perform [operations](ddb-mapper-operations.md) on it.

You never need to write or edit the generated code. Rebuilding your project regenerates it from your annotated classes.

## Add the plugin and dependencies
<a name="ddb-mapper-anno-schema-gen-plugin"></a>

Apply the plugin and add the runtime and annotations dependencies in your `build.gradle.kts`. Replace {{X.Y.Z}} with the [latest release of the SDK](https://github.com/aws/aws-sdk-kotlin/releases/latest).

```
// build.gradle.kts
val sdkVersion = "[.replaceable]##X.Y.Z##"

plugins {
    id("aws.sdk.kotlin.hll.dynamodbmapper.schema.generator") version sdkVersion
}

dependencies {
    implementation("aws.sdk.kotlin:dynamodb-mapper:$sdkVersion")
    implementation("aws.sdk.kotlin:dynamodb-mapper-annotations:$sdkVersion")
}
```

Each of these dependencies fulfills a different function:
+ The `dynamodbmapper.schema.generator` plugin generates the schemas
+ The `dynamodb-mapper` dependency provides the [`DynamoDbMapper`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper/-dynamo-db-mapper/index.html) type
+ The `dynamodb-mapper-annotations` dependency provides the annotations you apply to your classes

## Annotate a class
<a name="ddb-mapper-anno-schema-gen-annotate"></a>

Annotate the class with `@DynamoDbItem` and mark its primary key. Every top-level item type must have exactly one partition key (`@DynamoDbPartitionKey`) and can have at most one sort key (`@DynamoDbSortKey`). All other public properties are mapped to attributes automatically.

```
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbItem
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbPartitionKey
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbSortKey
import aws.smithy.kotlin.runtime.time.Instant

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
    val placedAt: Instant,
)
```

The generator maps the property types it knows about, including primitives, `String`, enums such as `OrderStatus`, collections, and several SDK runtime types such as `Instant`. For types it doesn’t support out of the box, supply a [custom converter](#ddb-mapper-anno-schema-gen-converters).

### Supported types
<a name="ddb-mapper-anno-schema-gen-supported-types"></a>

The following Kotlin types are automatically converted by DynamoDB Mapper into the given DynamoDB types:

| Kotlin type | DynamoDB type | Notes |
| --- | --- | --- |
|  [`Boolean`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/)  |  [`BOOL`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.Boolean) (Boolean) |  |
|  [`Byte`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte/)  |  [`N`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.Number) (Number) |  |
|  [`ByteArray`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/)  |  [`B`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.Binary) (Binary) |  |
|  [`Char`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char/)  |  [`S`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.String) (String) |  |
|  [`CharArray`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-array/)  |  [`S`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.String) (String) |  |
|  [`Document.Map`](/smithy-kotlin/api/latest/runtime-core/aws.smithy.kotlin.runtime.content/-document/-map/) (`aws.smithy.kotlin.runtime.content`) |  [`M`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.Document.Map) (Map) | Values in the map use the converter appropriate for their type |
|  [`Double`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/)  |  [`N`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.Number) (Number) |  |
|  ` [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/)<E>` (any enum class) |  [`S`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.String) (String) | Stored as the enum constant’s `name`  |
|  [`Float`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/)  |  [`N`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.Number) (Number) |  |
|  [`Instant`](/sdk-for-kotlin/api/latest/smithy-kotlin-runtime-time/aws.smithy.kotlin.runtime.time/-instant/index.html) (`aws.smithy.kotlin.runtime.time`) |  [`N`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.Number) (Number) | Stored as epoch seconds by default |
|  [`Int`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/)  |  [`N`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.Number) (Number) |  |
|  ` [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/)<E>`  |  [`L`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.Document.List) (List) | Elements in the list use the converter appropriate for their type |
|  [`Long`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/)  |  [`N`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.Number) (Number) |  |
|  ` [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/)<String, V>`  |  [`M`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.Document.Map) (Map) | Values in the map use the converter appropriate for their type |
|  ` [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/)<Byte>`  |  [`NS`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.SetTypes) (Number Set) |  |
|  ` [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/)<ByteArray>`  |  [`BS`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.SetTypes) (Binary Set) |  |
|  ` [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/)<Char>`  |  [`SS`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.SetTypes) (String Set) |  |
|  ` [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/)<CharArray>`  |  [`SS`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.SetTypes) (String Set) |  |
|  ` [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/)<Double>`  |  [`NS`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.SetTypes) (Number Set) |  |
|  ` [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/)<Float>`  |  [`NS`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.SetTypes) (Number Set) |  |
|  ` [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/)<Int>`  |  [`NS`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.SetTypes) (Number Set) |  |
|  ` [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/)<Long>`  |  [`NS`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.SetTypes) (Number Set) |  |
|  ` [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/)<Short>`  |  [`NS`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.SetTypes) (Number Set) |  |
|  ` [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/)<String>`  |  [`SS`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.SetTypes) (String Set) |  |
|  ` [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/)<UByte>`  |  [`NS`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.SetTypes) (Number Set) |  |
|  ` [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/)<UInt>`  |  [`NS`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.SetTypes) (Number Set) |  |
|  ` [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/)<ULong>`  |  [`NS`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.SetTypes) (Number Set) |  |
|  ` [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/)<UShort>`  |  [`NS`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.SetTypes) (Number Set) |  |
|  [`Short`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-short/)  |  [`N`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.Number) (Number) |  |
|  [`String`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/)  |  [`S`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.String) (String) |  |
|  [`UByte`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-u-byte/)  |  [`N`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.Number) (Number) |  |
|  [`UInt`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-u-int/)  |  [`N`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.Number) (Number) |  |
|  [`ULong`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-u-long/)  |  [`N`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.Number) (Number) |  |
|  [`UShort`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-u-short/)  |  [`N`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.Number) (Number) |  |
|  [`Url`](/sdk-for-kotlin/api/latest/smithy-kotlin-runtime/aws.smithy.kotlin.runtime.net.url/-url/index.html) (`aws.smithy.kotlin.runtime.net.url`) |  [`S`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.String) (String) |  |
| Any supported type `T?`  |  [`NULL`](/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes.Null) when the value is `null`; otherwise uses the converter for `T`  |  |

### Customize how properties map
<a name="ddb-mapper-anno-schema-gen-customize"></a>

Several property-level annotations can adjust the default mapping. For example:

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
```

In alphabetical order, the attribute-level annotations used in the preceding example are:
+  `@DynamoDbAttribute(name)`: store the property under a different DynamoDB attribute name (here, `placedAt` is stored as `created_at`). Without it, the attribute name matches the property name.
+  `@DynamoDbAttributeConverter(converter)`: supply a custom `ValueConverter` for a property whose type the generator doesn’t support on its own. See [Convert unsupported types](#ddb-mapper-anno-schema-gen-converters).
+  `@DynamoDbIgnore`: exclude a property from mapping entirely (here, a computed convenience property).

More property annotations enable various features and are covered in-depth in [DynamoDB Mapper annotations reference](ddb-mapper-anno-index.md).

## Convert unsupported types
<a name="ddb-mapper-anno-schema-gen-converters"></a>

For a property whose type the generator doesn’t natively map (for example, `kotlin.uuid.Uuid`), apply `@DynamoDbAttributeConverter` with a [`ValueConverter`](ddb-mapper-code-schemas.md#ddb-mapper-code-schemas-value-converters) that translates between your type and a DynamoDB attribute value. A value converter implements two methods: `convertRight` (your type → attribute value) and `convertLeft` (attribute value → your type).

```
import aws.sdk.kotlin.hll.dynamodbmapper.values.ValueConverter
import aws.sdk.kotlin.services.dynamodb.model.AttributeValue
import kotlin.uuid.Uuid

object UuidConverter : ValueConverter<Uuid> {
    override fun convertRight(from: Uuid): AttributeValue = AttributeValue.S(from.toString())
    override fun convertLeft(from: AttributeValue): Uuid = Uuid.parse(from.asS())
}
```

The class passed to `@DynamoDbAttributeConverter(…​)` must implement `ValueConverter`. See [Manually define schemas](ddb-mapper-code-schemas.md) for the full converter model and the built-in converters you can reuse.

## Use the generated schema
<a name="ddb-mapper-anno-schema-gen-use"></a>

After you build the project, the generator produces an `OrderSchema` object and, by default, a `getOrderTable` extension on [`DynamoDbMapper`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper/-dynamo-db-mapper/index.html). Note that the extension name contains the class name `Order`, while the string you pass is your actual table name `"orders"`:

```
val ordersTable = mapper.getOrderTable("orders")
```

Equivalently, pass the generated schema to [`getTable`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper/-dynamo-db-mapper/get-table.html). By default, the generated schema lives in a package derived from your class’s package plus `.dynamodbmapper.generatedschemas`. For instance, if your annotated class is `com.example.store.model.Order` then the default generated schema is `com.example.store.model.dynamodbmapper.generatedschemas.OrderSchema`:

```
import com.example.store.model.dynamodbmapper.generatedschemas.OrderSchema

val ordersTable = mapper.getTable("orders", OrderSchema)
```

## Configure the generator
<a name="ddb-mapper-anno-schema-gen-configure"></a>

The plugin contributes a `dynamoDbMapper` extension to your build script. All settings are optional; their defaults are shown in the following example.

```
// build.gradle.kts
import aws.sdk.kotlin.hll.codegen.rendering.Visibility
import aws.sdk.kotlin.hll.dynamodbmapper.codegen.annotations.DestinationPackage
import aws.sdk.kotlin.hll.dynamodbmapper.codegen.annotations.GenerateBuilderClasses

dynamoDbMapper {
    // When to generate builder classes for your item types: WHEN_REQUIRED (default) or ALWAYS.
    generateBuilderClasses = GenerateBuilderClasses.WHEN_REQUIRED

    // Visibility of generated declarations. Default: PUBLIC.
    visibility = Visibility.PUBLIC

    // Where generated code is placed. Relative(...) (default) appends to each class's own package;
    // Absolute(...) places everything in one fixed package.
    destinationPackage = DestinationPackage.Relative("dynamodbmapper.generatedschemas")

    // Whether to generate the DynamoDbMapper.get<Class>Table() convenience extensions. Default: true.
    generateGetTableExtension = true
}
```

The configurable settings, in alphabetical order:

| Setting | Type | Default | Purpose |
| --- | --- | --- | --- |
|  `destinationPackage`  |  `DestinationPackage`  |  `DestinationPackage.Relative("dynamodbmapper.generatedschemas")`  | Package for generated code. Use `DestinationPackage.Relative(suffix)` to place it relative to each source class’s package, or `DestinationPackage.Absolute(pkg)` to use one fixed package. |
|  `generateBuilderClasses`  |  `GenerateBuilderClasses`  |  `WHEN_REQUIRED`  |  `WHEN_REQUIRED` generates a builder only when a class can’t be built directly (for example, it has immutable members and no zero-arg constructor); `ALWAYS` always generates one. |
|  `generateGetTableExtension`  |  `Boolean`  |  `true`  | Whether to generate the `DynamoDbMapper.get<Class>Table(…​)` extensions. When `false`, obtain tables with `getTable(name, schema)`. |
|  `visibility`  |  `Visibility`  |  `PUBLIC`  | Visibility of generated declarations. |

## Related topics
<a name="ddb-mapper-anno-schema-gen-related"></a>
+  [Manually define schemas](ddb-mapper-code-schemas.md): define schemas in code instead of with annotations.
+  [DynamoDB Mapper annotations reference](ddb-mapper-anno-index.md): every annotation and its parameters.
+  [Built-in features (TTL, atomic counters)](ddb-mapper-builtins.md): runtime behavior of `@DynamoDbCounter` and `@DynamoDbTtlSeconds`.
