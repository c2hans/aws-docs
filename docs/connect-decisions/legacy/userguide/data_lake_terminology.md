---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/data_lake_terminology.html
---

# Terminology used in data lake
<a name="data_lake_terminology"></a>

The following terms are used in data lake:
+ **Entity** – Information about a data object for each category. For example, company, geography, and trading\_partner are entities for an organization. For more information, see [Data entities and columns used in AWS Supply Chain](data-model.md).
+ **Dataset** – Information related to the entity. You can have only one dataset per entity.
+ **Connector** – A way to import data into AWS Supply Chain.
+ **Recipe** – A set of steps that describes how to map source data into one dataset.
+ **Source Flows1** – Displays the datasets and fields that you uploaded.
+ **Destination Flows1** – Associates the data from your dataset to the AWS Supply Chain data entities in data lake.
+ **Source system1** – Your existing enterprise resource planning (ERP) system, Warehouse Management System (WMS), or any supply chain data management system.

1 – These terms are only displayed when you ingest data through Amazon S3 (or the **Upload any CSV** option in the web application).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
