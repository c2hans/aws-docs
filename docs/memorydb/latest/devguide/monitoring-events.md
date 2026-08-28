---
source_url: https://docs.aws.amazon.com/memorydb/latest/devguide/monitoring-events.html
---

# Monitoring MemoryDB events
<a name="monitoring-events"></a>

When significant events happen for a cluster, MemoryDB sends notification to a specific Amazon SNS topic. Examples include a failure to add a node, success in adding a node, the modification of a security group, and others. By monitoring for key events, you can know the current state of your clusters and, depending upon the event, be able to take corrective action.

**Topics**
+ [Managing MemoryDB Amazon SNS notifications](mdbevents.sns.md)
+ [Viewing MemoryDB events](mdbevents.viewing.md)
+ [Event Notifications and Amazon SNS](memorydbsns.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
