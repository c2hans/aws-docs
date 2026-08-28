---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-centric-use-cases/data-lifecycle.html
---

# Data lifecycle
<a name="data-lifecycle"></a>

To build a data pipeline, you must first ingest data into AWS from an external or internal data source, such as a file server, database, storage bucket, or from an API call. The ingested data may or may not go through transformation, such as anonymization, column dropping, or data cleaning.

This section provides an overview of the stages in the data lifecycle process, as shown in the following diagram.

![Data lifecycle overview diagram](http://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-centric-use-cases/images/guide-img/058e3d2f-f726-4dc0-989b-0f15dcd3bc33/images/4b010983-8fd8-4a6f-96bc-0b9638da76eb.png)

These stages include the following:
+ Data collection
+ Data preparation and cleaning
+ Data quality checks
+ Data visualization and analysis
+ Monitoring and debugging
+ IaC deployment
+ Automation and access control

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
