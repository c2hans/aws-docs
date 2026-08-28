---
source_url: https://docs.aws.amazon.com/keyspaces/latest/devguide/throughput-bursting.html
---

# Use burst capacity effectively in Amazon Keyspaces
<a name="throughput-bursting"></a>

Amazon Keyspaces provides some flexibility in your per-partition throughput provisioning by providing *burst capacity*. Whenever you're not fully using a partition's throughput, Amazon Keyspaces reserves a portion of that unused capacity for later *bursts* of throughput to handle usage spikes.

Amazon Keyspaces currently retains up to 5 minutes (300 seconds) of unused read and write capacity. During an occasional burst of read or write activity, these extra capacity units can be consumed quickly—even faster than the per-second provisioned throughput capacity that you've defined for your table.

Amazon Keyspaces can also consume burst capacity for background maintenance and other tasks without prior notice.

Note that these burst capacity details might change in the future.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
