---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/implementing-request-response-systems.html
---

# Implementing request-response systems in Amazon SQS
<a name="implementing-request-response-systems"></a>

When implementing a request-response or remote procedure call (RPC) system, keep the following best practices in mind:
+ **Create reply queues on start-up** – Instead of creating reply queues per message, create them on start-up, per producer. Use a correlation ID message attribute to map replies to requests efficiently.
+ **Avoid sharing reply queues among producers** – Ensure that each producer has its own reply queue. Sharing reply queues can result in a producer receiving response messages intended for another producer.

For more information about implementing the request-response pattern using the Temporary Queue Client, see [Request-response messaging pattern (virtual queues)](sqs-temporary-queues.md#request-reply-messaging-pattern).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
