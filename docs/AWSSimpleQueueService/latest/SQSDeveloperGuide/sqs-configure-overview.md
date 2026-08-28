---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-overview.html
---

# Understanding the Amazon SQS console
<a name="sqs-configure-overview"></a>

When you open the Amazon SQS console, choose **Queues** from the navigation pane. The **Queues** page provides information about all of your queues in the active region.

Each queue entry provides essential information about the queue, including its type and key attributes. [Standard queues](standard-queues.md), optimized for maximum throughput and best-effort message ordering, are distinguished from [First-In-First-Out (FIFO)](sqs-fifo-queues.md) queues, which prioritize message ordering and uniqueness for applications requiring strict message sequencing.

![Queues page in the Amazon SQS console.](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/images/sqs-config-queue-list.png)

**Interactive elements and actions**

From the Queues page, you have multiple options for managing your queues:

1. **Quick Actions** – Adjacent to each queue name, a dropdown menu offers quick access to common actions such as sending messages, viewing or deleting messages, configuring triggers, and deleting the queue itself.

1. **Detailed View and Configuration** – Clicking on a queue name opens its Details page, where you can delve deeper into queue settings and configurations. Here, you can adjust parameters like message retention period, visibility timeout, and maximum message size to tailor the queue to your application's requirements.

![Queue details page in the Amazon SQS console.](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/images/queue-details-page.png)

**Region selection and resource tags**

Ensure you're in the correct AWS Region to access and manage your queues effectively. Additionally, consider utilizing resource tags to organize and categorize your queues, enabling better resource management, cost allocation, and access control within your AWS shared environment.

By leveraging the features and functionalities offered within the Amazon SQS console, you can efficiently manage your messaging infrastructure, optimize queue performance, and ensure reliable message delivery for your applications.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
