---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/dynamodb-examples.html
---

The AWS SDK for JavaScript v2 has reached end-of-support. We recommend that you migrate to [AWS SDK for JavaScript v3](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-javascript-v2/).

# Amazon DynamoDB Examples
<a name="dynamodb-examples"></a>

Amazon DynamoDB is a fully managed NoSQL cloud database that supports both document and key-value store models. You create schemaless tables for data without the need to provision or maintain dedicated database servers.

![Relationship between JavaScript environments, the SDK, and DynamoDB](http://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/images/code-samples-dynamodb.png)

The JavaScript API for DynamoDB is exposed through the `AWS.DynamoDB`, `AWS.DynamoDBStreams`, and `AWS.DynamoDB.DocumentClient` client classes. For more information about using the DynamoDB client classes, see [`Class: AWS.DynamoDB`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/DynamoDB.html), [`Class: AWS.DynamoDBStreams`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/DynamoDBStreams.html), and [`Class: AWS.DynamoDB.DocumentClient`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/DynamoDB/DocumentClient.html) in the API reference.

**Topics**
+ [Creating and Using Tables in DynamoDB](dynamodb-examples-using-tables.md)
+ [Reading and Writing A Single Item in DynamoDB](dynamodb-example-table-read-write.md)
+ [Reading and Writing Items in Batch in DynamoDB](dynamodb-example-table-read-write-batch.md)
+ [Querying and Scanning a DynamoDB Table](dynamodb-example-query-scan.md)
+ [Using the DynamoDB Document Client](dynamodb-example-document-client.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for JavaScript SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-javascript` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
