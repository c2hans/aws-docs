---
source_url: https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/rel-02.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL 2. How do you plan your network topology?
<a name="rel-02"></a>

Workloads often exist in multiple environments. These include multiple cloud environments (both publicly accessible and private) and possibly your existing data center infrastructure. Plans must include network considerations such as intra- and intersystem connectivity, public IP address management, private IP address management, and domain name resolution.

**Topics**
+ [REL02-BP01 Use highly available network connectivity for your workload public endpoints](rel_planning_network_topology_ha_conn_users.md)
+ [REL02-BP02 Provision redundant connectivity between private networks in the cloud and on-premises environments](rel_planning_network_topology_ha_conn_private_networks.md)
+ [REL02-BP03 Ensure IP subnet allocation accounts for expansion and availability](rel_planning_network_topology_ip_subnet_allocation.md)
+ [REL02-BP04 Prefer hub-and-spoke topologies over many-to-many mesh](rel_planning_network_topology_prefer_hub_and_spoke.md)
+ [REL02-BP05 Enforce non-overlapping private IP address ranges in all private address spaces where they are connected](rel_planning_network_topology_non_overlap_ip.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
