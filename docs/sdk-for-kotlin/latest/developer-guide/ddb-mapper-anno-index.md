---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper-anno-index.html
---

# DynamoDB Mapper annotations reference
<a name="ddb-mapper-anno-index"></a>

This page lists the annotations used to generate schemas from your classes, as described in [Generate a schema from annotations](ddb-mapper-anno-schema-gen.md). Apply them to a class and its properties, then let the schema-generator plugin produce the schema.

All item annotations are in the `aws.sdk.kotlin.hll.dynamodbmapper` package and are provided by the `dynamodb-mapper-annotations` dependency.

## Annotations
<a name="ddb-mapper-anno-index-annotations"></a>

The following table lists the annotations alphabetically.

| Annotation | Applies to | Parameters | Behavior |
| --- | --- | --- | --- |
|  `@DynamoDbAttribute`  | Property |  `name: String`  | Maps the property to a DynamoDB attribute with the given `name` instead of the property name. |
|  `@DynamoDbAttributeConverter`  | Property |  `converter: KClass<out ValueConverter<*>>`  | Uses the specified [`ValueConverter`](ddb-mapper-code-schemas.md#ddb-mapper-code-schemas-value-converters) for this property, for types the generator doesn’t map on its own. |
|  `@DynamoDbCounter`  | Property |  *(none)*  | Marks a numeric property as an atomic counter that increments each time the item is persisted. See [Built-in features](ddb-mapper-builtins.md) for runtime behavior. |
|  `@DynamoDbHeterogeneousAttribute`  | Property |  `family: KClass<*>`  | Converts the property’s values with the converter of the given [heterogeneous family](ddb-mapper-anno-heterogeneous.md), including values inside collections. Required for ad-hoc families, whose values are typed as `Any`. Can’t be combined with `@DynamoDbAttributeConverter`. |
|  `@DynamoDbHeterogeneousType`  | Class, interface, or `object`  |  `typeAttribute: String`, `baseTypeName: String` (defaults to `""`), `baseMatch: DynamoDbSubtypeMatch` (defaults to `EXACT_TYPE`) | Marks the base of a [heterogeneous family](ddb-mapper-anno-heterogeneous.md) whose members are distinguished by the string stored in `typeAttribute`. On an open concrete class, a non-empty `baseTypeName` also registers instances of the base itself. On an `object`, declares an ad-hoc family whose values are typed as `Any`. Combine with `@DynamoDbItem` to make the family a table item. Implies `@DynamoDbMappable`. |
|  `@DynamoDbIgnore`  | Property |  *(none)*  | Excludes the property from mapping; it’s neither written nor read. |
|  `@DynamoDbItem`  | Class |  `converter: KClass<out ItemConverter<*>>` (defaults to an auto-generated converter) | Marks a class as a mapped item type. All public properties are mapped unless ignored. |
|  `@DynamoDbMappable`  | Class or interface |  `converter: KClass<out ItemConverter<*>>` (defaults to an auto-generated converter) | Marks a class as [mappable as a nested attribute](ddb-mapper-anno-schema-gen.md#ddb-mapper-anno-schema-gen-nested) of another class. Doesn’t describe a table item, so key, TTL, and counter annotations aren’t allowed. |
|  `@DynamoDbPartitionKey`  | Property |  *(none)*  | Marks the property as the partition key. Every top-level item type must have exactly one. |
|  `@DynamoDbSortKey`  | Property |  *(none)*  | Marks the property as the sort key. A top-level item type can have at most one. |
|  `@DynamoDbSubtype`  | Class, interface, or `object`  |  `typeName: String`, `match: DynamoDbSubtypeMatch` (defaults to `EXACT_TYPE`), `parent: KClass<*>` (defaults to inferring the family from supertypes), `converter: KClass<out ItemConverter<*>>` (defaults to an auto-generated converter) | Registers the type as a member of a [heterogeneous family](ddb-mapper-anno-heterogeneous.md), stored under `typeName`. `parent` must name the family’s `object` for ad-hoc families. Implies `@DynamoDbMappable`. |
|  `@DynamoDbTtlSeconds`  | Property |  `lifetime: Long`  | Marks a property used to track the item’s time-to-live (TTL), with the given `lifetime` in seconds. See [Built-in features](ddb-mapper-builtins.md) for runtime behavior. |

### `DynamoDbSubtypeMatch`
<a name="ddb-mapper-anno-index-subtype-match"></a>

The `match` parameter of `@DynamoDbSubtype` and the `baseMatch` parameter of `@DynamoDbHeterogeneousType` take one of the following values:
+  `EXACT_TYPE`: matches only objects whose class is exactly the annotated type.
+  `INSTANCE_OF`: matches objects of the annotated type or any of its subtypes.

For details, see [Control how objects match a subtype](ddb-mapper-anno-heterogeneous.md#ddb-mapper-anno-heterogeneous-match).

## Opt-in annotations
<a name="ddb-mapper-anno-index-optin"></a>

The following annotation is not a schema annotation; it gates an opt-in API surface.
+  ** `@ManualPagination` ** (`aws.sdk.kotlin.hll.dynamodbmapper.annotations`): a [`@RequiresOptIn`](https://kotlinlang.org/docs/opt-in-requirements.html) marker on the non-paginating [`query`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.operations/index.html) and [`scan`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.operations/index.html) operations. Opt in at the call site with `@OptIn(ManualPagination::class)` when you need to manage pagination tokens yourself. See [Manual pagination](ddb-mapper-operations.md#ddb-mapper-operations-manual-pagination) in the Operations overview.

## Related topics
<a name="ddb-mapper-anno-index-related"></a>
+  [Generate a schema from annotations](ddb-mapper-anno-schema-gen.md): how the annotations are used.
+  [Map heterogeneous types with annotations](ddb-mapper-anno-heterogeneous.md): how the heterogeneous-family annotations are used.
+  [Manually define schemas](ddb-mapper-code-schemas.md): the converter and key types the annotations stand in for.
+  [Built-in features (TTL, atomic counters)](ddb-mapper-builtins.md): runtime behavior of `@DynamoDbCounter` and `@DynamoDbTtlSeconds`.
