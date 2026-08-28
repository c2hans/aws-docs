---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-updating-iceberg-table-data.html
---

# Update Iceberg table data
<a name="querying-iceberg-updating-iceberg-table-data"></a>

You can manage Iceberg table data directly on Athena by using `INSERT`, `UPDATE`, and `DELETE` queries. Each data management transaction produces a new snapshot, which can be queried using time travel. The `UPDATE` and `DELETE` statements follow the Iceberg format v2 row-level [position delete](https://iceberg.apache.org/spec/#position-delete-files) specification and enforce snapshot isolation.

**Note**
Athena SQL does not currently support the copy-on-write approach. The `UPDATE`, `MERGE INTO`, and `DELETE FROM` operations always use the merge-on-read approach with positional deletes, regardless of specified table properties. In case you have setup table properties such as `write.update.mode`, `write.merge.mode`, and/or `write.delete.mode` to use copy-on-write, your queries won't fail as Athena will ignore them and keep using merge-on-read.

Use the following commands to perform data management operations on Iceberg tables.

**Topics**
+ [INSERT INTO](querying-iceberg-insert-into.md)
+ [DELETE](querying-iceberg-delete.md)
+ [UPDATE](querying-iceberg-update.md)
+ [MERGE INTO](querying-iceberg-merge-into.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
