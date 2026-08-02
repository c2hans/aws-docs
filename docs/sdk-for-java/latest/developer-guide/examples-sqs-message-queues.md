---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-sqs-message-queues.html
---

# Work with Amazon Simple Queue Service message queues
<a name="examples-sqs-message-queues"></a>

A *message queue* is the logical container used for sending messages reliably in Amazon Simple Queue Service. There are two types of queues: *standard* and *first-in, first-out* (FIFO). To learn more about queues and the differences between these types, see the [Amazon Simple Queue Service Developer Guide](https://docs.aws.amazon.com//AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html).

This topic describes how to create, list, delete, and get the URL of an Amazon Simple Queue Service queue by using the AWS SDK for Java.

The `sqsClient` variable that is used in the following examples can be created from the following snippet.

```
SqsClient sqsClient = SqsClient.create();
```

When you create an `SqsClient` by using the static `create()` method, the SDK configures the Region by using the [default region provider chain](region-selection.md#default-region-provider-chain) and the credentials by using the [default credentials provider chain](credentials-chain.md).

## Create a queue
<a name="sqs-create-queue"></a>

Use the `SqsClient’s` `createQueue` method, and provide a `[CreateQueueRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/model/CreateQueueRequest.html)` object that describes the queue parameters as shown in the following code snippet.

 **Imports**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.sqs.SqsClient;
import software.amazon.awssdk.services.sqs.model.*;
import java.util.List;
```

 **Code**

```
            CreateQueueRequest createQueueRequest = CreateQueueRequest.builder()
                .queueName(queueName)
                .build();

            sqsClient.createQueue(createQueueRequest);
```

See the [complete sample](https://github.com/awsdocs/aws-doc-sdk-examples/blob/cf25559da654a7b74bec039c0ab9397dc5951dd4/javav2/example_code/sqs/src/main/java/com/example/sqs/SQSExample.java#L52) on GitHub.

## List queues
<a name="sqs-list-queues"></a>

To list the Amazon Simple Queue Service queues for your account, call the `SqsClient’s` `listQueues` method with a `[ListQueuesRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/model/ListQueuesRequest.html)` object.

When you use the form of the [https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/SqsClient.html#listQueues()](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/SqsClient.html#listQueues()) method that takes no parameters, the service returns *all queues*—up to 1,000 queues.

You can supply a queue name prefix to the `[ListQueuesRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/model/ListQueuesRequest.html)` object to limit the results to queues that match that prefix as shown in the following code.

 **Imports**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.sqs.SqsClient;
import software.amazon.awssdk.services.sqs.model.*;
import java.util.List;
```

 **Code**

```
        String prefix = "que";

        try {
            ListQueuesRequest listQueuesRequest = ListQueuesRequest.builder().queueNamePrefix(prefix).build();
            ListQueuesResponse listQueuesResponse = sqsClient.listQueues(listQueuesRequest);

            for (String url : listQueuesResponse.queueUrls()) {
                System.out.println(url);
            }

        } catch (SqsException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
```

See the [complete sample](https://github.com/awsdocs/aws-doc-sdk-examples/blob/cf25559da654a7b74bec039c0ab9397dc5951dd4/javav2/example_code/sqs/src/main/java/com/example/sqs/SQSExample.java#L79) on GitHub.

## Get the URL for a queue
<a name="sqs-get-queue-url"></a>

The following code shows how to get the URL for a queue by calling the `SqsClient’s` `getQueueUrl` method with a `[GetQueueUrlRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/model/GetQueueUrlRequest.html)` object.

 **Imports**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.sqs.SqsClient;
import software.amazon.awssdk.services.sqs.model.*;
import java.util.List;
```

 **Code**

```
            GetQueueUrlResponse getQueueUrlResponse =
                sqsClient.getQueueUrl(GetQueueUrlRequest.builder().queueName(queueName).build());
            String queueUrl = getQueueUrlResponse.queueUrl();
            return queueUrl;
```

See the [complete sample](https://github.com/awsdocs/aws-doc-sdk-examples/blob/7486a1a092aa8e16a21698ef26f9d524fef62e55/javav2/example_code/sqs/src/main/java/com/example/sqs/SQSExample.java#L70) on GitHub.

## Delete a queue
<a name="sqs-delete-queue"></a>

Provide the queue’s [URL](#sqs-get-queue-url) to the `[DeleteQueueRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sqs/model/DeleteQueueRequest.html)` object. Then call the `SqsClient’s` `deleteQueue` method to delete a queue as shown in the following code.

 **Imports**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.sqs.SqsClient;
import software.amazon.awssdk.services.sqs.model.*;
import java.util.List;
```

 **Code**

```
    public static void deleteSQSQueue(SqsClient sqsClient, String queueName) {

        try {

            GetQueueUrlRequest getQueueRequest = GetQueueUrlRequest.builder()
                    .queueName(queueName)
                    .build();

            String queueUrl = sqsClient.getQueueUrl(getQueueRequest).queueUrl();

            DeleteQueueRequest deleteQueueRequest = DeleteQueueRequest.builder()
                    .queueUrl(queueUrl)
                    .build();

            sqsClient.deleteQueue(deleteQueueRequest);

        } catch (SqsException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```

See the [complete sample](https://github.com/awsdocs/aws-doc-sdk-examples/blob/6240df86c5f17eae1e23d1139d1435c7dc4b2a11/javav2/example_code/sqs/src/main/java/com/example/sqs/DeleteQueue.java#L48) on GitHub.

## More information
<a name="more-information"></a>
+  [CreateQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CreateQueue.html) in the Amazon Simple Queue Service API Reference
+  [GetQueueUrl](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueUrl.html) in the Amazon Simple Queue Service API Reference
+  [ListQueues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueues.html) in the Amazon Simple Queue Service API Reference
+  [DeleteQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteQueue.html) in the Amazon Simple Queue Service API Reference
