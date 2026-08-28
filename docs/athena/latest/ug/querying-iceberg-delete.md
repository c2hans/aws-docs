---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-delete.html
---

# DELETE
<a name="querying-iceberg-delete"></a>

Athena Iceberg `DELETE` writes Iceberg position delete files to a table. This is known as a merge-on-read delete. In contrast to a copy-on-write delete, a merge-on-read delete is more efficient because it does not rewrite file data. When Athena reads Iceberg data, it merges the Iceberg position delete files with data files to produce the latest view of a table. To remove these position delete files, you can run the [REWRITE DATA compaction action](querying-iceberg-data-optimization.md#querying-iceberg-data-optimization-rewrite-data-action). `DELETE` operations are charged by the amount of data scanned. For syntax, see [DELETE](delete-statement.md).

The following example deletes rows from `iceberg_table` that have `c3` as the value for `category`.

```
DELETE FROM iceberg_table WHERE category='c3'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
