---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/use-intermediate-table.html
---

# Using an intermediate table in analyses
<a name="use-intermediate-table"></a>

After you populate an intermediate table and attach an analysis rule, you can reference it in queries just like a configured table.

**Discovering intermediate tables**

All collaboration members can view intermediate tables on the **Tables** tab of a collaboration. The table type is shown as "Intermediate table."

**Referencing in SQL**

Reference an intermediate table by name in your SQL query, just like you reference a configured table. For example:

```
SELECT * FROM my_intermediate_table
```

**Referencing in PySpark**

In a PySpark analysis template, reference an intermediate table through the context object:

```
context['referencedTables']['my_intermediate_table']
```

**Requirements at analysis time**

AWS Clean Rooms enforces the following requirements when you run an analysis that references an intermediate table:
+ The intermediate table schema status must be **Ready** (populated and analysis rule attached).
+ The analysis rule is validated against inherited constraints from base tables.
+ Deferred controls are enforced, including disallowedOutputColumns and allowedResultReceivers.

**Using in ML workflows**

You can reference intermediate tables in ML workflows through the dataSource.protectedQueryInputParameters configuration.

**Viewing the schema**

To view the columns available in an intermediate table, choose the **Schema** tab on the intermediate table details page. You can view the column name and type. Choose **Edit schema** to update column types.

**Viewing dependencies**

To view the base tables that an intermediate table depends on, choose the **Dependencies** tab. You can view the table name, owner, type, and parent type for each dependency.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
