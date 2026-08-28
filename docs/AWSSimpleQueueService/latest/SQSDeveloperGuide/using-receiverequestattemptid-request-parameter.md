---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-receiverequestattemptid-request-parameter.html
---

# Using the Amazon SQS receive request attempt ID
<a name="using-receiverequestattemptid-request-parameter"></a>

The receive request attempt ID is a unique token used to deduplicate [`ReceiveMessage`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html) calls in Amazon SQS. During a network outage or connectivity issue between your application and Amazon SQS, it is best practice to:
+ Provide a receive request attempt ID when making a `ReceiveMessage` call.
+ Retry using the same receive request attempt ID if the operation fails.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
