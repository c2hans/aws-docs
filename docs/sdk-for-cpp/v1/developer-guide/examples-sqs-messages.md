---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-sqs-messages.html
---

# Sending, Receiving, and Deleting Amazon SQS Messages
<a name="examples-sqs-messages"></a>

Messages are always delivered using an [SQS queue](examples-sqs-message-queues.md). These C\+\+ examples show you how to use the AWS SDK for C\+\+ to send, receive, and delete Amazon SQS messages from SQS queues.

## Prerequisites
<a name="codeExamplePrereq"></a>

Before you begin, we recommend you read [Getting started using the AWS SDK for C\+\+](getting-started.md).

Download the example code and build the solution as described in [Getting started on code examples](getting-started-code-examples.md).

To run the examples, the user profile your code uses to make the requests must have proper permissions in AWS (for the service and the action). For more information, see [Providing AWS credentials](credentials.md).

## Send a Message
<a name="sqs-message-send"></a>

You can add a single message to an Amazon SQS queue by calling the SQSClient class `SendMessage` member function. You provide `SendMessage` with a [SendMessageRequest](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-sqs/html/class_aws_1_1_s_q_s_1_1_model_1_1_send_message_request.html) object containing the queue’s [URL](examples-sqs-message-queues.md#sqs-get-queue-url), the message body, and an optional delay value (in seconds).

 **Includes**

```
#include <aws/core/Aws.h>
#include <aws/sqs/SQSClient.h>
#include <aws/sqs/model/SendMessageRequest.h>
#include <iostream>
```

 **Code**

```
    Aws::SQS::SQSClient sqsClient(clientConfiguration);

    Aws::SQS::Model::SendMessageRequest request;
    request.SetQueueUrl(queueUrl);
    request.SetMessageBody(messageBody);

    const Aws::SQS::Model::SendMessageOutcome outcome = sqsClient.SendMessage(request);
    if (outcome.IsSuccess()) {
        std::cout << "Successfully sent message to " << queueUrl <<
                  std::endl;
    }
    else {
        std::cerr << "Error sending message to " << queueUrl << ": " <<
                  outcome.GetError().GetMessage() << std::endl;
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sqs/send_message.cpp).

## Receive Messages
<a name="sqs-messages-receive"></a>

Retrieve any messages that are currently in the queue by calling the SQSClient class `ReceiveMessage` member function, passing it the queue’s URL. Messages are returned as a list of [Message](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-sqs/html/class_aws_1_1_s_q_s_1_1_model_1_1_message.html) objects.

 **Includes**

```
#include <aws/core/Aws.h>
#include <aws/sqs/SQSClient.h>
#include <aws/sqs/model/ReceiveMessageRequest.h>
#include <iostream>
```

 **Code**

```
    Aws::SQS::SQSClient sqsClient(clientConfiguration);

    Aws::SQS::Model::ReceiveMessageRequest request;
    request.SetQueueUrl(queueUrl);
    request.SetMaxNumberOfMessages(1);

    const Aws::SQS::Model::ReceiveMessageOutcome outcome = sqsClient.ReceiveMessage(
            request);
    if (outcome.IsSuccess()) {

        const Aws::Vector<Aws::SQS::Model::Message> &messages =
                outcome.GetResult().GetMessages();
        if (!messages.empty()) {
            const Aws::SQS::Model::Message &message = messages[0];
            std::cout << "Received message:" << std::endl;
            std::cout << "  MessageId: " << message.GetMessageId() << std::endl;
            std::cout << "  ReceiptHandle: " << message.GetReceiptHandle() << std::endl;
            std::cout << "  Body: " << message.GetBody() << std::endl << std::endl;
        }
        else {
            std::cout << "No messages received from queue " << queueUrl <<
                      std::endl;

        }
    }
    else {
        std::cerr << "Error receiving message from queue " << queueUrl << ": "
                  << outcome.GetError().GetMessage() << std::endl;
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sqs/receive_message.cpp).

### Delete Messages after Receipt
<a name="sqs-messages-delete"></a>

After receiving a message and processing its contents, delete the message from the queue by sending the message’s receipt handle and the queue URL to the SQSClient class `DeleteMessage` member function.

 **Includes**

```
#include <aws/core/Aws.h>
#include <aws/sqs/SQSClient.h>
#include <aws/sqs/model/DeleteMessageRequest.h>
#include <iostream>
```

 **Code**

```
    Aws::SQS::Model::DeleteMessageRequest request;
    request.SetQueueUrl(queueUrl);
    request.SetReceiptHandle(messageReceiptHandle);

    const Aws::SQS::Model::DeleteMessageOutcome outcome = sqsClient.DeleteMessage(
            request);
    if (outcome.IsSuccess()) {
        std::cout << "Successfully deleted message from queue " << queueUrl
                  << std::endl;
    }
    else {
        std::cerr << "Error deleting message from queue " << queueUrl << ": " <<
                  outcome.GetError().GetMessage() << std::endl;
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sqs/receive_message.cpp).

## More Info
<a name="more-info"></a>
+  [How Amazon SQS Queues Work](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-how-it-works.html) in the Amazon Simple Queue Service Developer Guide
+  [SendMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html) in the Amazon Simple Queue Service API Reference
+  [SendMessageBatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessageBatch.html) in the Amazon Simple Queue Service API Reference
+  [ReceiveMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html) in the Amazon Simple Queue Service API Reference
+  [DeleteMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.html) in the Amazon Simple Queue Service API Reference
