---
source_url: https://docs.aws.amazon.com/memorydb/latest/devguide/subnetgroups.ipv6.html
---

# MemoryDB and IPV6
<a name="subnetgroups.ipv6"></a>

You can create new dual stack and ipv6-only clusters with both Valkey and Redis OSS engines, by providing subnet groups with dual stack and ipv6-only subnets. You cannot change the network type for an existing cluster.

With this functionality you can:
+ Create ipv4-only and dual stack clusters on dual stack subnets.
+ Create ipv6-only clusters on ipv6-only subnets.
+ Create new subnet groups to support ipv4-only, dual stack, and ipv6-only subnets.
+ Modify existing subnet groups to include additional subnets from the underlying VPC.
+ Modify existing subnets in subnet groups
  + Add IPv6 only subnets to subnet groups configured for IPv6
  + Add IPv4 or dual stack subnets to subnet groups configured for IPv4 and dual stack support
+ Discover all the nodes in the cluster with ipv4 OR ipv6 addresses, through engine discovery commands for dual stack and ipv6 clusters. These discovery commands include `redis_info`, `redis_cluster`, and similar.
+ Discover the ipv4 and ipv6 addresses of all the nodes in the cluster, through DNS discovery commands for dual stack and ipv6 clusters.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
