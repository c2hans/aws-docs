---
source_url: https://docs.aws.amazon.com/memorydb/latest/devguide/parametergroups.tiers.html
---

# Parameter group tiers
<a name="parametergroups.tiers"></a>

*MemoryDB parameter group tiers*

**Global Default**

The top-level root parameter group for all MemoryDB customers in the region.

The global default parameter group:
+ Is reserved for MemoryDB and not available to the customer.

**Customer Default**

A copy of the Global Default parameter group which is created for the customer's use.

The Customer Default parameter group:
+ Is created and owned by MemoryDB.
+ Is available to the customer for use as a parameter group for any clusters running an engine version supported by this parameter group.
+ Cannot be edited by the customer.

**Customer Owned**

A copy of the Customer Default parameter group. A Customer Owned parameter group is created whenever the customer creates a parameter group.

The Customer Owned parameter group:
+ Is created and owned by the customer.
+ Can be assigned to any of the customer's compatible clusters.
+ Can be modified by the customer to create a custom parameter group. 

   Not all parameter values can be modified. For more information, see [Engine specific parameters](parametergroups.redis.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
