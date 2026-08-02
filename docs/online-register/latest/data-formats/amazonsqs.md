---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/amazonsqs.html
---

# Data retrieval APIs for Amazon SQS
<a name="amazonsqs"></a>

Amazon SQS provides the following APIs for data retrieval.

****

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="sqs-GetQueueAttributes"></a>[https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.html) | Get attributes for the specified queue | Read |
| <a name="sqs-GetQueueUrl"></a>[https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueUrl.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueUrl.html) | Return the URL of an existing queue | Read |
| <a name="sqs-ListDeadLetterSourceQueues"></a>[https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListDeadLetterSourceQueues.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListDeadLetterSourceQueues.html) | Return a list of your queues that have the RedrivePolicy queue attribute configured with a dead letter queue | Read |
| <a name="sqs-ListMessageMoveTasks"></a>[https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListMessageMoveTasks.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListMessageMoveTasks.html) | List message move tasks | Read |
| <a name="sqs-ListQueueTags"></a>[https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueueTags.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueueTags.html) | List tags added to an SQS queue | Read |
| <a name="sqs-ListQueues"></a>[https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueues.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueues.html) | Return a list of your queues | Read |
| <a name="sqs-ReceiveMessage"></a>[https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html) | Retrieve one or more messages, with a maximum limit of 10 messages, from the specified queue | Read |
