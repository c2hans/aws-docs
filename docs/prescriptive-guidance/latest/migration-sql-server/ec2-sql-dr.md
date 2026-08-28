---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/ec2-sql-dr.html
---

# Disaster recovery
<a name="ec2-sql-dr"></a>

Many organizations implement high availability for their SQL Server databases, but that isn't sufficient for organizations that require true IT resilience. We recommend that you implement a disaster recovery solution to avoid data loss and downtime of mission-critical databases. Adopting a multi-Region disaster recovery architecture for your SQL Server deployments help you:
+ Achieve business continuity
+ Improve latency for your geographically distributed customer base
+ Satisfy your auditing and regulatory requirements

Options for disaster recovery include [log shipping](log-shipping.md), [Always On availability groups](always-on.md), [Amazon EBS snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-copy-snapshot.html) that are stored in Amazon S3 and replicated across AWS Regions, [Always On Failover Cluster Instances (FCIs)](ec2-sql-ha.md#ec2-fci) combined with Always On availability groups, and distributed availability groups.

## Distributed availability groups
<a name="ec2-distributed-groups"></a>

An architecture with distributed availability groups is an optimal approach for multi-Region SQL Server deployment. A distributed availability group is a special type of availability group that spans two separate availability groups. You can think of it as an availability group of availability groups. The underlying availability groups are configured on two different WSFC clusters.

Distributed availability groups are loosely coupled, which means that they don't require a single WSFC cluster and they're maintained by SQL Server. Because the WSFC clusters are maintained individually and transmissions are primarily asynchronous between two availability groups, it's easier to configure disaster recovery at another site. The primary replicas in each availability group synchronize their own secondary replicas.

Distributed availability groups support only manual failover at this time. To ensure that no data is lost, stop all transactions on the global primary databases (that is, on the databases of the primary availability group). Then set the distributed availability group to synchronous commit.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
