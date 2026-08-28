---
source_url: https://docs.aws.amazon.com/glue/latest/dg/populate-dg-manual.html
---

# Defining metadata manually
<a name="populate-dg-manual"></a>

 The AWS Glue Data Catalog is a central repository that stores metadata about your data sources and data sets. While a crawler can automatically crawl and populate metadata for supported data sources, there are certain scenarios where you may need to define metadata manually in the Data Catalog:
+ Unsupported data formats – If you have data sources that are not supported by the crawler, you need to manually define the metadata for those data sources in the Data Catalog.
+ Custom metadata requirements – The AWS Glue crawler infers metadata based on predefined rules and conventions. If you have specific metadata requirements that are not covered by the AWS Glue crawler inferred metadata, you can manually define the metadata to meet your needs
+ Data governance and standardization – In some cases, you may want to have more control over the metadata definitions for data governance, compliance, or security reasons. Manually defining metadata allows you to ensure that the metadata adheres to your organization's standards and policies.
+ Placeholder for future data ingestion – If you have data sources that are not immediately available or accessible, you can create empty schema tables as placeholders. Once the data sources become available, you can populate the tables with the actual data, while maintaining the predefined structure.

 To define metadata manually, you can use the AWS Glue console, Lake Formation console, AWS Glue API, or the AWS Command Line Interface (AWS CLI). You can create databases, tables, and partitions, and specify metadata properties such as column names, data types, descriptions, and other attributes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
