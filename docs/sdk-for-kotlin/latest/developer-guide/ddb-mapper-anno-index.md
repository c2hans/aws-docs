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
|  `@DynamoDbIgnore`  | Property |  *(none)*  | Excludes the property from mapping; it’s neither written nor read. |
|  `@DynamoDbItem`  | Class |  `converter: KClass<out ItemConverter<*>>` (defaults to an auto-generated converter) | Marks a class as a mapped item type. All public properties are mapped unless ignored. |
|  `@DynamoDbPartitionKey`  | Property |  *(none)*  | Marks the property as the partition key. Every top-level item type must have exactly one. |
|  `@DynamoDbSortKey`  | Property |  *(none)*  | Marks the property as the sort key. A top-level item type can have at most one. |
|  `@DynamoDbTtlSeconds`  | Property |  `lifetime: Long`  | Marks a property used to track the item’s time-to-live (TTL), with the given `lifetime` in seconds. See [Built-in features](ddb-mapper-builtins.md) for runtime behavior. |

## Opt-in annotations
<a name="ddb-mapper-anno-index-optin"></a>

The following annotation is not a schema annotation; it gates an opt-in API surface.
+  ** `@ManualPagination` ** (`aws.sdk.kotlin.hll.dynamodbmapper.annotations`): a [`@RequiresOptIn`](https://kotlinlang.org/docs/opt-in-requirements.html) marker on the non-paginating [`query`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.operations/index.html) and [`scan`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.operations/index.html) operations. Opt in at the call site with `@OptIn(ManualPagination::class)` when you need to manage pagination tokens yourself. See [Manual pagination](ddb-mapper-operations.md#ddb-mapper-operations-manual-pagination) in the Operations overview.

## Related topics
<a name="ddb-mapper-anno-index-related"></a>
+  [Generate a schema from annotations](ddb-mapper-anno-schema-gen.md): how the annotations are used.
+  [Manually define schemas](ddb-mapper-code-schemas.md): the converter and key types the annotations stand in for.
+  [Built-in features (TTL, atomic counters)](ddb-mapper-builtins.md): runtime behavior of `@DynamoDbCounter` and `@DynamoDbTtlSeconds`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
