---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-v1-xspec-migrate.html
---

# V1 Xpec API to V2 Expressions API
<a name="ddb-v1-xspec-migrate"></a>

The Expression Specification (Xspec) API available in V1 that helps create expressions to work with document-oriented data is not available in V2. V2 uses the Expression API, which works with both document-oriented data and object-to-item mapped data.

****

|  | V1 | V2 |
| --- | --- | --- |
| API name | Expression Specification (Xspec) API | Expression API |
| Works with | Methods of the Document API [Table](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/dynamodbv2/document/Table.html) class such as [updateItem](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/dynamodbv2/document/Table.html#updateItem-java.lang.String-java.lang.Object-com.amazonaws.services.dynamodbv2.xspec.UpdateItemExpressionSpec-) and [scan](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/dynamodbv2/document/Table.html#scan-com.amazonaws.services.dynamodbv2.xspec.ScanExpressionSpec-) | Both APIs of DynamoDB Enhanced Client:[See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-v1-xspec-migrate.html)<br />For both types of APIs, after you have acquired a [https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/DynamoDbTable.html](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/DynamoDbTable.html) instance:[See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-v1-xspec-migrate.html)<br />you use expressions in `DynamoDbTable` methods when you create request objects. For example in the `filterExpression` method of the [https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/model/QueryEnhancedRequest.Builder.html](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/model/QueryEnhancedRequest.Builder.html) |
| Resources |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-v1-xspec-migrate.html)  | [Expressions information](ddb-en-client-expressions.md) in this Java Developer Guide |
