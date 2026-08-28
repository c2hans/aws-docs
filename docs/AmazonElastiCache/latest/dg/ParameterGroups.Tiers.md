---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ParameterGroups.Tiers.html
---

# Cache parameter group tiers in ElastiCache
<a name="ParameterGroups.Tiers"></a>

Amazon ElastiCache has three tiers of cache parameter groups as shown following.

![Image: Amazon ElastiCache parameter group tiers](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/images/ElastiCache-ParameterGroups-Tiers.png)

*Amazon ElastiCache parameter group tiers*

**Global Default**

The top-level root parameter group for all Amazon ElastiCache customers in the region.

The global default cache parameter group:
+ Is reserved for ElastiCache and not available to the customer.

**Customer Default**

A copy of the Global Default cache parameter group which is created for the customer's use.

The Customer Default cache parameter group:
+ Is created and owned by ElastiCache.
+ Is available to the customer for use as a cache parameter group for any clusters running an engine version supported by this cache parameter group.
+ Cannot be edited by the customer.

**Customer Owned**

A copy of the Customer Default cache parameter group. A Customer Owned cache parameter group is created whenever the customer creates a cache parameter group.

The Customer Owned cache parameter group:
+ Is created and owned by the customer.
+ Can be assigned to any of the customer's compatible clusters.
+ Can be modified by the customer to create a custom cache parameter group. 

   Not all parameter values can be modified. For more information on Memcached values, see [Memcached specific parameters](ParameterGroups.Engine.md#ParameterGroups.Memcached). For more information on Valkey and Redis OSS values, see [Valkey and Redis OSS parameters](ParameterGroups.Engine.md#ParameterGroups.Redis).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
