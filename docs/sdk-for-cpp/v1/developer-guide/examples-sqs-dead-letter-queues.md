---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-sqs-dead-letter-queues.html
---

# Using Dead Letter Queues in Amazon SQS
<a name="examples-sqs-dead-letter-queues"></a>

Amazon SQS provides support for *dead letter queues*. A dead letter queue is a queue that other queues can target for messages that can’t be processed successfully. You can set aside and isolate these messages in the dead letter queue to determine why their processing did not succeed.

To create a dead letter queue, you must first create a *redrive policy*, and then set the policy in the queue’s attributes.

**Important**
A dead letter queue must be the same type of queue (FIFO or standard) that the source queue is. It must also be created using the same AWS account and AWS Region as the source queue.

## Prerequisites
<a name="codeExamplePrereq"></a>

Before you begin, we recommend you read [Getting started using the AWS SDK for C\+\+](getting-started.md).

Download the example code and build the solution as described in [Getting started on code examples](getting-started-code-examples.md).

To run the examples, the user profile your code uses to make the requests must have proper permissions in AWS (for the service and the action). For more information, see [Providing AWS credentials](credentials.md).

## Create a Redrive Policy
<a name="sqs-dead-letter-queue-create-redrive-policy"></a>

A redrive policy is specified in JSON. To create it, you can use the JSON utility class provided with the AWS SDK for C\+\+.

Here is an example function that creates a redrive policy by providing it with the ARN of your dead letter queue and the maximum number of times the message can be received and not processed before it’s sent to the dead letter queue.

 **Includes**

```
#include <aws/core/Aws.h>
#include <aws/core/utils/json/JsonSerializer.h>
```

 **Code**

```
Aws::String MakeRedrivePolicy(const Aws::String &queueArn, int maxReceiveCount) {
    Aws::Utils::Json::JsonValue redrive_arn_entry;
    redrive_arn_entry.AsString(queueArn);

    Aws::Utils::Json::JsonValue max_msg_entry;
    max_msg_entry.AsInteger(maxReceiveCount);

    Aws::Utils::Json::JsonValue policy_map;
    policy_map.WithObject("deadLetterTargetArn", redrive_arn_entry);
    policy_map.WithObject("maxReceiveCount", max_msg_entry);

    return policy_map.View().WriteReadable();
}
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sqs/dead_letter_queue.cpp).

## Set the Redrive Policy on your Source Queue
<a name="sqs-dead-letter-queue-set-redrive-policy"></a>

To finish setting up your dead letter queue, call the SQSClient class’ `SetQueueAttributes` member function with a [SetQueueAttributesRequest](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-sqs/html/class_aws_1_1_s_q_s_1_1_model_1_1_set_queue_attributes_request.html) object for which you’ve set the `RedrivePolicy` attribute with your JSON redrive policy.

 **Includes**

```
#include <aws/sqs/SQSClient.h>
#include <aws/sqs/model/SetQueueAttributesRequest.h>
#include <iostream>
```

 **Code**

```
    Aws::SQS::Model::SetQueueAttributesRequest request;
    request.SetQueueUrl(srcQueueUrl);
    request.AddAttributes(
            Aws::SQS::Model::QueueAttributeName::RedrivePolicy,
            redrivePolicy);

    const Aws::SQS::Model::SetQueueAttributesOutcome outcome =
            sqsClient.SetQueueAttributes(request);
    if (outcome.IsSuccess()) {
        std::cout << "Successfully set dead letter queue for queue  " <<
                  srcQueueUrl << " to " << deadLetterQueueARN << std::endl;
    }
    else {
        std::cerr << "Error setting dead letter queue for queue " <<
                  srcQueueUrl << ": " << outcome.GetError().GetMessage() <<
                  std::endl;
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sqs/dead_letter_queue.cpp).

## More Info
<a name="more-info"></a>
+  [Using Amazon SQS Dead Letter Queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) in the Amazon Simple Queue Service Developer Guide
+  [SetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SetQueueAttributes.html) in the Amazon Simple Queue Service API Reference

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for C++. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-cpp` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
