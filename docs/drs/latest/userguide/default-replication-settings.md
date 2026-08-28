---
source_url: https://docs.aws.amazon.com/drs/latest/userguide/default-replication-settings.html
---

# AWS DRS default replication
<a name="default-replication-settings"></a>

 **Default replication** settings are created during the DRS Service Initialization within a Region. [Learn more about configuring your **Default replication** settings](getting-started-initializing.md). The options configured within the **Default replication** automatically apply to any newly added Source Server. Any changes made to the **Default replication** only apply to any Source Server added after the changes were made, they do not automatically update the corresponding settings on existing Source Servers.

 Most Replication Settings can be configured through the Default replication settings:

| Replication setting | Default replication |
| --- | --- |
| Staging area subnet | Supported |
| Replication server instance type | Supported |
| EBS volume type | Supported |
| EBS encryption | Supported |
| Automatically replicate new disks | Supported |
| Always use AWS Elastic Disaster Recovery security group | Supported |
| Security Group | Supported |
| Dedicated instance for replication server | Unsupported |
| Data Routing (Private IP) | Supported |
| IP Version | Supported |
| Create public IP | Supported |
| Network Bandwidth Throttling | Supported |
| Point in time (PIT) policy | Supported |
| MAP program tagging | Supported |
| Tags | Supported |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
