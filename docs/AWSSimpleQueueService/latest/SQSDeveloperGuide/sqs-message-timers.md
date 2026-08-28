---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-timers.html
---

# Amazon SQS message timers
<a name="sqs-message-timers"></a>

Message timers allow you to set an initial invisibility period for a message when it's added to a queue. For example, if you send a message with a 45-second timer, it remains hidden from consumers for the first 45 seconds. The default (minimum) delay for a message is 0 seconds. The maximum is 15 minutes. For information about sending messages with timers using the console, see [Sending a message using a standard queue](creating-sqs-standard-queues.md#sqs-send-messages).

**Note**
FIFO queues don't support timers on individual messages.

To set a delay period on an entire queue, rather than on individual messages, use [delay queues](sqs-delay-queues.md). A message timer setting for an individual message overrides any `DelaySeconds` value on an Amazon SQS delay queue.

**Extended scheduling options**

While Amazon SQS delay queues and message timers allow scheduling of message delivery up to 15 minutes in the future, you may require more flexible scheduling capabilities. In such cases, consider using [EventBridge Scheduler](https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html), which enables you to schedule billions of one-time or recurring API actions without time limitations. EventBridge Scheduler is the recommended solution for advanced message scheduling use cases.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
