---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper-anno-schema-gen.html
---

# Generate a schema from annotations
<a name="ddb-mapper-anno-schema-gen"></a>

**Important**
DynamoDB Mapper is a Developer Preview release. It is not feature complete and is subject to change.

DynamoDB Mapper relies on schemas that define the mapping between your Kotlin classes and DynamoDB items. Your Kotlin classes can drive the creation of schemas by using the schema generator Gradle plugin.

## Apply the plugin
<a name="ddb-mapper-anno-schema-gen-plugin"></a>

To start code generating schemas for your classes, apply the plugin in your application’s build script and add a dependency on the annotations module. The following Gradle script snippet shows the necessary setup for code generation.

Replace {{X.Y.Z}} with the version you’re using in your app or with the [latest version available](https://github.com/awslabs/aws-sdk-kotlin/releases/latest).

```
// build.gradle.kts
val sdkVersion: String = {{X.Y.Z}}

plugins {
    id("aws.sdk.kotlin.hll.dynamodbmapper.schema.generator") version "$sdkVersion-beta" // For the Developer Preview, use the beta version of the latest SDK.
}

dependencies {
    implementation("aws.sdk.kotlin:dynamodb-mapper:$sdkVersion-beta")
    implementation("aws.sdk.kotlin:dynamodb-mapper-annotations:$sdkVersion-beta")
}
```

## Configure the plugin
<a name="ddb-mapper-anno-schema-gen-conf-plugin"></a>

The plugin offers a number of configuration options that you can apply by using the `dynamoDbMapper { …​ }` plugin extension in your build script:

| Option | Option description | Values |
| --- | --- | --- |
|  `generateBuilderClasses`  | Controls whether DSL-style builder classes will be generated for classes annotated with `@DynamoDbItem`  |  `WHEN_REQUIRED` (default): Builder classes will not be generated for classes which consist of only public mutable members and have a zero-arg constructor<br /> `ALWAYS`: Builder classes will always be generated |
|  `visibility`  | Controls the visibility of generated classes |  `PUBLIC` (default)<br /> `INTERNAL`  |
|  `destinationPackage`  | Specifies the package name for generated classes |  `RELATIVE` (default): Schema classes will be generated in a sub-package relative to your annotated class. By default, the sub-package is named `dynamodbmapper.generatedschemas`, and this is configurable by passing a string parameter<br /> `ABSOLUTE`: Schema classes will be generated in an absolute package relative to the root of your application. By default, the package is named `aws.sdk.kotlin.hll.dynamodbmapper.generatedschemas`, and this is configurable by passing a string parameter. |
|  `generateGetTableExtension`  | Controls whether a `DynamoDbMapper.get${CLASS_NAME}Table` extension method will be generated |  `true` (default)<br /> `false`  |

### Example of code-generation plugin configuration
<a name="_example_of_code_generation_plugin_configuration"></a>

This following example configures the destination package and visibility of the generated schema:

```
// build.gradle.kts

import aws.sdk.kotlin.hll.dynamodbmapper.codegen.annotations.DestinationPackage
import aws.sdk.kotlin.hll.dynamodbmapper.codegen.annotations.Visibility
import aws.smithy.kotlin.runtime.ExperimentalApi

@OptIn(ExperimentalApi::class)
dynamoDbMapper {
    destinationPackage = DestinationPackage.RELATIVE("my.configured.package")
    visibility = Visibility.INTERNAL
}
```

## Annotate classes
<a name="ddb-mapper-anno-schema-gen-annotate"></a>

The schema generator looks for class annotations to determine which classes to generate schemas for. To opt in to generating schemas, annotate your classes with `@DynamoDbItem`. You must also annotate a class property which serves as the item’s partition key with the `@DynamoDbPartitionKey` annotation.

The following class definition shows the minimally required annotations for schema generation:

### Example
<a name="_example"></a>

```
@DynamoDbItem
data class Employee(
    @DynamoDbPartitionKey
    val id: Int,

    val name: String,
    val role: String,
)
```

### Class annotations
<a name="ddb-mapper-anno-schema-gen-class-annos"></a>

The following annotations are applied to classes to control schema generation:
+  `@DynamoDbItem`: Specifies that this class/interface describes an item type in a table. All public properties of this type will be mapped to attributes unless they are explicitly ignored. When present, a schema will be generated for this class.
  +  `converterName`: An optional parameter which indicates a custom schema should be used rather than the one created by the schema generator plugin. This is the fully qualified name of the custom `ItemConverter` class. The [Define a custom item converter](#ddb-mapper-anno-schema-custom) section shows an example of creating and using a custom schema.

### Property annotations
<a name="ddb-mapper-anno-schema-gen-prop-annos"></a>

You can apply the following annotations to class properties to control schema generation:
+  `@DynamoDbPartitionKey`: Specifies the partition key for the item.
+  `@DynamoDbSortKey`: Specifies an optional sort key for the item.
+  `@DynamoDbIgnore`: Specifies that this class property should not be converted to/from an Item attribute by the DynamoDB Mapper.
+  `@DynamoDbAttribute`: Specifies an optional custom attribute name for this class property.

## Define a custom item converter
<a name="ddb-mapper-anno-schema-custom"></a>

In some cases, you may want to define a custom item converter for your class. One reason for this would be if your class uses a type that’s not supported by the schema generator plugin. We use the following version of the `Employee` class as an example:

```
import kotlin.uuid.Uuid

@DynamoDbItem
data class Employee(
    @DynamoDbPartitionKey
    var id: Int,

    var name: String,
    var role: String,
    var workstationId: Uuid
)
```

The `Employee` class now uses a `kotlin.uuid.Uuid` type, which is not currently supported by the schema generator. Schema generation fails with an error: `Unsupported attribute type TypeRef(pkg=kotlin.uuid, shortName=Uuid, genericArgs=[], nullable=false)`. This error indicates that the plugin cannot generate an item converter for this class. Therefore, we need to write our own.

To do this, we implement an `ItemConverter` for the class, then modify the `@DynamoDbItem` class annotation by specifying the fully qualified name of the new item converter.

First, we implement a `ValueConverter` for the `kotlin.uuid.Uuid` class:

```
import aws.sdk.kotlin.hll.dynamodbmapper.values.ValueConverter
import aws.sdk.kotlin.services.dynamodb.model.AttributeValue
import kotlin.uuid.Uuid

public val UuidValueConverter = object : ValueConverter<Uuid> {
    override fun convertFrom(to: AttributeValue): Uuid =
        Uuid.parseHex(to.asS())

    override fun convertTo(from: Uuid): AttributeValue =
        AttributeValue.S(from.toHexString())
}
```

Then, we implement an `ItemConverter` for our `Employee` class. The `ItemConverter` uses this new value converter in the attribute descriptor for "workstationId":

```
import aws.sdk.kotlin.hll.dynamodbmapper.items.AttributeDescriptor
import aws.sdk.kotlin.hll.dynamodbmapper.items.ItemConverter
import aws.sdk.kotlin.hll.dynamodbmapper.items.SimpleItemConverter
import aws.sdk.kotlin.hll.dynamodbmapper.values.scalars.IntConverter
import aws.sdk.kotlin.hll.dynamodbmapper.values.scalars.StringConverter

public object MyEmployeeConverter : ItemConverter<Employee> by SimpleItemConverter(
    builderFactory = { Employee() },
    build = { this },
    descriptors = arrayOf(
        AttributeDescriptor(
            "id",
            Employee::id,
            Employee::id::set,
            IntConverter,
        ),
        AttributeDescriptor(
            "name",
            Employee::name,
            Employee::name::set,
            StringConverter,
        ),
        AttributeDescriptor(
            "role",
            Employee::role,
            Employee::role::set,
            StringConverter
        ),
        AttributeDescriptor(
            "workstationId",
            Employee::workstationId,
            Employee::workstationId::set,
            UuidValueConverter
        )
    ),
)
```

Now that we have defined the item converter, we can apply it to our class. We update the `@DynamoDbItem` annotation to reference the item converter by providing the fully-qualified class name as shown in the following:

```
import kotlin.uuid.Uuid

@DynamoDbItem("my.custom.item.converter.MyEmployeeConverter")
data class Employee(
    @DynamoDbPartitionKey
    var id: Int,

    var name: String,
    var role: String,
    var workstationId: Uuid
)
```

Finally we can begin using the class with DynamoDB Mapper.
