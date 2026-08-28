---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Scaling-self-designed.html
---

# Scaling node-based clusters
<a name="Scaling-self-designed"></a>

The amount of data your application needs to process is seldom static. It increases and decreases as your business grows or experiences normal fluctuations in demand. If you self-manage your cache, you need to provision sufficient hardware for your demand peaks, which can be expensive. By using Amazon ElastiCache you can scale to meet current demand, paying only for what you use. ElastiCache enables you to scale your cache to match demand.

**Note**
If a Valkey or Redis OSS cluster is replicated across one or more Regions, then those Regions are scaled in order. When scaling up, secondary Regions are scaled first and then the primary Region. When scaling down, the primary Region is first and then any secondary Regions follow.
When updating the engine version, the order is secondary Region and then primary Region.

**Topics**
+ [On-demand scaling for Memcached clusters](Scaling-self-designed.mem-heading.md)
+ [Manual scaling for Memcached clusters](Scaling.Memcached.manually.md)
+ [Scaling for Valkey or Redis OSS (Cluster Mode Disabled) clusters](scaling-redis-classic.md)
+ [Scaling replica nodes for Valkey or Redis OSS (Cluster Mode Disabled)](Scaling.RedisReplGrps.md)
+ [Scaling Valkey or Redis OSS (Cluster Mode Enabled) clusters](scaling-redis-cluster-mode-enabled.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
