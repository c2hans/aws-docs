---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-servers-over-private-networks-mgn/scenarios.html
---

# Scenarios
<a name="scenarios"></a>

This guide covers the required infrastructure components to be created to complete the migration for the following scenarios:
+ Replication over private networks only, which is the most common and restrictive scenario.
+ Hybrid scenario where HTTPS egress communication is allowed but all other traffic is restricted. This scenario consists of two options:
  + Public HTTPS egress at the source and private staging area resources
  + Public HTTPS egress at the source and public staging area resources

For each scenario, the guide provides an example configuration and the full list of required AWS components.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
