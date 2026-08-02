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
