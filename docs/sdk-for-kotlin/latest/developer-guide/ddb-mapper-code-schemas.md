---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper-code-schemas.html
---

# Manually define schemas
<a name="ddb-mapper-code-schemas"></a>

**Important**
DynamoDB Mapper is a Developer Preview release. It is not feature complete and is subject to change.

## Define a schema in code
<a name="ddb-mapper-gs-manual-schema-def"></a>

For maximum control and customizability, you can manually define and customize schemas in code.

As shown in the following snippet, you need to include fewer dependencies in your `build.gradle.kts` file compared to using annotation-driven schema creation.

Replace {{X.Y.Z}} with the version you’re using in your app or with the [latest version available](https://github.com/awslabs/aws-sdk-kotlin/releases/latest).

```
// build.gradle.kts
val sdkVersion: String = {{X.Y.Z}}

dependencies {
    implementation("aws.sdk.kotlin:dynamodb-mapper:$sdkVersion-beta") // For the Developer Preview, use the beta version of the latest SDK.
}
```

Note that you don’t need the schema generator plugin nor the annotation package.

The mapping between a Kotlin class and a DynamoDB item requires an `ItemSchema<T>` implementation, where `T` is the type of the Kotlin class. A schema consists of the following elements:
+ An item converter, which defines how to convert between Kotlin object instances and DynamoDB items.
+ A partition key specification, which defines the name and type of the partition key attribute.
+ Optionally, a sort key specification, which defines the name and type of the sort key attribute.

In the following code we manually create a `CarSchema` instance:

```
import aws.sdk.kotlin.hll.dynamodbmapper.items.ItemConverter
import aws.sdk.kotlin.hll.dynamodbmapper.items.ItemSchema
import aws.sdk.kotlin.hll.dynamodbmapper.model.itemOf

// We define a schema for this data class.
data class Car(val make: String, val model: String, val initialYear: Int)

// First, define an item converter.
val carConverter = object : ItemConverter<Car> {
    override fun convertTo(from: Car, onlyAttributes: Set<String>?): Item  = itemOf(
        "make" to AttributeValue.S(from.make),
        "model" to AttributeValue.S(from.model),
        "initialYear" to AttributeValue.N(from.initialYear.toString()),
    )

    override fun convertFrom(to: Item): Car = Car(
        make = to["make"]?.asSOrNull() ?: error("Invalid attribute `make`"),
        model = to["model"]?.asSOrNull() ?: error("Invalid attribute `model`"),
        initialYear = to["initialYear"]?.asNOrNull()?.toIntOrNull()
            ?: error("Invalid attribute `initialYear`"),
    )
}

// Next, define the specifications for the partition key and sort key.
val makeKey = KeySpec.String("make")
val modelKey = KeySpec.String("model")

// Finally, create the schema from the converter and key specifications.
// Note that the KeySpec for the partition key comes first in the ItemSchema constructor.
val CarSchema = ItemSchema(carConverter, makeKey, modelKey)
```

The previous code creates a converter named `carConverter`, which is defined as an anonymous implementation of `ItemConverter<Car>`. The converter’s `convertTo` method accepts a `Car` argument and returns an `Item` instance representing the literal keys and values of DynamoDB item attributes. The converter’s `convertFrom` method accepts an `Item` argument and returns a `Car` instance from the attribute values of the `Item` argument.

Next the code creates two key specifications: one for the partition key and one for the sort key. Every DynamoDB table or index must have exactly one partition key and, correspondingly, so must every DynamoDB Mapper schema definition. Schemas may also have one sort key.

In the last statement, the code creates a schema for the `cars` DynamoDB table from the converter and key specifications.

The resulting schema is equivalent to the annotation-driven schema that we generated in the [Define a schema with class annotations](ddb-mapper-get-started.md#ddb-mapper-gs-anno-schema-def) section. For reference, the following is the annotated class we used:

### Car class with DynamoDB Mapper annotations
<a name="_car_class_with_dynamodb_mapper_annotations"></a>

```
@DynamoDbItem
data class Car(
    @DynamoDbPartitionKey
    val make: String,

    @DynamoDbSortKey
    val model: String,

    val initialYear: Int
)
```

In addition to implementing your own `ItemConverter`, DynamoDB Mapper includes several helpful implementations such as:
+  `SimpleItemConverter`: provides simple conversion logic by using a builder class and attribute descriptors. See the example in the [Define a custom item converter](ddb-mapper-anno-schema-gen.md#ddb-mapper-anno-schema-custom) for how you can make use of this implementation.
+  `HeterogeneousItemConverter`: provides polymorphic type conversion logic by using a discriminator attribute and delegate `ItemConverter` instances for subtypes.
+  `DocumentConverter`: provides conversion logic for unstructured data in [Document](/smithy-kotlin/api/latest/runtime-core/aws.smithy.kotlin.runtime.content/-document.html) objects.
