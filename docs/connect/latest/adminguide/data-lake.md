---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/data-lake.html
---

# Connect Customer data lake
<a name="data-lake"></a>

You can use the Connect Customer data lake as a central location to query various types of data from Connect Customer. This data includes contact records, conversational analytics data, performance evaluations, and more. Data is refreshed after a record is created with a small delay for processing and should be available in less than an hour. You can use the data lake to create custom reports or run SQL queries.

For information about related API actions, see [Data lake actions](https://docs.aws.amazon.com/connect/latest/APIReference/analyticsdataset-api.html) in the *Connect Customer API Reference*.

**Topics**
+ [Access the data lake](access-datalake.md)
+ [Associate tables](datalake-tables.md)
+ [Manage access to Resource link tables](manage-access-to-resource-link-tables.md)
+ [Data type definitions](data-type-definitions.md)
+ [Data retention](data-lake-data-retention.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
