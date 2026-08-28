---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-glue-catalog-listing-partitions.html
---

# List partitions for a specific table
<a name="querying-glue-catalog-listing-partitions"></a>

You can use `SHOW PARTITIONS {{table_name}}` to list the partitions for a specified table, as in the following example.

```
SHOW PARTITIONS cloudtrail_logs_test2
```

You can also use a `$partitions` metadata query to list the partition numbers and partition values for a specific table.

**Example – Querying the partitions for a table using the $partitions syntax**
The following example query lists the partitions for the table `cloudtrail_logs_test2` using the `$partitions` syntax.

```
SELECT * FROM default."cloudtrail_logs_test2$partitions" ORDER BY partition_number
```
The following table shows sample results.

|  | table\_catalog | table\_schema | table\_name | Year | Month | Day |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | awsdatacatalog | default | cloudtrail\_logs\_test2 | 2020 | 08 | 10 |
| 2 | awsdatacatalog | default | cloudtrail\_logs\_test2 | 2020 | 08 | 11 |
| 3 | awsdatacatalog | default | cloudtrail\_logs\_test2 | 2020 | 08 | 12 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
