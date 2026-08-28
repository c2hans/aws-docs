---
source_url: https://docs.aws.amazon.com/athena/latest/ug/delta-lake-tables-querying.html
---

# Query Delta Lake tables with SQL
<a name="delta-lake-tables-querying"></a>

To query a Delta Lake table, use standard SQL `SELECT` syntax:

```
[ WITH with_query [, ...] ]SELECT [ ALL | DISTINCT ] select_expression [, ...]
[ FROM from_item [, ...] ]
[ WHERE condition ]
[ GROUP BY [ ALL | DISTINCT ] grouping_element [, ...] ]
[ HAVING condition ]
[ { UNION | INTERSECT | EXCEPT } [ ALL | DISTINCT ] select ]
[ ORDER BY expression [ ASC | DESC ] [ NULLS FIRST | NULLS LAST] [, ...] ]
[ OFFSET count [ ROW | ROWS ] ]
[ LIMIT [ count | ALL ] ]
```

For more information about `SELECT` syntax, see [SELECT](select.md) in the Athena documentation.

The Delta Lake format stores the minimum and maximum values per column of each data file. Athena makes use of this information to enable file skipping on predicates to eliminate unnecessary files from consideration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
