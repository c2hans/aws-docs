---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-sqs-long-polling.html
---

# Enabling Long Polling for Amazon SQS Message Queues
<a name="examples-sqs-long-polling"></a>

Amazon SQS uses *short polling* by default, querying only a subset of the servers—based on a weighted random distribution—to determine whether any messages are available for inclusion in the response.

Long polling helps reduce your cost of using Amazon SQS by reducing the number of empty responses when there are no messages available to return in reply to a ReceiveMessage request sent to an Amazon SQS queue and eliminating false empty responses. You can set a long polling frequency from *1–20 seconds*.

## Prerequisites
<a name="codeExamplePrereq"></a>

Before you begin, we recommend you read [Getting started using the AWS SDK for C\+\+](getting-started.md).

Download the example code and build the solution as described in [Getting started on code examples](getting-started-code-examples.md).

To run the examples, the user profile your code uses to make the requests must have proper permissions in AWS (for the service and the action). For more information, see [Providing AWS credentials](credentials.md).

## Enable Long Polling when Creating a Queue
<a name="sqs-long-polling-create-queue"></a>

To enable long polling when creating an Amazon SQS queue, set the `ReceiveMessageWaitTimeSeconds` attribute on the [CreateQueueRequest](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-sqs/html/class_aws_1_1_s_q_s_1_1_model_1_1_create_queue_request.html) object before calling the SQSClient class’ `CreateQueue` member function.

 **Includes**

```
#include <aws/core/Aws.h>
#include <aws/sqs/SQSClient.h>
#include <aws/sqs/model/CreateQueueRequest.h>
#include <iostream>
```

 **Code**

```
    Aws::SQS::SQSClient sqsClient(clientConfiguration);

    Aws::SQS::Model::CreateQueueRequest request;
    request.SetQueueName(queueName);
    request.AddAttributes(
            Aws::SQS::Model::QueueAttributeName::ReceiveMessageWaitTimeSeconds,
            pollTimeSeconds);

    const Aws::SQS::Model::CreateQueueOutcome outcome = sqsClient.CreateQueue(request);
    if (outcome.IsSuccess()) {
        std::cout << "Successfully created queue " << queueName <<
                  std::endl;
    }
    else {
        std::cout << "Error creating queue " << queueName << ": " <<
                  outcome.GetError().GetMessage() << std::endl;
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sqs/long_polling_on_create_queue.cpp).

## Enable Long Polling on an Existing Queue
<a name="sqs-long-polling-existing-queue"></a>

In addition to enabling long polling when creating a queue, you can also enable it on an existing queue by setting `ReceiveMessageWaitTimeSeconds` on the [SetQueueAttributesRequest](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-sqs/html/class_aws_1_1_s_q_s_1_1_model_1_1_set_queue_attributes_request.html) before calling the SQSClient class’ `SetQueueAttributes` member function.

 **Includes**

```
#include <aws/core/Aws.h>
#include <aws/sqs/SQSClient.h>
#include <aws/sqs/model/SetQueueAttributesRequest.h>
#include <iostream>
```

 **Code**

```
    Aws::SQS::SQSClient sqsClient(clientConfiguration);

    Aws::SQS::Model::SetQueueAttributesRequest request;
    request.SetQueueUrl(queueURL);
    request.AddAttributes(
            Aws::SQS::Model::QueueAttributeName::ReceiveMessageWaitTimeSeconds,
            pollTimeSeconds);

    const Aws::SQS::Model::SetQueueAttributesOutcome outcome = sqsClient.SetQueueAttributes(
            request);
    if (outcome.IsSuccess()) {
        std::cout << "Successfully updated long polling time for queue " <<
                  queueURL << " to " << pollTimeSeconds << std::endl;
    }
    else {
        std::cout << "Error updating long polling time for queue " <<
                  queueURL << ": " << outcome.GetError().GetMessage() <<
                  std::endl;
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sqs/long_polling_on_existing_queue.cpp).

## Enable Long Polling on Message Receipt
<a name="sqs-long-polling-receive-message"></a>

You can enable long polling when receiving a message by setting the wait time in seconds on the [ReceiveMessageRequest](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-sqs/html/class_aws_1_1_s_q_s_1_1_model_1_1_receive_message_request.html) that you supply to the SQSClient class’ ReceiveMessage member function.

**Note**
You should make sure that the AWS client’s request timeout is larger than the maximum long poll time (20s) so that your `ReceiveMessage` requests don’t time out while waiting for the next poll event\!

 **Includes**

```
#include <aws/core/Aws.h>
#include <aws/sqs/SQSClient.h>
#include <aws/sqs/model/ReceiveMessageRequest.h>
```

 **Code**

```
    Aws::SQS::SQSClient sqsClient(customConfiguration);

    Aws::SQS::Model::ReceiveMessageRequest request;
    request.SetQueueUrl(queueUrl);
    request.SetMaxNumberOfMessages(1);
    request.SetWaitTimeSeconds(waitTimeSeconds);

    auto outcome = sqsClient.ReceiveMessage(request);
    if (outcome.IsSuccess()) {
        const auto &messages = outcome.GetResult().GetMessages();
        if (messages.empty()) {
            std::cout << "No messages received from queue " << queueUrl <<
                      std::endl;
        }
        else {
            const auto &message = messages[0];
            std::cout << "Received message:" << std::endl;
            std::cout << "  MessageId: " << message.GetMessageId() << std::endl;
            std::cout << "  ReceiptHandle: " << message.GetReceiptHandle() << std::endl;
            std::cout << "  Body: " << message.GetBody() << std::endl << std::endl;
        }
    }
    else {
        std::cout << "Error receiving message from queue " << queueUrl << ": "
                  << outcome.GetError().GetMessage() << std::endl;
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sqs/long_polling_on_message_receipt.cpp).

## More Info
<a name="more-info"></a>
+  [Amazon SQS Long Polling](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-long-polling.html) in the Amazon Simple Queue Service Developer Guide
+  [CreateQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CreateQueue.html) in the Amazon Simple Queue Service API Reference
+  [ReceiveMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html) in the Amazon Simple Queue Service API Reference
+  [SetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SetQueueAttributes.html) in the Amazon Simple Queue Service API Reference
