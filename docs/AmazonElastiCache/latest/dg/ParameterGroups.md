---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ParameterGroups.html
---

# Configuring engine parameters using ElastiCache parameter groups
<a name="ParameterGroups"></a>

Amazon ElastiCache uses parameters to control the runtime properties of your nodes and clusters. Generally, newer engine versions include additional parameters to support the newer functionality. For tables of Memcached parameters, see [Memcached specific parameters](ParameterGroups.Engine.md#ParameterGroups.Memcached). For tables of Valkey and Redis OSS parameters, see [Valkey and Redis OSS parameters](ParameterGroups.Engine.md#ParameterGroups.Redis).

As you would expect, some parameter values, such as `maxmemory`, are determined by the engine and node type. For a table of these Memcached parameter values by node type, see [Memcached node-type specific parameters](ParameterGroups.Engine.md#ParameterGroups.Memcached.NodeSpecific). For a table of these Valkey and Redis OSS parameter values by node type, see [Redis OSS node-type specific parameters](ParameterGroups.Engine.md#ParameterGroups.Redis.NodeSpecific).

**Note**
For a list of Memcached-specific parameters, see [Memcached Specific Parameters](ParameterGroups.Engine.md#ParameterGroups.Memcached).

**Topics**
+ [Parameter management in ElastiCache](ParameterGroups.Management.md)
+ [Cache parameter group tiers in ElastiCache](ParameterGroups.Tiers.md)
+ [Creating an ElastiCache parameter group](ParameterGroups.Creating.md)
+ [Listing ElastiCache parameter groups by name](ParameterGroups.ListingGroups.md)
+ [Listing an ElastiCache parameter group's values](ParameterGroups.ListingValues.md)
+ [Modifying an ElastiCache parameter group](ParameterGroups.Modifying.md)
+ [Deleting an ElastiCache parameter group](ParameterGroups.Deleting.md)
+ [Engine specific parameters](ParameterGroups.Engine.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
