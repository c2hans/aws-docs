---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-update.html
---

# UPDATE
<a name="querying-iceberg-update"></a>

Athena Iceberg `UPDATE` writes Iceberg position delete files and newly updated rows as data files in the same transaction. `UPDATE` can be imagined as a combination of `INSERT INTO` and `DELETE`. `UPDATE` operations are charged by the amount of data scanned. For syntax, see [UPDATE](update-statement.md).

The following example updates the specified values in the table `iceberg_table`.

```
UPDATE iceberg_table SET category='c2' WHERE category='c1'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
