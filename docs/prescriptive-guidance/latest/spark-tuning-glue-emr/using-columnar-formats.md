---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/spark-tuning-glue-emr/using-columnar-formats.html
---

# Using columnar formats for better query performance
<a name="using-columnar-formats"></a>

Spark can use various input file formats, such as Apache Parquet, Optimized Row Columnar (ORC), and CSV. However, Parquet works best within Spark SQL. It provides faster runtimes, higher scan throughput, reduced disk I/O, and lower cost of operation. Spark can automatically filter useless data by using Parquet file statistical data by push-down filters, such as min-max statistics. On the other hand, you can enable Spark parquet vectorized reader to read Parquet files by batch. When you are using Spark SQL to process data, we recommend that you use Parquet file formats if possible.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
