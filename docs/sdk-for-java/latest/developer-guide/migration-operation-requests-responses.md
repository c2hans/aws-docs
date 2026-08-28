---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-operation-requests-responses.html
---

# Operations, requests and responses changes
<a name="migration-operation-requests-responses"></a>

In version 2 of the SDK for Java, requests are passed to a client operation. For example `DynamoDbClient's` `PutItemRequest` is passed to `DynamoDbClient.putItem` operation. These operations return a response from the AWS service, such as a `PutItemResponse`.

Version 2 of the SDK for Java has the following changes from version 1.
+ Operations with multiple response pages now have a `Paginator` method for automatically iterating over all items in the response.
+ You cannot mutate requests and responses.
+ You must create requests and responses with a static builder method instead of a constructor. For example, version 1's `new PutItemRequest().withTableName(...)` is now `PutItemRequest.builder().tableName(...).build()`.
+ Operations support a short-hand way to create requests: `dynamoDbClient.putItem(request -> request.tableName(...))`.

The following sections describe specific changes between version 1 and version 2. Some parameter type changes can be converted automatically using the [migration tool](migration-tool.md), while other changes require manual updates to your code.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
