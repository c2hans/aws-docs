---
source_url: https://docs.aws.amazon.com/memorydb/latest/devguide/subnetgroups.ipcapacity.html
---

# Ensuring sufficient IP addresses for scaling operations
<a name="subnetgroups.ipcapacity"></a>

When you scale out a cluster by adding shards or replicas, MemoryDB provisions new nodes. Each node requires an available IP address in a subnet within the target Availability Zone. If the subnets in an Availability Zone do not have enough free IP addresses, the scaling operation can fail.

To avoid this issue, review the available IP address capacity of your subnet group's subnets before you scale. You can check the number of available IP addresses for each subnet with the Amazon EC2 `DescribeSubnets` API or in the Amazon VPC console.

If a subnet is approaching IP address exhaustion, take one of the following actions before you scale:
+ Add a subnet with sufficient available IP addresses to the subnet group in the same Availability Zone.
+ Free IP addresses in the existing subnet by removing unused resources such as unattached network interfaces.
+ Replace the subnet with one that uses a larger CIDR block.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
