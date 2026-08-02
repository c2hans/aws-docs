---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-sqs-message-queues.html
---

# Working with Amazon SQS Message Queues
<a name="examples-sqs-message-queues"></a>

A *message queue* is the logical container you use to send messages reliably in Amazon SQS. There are two types of queues: *standard* and *first-in, first-out* (FIFO). To learn more about queues and the differences between these types, see the [Amazon Simple Queue Service Developer Guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/).

These C\+\+ examples show you how to use the AWS SDK for C\+\+ to create, list, delete, and get the URL of an Amazon SQS queue.

## Prerequisites
<a name="codeExamplePrereq"></a>

Before you begin, we recommend you read [Getting started using the AWS SDK for C\+\+](getting-started.md).

Download the example code and build the solution as described in [Getting started on code examples](getting-started-code-examples.md).

To run the examples, the user profile your code uses to make the requests must have proper permissions in AWS (for the service and the action). For more information, see [Providing AWS credentials](credentials.md).

## Create a Queue
<a name="sqs-create-queue"></a>

Use the SQSClient class `CreateQueue` member function, and provide it with a [CreateQueueRequest](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-sqs/html/class_aws_1_1_s_q_s_1_1_model_1_1_create_queue_request.html) object that describes the queue parameters.

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

    const Aws::SQS::Model::CreateQueueOutcome outcome = sqsClient.CreateQueue(request);
    if (outcome.IsSuccess()) {
        std::cout << "Successfully created queue " << queueName << " with a queue URL "
                  << outcome.GetResult().GetQueueUrl() << "." << std::endl;
    }
    else {
        std::cerr << "Error creating queue " << queueName << ": " <<
                  outcome.GetError().GetMessage() << std::endl;
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sqs/create_queue.cpp).

## List Queues
<a name="sqs-list-queues"></a>

To list Amazon SQS queues for your account, call the SQSClient class `ListQueues` member function, and pass it a [ListQueuesRequest](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-sqs/html/class_aws_1_1_s_q_s_1_1_model_1_1_list_queues_request.html) object.

 **Includes**

```
#include <aws/core/Aws.h>
#include <aws/sqs/SQSClient.h>
#include <aws/sqs/model/ListQueuesRequest.h>
#include <iostream>
```

 **Code**

```
    Aws::SQS::SQSClient sqsClient(clientConfiguration);

    Aws::SQS::Model::ListQueuesRequest listQueuesRequest;

    Aws::String nextToken; // Used for pagination.
    Aws::Vector<Aws::String> allQueueUrls;

    do {
        if (!nextToken.empty()) {
            listQueuesRequest.SetNextToken(nextToken);
        }
        const Aws::SQS::Model::ListQueuesOutcome outcome = sqsClient.ListQueues(
                listQueuesRequest);
        if (outcome.IsSuccess()) {
            const Aws::Vector<Aws::String> &queueUrls = outcome.GetResult().GetQueueUrls();
            allQueueUrls.insert(allQueueUrls.end(),
                                queueUrls.begin(),
                                queueUrls.end());

            nextToken = outcome.GetResult().GetNextToken();
        }
        else {
            std::cerr << "Error listing queues: " <<
                      outcome.GetError().GetMessage() << std::endl;
            return false;
        }

    } while (!nextToken.empty());

    std::cout << allQueueUrls.size() << " Amazon SQS queue(s) found." << std::endl;
    for (const auto &iter: allQueueUrls) {
        std::cout << " " << iter << std::endl;
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sqs/list_queues.cpp).

## Get the Queue’s URL
<a name="sqs-get-queue-url"></a>

To get the URL for an existing Amazon SQS queue, call the SQSClient class `GetQueueUrl` member function.

 **Includes**

```
#include <aws/core/Aws.h>
#include <aws/sqs/SQSClient.h>
#include <aws/sqs/model/GetQueueUrlRequest.h>
#include <iostream>
```

 **Code**

```
    Aws::SQS::SQSClient sqsClient(clientConfiguration);

    Aws::SQS::Model::GetQueueUrlRequest request;
    request.SetQueueName(queueName);

    const Aws::SQS::Model::GetQueueUrlOutcome outcome = sqsClient.GetQueueUrl(request);
    if (outcome.IsSuccess()) {
        std::cout << "Queue " << queueName << " has url " <<
                  outcome.GetResult().GetQueueUrl() << std::endl;
    }
    else {
        std::cerr << "Error getting url for queue " << queueName << ": " <<
                  outcome.GetError().GetMessage() << std::endl;
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sqs/get_queue_url.cpp).

## Delete a Queue
<a name="sqs-delete-queue"></a>

Provide the [URL](#sqs-get-queue-url) to the SQSClient class `DeleteQueue` member function.

 **Includes**

```
#include <aws/core/Aws.h>
#include <aws/core/client/DefaultRetryStrategy.h>
#include <aws/sqs/SQSClient.h>
#include <aws/sqs/model/DeleteQueueRequest.h>
#include <iostream>
```

 **Code**

```
    Aws::SQS::Model::DeleteQueueRequest request;
    request.SetQueueUrl(queueURL);

    const Aws::SQS::Model::DeleteQueueOutcome outcome = sqsClient.DeleteQueue(request);
    if (outcome.IsSuccess()) {
        std::cout << "Successfully deleted queue with url " << queueURL <<
                  std::endl;
    }
    else {
        std::cerr << "Error deleting queue " << queueURL << ": " <<
                  outcome.GetError().GetMessage() << std::endl;
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sqs/delete_queue.cpp).

## More Info
<a name="more-info"></a>
+  [How Amazon SQS Queues Work](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-how-it-works.html) in the Amazon Simple Queue Service Developer Guide
+  [CreateQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CreateQueue.html) in the Amazon Simple Queue Service API Reference
+  [GetQueueUrl](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueUrl.html) in the Amazon Simple Queue Service API Reference
+  [ListQueues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueues.html) in the Amazon Simple Queue Service API Reference
+  [DeleteQueues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteQueues.html) in the Amazon Simple Queue Service API Reference
