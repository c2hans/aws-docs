---
source_url: https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-data-access.html
---

# Managing data access for Security Lake subscribers
<a name="subscriber-data-access"></a>

Subscribers with data access to source data in Amazon Security Lake are notified of new objects for the source as the data is written to the S3 bucket. By default, subscribers are notified about new objects through an HTTPS endpoint that they provide. Alternatively, subscribers can be notified about new objects by polling an Amazon Simple Queue Service (Amazon SQS) queue.

Subscribers are notified of new Amazon S3 objects for a source as the objects are written to the Security Lake data lake. Subscribers can directly access the S3 objects and receive notifications of new objects through a subscription endpoint or by polling an Amazon Simple Queue Service (Amazon SQS) queue. This subscription type is identified as `S3` in the `accessTypes` parameter of the [CreateSubscriber](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateSubscriber.html) API.

**Topics**
+ [Prerequisites](prereqs-creating-subscriber.md)
+ [Creating a subscriber with data access](create-subscriber-data-access.md)
+ [Updating a data subscriber](subscriber-update.md)
+ [Removing a data subscriber](remove-data-access-subscriber.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
