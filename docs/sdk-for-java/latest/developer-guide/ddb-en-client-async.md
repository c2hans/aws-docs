---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-async.html
---

# Use the DynamoDB Enhanced Client API asynchronously
<a name="ddb-en-client-async"></a>

If your application requires non-blocking, asynchronous calls to DynamoDB, you can use the [DynamoDbEnhancedAsyncClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/DynamoDbEnhancedAsyncClient.html). It's similar to the synchronous implementation but with the following key differences:

1. When you build the `DynamoDbEnhancedAsyncClient`, you must provide the asynchronous version of the standard client, `DynamoDbAsyncClient`, as shown in the following snippet.

   ```
    DynamoDbEnhancedAsyncClient enhancedClient =
        DynamoDbEnhancedAsyncClient.builder()
                                   .dynamoDbClient(dynamoDbAsyncClient)
                                   .build();
   ```

1. Methods that return a single data object return a `CompletableFuture` of the result instead of only the result. Your application can then do other work without having to block on the result. The following snippet shows the asynchronous `getItem()` method.

   ```
   CompletableFuture<Customer> result = customerDynamoDbTable.getItem(customer);
   // Perform other work here.
   return result.join();   // Now block and wait for the result.
   ```

1. Methods that return paginated lists of results return an [`SdkPublisher`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/async/SdkPublisher.html) instead of an [`SdkIterable`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/pagination/sync/SdkIterable.html) that the synchronous `DynamoDbEnhanceClient` returns for the same methods. Your application can then subscribe a handler to that publisher to deal with the results asynchronously without having to block.

   ```
   PagePublisher<Customer> results = customerDynamoDbTable.query(r -> r.queryConditional(keyEqualTo(k -> k.partitionValue("Smith"))));
   results.subscribe(myCustomerResultsProcessor);
   // Perform other work and let the processor handle the results asynchronously.
   ```

   For a more complete example of working with the `SdkPublisher API`, see [the example](ddb-en-client-use-multirecord.md#ddb-en-client-use-multirecord-scan-async) in the section that discusses the asynchronous `scan()` method of this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
