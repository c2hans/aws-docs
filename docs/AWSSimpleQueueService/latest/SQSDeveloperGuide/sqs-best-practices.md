---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-best-practices.html
---

# Amazon SQS best practices
<a name="sqs-best-practices"></a>

Amazon SQS manages and processes message queues, enabling different parts of an application to exchange messages reliably and at scale. This topic covers key operational best practices, including using long polling to reduce empty responses, implementing dead-letter queues to handle processing errors, and optimizing queue permissions for security.

****Topics****
+ [Error handling and problematic messages](best-practices-error-handling.md)
+ [Message deduplication and grouping](best-practices-message-deduplication.md)
+ [Message processing and timing](best-practices-message-processing.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
