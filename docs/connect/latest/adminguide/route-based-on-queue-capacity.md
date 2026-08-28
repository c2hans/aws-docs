---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/route-based-on-queue-capacity.html
---

# Route contacts based on queue capacity using Connect Customer
<a name="route-based-on-queue-capacity"></a>

To define routing decisions based on queue capacity, use a [Transfer to queue](transfer-to-queue.md) block to check whether a queue is full ([Maximum contacts in queue](set-maximum-queue-limit.md)), and then route the contact accordingly.

The [Transfer to queue](transfer-to-queue.md) block checks the [Maximum contacts in queue](set-maximum-queue-limit.md). If no limit is set, the queue is limited to the number of total concurrent contacts for the following quotas:
+ Active tasks per instance
+ Concurrent active emails per instance
+ Concurrent calls per instance
+ Concurrent chats per instance

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
