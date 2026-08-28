---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-glue-catalog-listing-columns-in-common.html
---

# List the columns that specific tables have in common
<a name="querying-glue-catalog-listing-columns-in-common"></a>

You can list the columns that specific tables in a database have in common.
+ Use the syntax `SELECT column_name FROM information_schema.columns`.
+ For the `WHERE` clause, use the syntax `WHERE table_name IN ('table1', 'table2')`.

**Example – Listing common columns for two tables in the same database**
The following example query lists the columns that the tables `table1` and `table2` have in common.

```
SELECT column_name
FROM information_schema.columns
WHERE table_name IN ('table1', 'table2')
GROUP BY column_name
HAVING COUNT(*) > 1;
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
