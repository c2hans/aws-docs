---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/step-delete-queue.html
---

# Deleting an Amazon SQS queue
<a name="step-delete-queue"></a>

If you no longer use an Amazon SQS queue and don’t plan to use it in the near future, delete the queue.

**Tip**
If you want to verify that a queue is empty before you delete it, see [Confirming that an Amazon SQS queue is empty](confirm-queue-is-empty.md).

You can delete a queue even when it isn't empty. To delete the messages in a queue but not the queue itself, [purge the queue](sqs-using-purge-queue.md).

**To delete a queue (console)**

1. Open the Amazon SQS console at [https://console.aws.amazon.com/sqs/](https://console.aws.amazon.com/sqs/).

1. In the navigation pane, choose **Queues**.

1. On the **Queues** page, choose the queue to delete.

1. Choose **Delete**.

1. In the **Delete queue** dialog box, confirm the deletion by entering **delete**.

1. Choose **Delete**.

**To delete a queue (AWS CLI and API)**
Choose the appropriate method to delete your queue based on your needs:
+ AWS CLI: `[aws sqs delete-queue](https://docs.aws.amazon.com/cli/latest/reference/sqs/delete-queue.html)`
+ AWS API: `[DeleteQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteQueue.html)`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
