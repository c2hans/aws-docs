---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/sample-queue-customer.html
---

# Sample queue customer flow in Connect Customer
<a name="sample-queue-customer"></a>

**Note**
This topic explains a sample flow that is included with Connect Customer. For information about locating the sample flows in your instance, see [Sample flows in Connect Customer](contact-flow-samples.md).

Type: Flow (inbound)

This flow performs checks before placing customer into a queue. Here's how it works:

1. The **Set working queue** block determines which queue to transfer the customer to.

1. The **Check hours of operation** block perform checks to avoid the customer being queued during non-working hours.

1. The customer is transferred to the queue if it is within business hours, and the queue can handle this call. Otherwise, the customer is played a message "We are not able to take your call right now. Goodbye." And then the customer is disconnected.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
