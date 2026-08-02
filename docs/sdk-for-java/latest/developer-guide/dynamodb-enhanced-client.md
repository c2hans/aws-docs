---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-enhanced-client.html
---

# Map Java objects to DynamoDB items with the AWS SDK for Java 2.x
<a name="dynamodb-enhanced-client"></a>

The [DynamoDB Enhanced Client API](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/package-summary.html) is a high-level library that is the successor to the `DynamoDBMapper` class of in the SDK for Java v1.x. It offers a straightforward way to map client-side classes to DynamoDB tables. You define the relationships between tables and their corresponding data classes in your code. After you define those relationships, you can intuitively perform various create, read, update, or delete (CRUD) operations on tables or items in DynamoDB.

The DynamoDB Enhanced Client API also includes the [Enhanced Document API](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/document/package-summary.html) that enables you to work with document-type items that do not follow a defined schema.

**Topics**
+ [Get Started using the DynamoDB Enhanced Client API](ddb-en-client-getting-started.md)
+ [Learn the basics of the DynamoDB Enhanced Client API](ddb-en-client-use.md)
+ [Use advanced mapping features](ddb-en-client-adv-features.md)
+ [Work with JSON documents with the Enhanced Document API for DynamoDB](ddb-en-client-doc-api.md)
+ [Use extensions to customize DynamoDB Enhanced Client operations](ddb-en-client-extensions.md)
+ [Use the DynamoDB Enhanced Client API asynchronously](ddb-en-client-async.md)
+ [Data class annotations](ddb-en-client-anno-index.md)
