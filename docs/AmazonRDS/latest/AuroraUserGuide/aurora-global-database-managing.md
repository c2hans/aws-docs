---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-managing.html
---

# Managing an Amazon Aurora global database
<a name="aurora-global-database-managing"></a>

You perform most management operations on the individual clusters that make up an Aurora global database. When you choose **Group related resources** on the **Databases** page in the console, you see the primary cluster and secondary clusters grouped under the associated global database. To find the AWS Regions where a global database's DB clusters are running, its Aurora DB engine and version, and its identifier, use its **Configuration** tab.

 The cross-Region database failover processes are available to Aurora global databases only, not for a single Aurora DB cluster. To learn more, see [Using switchover or failover in Amazon Aurora Global Database](aurora-global-database-disaster-recovery.md).

 To recover an Aurora global database from an unplanned outage in its primary Region, see [Recovering an Amazon Aurora global database from an unplanned outage](aurora-global-database-disaster-recovery.md#aurora-global-database-failover).

**Topics**
+ [Modifying an Amazon Aurora global database](aurora-global-database-modifying.md)
+ [Modifying parameters for an Aurora global database](aurora-global-database-modifying.parameters.md)
+ [Removing a cluster from an Amazon Aurora global database](aurora-global-database-detaching.md)
+ [Deleting an Amazon Aurora global database](aurora-global-database-deleting.md)
+ [Tagging Amazon Aurora Global Database resources](aurora-global-database-tagging.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
