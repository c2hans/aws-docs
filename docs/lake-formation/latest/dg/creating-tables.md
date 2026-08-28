---
source_url: https://docs.aws.amazon.com/lake-formation/latest/dg/creating-tables.html
---

# Creating tables
<a name="creating-tables"></a>

AWS Lake Formation metadata tables contain information about data in the data lake, including schema information, partition information, and data location. These tables are stored in the AWS Glue Data Catalog. You use them to access underlying data in the data lake and manage that data with Lake Formation permissions. Tables are stored within databases in the Data Catalog.

There are several ways to create Data Catalog tables:
+ Run a crawler in AWS Glue. See [Defining crawlers](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) in the *AWS Glue Developer Guide*.
+ Create and run a workflow. See [Importing data using workflows in Lake Formation](workflows.md).
+ Create a table manually using the Lake Formation console, AWS Glue API, or AWS Command Line Interface (AWS CLI).
+ Create a table using Amazon Athena.
+ Create a resource link to a table in an external account. See [Creating resource links](creating-resource-links.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
