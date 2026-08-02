---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper.html
---

# Map classes to DynamoDB items by using the DynamoDB Mapper (Developer Preview)
<a name="ddb-mapper"></a>

**Important**
DynamoDB Mapper is a Developer Preview release. It is not feature complete and is subject to change.

DynamoDB Mapper is a high-level library that offers mechanisms to map Kotlin classes to DynamoDB tables and indices, similar to the AWS SDK for Java’s [DynamoDB Enhanced Client](/sdk-for-java/latest/developer-guide/dynamodb-enhanced-client.html) or the AWS SDK for .NET’s [Object Persistence Model](/amazondynamodb/latest/developerguide/DotNetSDKHighLevel.html).

You define schemas that describe your data object and how to convert them to DynamoDB items. After you define the schema, DynamoDB Mapper provides an intuitive interface to use your objects in create, read, update, or delete (CRUD) operations on your tables and indices.

**Topics**
+ [Get started with DynamoDB Mapper](ddb-mapper-get-started.md)
+ [Configure DynamoDB Mapper](ddb-mapper-configuration.md)
+ [Generate a schema from annotations](ddb-mapper-anno-schema-gen.md)
+ [Manually define schemas](ddb-mapper-code-schemas.md)
+ [Use secondary indices with DynamoDB Mapper](ddb-mapper-secondary-indices.md)
+ [Use expressions](ddb-mapper-expressions.md)
