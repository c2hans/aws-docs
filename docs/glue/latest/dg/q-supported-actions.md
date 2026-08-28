---
source_url: https://docs.aws.amazon.com/glue/latest/dg/q-supported-actions.html
---

# Supported code generation abilities
<a name="q-supported-actions"></a>

 The following are the combinations of the code generation abilities of Amazon Q data integration.

| Sources and Targets | Transformation |
| --- | --- |
| S3 with the following format types: json, csv, parquet, hudi, delta | Drop |
| AWS Glue Data Catalog | Aggregate |
| Redlake | DropDuplicates |
| Amazon DynamoDB | Join |
| MySQL | Filter |
| Oracle | RenameColumns |
| PostgresSQL | FillNull |
| Microsoft SQL Server | DropNull |
| Amazon DocumentDB / MongoDB | WithColumns |
| Snowflake | SQL Query |
| Google BigQuery | Union |
| Teradata | Select |
| Amazon OpenSearch Service |  |
| Vertica |  |
| SAP HANA |  |
| Amazon Redshift |  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
