---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_SELECT_synopsis.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# SELECT
<a name="r_SELECT_synopsis"></a>

Returns rows from tables, views, and user-defined functions.

**Note**
The maximum size for a single SQL statement is 16 MB.

## Syntax
<a name="r_SELECT_synopsis-synopsis"></a>

```
[ WITH with_subquery [, ...] ]
SELECT
[ TOP number | [ ALL | DISTINCT ]
* | expression [ AS output_name ] [, ...] ]
[ EXCLUDE column_list ]
[ FROM table_reference [, ...] ]
[ WHERE condition ]
[ [ START WITH expression ] CONNECT BY expression ]
[ GROUP BY ALL | expression [, ...] ]
[ HAVING condition ]
[ QUALIFY condition ]
[ { UNION | ALL | INTERSECT | EXCEPT | MINUS } query ]
[ ORDER BY expression [ ASC | DESC ] ]
[ LIMIT { number | ALL } ]
[ OFFSET start ]
```

**Topics**
+ [Syntax](#r_SELECT_synopsis-synopsis)
+ [WITH clause](r_WITH_clause.md)
+ [SELECT list](r_SELECT_list.md)
+ [EXCLUDE column\_list](r_EXCLUDE_list.md)
+ [FROM clause](r_FROM_clause30.md)
+ [WHERE clause](r_WHERE_clause.md)
+ [GROUP BY clause](r_GROUP_BY_clause.md)
+ [HAVING clause](r_HAVING_clause.md)
+ [QUALIFY clause](r_QUALIFY_clause.md)
+ [UNION, INTERSECT, and EXCEPT](r_UNION.md)
+ [ORDER BY clause](r_ORDER_BY_clause.md)
+ [CONNECT BY clause](r_CONNECT_BY_clause.md)
+ [Subquery examples](r_Subquery_examples.md)
+ [Correlated subqueries](r_correlated_subqueries.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
