---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aurora-replication-options/aurora-global-database.html
---

# Aurora global databases
<a name="aurora-global-database"></a>

An Aurora global database consists of a primary Aurora DB cluster in one AWS Region, where your data is written, and up to five read-only secondary DB clusters in up to five other AWS Regions. You issue write operations directly to the primary DB cluster in the primary AWS Region. Aurora replicates data to the secondary AWS Regions using dedicated infrastructure, with latency typically under one second. For replication, Aurora global databases use the cluster storage volume instead of the database engine. For an example of an Aurora global database that spans two AWS Regions, see the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html).

Aurora global databases use storage block–based replication to keep the secondary clusters in sync. This replication is asynchronous, which means that writes on the primary cluster don't wait for the secondary cluster to receive and process the changes.

There are several limitations to note when you consider using an Aurora global database. For example, you cannot use the Backtrack feature in Aurora with an Aurora global database. For more information, see the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html#aurora-global-database.limitations).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
