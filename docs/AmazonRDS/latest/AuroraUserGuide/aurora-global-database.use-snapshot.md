---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.use-snapshot.html
---

# Creating an Amazon Aurora global database from an Aurora or Amazon RDS snapshot
<a name="aurora-global-database.use-snapshot"></a>

You can restore a snapshot of an Aurora DB cluster or from an Amazon RDS DB instance to use as the starting point for your Aurora global database. You restore the snapshot and create a new Aurora provisioned DB cluster at the same time. You then add another AWS Region to the restored DB cluster, thus turning it into an Aurora global database. Any Aurora DB cluster that you create using a snapshot in this way becomes the primary cluster of your Aurora global database.

The snapshot that you use can be from a `provisioned` or from a `serverless` Aurora DB cluster.

During the restore process, choose the same DB engine type as the snapshot. For example, suppose that you want to restore a snapshot that was made from an Aurora Serverless DB cluster running Aurora PostgreSQL. In this case, you create an Aurora PostgreSQL DB cluster using that same Aurora DB engine and version.

 The restored DB cluster assumes the role of primary cluster for the Aurora global database when you add an AWS Region to it. All data contained in this primary cluster is replicated to any secondary clusters that you add to your Aurora global database.

![the restore snapshot page for an Aurora global database.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/aurora-global-databases-restore-snapshot-01.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
