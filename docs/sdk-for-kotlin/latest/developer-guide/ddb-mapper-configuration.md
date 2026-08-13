---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper-configuration.html
---

# Configure DynamoDB Mapper
<a name="ddb-mapper-configuration"></a>

You configure a [`DynamoDbMapper`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper/-dynamo-db-mapper/index.html) by passing a configuration block when you create it. The primary configuration mechanism is **interceptors**, which are objects that hook into the mapper’s request pipeline to observe or modify operations as they run.

```
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbMapper

val mapper = DynamoDbMapper(client) {
    interceptors += LoggingInterceptor()
}
```

The mapper’s [built-in features](ddb-mapper-builtins.md) (TTL and atomic counters) are themselves implemented as interceptors that are registered by default, so adding your own with `+=` augments that default set rather than replacing it.

## The request pipeline
<a name="ddb-mapper-configuration-pipeline"></a>

Every mapper operation flows through a five-step pipeline:

1.  **Initialization**: set up the operation and gather initial context.

1.  **Serialization**: convert the high-level request (and your objects) into a low-level request (and DynamoDB items).

1.  **Low-level invocation**: call the underlying [`DynamoDbClient`](/sdk-for-kotlin/api/latest/dynamodb/aws.sdk.kotlin.services.dynamodb/-dynamo-db-client/index.html).

1.  **Deserialization**: convert the low-level response (and DynamoDB items) into a high-level response (and your objects).

1.  **Completion**: finalize the high-level response or exception to return to the caller.

## Hooks
<a name="ddb-mapper-configuration-hooks"></a>

An interceptor exposes **hooks** that run before or after pipeline steps. Hooks come in two kinds:
+  **Read-only hooks** observe an operation without changing it. They are useful for logging, metrics, and debugging. They run before and after each step and return nothing.
+  **Modify hooks** can change the request or response in flight. They run before each step and return the (possibly modified) value.

The following table lists the hooks in pipeline execution order:

| Hook | Kind | Runs |
| --- | --- | --- |
|  `readAfterInitialization`  | read-only | after Initialization |
|  `modifyBeforeSerialization`  | modify | before Serialization |
|  `readBeforeSerialization`  | read-only | before Serialization |
|  `readAfterSerialization`  | read-only | after Serialization |
|  `modifyBeforeInvocation`  | modify | before Low-level invocation |
|  `readBeforeInvocation`  | read-only | before Low-level invocation |
|  `readAfterInvocation`  | read-only | after Low-level invocation |
|  `modifyBeforeDeserialization`  | modify | before Deserialization |
|  `readBeforeDeserialization`  | read-only | before Deserialization |
|  `readAfterDeserialization`  | read-only | after Deserialization |
|  `modifyBeforeCompletion`  | modify | before Completion |
|  `readBeforeCompletion`  | read-only | before Completion |

All hooks have default no-op implementations, so an interceptor overrides only the hooks it needs.

### Execution order
<a name="ddb-mapper-configuration-execution-order"></a>

When multiple interceptors are registered, the order they appear in `interceptors` determines execution order:
+ For phases **before** the low-level invocation, hooks run in registration order.
+ For phases **after** the low-level invocation, hooks run in reverse registration order.

This mirrors a nested call stack: each interceptor "wraps" the ones registered after it.

## Write an interceptor
<a name="ddb-mapper-configuration-write"></a>

Implement `InterceptorAny` (a type alias for an interceptor over any item, request, and response types) and override the hooks you care about. This read-only interceptor logs each operation as it enters the pipeline and just before the service call:

```
import aws.sdk.kotlin.hll.dynamodbmapper.items.ItemSchema
import aws.sdk.kotlin.hll.dynamodbmapper.pipeline.HReqContext
import aws.sdk.kotlin.hll.dynamodbmapper.pipeline.InterceptorAny
import aws.sdk.kotlin.hll.dynamodbmapper.pipeline.LReqContext

class LoggingInterceptor : InterceptorAny {
    override fun readAfterInitialization(ctx: HReqContext<Any, ItemSchema<Any>, Any>) {
        println("Starting operation for request: ${ctx.highLevelRequest}")
    }

    override fun readBeforeInvocation(ctx: LReqContext<Any, ItemSchema<Any>, Any, Any>) {
        println("Calling DynamoDB: ${ctx.lowLevelRequest}")
    }
}
```

Each hook receives a **context** object that exposes the state available at that point in the pipeline. For example, `highLevelRequest` is available early on, and `lowLevelRequest` is available once serialization has produced it. A modify hook returns the value it wants to pass downstream (the relevant part of the context), while a read-only hook returns nothing.

## Register interceptors
<a name="ddb-mapper-configuration-register"></a>

Add interceptors in the configuration block when creating the mapper:

```
val mapper = DynamoDbMapper(client) {
    interceptors += LoggingInterceptor()
}
```

Using `+=` preserves the default interceptors that power TTL and atomic counters. Assigning the `interceptors` list outright replaces them, which disables those built-in features. Prefer `+=` unless you intend to remove the defaults.

## Related topics
<a name="ddb-mapper-configuration-related"></a>
+  [Built-in features (TTL, atomic counters)](ddb-mapper-builtins.md): features implemented as default interceptors.
+  [Get started with DynamoDB Mapper](ddb-mapper-get-started.md): creating a mapper.
