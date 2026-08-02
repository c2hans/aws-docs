---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-sqs-messages.html
---

# Send, receive, and delete Amazon Simple Queue Service messages
<a name="examples-sqs-messages"></a>

A message is a piece of data that can be sent and received by distributed components. Messages are always delivered using an [SQS Queue](examples-sqs-message-queues.md).

The `sqsClient` variable that is used in the following examples can be created from the following snippet.

```
SqsClient sqsClient = SqsClient.create();
```

When you create an `SqsClient` by using the static `create()` method, the SDK configures the Region by using the [default region provider chain](region-selection.md#default-region-provider-chain) and the credentials by using the [default credentials provider chain](credentials-chain.md).

## Send a message
<a name="sqs-message-send"></a>

Add a single message to an Amazon Simple Queue Service queue by calling the SqsClient client `sendMessage` method. Provide a [SendMessageRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/model/SendMessageRequest.html) object that contains the queue’s [URL](examples-sqs-message-queues.md#sqs-get-queue-url), message body, and optional delay value (in seconds).

 **Imports**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.sqs.SqsClient;
import software.amazon.awssdk.services.sqs.model.*;
import java.util.List;
```

 **Code**

```
            sqsClient.sendMessage(SendMessageRequest.builder()
                .queueUrl(queueUrl)
                .messageBody("Hello world!")
                .delaySeconds(10)
                .build());

            sqsClient.sendMessage(sendMsgRequest);
```

## Send multiple messages in a request
<a name="sqs-messages-send-multiple"></a>

Send more than one message in a single request by using the SqsClient `sendMessageBatch` method. This method takes a [SendMessageBatchRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/model/SendMessageBatchRequest.html) that contains the queue URL and a list of messages to send. (Each message is a [SendMessageBatchRequestEntry](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/model/SendMessageBatchRequestEntry.html).) You can also delay sending a specific message by setting a delay value on the message.

 **Imports**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.sqs.SqsClient;
import software.amazon.awssdk.services.sqs.model.*;
import java.util.List;
```

 **Code**

```
            SendMessageBatchRequest sendMessageBatchRequest = SendMessageBatchRequest.builder()
                .queueUrl(queueUrl)
                .entries(SendMessageBatchRequestEntry.builder().id("id1").messageBody("Hello from msg 1").build(),
                        SendMessageBatchRequestEntry.builder().id("id2").messageBody("msg 2").delaySeconds(10).build())
                .build();
            sqsClient.sendMessageBatch(sendMessageBatchRequest);
```

See the [complete sample](https://github.com/awsdocs/aws-doc-sdk-examples/blob/cf25559da654a7b74bec039c0ab9397dc5951dd4/javav2/example_code/sqs/src/main/java/com/example/sqs/SQSExample.java#L133) on GitHub.

## Retrieve Messages
<a name="sqs-messages-receive"></a>

Retrieve any messages that are currently in the queue by calling the SqsClient `receiveMessage` method. This method takes a [ReceiveMessageRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/model/ReceiveMessageRequest.html) that contains the queue URL. You can also specify the maximum number of messages to return. Messages are returned as a list of [Message](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/model/Message.html) objects.

 **Imports**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.sqs.SqsClient;
import software.amazon.awssdk.services.sqs.model.*;
import java.util.List;
```

 **Code**

```
        try {
            ReceiveMessageRequest receiveMessageRequest = ReceiveMessageRequest.builder()
                .queueUrl(queueUrl)
                .maxNumberOfMessages(5)
                .build();
            List<Message> messages = sqsClient.receiveMessage(receiveMessageRequest).messages();
            return messages;
        } catch (SqsException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
        return null;
```

See the [complete sample](https://github.com/awsdocs/aws-doc-sdk-examples/blob/cf25559da654a7b74bec039c0ab9397dc5951dd4/javav2/example_code/sqs/src/main/java/com/example/sqs/SQSExample.java#L148) on GitHub.

## Delete a message after receipt
<a name="sqs-messages-delete"></a>

After receiving a message and processing its contents, delete the message from the queue by sending the message's receipt handle and queue URL to the `SqsClient's` [https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/SqsClient.html#deleteMessage(software.amazon.awssdk.services.sqs.model.DeleteMessageRequest)](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/SqsClient.html#deleteMessage(software.amazon.awssdk.services.sqs.model.DeleteMessageRequest)) method.

 **Imports**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.sqs.SqsClient;
import software.amazon.awssdk.services.sqs.model.*;
import java.util.List;
```

 **Code**

```
        try {
            for (Message message : messages) {
                DeleteMessageRequest deleteMessageRequest = DeleteMessageRequest.builder()
                        .queueUrl(queueUrl)
                        .receiptHandle(message.receiptHandle())
                        .build();
                sqsClient.deleteMessage(deleteMessageRequest);
            }
```

See the [complete sample](https://github.com/awsdocs/aws-doc-sdk-examples/blob/cf25559da654a7b74bec039c0ab9397dc5951dd4/javav2/example_code/sqs/src/main/java/com/example/sqs/SQSExample.java#L187) on GitHub.

## More Info
<a name="more-info"></a>
+  [How Amazon Simple Queue Service Queues Work](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-basic-architecture.html) in the Amazon Simple Queue Service Developer Guide
+  [SendMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html) in the Amazon Simple Queue Service API Reference
+  [SendMessageBatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessageBatch.html) in the Amazon Simple Queue Service API Reference
+  [ReceiveMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html) in the Amazon Simple Queue Service API Reference
+  [DeleteMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.html) in the Amazon Simple Queue Service API Reference
