---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ECEvents.html
---

# Amazon SNS monitoring of ElastiCache events
<a name="ECEvents"></a>

When significant events happen for a cluster, ElastiCache sends notification to a specific Amazon SNS topic. Examples include a failure to add a node, success in adding a node, the modification of a security group, and others. By monitoring for key events, you can know the current state of your clusters and, depending upon the event, be able to take corrective action.

**Topics**
+ [Managing ElastiCache Amazon SNS notifications](ECEvents.SNS.md)
+ [Viewing ElastiCache events](ECEvents.Viewing.md)
+ [Event Notifications and Amazon SNS](ElastiCacheSNS.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
