---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-v1-xspec-migrate.html
---

# V1 Xpec API to V2 Expressions API
<a name="ddb-v1-xspec-migrate"></a>

The Expression Specification (Xspec) API available in V1 that helps create expressions to work with document-oriented data is not available in V2. V2 uses the Expression API, which works with both document-oriented data and object-to-item mapped data.

|  | V1 | V2 |
| --- | --- | --- |
| API name | Expression Specification (Xspec) API | Expression API |
| Works with | Methods of the Document API [Table](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/dynamodbv2/document/Table.html) class such as [updateItem](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/dynamodbv2/document/Table.html#updateItem-java.lang.String-java.lang.Object-com.amazonaws.services.dynamodbv2.xspec.UpdateItemExpressionSpec-) and [scan](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/dynamodbv2/document/Table.html#scan-com.amazonaws.services.dynamodbv2.xspec.ScanExpressionSpec-) | Both APIs of DynamoDB Enhanced Client:1.  methods of the object-to-item mapping API <br />2.  methods of the Enhanced Document API for working with document-oriented data (JSON) <br />For both types of APIs, after you have acquired a [`DynamoDbTable`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/DynamoDbTable.html) instance:+  From a [`BeanTableSchema`, for instance, for the object-to-item mapping API](ddb-en-client-getting-started-dynamodbTable.md#ddb-en-client-getting-started-dynamodbTable-table) <br />+  From a [`DocumentTableSchema` for the document-oriented API](ddb-en-client-doc-api-steps.md#ddb-en-client-doc-api-steps-createschema) <br />you use expressions in `DynamoDbTable` methods when you create request objects. For example in the `filterExpression` method of the [`QueryEnhancedRequest.Builder`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/model/QueryEnhancedRequest.Builder.html) |
| Resources |  +  [Xpec initial release blog post](https://aws.amazon.com/blogs/developer/dynamodb-xspec-api/) <br />+  [API reference](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/dynamodbv2/xspec/package-summary.html)   | [Expressions information](ddb-en-client-expressions.md) in this Java Developer Guide |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
