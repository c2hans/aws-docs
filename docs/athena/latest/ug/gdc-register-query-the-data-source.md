---
source_url: https://docs.aws.amazon.com/athena/latest/ug/gdc-register-query-the-data-source.html
---

# Query AWS Glue data catalogs in Athena
<a name="gdc-register-query-the-data-source"></a>

To query data catalogs from Athena, do one of the following.
+ Register the catalog in Athena as a data source, then use the data source name to query the catalog. In this usage, the following queries are equivalent.

  ```
  SELECT * FROM my_data_source.my_database.my_table
  ```
+ If you are querying a catalog that has not been registered as an Athena data source, you can supply the full path to the catalog in your `SELECT` queries, as in the following example.

  ```
  SELECT * FROM "my_catalog/my_subcatalog".my_database.my_table
  ```
+ You can also do this through the AWS Management Console.

  1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/)

  1. In the query editor, for **Data source**, choose **AwsDataCatalog**.

  1. For **Catalog**, choose the name of the catalog that you want to use.

  1. For **Database**, choose the database that contains the table that you want to query.

  1. Enter a query like `SELECT * FROM {{my_table}}`, and then choose **Run**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
