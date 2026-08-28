---
source_url: https://docs.aws.amazon.com/memorydb/latest/devguide/parametergroups.html
---

# Configuring engine parameters using parameter groups
<a name="parametergroups"></a>

MemoryDB uses parameters to control the runtime properties of your nodes and clusters. Generally, newer engine versions include additional parameters to support the newer functionality. For tables of parameters, see [Engine specific parameters](parametergroups.redis.md).

As you would expect, some parameter values, such as `maxmemory`, are determined by the engine and node type. For a table of these parameter values by node type, see [MemoryDB node-type specific parameters](parametergroups.redis.md#parametergroups.redis.nodespecific).

**Topics**
+ [Parameter management](parametergroups.management.md)
+ [Parameter group tiers](parametergroups.tiers.md)
+ [Creating a parameter group](parametergroups.creating.md)
+ [Listing parameter groups by name](parametergroups.listingGroups.md)
+ [Listing a parameter group's values](parametergroups.listingValues.md)
+ [Modifying a parameter group](parametergroups.modifying.md)
+ [Deleting a parameter group](parametergroups.deleting.md)
+ [Engine specific parameters](parametergroups.redis.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
