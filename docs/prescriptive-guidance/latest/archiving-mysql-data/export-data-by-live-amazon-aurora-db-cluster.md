---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/archiving-mysql-data/export-data-by-live-amazon-aurora-db-cluster.html
---

# Export data from a live Aurora DB cluster
<a name="export-data-by-live-amazon-aurora-db-cluster"></a>

You can export data from a live Amazon Aurora DB cluster to an S3 bucket. The export process runs in the background and doesn't affect the performance of your active DB cluster.

By default, all data in the DB cluster is exported. However, you can choose to export specific sets of databases, schemas, or tables. Aurora clones the DB cluster, extracts data from the clone, and stores the data in an S3 bucket. The data is stored in an Apache Parquet format that is compressed and consistent. Individual Parquet files are usually 1–10 MB in size.

For more information, see the [Aurora documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/export-cluster-data.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
