---
source_url: https://docs.aws.amazon.com/glue/latest/dg/developing-blueprints-samples.html
---

# Blueprint samples
<a name="developing-blueprints-samples"></a>

There are a number of sample blueprint projects available on the [AWS Glue blueprint Github repository](https://github.com/awslabs/aws-glue-blueprint-libs/tree/master/samples). These samples are for reference only and are not intended for production use.

The titles of the sample projects are:
+ Compaction: this blueprint creates a job that compacts input files into larger chunks based on desired file size.
+ Conversion: this blueprint converts input files in various standard file formats into Apache Parquet format, which is optimized for analytic workloads.
+ Crawling Amazon S3 locations: this blueprint crawls multiple Amazon S3 locations to add metadata tables to the Data Catalog.
+ Custom connection to Data Catalog: this blueprint accesses data stores using AWS Glue custom connectors, reads the records, and populates the table definitions in the AWS Glue Data Catalog based on the record schema.
+ Encoding: this blueprint converts your non-UTF files into UTF encoded files.
+ Partitioning: this blueprint creates a partitioning job that places output files into partitions based on specific partition keys.
+ Importing Amazon S3 data into a DynamoDB table: this blueprint imports data from Amazon S3 into a DynamoDB table.
+ Standard table to governed: this blueprint imports an AWS Glue Data Catalog table into a Lake Formation table.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
