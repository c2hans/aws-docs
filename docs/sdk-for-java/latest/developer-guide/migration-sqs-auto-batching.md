---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-sqs-auto-batching.html
---

# Changes in automatic Amazon SQS request batching from version 1 to version 2
<a name="migration-sqs-auto-batching"></a>

This topic details the changes in automatic request batching for Amazon SQS between version 1 and version 2 of the AWS SDK for Java.

## High-level changes
<a name="migration-sqs-auto-batching-high-level-changes"></a>

The AWS SDK for Java 1.x performs client-side buffering using a separate `[AmazonSQSBufferedAsyncClient](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/sqs/buffered/AmazonSQSBufferedAsyncClient.html)` class that requires explicit initialization for request batching.

The AWS SDK for Java 2.x simplifies and enhances buffering functionality with the `[SqsAsyncBatchManager](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/batchmanager/SqsAsyncBatchManager.html)`. The implementation of this interface provides automatic request batching capabilities directly integrated with the standard `[SqsAsyncClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/SqsAsyncClient.html)`. To learn about v2's `SqsAsyncBatchManager`, see the [Use automatic request batching for Amazon SQS with the AWS SDK for Java 2.x](sqs-auto-batch.md) topic in this guide.

| Change | v1 | v2 |
| --- | --- | --- |
|  <br />Maven dependencies |  <pre><dependencyManagement><br />    <dependencies><br />        <dependency><br />            <groupId>com.amazonaws</groupId><br />            <artifactId>aws-java-sdk-bom</artifactId><br />            <version>{{1.12.7821}}</version><br />            <type>pom</type><br />            <scope>import</scope><br />        </dependency><br />    </dependencies><br /></dependencyManagement><br /><dependencies><br />    <dependency><br />        <groupId>com.amazonaws</groupId><br />        <artifactId>aws-java-sdk-sqs</artifactId><br />    </dependency><br /></dependencies><br /></pre>  |  <pre><dependencyManagement><br />    <dependencies><br />        <dependency><br />            <groupId>software.amazon.awssdk</groupId><br />            <artifactId>bom</artifactId><br />            <version>{{2.31.152}}</version><br />            <type>pom</type><br />            <scope>import</scope><br />        </dependency><br />    </dependencies><br /></dependencyManagement><br /><dependencies><br />    <dependency><br />        <groupId>software.amazon.awssdk</groupId><br />        <artifactId>sqs</artifactId><br />    </dependency><br /></dependencies></pre>  |
| Package names | com.amazonaws.services.sqs.buffered | software.amazon.awssdk.services.sqs.batchmanager |
| Class names | `[AmazonSQSBufferedAsyncClient](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/sqs/buffered/AmazonSQSBufferedAsyncClient.html)` | [SqsAsyncBatchManager](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/batchmanager/SqsAsyncBatchManager.html) |

1 [Latest version](https://central.sonatype.com/artifact/com.amazonaws/aws-java-sdk-bom). 2 [Latest version](https://central.sonatype.com/artifact/software.amazon.awssdk/bom).

## Using automatic SQS request batching
<a name="migration-sqs-auto-batching-using"></a>

| Change | v1 | v2 |
| --- | --- | --- |
| Create a batch manager |  <pre>AmazonSQSAsync sqsAsync = new AmazonSQSAsyncClient();<br />AmazonSQSAsync bufferedSqs = new <br />            AmazonSQSBufferedAsyncClient(sqsAsync);</pre>  |  <pre>SqsAsyncClient asyncClient = SqsAsyncClient.create();<br />SqsAsyncBatchManager sqsAsyncBatchManager = <br />            asyncClient.batchManager();</pre>  |
| Create a batch manager with custom configuration |  <pre>AmazonSQSAsync sqsAsync = new AmazonSQSAsyncClient();<br /><br />QueueBufferConfig queueBufferConfig = new QueueBufferConfig()<br />        .withMaxBatchOpenMs(200)<br />        .withMaxBatchSize(10)<br />        .withMinReceiveWaitTimeMs(1000)<br />        .withVisibilityTimeoutSeconds(20)<br />        .withReceiveMessageAttributeNames(messageAttributeValues);<br /><br />AmazonSQSAsync bufferedSqs = <br />        new AmazonSQSBufferedAsyncClient(sqsAsync, queueBufferConfig);</pre>  |  <pre>BatchOverrideConfiguration batchOverrideConfiguration = <br />    BatchOverrideConfiguration.builder()<br />        .sendRequestFrequency(Duration.ofMillis(200))<br />        .maxBatchSize(10)<br />        .receiveMessageMinWaitDuration(Duration.ofMillis(1000))<br />        .receiveMessageVisibilityTimeout(Duration.ofSeconds(20))<br />        .receiveMessageSystemAttributeNames(messageSystemAttributeNames)<br />        .receiveMessageAttributeNames(messageAttributeValues)<br />        .build();<br /><br />SqsAsyncBatchManager sqsAsyncBatchManager = SqsAsyncBatchManager.builder()<br />        .overrideConfiguration(batchOverrideConfiguration)<br />        .client(SqsAsyncClient.create())<br />        .scheduledExecutor(Executors.newScheduledThreadPool(8))<br />        .build();</pre>  |
| Send messages |  <pre>Future<SendMessageResult> sendResultFuture = <br />        bufferedSqs.sendMessageAsync(new SendMessageRequest()<br />                .withQueueUrl(queueUrl)<br />                .withMessageBody(body));</pre>  |  <pre>CompletableFuture<SendMessageResponse> sendCompletableFuture = <br />        sqsAsyncBatchManager.sendMessage(<br />                SendMessageRequest.builder()<br />                        .queueUrl(queueUrl)<br />                        .messageBody(body)<br />                        .build());</pre>  |
| Delete messages |  <pre>Future<DeleteMessageResult> deletResultFuture =<br />        bufferedSqs.deleteMessageAsync(new DeleteMessageRequest()<br />                .withQueueUrl(queueUrl));</pre>  |  <pre>CompletableFuture<DeleteMessageResponse> deleteResultCompletableFuture<br />        = sqsAsyncBatchManager.deleteMessage(<br />                DeleteMessageRequest.builder()<br />                        .queueUrl(queueUrl)<br />                        .build());</pre>  |
| Change visibility of messages |  <pre>Future<ChangeMessageVisibilityResult> changeVisibilityResultFuture =<br />        bufferedSqs.changeMessageVisibilityAsync<br />                (new ChangeMessageVisibilityRequest()<br />                        .withQueueUrl(queueUrl)<br />                        .withVisibilityTimeout(20));</pre>  |  <pre>CompletableFuture<ChangeMessageVisibilityResponse> changeResponseCompletableFuture<br />        = sqsAsyncBatchManager.changeMessageVisibility(<br />                ChangeMessageVisibilityRequest.builder()<br />                        .queueUrl(queueUrl)<br />                        .visibilityTimeout(20)<br />                        .build());</pre>  |
| Receive messages |  <pre>ReceiveMessageResult receiveResult =<br />        bufferedSqs.receiveMessage(<br />                new ReceiveMessageRequest()<br />                        .withQueueUrl(queueUrl));</pre>  |  <pre>CompletableFuture<ReceiveMessageResponse> <br />        responseCompletableFuture = sqsAsyncBatchManager.receiveMessage(<br />                ReceiveMessageRequest.builder()<br />                        .queueUrl(queueUrl)<br />                        .build());</pre>  |

## Asynchronous return type differences
<a name="migration-sqs-auto-batching-asyc-return-type"></a>

| Change | v1 | v2 |
| --- | --- | --- |
| Return type | Future<ResultType> | CompletableFuture<ResponseType> |
| Callback mechanism | Requires an AsyncHandler with separate onSuccess and onError methods | Uses CompletableFuture APIs provided by the JDK, such as whenComplete(), thenCompose(), thenApply() |
| Exception handling | Uses AsyncHandler\#onError() method | Uses CompletableFuture APIs provided by the JDK, such as exceptionally(), handle(), or whenComplete() |
| Cancellation | Basic support through Future.cancel() | Cancelling a parent CompletableFuture automatically cancels all dependent futures in the chain |

## Asynchronous completion handling differences
<a name="migration-sqs-auto-batching-asyc-completion-handling"></a>

| Change | v1 | v2 |
| --- | --- | --- |
| Response handler implementation |  <pre>Future<ReceiveMessageResult> future = bufferedSqs.receiveMessageAsync(<br />        receiveRequest,<br />        new AsyncHandler<ReceiveMessageRequest, ReceiveMessageResult>() {<br />            @Override<br />            public void onSuccess(ReceiveMessageRequest request, <br />                              ReceiveMessageResult result) {<br />                List<Message> messages = result.getMessages();<br />                System.out.println("Received " + messages.size() + " messages");<br />                for (Message message : messages) {<br />                    System.out.println("Message ID: " + message.getMessageId());<br />                    System.out.println("Body: " + message.getBody());<br />                }<br />            }<br /><br />            @Override<br />            public void onError(Exception e) {<br />                System.err.println("Error receiving messages: " + e.getMessage());<br />                e.printStackTrace();<br />            }<br />        }<br />);</pre>  |  <pre>CompletableFuture<ReceiveMessageResponse> completableFuture = sqsAsyncBatchManager<br />               .receiveMessage(ReceiveMessageRequest.builder()<br />               .queueUrl(queueUrl).build())<br />        .whenComplete((receiveMessageResponse, throwable) -> {<br />            if (throwable != null) {<br />                System.err.println("Error receiving messages: " + throwable.getMessage());<br />                throwable.printStackTrace();<br />            } else {<br />                List<Message> messages = receiveMessageResponse.messages();<br />                System.out.println("Received " + messages.size() + " messages");<br />                for (Message message : messages) {<br />                    System.out.println("Message ID: " + message.messageId());<br />                    System.out.println("Body: " + message.body());<br />                }<br />            }<br />        });</pre>  |

## Key configuration parameters
<a name="migration-sqs-auto-batching-params"></a>

| Parameter | v1 | v2 |
| --- | --- | --- |
| Maximum batch size | maxBatchSize (default 10 requests per batch) | maxBatchSize (default 10 requests per batch) |
| Batch wait time | maxBatchOpenMs (default 200 ms) | sendRequestFrequency (default 200 ms) |
| Visibility timeout | visibilityTimeoutSeconds (-1 for queue default) | receiveMessageVisibilityTimeout (queue default) |
| Minimum wait time | longPollWaitTimeoutSeconds (20s when longPoll is true) | receiveMessageMinWaitDuration (default 50 ms) |
| Message attributes | Set using ReceiveMessageRequest | receiveMessageAttributeNames (none by default) |
| System attributes | Set using ReceiveMessageRequest | receiveMessageSystemAttributeNames (none by default) |
| Long polling | longPoll (default is true) | Not supported to avoid open connections waiting until the server sends the messages |
| Maximum wait time for long polling | longPollWaitTimeoutSeconds (default 20s) | Not supported to avoid open connections waiting until the server sends the messages |
| Maximum number of prefetched receive batches stored client-side | maxDoneReceiveBatches (10 batches) | Not supported because it is handled internally |
| Maximum number of active outbound batches processed simultaneously | maxInflightOutboundBatches (default 5 batches) | Not supported because it is handled internally |
| Maximum number of active receive batches processed simultaneously | maxInflightReceiveBatches (default 10 batches) | Not supported because it is handled internally |
