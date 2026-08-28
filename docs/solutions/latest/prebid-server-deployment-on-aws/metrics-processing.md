---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/metrics-processing.html
---

# Metrics processing
<a name="metrics-processing"></a>

An AWS Glue job is configured to perform ETL operation on the metrics log data present in the S3 bucket containing the raw logs. The ETL operation structures the metric data present in the log files into a single database with several tables. For details, see [Glue table schemas](glue-table-schemas.md) in the Querying metrics with Athena section. The processed data is written into the `MetricsEtl` S3 bucket, which contains the metric log data transformed and partitioned through ETL in the previous steps. The data is made available via AWS AWS Glue Data Catalog, a persistent technical metadata store for analytics users to discover and prepare the data. Also, you can immediately search and query cataloged data using Amazon Athena, [Amazon EMR](https://aws.amazon.com/emr/), and [Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-using-spectrum.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Deploying a Prebid Server on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
