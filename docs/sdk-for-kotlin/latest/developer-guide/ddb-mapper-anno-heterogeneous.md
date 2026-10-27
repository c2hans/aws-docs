---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper-anno-heterogeneous.html
---

# Map heterogeneous types with annotations
<a name="ddb-mapper-anno-heterogeneous"></a>

A single DynamoDB table or attribute often holds items of several different shapes. For example, a table of vehicles may store cars, bikes, and trucks, each with its own attributes, or a single-table design may store users and orders side by side. DynamoDB Mapper handles these with a **heterogeneous family**: a base type plus a set of registered subtypes, distinguished by a string **type attribute** stored with every item.

You declare a family with two annotations, and the schema-generator plugin builds the family’s [`HeterogeneousItemConverter`](ddb-mapper-code-schemas.md#ddb-mapper-code-schemas-heterogeneous) for you:
+  `@DynamoDbHeterogeneousType` on the family’s base type names the type attribute.
+  `@DynamoDbSubtype` on each member type gives the type name stored in that attribute.

This topic assumes you’re familiar with [generating schemas from annotations](ddb-mapper-anno-schema-gen.md). For the full list of parameters, see the [annotations reference](ddb-mapper-anno-index.md).

## Declare a family
<a name="ddb-mapper-anno-heterogeneous-sealed"></a>

The following example declares a family based on the sealed interface `Vehicle`. Because the base also carries `@DynamoDbItem`, the family describes a table item:

```
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbHeterogeneousType
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbItem
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbPartitionKey
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbSubtype

@DynamoDbItem
@DynamoDbHeterogeneousType(typeAttribute = "type")
sealed interface Vehicle {
    @DynamoDbPartitionKey
    val id: Int
    val manufacturer: String
}

@DynamoDbSubtype("car")
data class Car(override val id: Int, override val manufacturer: String, val model: String) : Vehicle

@DynamoDbSubtype("bike")
data class Bike(override val id: Int, override val manufacturer: String, val gears: Int) : Vehicle

@DynamoDbSubtype("unicycle")
data object Unicycle : Vehicle {
    override val id = 0
    override val manufacturer = "Generic"
}
```

The plugin generates a `VehicleSchema` object and a `getVehicleTable` extension, just as it does for an ordinary `@DynamoDbItem` class. The resulting table reads and writes any `Vehicle`:

```
val vehicles = mapper.getVehicleTable("vehicles")

vehicles.putItem { item = Car(1, "Ford", "Model T") }
vehicles.putItem { item = Bike(2, "Schwinn", 10) }

when (val vehicle = vehicles.getItem(1).item) {
    is Car -> println("Car: ${vehicle.model}")
    is Bike -> println("Bike with ${vehicle.gears} gears")
    else -> println("Other vehicle: $vehicle")
}
```

Each item is stored with only the attributes of its own subtype, plus the type attribute:

| id | type | manufacturer | model | gears |
| --- | --- | --- | --- | --- |
| 1 |  `car`  | Ford | Model T |  |
| 2 |  `bike`  | Schwinn |  | 10 |

Keep the following in mind when you declare a family:
+  **Type names are required and permanent.** The type name is stored with every item and used to choose a subtype when reading, so renaming a class is safe but changing its type name orphans existing data. Type names must be non-blank and unique within a family.
+  **Every subtype is mappable.** `@DynamoDbSubtype` implies `@DynamoDbMappable`, so you don’t need to add it. Classes, data classes, and `object`/`data object` declarations are all supported.
+  **A type belongs to one family.** A subtype can’t be registered in more than one family.
+  **The type attribute is reserved.** It’s a compile error for a member to have a property mapped to the same attribute name.
+  **Unknown types fail on read.** Reading an item whose type attribute is missing, isn’t a string, or has an unregistered value throws `IllegalArgumentException`.
+  **Sealed families must be complete.** In a sealed hierarchy, it’s a compile error for a concrete subtype not to be covered by any registration.

## Declare keys
<a name="ddb-mapper-anno-heterogeneous-keys"></a>

A table family needs a single primary key that every member agrees on. You can declare the key properties in any of the following ways:
+  **On the base,** as in the preceding `Vehicle` example. Subtypes that override `id` inherit its `@DynamoDbPartitionKey` annotation.
+  **On each subtype,** which is required when the base has no properties to annotate (see [Group unrelated types into an ad-hoc family](#ddb-mapper-anno-heterogeneous-ad-hoc)).
+  **On both,** such as a partition key on the base and a sort key on each subtype.

Whichever way you choose, every member must end up with the same key attribute names and types. A mismatch, for example a `String` partition key on one subtype and an `Int` partition key on another, is a compile error.

 `@DynamoDbTtlSeconds` and `@DynamoDbCounter` follow the same rule. DynamoDB Mapper sets TTL and counter attributes on every item that it writes through a table, whatever the item’s subtype. So every member must declare the same TTL attributes, with the same lifetimes, and the same counter attributes. Declare them on the base, or on each subtype. A TTL or counter attribute that only some members declare is a compile error. For more information about these annotations, see [Built-in features](ddb-mapper-builtins.md).

## Control how objects match a subtype
<a name="ddb-mapper-anno-heterogeneous-match"></a>

When you write an object, DynamoDB Mapper chooses the registration that matches it. The `match` parameter of `@DynamoDbSubtype` controls how a registration matches:
+  `DynamoDbSubtypeMatch.EXACT_TYPE` (the default) matches only objects whose class is exactly the annotated class. Because no object’s class is exactly an interface or abstract class, using `EXACT_TYPE` on one is a compile error.
+  `DynamoDbSubtypeMatch.INSTANCE_OF` matches objects of the annotated class or any of its subclasses.

When an object matches more than one registration, the most specific type always wins, regardless of the order in which the classes are declared. In the following example, from the `Animal` family described in [Use open and abstract base types](#ddb-mapper-anno-heterogeneous-open), a `Puppy` is stored as `puppy`, and any other `Dog` (including an unregistered subclass such as `Poodle`) is stored as `dog`:

```
@DynamoDbSubtype("dog", match = DynamoDbSubtypeMatch.INSTANCE_OF)
open class Dog(var breed: String = "") : Animal()

@DynamoDbSubtype("puppy")
class Puppy(var ageWeeks: Int = 0) : Dog()

class Poodle : Dog()
```

**Important**
An object stored under an `INSTANCE_OF` registration is written and read back using that registration’s converter. In the preceding example, a `Poodle` is read back as a `Dog`, and any properties `Poodle` declares beyond those of `Dog` aren’t stored.

### Multi-level hierarchies
<a name="ddb-mapper-anno-heterogeneous-multi-level"></a>

Intermediate types in a hierarchy take part in a family only if they’re annotated:
+  **An unannotated intermediate type is ignored.** Its annotated descendants are registered directly in the family.
+  **An annotated intermediate type is registered as a whole.** An abstract or sealed intermediate type must use `INSTANCE_OF`, and must either supply its own `converter` or be a family itself, with its own type attribute.

In the following example, `TwoWheeler` is unannotated, so `Bike` is registered directly in `Vehicle`. `Truck` is registered in `Vehicle` under the type name `truck`, and is itself a family whose members are distinguished by `truckType`:

```
// Unannotated, so ignored by the Vehicle family
sealed interface TwoWheeler : Vehicle

@DynamoDbSubtype("bike")
data class Bike(override val id: Int, override val manufacturer: String, val gears: Int) : TwoWheeler

@DynamoDbSubtype("truck", match = DynamoDbSubtypeMatch.INSTANCE_OF)
@DynamoDbHeterogeneousType(typeAttribute = "truckType")
sealed class Truck : Vehicle

@DynamoDbSubtype("pickup")
data class Pickup(override val id: Int, override val manufacturer: String, val bedLength: Int) : Truck()

@DynamoDbSubtype("flatbed")
data class Flatbed(override val id: Int, override val manufacturer: String, val deckLength: Int) : Truck()
```

A `Pickup` is stored with both type attributes: `type` is `truck` and `truckType` is `pickup`.

## Use open and abstract base types
<a name="ddb-mapper-anno-heterogeneous-open"></a>

The base of a family doesn’t need to be sealed. Interfaces, abstract classes, and open classes are all supported. Because the plugin can’t know every subclass of an unsealed base, writing an object that matches no registration throws `IllegalArgumentException`.

An open concrete base can also register its own instances by setting `baseTypeName`. The plugin then generates a converter for the base’s own properties, and registers it after every subtype. With the default `baseMatch = DynamoDbSubtypeMatch.EXACT_TYPE`, the base registration matches only objects whose class is exactly the base, and writing an unregistered subclass throws `IllegalArgumentException`.

To have the base registration catch any subclass that no other registration matches, set `baseMatch = DynamoDbSubtypeMatch.INSTANCE_OF`:

```
@DynamoDbHeterogeneousType(typeAttribute = "kind", baseTypeName = "animal", baseMatch = DynamoDbSubtypeMatch.INSTANCE_OF)
open class Animal(var name: String = "")

@DynamoDbSubtype("dog", match = DynamoDbSubtypeMatch.INSTANCE_OF)
open class Dog(var breed: String = "") : Animal()

// Unregistered, so stored as "animal" with only the properties of Animal
class Cat(var indoor: Boolean = false) : Animal()
```

## Group unrelated types into an ad-hoc family
<a name="ddb-mapper-anno-heterogeneous-ad-hoc"></a>

Some designs, such as [single-table designs](/amazondynamodb/latest/developerguide/bp-general-nosql-design.html), store unrelated classes in one table. These classes share no common supertype other than `Any`. To group them, annotate an `object` with `@DynamoDbHeterogeneousType`. The object only names the family. Each member must name it explicitly with `parent`, and declares its own key properties:

```
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbHeterogeneousType
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbItem
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbPartitionKey
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbSortKey
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbSubtype

@DynamoDbItem
@DynamoDbHeterogeneousType(typeAttribute = "entityType")
object Entities

@DynamoDbSubtype("user", parent = Entities::class)
data class UserEntity(
    @DynamoDbPartitionKey val pk: String,
    @DynamoDbSortKey val sk: String,
    val name: String,
)

@DynamoDbSubtype("order", parent = Entities::class)
data class OrderEntity(
    @DynamoDbPartitionKey val pk: String,
    @DynamoDbSortKey val sk: String,
    val totalCents: Long,
)
```

The generated `getEntitiesTable` extension returns a table whose items are typed as `Any`. Use `is` checks or `when` to work with the specific types you read.

## Use a family as a nested attribute
<a name="ddb-mapper-anno-heterogeneous-nested"></a>

A family can be used as the type of a property in another mapped class, including inside collections and as a nullable type. The family’s base doesn’t need `@DynamoDbItem` for this; without it, the family can be used only as a nested attribute. Each value is stored as a map that includes the type attribute:

```
@DynamoDbItem
data class Garage(
    @DynamoDbPartitionKey val name: String,
    val vehicles: List<Vehicle>,
    val favorite: Vehicle?,
)
```

The plugin can’t infer an ad-hoc family from a property of type `Any`. Annotate such properties with `@DynamoDbHeterogeneousAttribute` and name the family’s object. The annotation applies to each family value in the property, including the elements of a list or the values of a map:

```
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbHeterogeneousAttribute
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbMappable

@DynamoDbMappable
data class AuditRecord(
    @DynamoDbHeterogeneousAttribute(Entities::class) val entity: Any,
    @DynamoDbHeterogeneousAttribute(Entities::class) val related: List<Any>,
)
```

 `@DynamoDbHeterogeneousAttribute` can’t be combined with `@DynamoDbAttributeConverter` on the same property. For families with a common base type, such as `Vehicle`, the annotation is optional.

## Supply a custom converter for a subtype
<a name="ddb-mapper-anno-heterogeneous-custom"></a>

To control how a single subtype is converted, pass your own [`ItemConverter`](ddb-mapper-code-schemas.md#ddb-mapper-code-schemas-item-converters) with the `converter` parameter, as you would with `@DynamoDbItem(converter = …​)`. The family’s converter still writes and reads the type attribute, so your converter must not write that attribute itself:

```
@DynamoDbSubtype("car", converter = CustomCarConverter::class)
data class Car(override val id: Int, override val manufacturer: String, val model: String) : Vehicle
```

## Limitations
<a name="ddb-mapper-anno-heterogeneous-limits"></a>
+ A family’s base and all of its members must be defined in the same module.
+ A family can’t be nested within itself, directly or indirectly. For example, a `Car` with a `Vehicle` property is a compile error.

## Related topics
<a name="ddb-mapper-anno-heterogeneous-related"></a>
+  [Generate a schema from annotations](ddb-mapper-anno-schema-gen.md): the basics of annotation-based schemas.
+  [`HeterogeneousItemConverter`](ddb-mapper-code-schemas.md#ddb-mapper-code-schemas-heterogeneous): build the same converter manually in code.
+  [DynamoDB Mapper annotations reference](ddb-mapper-anno-index.md): every annotation and its parameters.
