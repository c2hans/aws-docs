---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper-configuration.html
---

# Configure DynamoDB Mapper
<a name="ddb-mapper-configuration"></a>

**Important**
DynamoDB Mapper is a Developer Preview release. It is not feature complete and is subject to change.

DynamoDB Mapper offers configuration options that you can use customize the behavior of the library to fit your application.

## Use interceptors
<a name="ddb-mapper-interceptors"></a>

The DynamoDB Mapper library defines hooks that you can tap into at critical stages of the mapper’s request pipeline. You can implement the `Interceptor` interface to implement hooks to observe or modify the mapper process.

You can register one or more interceptors on a single DynamoDB Mapper as a configuration option. See the [example](#ddb-mapper-interceptors-hooks-example-conf) at the end of this section for how you register an interceptor.

### Understand the request pipeline
<a name="ddb-mapper-interceptors-pipeline"></a>

The mapper’s request pipeline consist of the following 5 steps:

1.  **Initialization:** Set up the operation and gathering initial context.

1.  **Serialization:** Convert high-level request objects into low-level request objects. This step converts high-level Kotlin objects into DynamoDB items that consist of attribute names and values.

1.  **Low-level invocation:** Execute a request on the underlying DynamoDB client.

1.  **Deserialization:** Convert low-level response objects into high-level response objects. This step includes converting DynamoDB items that consist of attribute names and values into high-level Kotlin objects.

1.  **Completion:** Finalize the high-level response to return to the caller. If an exception was thrown during the execution of the pipeline, this step finalizes the exception that is thrown to the caller.

### Hooks
<a name="ddb-mapper-interceptors-hooks"></a>

Hooks are interceptor methods that the mapper invokes before or after specific steps in the pipeline. There are two variants of hooks: *read-only* and *modify* (or read-write). For example, `readBeforeInvocation` is a read-only hook that the mapper executes in the phase before the low-level invocation step.

#### Read-only hooks
<a name="ddb-mapper-interceptors-hooks-ro"></a>

The mapper invokes read-only hooks before and after each step in the pipeline (except before the *Initialization* step and after the *Completion* step). Read-only hoods offer a read-only view of a high-level operation in progress. They provide a mechanism to examine the state of an operation for logging, debugging, collecting metrics, for example. Each read-only hook receives a context argument and returns `Unit`.

The mapper catches any exception that is thrown during a read-only hook and adds it to the context. It then passes the context with the exception to subsequent interceptor hooks in the same phase. The mapper throws any exception to the caller only after it calls the last interceptor’s read-only hook for the same phase. For example, if a mapper is configured with two interceptors `A` and `B`, and `A’s `readAfterSerialization` hook throws an exception, the mapper adds the exception to the context passed to `B’s `readAfterSerialization` hook. After `B’s `readAfterSerialization` hook has completed, the mapper throws the exception back to the caller.

#### Modify hooks
<a name="ddb-mapper-interceptors-hooks-modify"></a>

The mapper invokes modify hooks before each step in the pipeline (except before *Initialization* ). Modify hooks offer the ability to see and modify a high-level operation in progress. They can be used to customize behavior and data in ways that mapper configuration and item schemas do not. Each modify hook receives a context argument and returns some subset of that context as a result—either modified by the hook or passed-through from the input context.

If the mapper catches any exception while it executes a modify hook, it doesn’t execute any other interceptors' modify hooks in the same phase. The mapper adds the exception to the context and passes it to the next read-only hook. The mapper throws any exception to the caller only after it calls the last interceptors' read-only hook for the same phase. For example, if a mapper is configured with two interceptors `A` and `B`, and `A’s `modifyBeforeSerialization` hook throws an exception, `B’s `modifyBeforeSerialization` hook will not be invoked. Interceptors `A’s and `B'` s `readAfterSerialization` hook will execute, after which the exception will be thrown back to the caller.

#### Execution order
<a name="ddb-mapper-interceptors-hooks-ex-order"></a>

The order in which interceptors are defined in a mapper’s configuration determines the order that the mapper calls the hooks:
+ For phases *before* the *Low-level invocation* step, it executes hooks in the *same order* that they were added in the configuration.
+ For phases *after* the *Low-level invocation* step, it executes hooks in the *reverse order* from the order they were added in the configuration.

The following diagram shows the execution order of hook methods:

![Flowchart of interceptor hook methods.](http://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/images/KotlinDevGuide-dynamodbMapper-hook-flowchart.png)

##### Text description of the execution order of hook methods
<a name="_text_description_of_the_execution_order_of_hook_methods"></a>

A mapper executes an interceptor’s hooks in the following order:

1. DynamoDB Mapper invokes a high-level request

1. Read before execution

1. Modify before serialization

1. Read before serialization

1. DynamoDB Mapper converts objects to items

1. Read after serialization

1. Modify before invocation

1. Read before invocation

1. DynamoDB Mapper invokes the low-level operation

1. Read after invocation

1. Modify before deserialization

1. Read before deserialization

1. DynamoDB Mapper converts items to objects

1. Read after deserialization

1. Modify before completion

1. Read after execution

1. DynamoDB Mapper returns a high-level response

#### Example configuration
<a name="ddb-mapper-interceptors-hooks-example-conf"></a>

The following example shows how to configure an interceptor on a `DynamoDbMapper` instance:

```
import aws.sdk.kotlin.hll.dynamodbmapper.DynamoDbMapper
import aws.sdk.kotlin.hll.dynamodbmapper.operations.ScanRequest
import aws.sdk.kotlin.hll.dynamodbmapper.operations.ScanResponse
import aws.sdk.kotlin.hll.dynamodbmapper.pipeline.Interceptor
import aws.sdk.kotlin.services.dynamodb.DynamoDbClient
import aws.sdk.kotlin.services.dynamodb.model.ScanRequest as LowLevelScanRequest
import aws.sdk.kotlin.services.dynamodb.model.ScanResponse as LowLevelScanResponse

val printingInterceptor = object : Interceptor<User, ScanRequest<User>, LowLevelScanRequest, LowLevelScanResponse, ScanResponse<User>> {
    override fun readBeforeDeserialization(ctx: LResContext<User, ScanRequest<User>, LowLevelScanRequest, LowLevelScanResponse>) {
        println("Scan response contains ${ctx.lowLevelResponse.count} items.")
    }
}

val client = DynamoDbClient.fromEnvironment()

val mapper = DynamoDbMapper(client) {
    interceptors += printingInterceptor
}
```
