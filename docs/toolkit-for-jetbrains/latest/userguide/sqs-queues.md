---
source_url: https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/sqs-queues.html
---

# Working with Amazon Simple Queue Service queues
<a name="sqs-queues"></a>

The following topics describe how to use the AWS Toolkit for JetBrains to work with Amazon Simple Queue Service queues and messages.

Standard and FIFO (First-In-Last-Out) are the two kinds of messages you can send using Amazon SQS in the AWS Toolkit for JetBrains.

**To create an Amazon SQS queue**

1. From the AWS Toolkit for JetBrains, expand the AWS Explorer to view your AWS services.

1. From the AWS Explorer, open the context menu for (right-click) the **Amazon SQS** service, and choose **Create Queue...**.

1. Provide a queue name and choose the queue type.
**Note**
For more information on queue types, see the [Amazon SQS standard queues](https://docs.aws.amazon.com//AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.html) and [Amazon SQS FIFO (First-In-First-Out) queues](https://docs.aws.amazon.com//AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html) topics in the *Amazon Simple Queue Service Developer Guide*.

1. Choose **Create**.

**To view Amazon SQS messages**

1. From the AWS Toolkit for JetBrains, expand the AWS Explorer to view your AWS services.

1. From the AWS Explorer, expand the **Amazon SQS** service to view a list of your existing queues.

1. Right-click the queue you want to view and choose **View Messages**.

1. Choose **View Messages** to view the messages in this queue.

**To edit Amazon SQS queue properties**

1. From the AWS Toolkit for JetBrains, expand the AWS Explorer to view your AWS services.

1. From the AWS Explorer, expand the **Amazon SQS** service to view a list of your existing queues.

1. Right-click the queue that you want to edit and choose **Edit Queue Properties...**.

1. In the **Edit Queue Properties** dialog box that opens, review and modify your queue properties. For more information on Amazon SQS properties, see [Configuring queue parameters (console)](https://docs.aws.amazon.com//AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-queue-parameters.html) in the *Amazon Simple Queue Service Developer Guide*.

**To send Standard messages**

1. From the AWS Toolkit for JetBrains, expand the AWS Explorer to view your AWS services.

1. From the AWS Explorer, expand the **Amazon SQS** service to view a list of your existing queues.

1. Right-click the queue for sending your message and choose **Send a message**.

1. Populate the message and choose **Send**. After you send the message, you see a confirmation that includes the message ID.

**To send FIFO messages**

1. From the AWS Toolkit for JetBrains, expand the AWS Explorer to view your AWS services.

1. From the AWS Explorer, expand the **Amazon SQS** service to view a list of your existing queues.

1. Right-click the queue for sending your message and choose **Send a message**.

1. Populate the message, group id, and an optional deduplication id.
**Note**
If no deduplication id is provided, one will be generated.

1. Choose **Send**. After you send the message, you see a confirmation that includes the message ID.

**To delete an Amazon SQS queue**

1. Verify that a queue is empty before you delete it. For more information see [Confirming that a queue is empty](https://docs.aws.amazon.com//AWSSimpleQueueService/latest/SQSDeveloperGuide/confirm-queue-is-empty.html) in the *Amazon Simple Queue Service Developer Guide*.

1. From the AWS Toolkit for JetBrains, expand the AWS Explorer to view your AWS services.

1. From the AWS Explorer, expand the **Amazon SQS** service to view a list of your existing queues.

1. Right-click **Amazon SQS**, and choose **Delete Queue...**.

1. Confirm that you want to delete the queue, and choose **OK** in the deletion dialog box.
