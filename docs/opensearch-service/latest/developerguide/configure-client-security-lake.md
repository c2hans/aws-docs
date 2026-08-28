---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-security-lake.html
---

# Using an OpenSearch Ingestion pipeline with Amazon Security Lake
<a name="configure-client-security-lake"></a>

You can use the [S3 source plugin](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/s3/) to ingest data from [Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html) into your OpenSearch Ingestion pipeline. Security Lake automatically centralizes security data from AWS environments, on-premises environments, and SaaS providers into a purpose-built data lake. You can create a subscription that replicates data from Security Lake to your OpenSearch Ingestion pipeline, which then writes it to your OpenSearch Service domain or OpenSearch Serverless collection.

To configure your pipeline to read from Security Lake, use the preconfigured Security Lake blueprint. The blueprint includes a default configuration for ingesting Open Cybersecurity Schema Framework (OCSF) parquet files from Security Lake. For more information, see [Working with blueprints](pipeline-blueprint.md).

**Topics**
+ [Using an OpenSearch Ingestion pipeline with Amazon Security Lake as a source](configure-client-source-security-lake.md)
+ [Using an OpenSearch Ingestion pipeline with Amazon Security Lake as a sink](configure-client-sink-security-lake.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
