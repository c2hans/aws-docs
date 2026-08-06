---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper.html
---

# Map classes to DynamoDB items by using the DynamoDB Mapper
<a name="ddb-mapper"></a>

DynamoDB Mapper is a high-level library that maps your Kotlin classes to Amazon DynamoDB tables and indexes, similar to the AWS SDK for Java’s [DynamoDB Enhanced Client](/sdk-for-java/latest/developer-guide/dynamodb-enhanced-client.html) or the AWS SDK for .NET’s [Object Persistence Model](/amazondynamodb/latest/developerguide/DotNetSDKHighLevel.html).

You define schemas that describe your data objects and how to convert them to DynamoDB items. After you define a schema, DynamoDB Mapper provides an intuitive, idiomatic Kotlin interface to use your objects in create, read, update, and delete (CRUD) operations on your tables and indexes.

DynamoDB Mapper supports the following:
+  **Single-item operations** on a table, such as `deleteItem`, `getItem`, `putItem`, `queryPaginated`, `scanPaginated`, and `updateItem`, invoked with a coroutine-friendly DSL.
+  **Batch operations** (`batchGetItem` and `batchWriteItem`) that read or write many items, across one or more tables, in a single call.
+  **Transactional operations** (`transactGetItems` and `transactWriteItems`) that read or write across multiple tables atomically.
+  **Two ways to define schemas:** generate them automatically from annotated classes at build time, or define them manually in code for full control.
+  **Idiomatic Kotlin:** suspending operations, `Flow`-based pagination, and DSLs for keys, filter expressions, and update expressions.

DynamoDB Mapper uses the SDK’s low-level [/sdk-for-kotlin/api/latest/dynamodb/aws.sdk.kotlin.services.dynamodb/-dynamo-db-client/index.html](/sdk-for-kotlin/api/latest/dynamodb/aws.sdk.kotlin.services.dynamodb/-dynamo-db-client/index.html) for its underlying calls to the service.

**Topics**
+ [Get started](ddb-mapper-get-started.md)
+ [Operations overview](ddb-mapper-operations.md)
+ [Batch operations](ddb-mapper-batch.md)
+ [Transactional operations](ddb-mapper-transactions.md)
+ [Generate schemas](ddb-mapper-anno-schema-gen.md)
+ [Manual schemas](ddb-mapper-code-schemas.md)
+ [Secondary indexes](ddb-mapper-secondary-indexes.md)
+ [Expressions](ddb-mapper-expressions.md)
+ [Configuration](ddb-mapper-configuration.md)
+ [Built-in features](ddb-mapper-builtins.md)
+ [Annotations reference](ddb-mapper-anno-index.md)
