---
source_url: https://docs.aws.amazon.com/glue/latest/dg/auto-column-stats-generation.html
---

# Automatic column statistics generation
<a name="auto-column-stats-generation"></a>

Automatic generation of column statistics allows you to schedule and automatically compute statistics on new tables in the AWS Glue Data Catalog. When you enable automatic statistics generation, the Data Catalog discovers new tables with specific data formats such as Parquet, JSON, CSV, XML, ORC, ION, and Apache Iceberg, along with their individual bucket paths. With a one-time catalog configuration, the Data Catalog generates statistics for these tables.

 Data lake administrators can configure the statistics generation by selecting the default catalog in the Lake Formation console, and enabling table statistics using the `Optimization configuration` option. When you create new tables or update existing tables in the Data Catalog, the Data Catalog collects the number of distinct values (NDVs) for Apache Iceberg tables, and additional statistics such as the number of nulls, maximum, minimum, and average length for other supported file formats on a weekly basis.

If you have configured statistics generation at the table-level or if you have previously deleted the statistics generation settings for a table, those table-specific settings take precedence over the default catalog settings for automatic column statistics generation.

 Automatic statistics generation task analyzes 50% of records in the tables to calculate statistics. Automatic column statistics generation ensures that the Data Catalog maintains weekly metrics that can be used by query engines like Amazon Athena and Amazon Redshift Spectrum for improved query performance and potential cost savings. It allows scheduling statistics generation using AWS Glue APIs or the console, providing an automated process without manual intervention.

**Topics**
+ [Enabling catalog-level automatic statistics generation](enable-auto-column-stats-generation.md)
+ [Viewing automated table-level settings](view-auto-column-stats-settings.md)
+ [Disabling catalog-level column statistics generation](disable-auto-column-stats-generation.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
