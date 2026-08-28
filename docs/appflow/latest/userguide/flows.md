---
source_url: https://docs.aws.amazon.com/appflow/latest/userguide/flows.html
---

# Amazon AppFlow flows
<a name="flows"></a>

With Amazon AppFlow, a *flow* transfers data between a source and a destination. Amazon AppFlow supports a variety of AWS services and SaaS applications as sources or destinations.

A *data mapping* determines how data from the source is placed in the destination. You can map the fields in each source object to fields in the destination. You can concatenate multiple fields in a source object to a single field in the destination. You can mask the values of sensitive fields so that the destination field contains only an asterisk (\*). You can also truncate fields to a fixed length.

A *filter* controls which data records are transferred to the destination. Amazon AppFlow transfers only the records that meet the filter criteria.

A *trigger* determines how a flow runs. The following are the supported flow trigger types:
+ **Run on demand** — Users manually run the flow as needed.
+ **Run on event** — Amazon AppFlow runs the flow in response to an event from a SaaS application.
+ **Run on schedule** — Amazon AppFlow runs the flow on a recurring schedule.

When a flow is run, Amazon AppFlow verifies that the data is available in the source, processes the data according to the flow configuration, and transfers the processed data to the destination.

**Topics**
+ [Creating flows](create-flow.md)
+ [Managing flows](flows-manage.md)
+ [Cataloging flow output](flows-catalog.md)
+ [Partitioning and aggregating](flows-partition.md)
+ [Flow triggers](flow-triggers.md)
+ [Private flows](private-flows.md)
+ [Flow notifications](flow-notifications.md)
+ [General information](general.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon AppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
