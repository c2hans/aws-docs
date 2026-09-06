---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-mapping.html
---

# DynamoDB mapping API differences between version 1 and version 2 of the AWS SDK for Java
<a name="ddb-mapping"></a>

The DynamoDB mapping APIs changed significantly between version 1 and version 2 of the AWS SDK for Java. In version 1, you use the `DynamoDBMapper` to work with Java POJOs. In version 2, you use the `DynamoDbEnhancedClient` with updated method names, enhanced schema definition options, and improved type safety.

Key differences include:
+ New method names (such as `getItem` instead of `load`)
+ Explicit table schema creation
+ Built-in support for both synchronous and asynchronous operations
+ Changes in how empty strings and configuration are handled

This section covers the mapping API changes, annotation differences, configuration updates, and migration guidance to help you transition from the v1 `DynamoDBMapper` to the v2 `DynamoDbEnhancedClient`.

**Contents**
+ [High-level changes in mapping libraries from version 1 to version 2 of the SDK for Java](dynamodb-mapping-high-level.md)
  + [Import dependency differences](dynamodb-mapping-high-level.md#dynamodb-mapping-deps)
+ [Changes in the DynamoDB mapping APIs between version 1 and version 2 of the SDK for Java](dynamodb-mapping-api-changes.md)
  + [Create a client](dynamodb-mapping-api-changes.md#dynamodb-mapping-api-changes-client)
  + [Establish mapping to DynamoDB table/index](dynamodb-mapping-api-changes.md#dynamodb-mapping-api-changes-mapping)
  + [Table operations](dynamodb-mapping-api-changes.md#dynamodb-mapping-api-changes-tobleops)
  + [Map classes and properties](dynamodb-mapping-api-changes.md#dynamodb-mapping-schemas)
    + [Bean annotations](dynamodb-mapping-api-changes.md#dynamodb-mapping-schemas-annos)
    + [V2 additional annotations](dynamodb-mapping-api-changes.md#dynamodb-mapping-schemas-annos-v2-addnl)
  + [Configuration](dynamodb-mapping-api-changes.md#dynamodb-mapping-configuration)
    + [Per-operation configuration](dynamodb-mapping-api-changes.md#dynamodb-mapping-configuration-per-op)
  + [Conditionals](dynamodb-mapping-api-changes.md#dynamodb-mapping-conditionals)
  + [Type conversion](dynamodb-mapping-api-changes.md#dynamodb-mapping-type-conv)
    + [Default converters](dynamodb-mapping-api-changes.md#dynamodb-mapping-type-conv-defaults)
    + [Set a custom converter for an attribute](dynamodb-mapping-api-changes.md#dynamodb-mapping-type-conv-anno)
    + [Add a type converter factory or provider](dynamodb-mapping-api-changes.md#dynamodb-mapping-type-conv-factory)
+ [String handling differences between version 1 and version 2 of the SDK for Java](dynamodb-migration-string-handling.md)
+ [Optimistic locking differences between version 1 and version 2 of the SDK for Java](dynamodb-migrate-optimstic-locking.md)
+ [Fluent setters differences between version 1 and version 2 of the SDK for Java](dynamodb-migrate-fluent-setters.md)
