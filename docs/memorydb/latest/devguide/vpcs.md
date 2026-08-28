---
source_url: https://docs.aws.amazon.com/memorydb/latest/devguide/vpcs.html
---

# MemoryDB and Amazon VPC
<a name="vpcs"></a>

The Amazon Virtual Private Cloud (Amazon VPC) service defines a virtual network that closely resembles a traditional data center. When you configure a virtual private cloud (VPC) with Amazon VPC, you can select its IP address range, create subnets, and configure route tables, network gateways, and security settings. You can also add a cluster to the virtual network, and control access to the cluster by using Amazon VPC security groups.

This section explains how to manually configure a MemoryDB cluster in a VPC. This information is intended for users who want a deeper understanding of how MemoryDB and Amazon VPC work together.

**Topics**
+ [Understanding MemoryDB and VPCs](vpcs.mdb.md)
+ [Access Patterns for Accessing a MemoryDB Cluster in an Amazon VPC](memorydb-vpc-accessing.md)
+ [Creating a Virtual Private Cloud (VPC)](VPCs.creatingVPC.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
