---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-doc-api.html
---

# Work with JSON documents with the Enhanced Document API for DynamoDB
<a name="ddb-en-client-doc-api"></a>

The [Enhanced Document API](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/document/package-summary.html) for AWS SDK for Java 2.x is designed to work with document-oriented data that has no fixed schema. However, it also lets you use custom classes to map individual attributes.

 The Enhanced Document API is the successor to the [Document API](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/dynamodbv2/document/DynamoDB.html) of the AWS SDK for Java v1.x.

**Contents**
+ [Get started using the Enhanced Document API](ddb-en-client-doc-api-steps.md)
  + [Create a `DocumentTableSchema` and a `DynamoDbTable`](ddb-en-client-doc-api-steps.md#ddb-en-client-doc-api-steps-createschema)
+ [Build enhanced documents](ddb-en-client-doc-api-steps-create-ed.md)
  + [Build from a JSON string](ddb-en-client-doc-api-steps-create-ed.md#ddb-en-client-doc-api-steps-create-ed-fromJson)
  + [Build from individual elements](ddb-en-client-doc-api-steps-create-ed.md#ddb-en-client-doc-api-steps-create-ed-fromparts)
+ [Perform CRUD operations](ddb-en-client-doc-api-steps-use.md)
+ [Access enhanced document attributes as custom objects](ddb-en-client-doc-api-convert.md)
+ [Use an `EnhancedDocument` without DynamoDB](ddb-en-client-doc-api-standalone.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
