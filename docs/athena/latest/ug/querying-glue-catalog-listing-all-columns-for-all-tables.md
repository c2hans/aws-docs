---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-glue-catalog-listing-all-columns-for-all-tables.html
---

# List all columns for all tables
<a name="querying-glue-catalog-listing-all-columns-for-all-tables"></a>

You can list all columns for all tables in `AwsDataCatalog` or for all tables in a specific database in `AwsDataCatalog`.
+ To list all columns for all databases in `AwsDataCatalog`, use the query `SELECT * FROM information_schema.columns`.
+ To restrict the results to a specific database, use `table_schema='{{database_name}}'` in the `WHERE` clause.

**Example – Listing all columns for all tables in a specific database**
The following example query lists all columns for all tables in the database `webdata`.

```
SELECT * FROM information_schema.columns WHERE table_schema = 'webdata'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
