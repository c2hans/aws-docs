---
source_url: https://docs.aws.amazon.com/security-lake/latest/userguide/source-management.html
---

# Source management in Security Lake
<a name="source-management"></a>

Sources are logs and events generated from a single system that match a specific event class in the [Open Cybersecurity Schema Framework (OCSF) in Security Lake](open-cybersecurity-schema-framework.md) schema. Amazon Security Lake can collect logs and events from a variety of sources, including natively supported AWS services and third-party custom sources.

Security Lake runs extract, transform, and load (ETL) jobs on raw source data, and converts the data to Apache Parquet format and the OCSF schema. After processing, Security Lake stores source data in an Amazon Simple Storage Service (Amazon S3) bucket in your AWS account in the AWS Region that the data was generated in. Security Lake creates a different Amazon S3 bucket for each Region in which you enable the service. Each source gets a separate prefix in your S3 bucket, and Security Lake organizes data from each source in a separate set of AWS Lake Formation tables.

**Topics**
+ [Collecting data from AWS services in Security Lake](internal-sources.md)
+ [Collecting data from custom sources in Security Lake](custom-sources.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
