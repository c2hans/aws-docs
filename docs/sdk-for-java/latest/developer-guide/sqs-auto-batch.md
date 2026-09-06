---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/sqs-auto-batch.html
---

# Use automatic request batching for Amazon SQS with the AWS SDK for Java 2.x
<a name="sqs-auto-batch"></a>

The Automatic Request Batching API for Amazon SQS is a high-level library that provides an efficient way to batch and buffer requests for SQS operations. By using the batching API, you reduce the number of requests to SQS, which improves throughput and minimizes costs.

Because the batch API methods match the `[SqsAsyncClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/SqsAsyncClient.html)` methods—`sendMessage`, `changeMessageVisibility`, `deleteMessage`, `receiveMessage`—you can use the batch API as a drop-in replacement with minimal changes.

This topic gives you an overview of how to configure and work with the Automatic Request Batching API for Amazon SQS.

## Check prerequisites
<a name="sqs-auto-batch-requirements"></a>

You need to use version *2.28.0 *or later of the SDK for Java 2.x to have access to the batching API. Your Maven `pom.xml` should at least contain the following elements.

```
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>software.amazon.awssdk</groupId>
            <artifactId>bom</artifactId>
            <version>{{2.28.231}}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
<dependencies>
    <dependency>
        <groupId>software.amazon.awssdk</groupId>
        <artifactId>sqs</artifactId>
    </dependency>
</dependencies>
```

1 [Latest version](https://central.sonatype.com/artifact/software.amazon.awssdk/bom)

## Create a batch manager
<a name="sqs-auto-batch-create"></a>

The automatic request batching API is implemented by the [SqsAsyncBatchManager](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/batchmanager/SqsAsyncBatchManager.html) interface. You can create an instance of the manager a couple ways.

### Default configuration by using `SqsAsyncClient`
<a name="sqs-batch-manager-create-default"></a>

The simplest way you can create a batch manager is to call the `batchManager` factory method on an existing [SqsAsyncClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/SqsAsyncClient.html) instance. The simple approach is shown in the following snippet.

```
SqsAsyncClient asyncClient = SqsAsyncClient.create();
SqsAsyncBatchManager sqsAsyncBatchManager = asyncClient.batchManager();
```

When you use this approach, the `SqsAsyncBatchManager` instance uses the default values that are shown in the table in the [Override configuration settings for `SqsAsyncBatchManager`](#sqs-auto-batch-config-settings) section. Additionally, the `SqsAsyncBatchManager` instance uses the `ExecutorService` of the `SqsAsyncClient` instance that it was created from.

### Custom configuration by using `SqsAsyncBatchManager.Builder`
<a name="sqs-batch-manager-create-custom"></a>

For more advanced use cases, you can customize the batch manager using the [`SqsAsyncBatchManager.Builder`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/batchmanager/SqsAsyncBatchManager.Builder.html). By using this approach to create a `SqsAsyncBatchManager` instance, you can fine tune the batching behavior. The following snippet shows an example of how to use the builder to customize batching behavior.

```
SqsAsyncBatchManager batchManager = SqsAsyncBatchManager.builder()
    .client(SqsAsyncClient.create())
    .scheduledExecutor(Executors.newScheduledThreadPool(5))
    .overrideConfiguration(b -> b
        .receiveMessageMinWaitDuration(Duration.ofSeconds(10))
        .receiveMessageVisibilityTimeout(Duration.ofSeconds(1))
        .receiveMessageAttributeNames(Collections.singletonList("*"))
        .receiveMessageSystemAttributeNames(Collections.singletonList(MessageSystemAttributeName.ALL)))
    .build();
```

When you use this approach, you can adjust the settings on the `BatchOverrideConfiguration` object that are shown in the table in the [Override configuration settings for `SqsAsyncBatchManager`](#sqs-auto-batch-config-settings) section. You can also provide a custom [`ScheduledExecutorService`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ScheduledExecutorService.html) for the batch manager by using this approach.

## Send messages
<a name="sqs-auto-batch-send"></a>

To send messages with the batch manager, use the `[SqsAsyncBatchManager\#sendMessage](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/batchmanager/SqsAsyncBatchManager.html#sendMessage(software.amazon.awssdk.services.sqs.model.SendMessageRequest))` method. The SDK buffers requests and sends them as a batch when the `maxBatchSize` or `sendRequestFrequency` values are reached.

The following example show a `sendMessage` request immediately following by another request. In this case, the SDK sends both messages in a single batch.

```
// Sending the first message
CompletableFuture<SendMessageResponse> futureOne =
    sqsAsyncBatchManager.sendMessage(r -> r.messageBody("One").queueUrl("queue"));

// Sending the second message
CompletableFuture<SendMessageResponse> futureTwo =
    sqsAsyncBatchManager.sendMessage(r -> r.messageBody("Two").queueUrl("queue"));

// Waiting for both futures to complete and retrieving the responses
SendMessageResponse messageOne = futureOne.join();
SendMessageResponse messageTwo = futureTwo.join();
```

## Change the message visibility timeout
<a name="sqs-auto-batch-change-vis"></a>

You can change the visibility timeout of messages in a batch by using the [`SqsAsyncBatchManager#changeMessageVisibility`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/batchmanager/SqsAsyncBatchManager.html#changeMessageVisibility(java.util.function.Consumer)) method. The SDK buffers requests and sends them as a batch when the `maxBatchSize` or `sendRequestFrequency` values are reached.

The following example shows how to call the `changeMessageVisibility` method.

```
CompletableFuture<ChangeMessageVisibilityResponse> futureOne =
    sqsAsyncBatchManager.changeMessageVisibility(r ->
        r.receiptHandle("receiptHandle")
         .queueUrl("queue"));
ChangeMessageVisibilityResponse response = futureOne.join();
```

## Delete messages
<a name="sqs-auto-batch-delete"></a>

You can delete messages in a batch using the [`SqsAsyncBatchManager#deleteMessage`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/batchmanager/SqsAsyncBatchManager.html#deleteMessage(java.util.function.Consumer)) method. The SDK buffers requests and sends them as a batch when the `maxBatchSize` or `sendRequestFrequency` values are reached.

The following example shows how you can call the `deleteMessage` method.

```
CompletableFuture<DeleteMessageResponse> futureOne =
    sqsAsyncBatchManager.deleteMessage(r ->
        r.receiptHandle("receiptHandle")
         .queueUrl("queue"));
DeleteMessageResponse response = futureOne.join();
```

## Receive messages
<a name="sqs-auto-batch-receive"></a>

### Use default settings
<a name="sqs-auto-batch-receive-default-settings"></a>

When you poll the `[SqsAsyncBatchManager\#receiveMessage](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/batchmanager/SqsAsyncBatchManager.html#receiveMessage(java.util.function.Consumer))` method in your application, the batch manager fetches messages from its internal buffer, which the SDK automatically updates in the background.

The following example shows how to call the `receiveMessage` method.

```
CompletableFuture<ReceiveMessageResponse> responseFuture =
    sqsAsyncBatchManager.receiveMessage(r -> r.queueUrl("queueUrl"));
```

### Use custom settings
<a name="sqs-auto-batch-receive-custom-settings"></a>

If you want to customize the request further, for example by setting custom wait times and specifying the number of messages to retrieve, you can customize the request as shown in the following example.

```
CompletableFuture<ReceiveMessageResponse> response =
    sqsAsyncBatchManager.receiveMessage(r ->
        r.queueUrl("queueUrl")
         .waitTimeSeconds(5)
         .visibilityTimeout(20));
```

**Note**
If you call `receiveMessage` with a `[ReceiveMessageRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/model/ReceiveMessageRequest.html)` that includes any of the following parameters, the SDK bypasses the batch manager and sends a regular asynchronous `receiveMessage` request:
`messageAttributeNames`
`messageSystemAttributeNames`
`messageSystemAttributeNamesWithStrings`
`overrideConfiguration`

## Override configuration settings for `SqsAsyncBatchManager`
<a name="sqs-auto-batch-config-settings"></a>

You can adjust the following settings when you create an `SqsAsyncBatchManager` instance. The following list of settings are available on the [`BatchOverrideConfiguration.Builder`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/batchmanager/BatchOverrideConfiguration.Builder.html).

| Setting | Description | Default value |
| --- | --- | --- |
| maxBatchSize | Maximum number of request per batch for each SendMessageBatchRequest, ChangeMessageVisibilityBatchRequest, or DeleteMessageBatchRequest. The maximum value is 10. | 10 |
| sendRequestFrequency | Time before sending a batch, unless `maxBatchSize` is reached earlier. Higher values may reduce requests but increase latency. | 200ms |
| receiveMessageVisibilityTimeout | Visibility timeout for messages. If unset, the queue's default is used. | Queue's default |
| receiveMessageMinWaitDuration | Minimum wait time for receiveMessage requests. Avoid setting to 0 to prevent CPU waste. | 50ms |
| receiveMessageSystemAttributeNames | List of [system attribute names](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/model/MessageSystemAttributeName.html) to request for receiveMessage calls. | None |
| receiveMessageAttributeNames | List of [attribute names](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-metadata.html#sqs-message-attributes) to request for receiveMessage calls. | None |
