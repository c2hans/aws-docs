---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/postgresql-query-tuning/explain-query-plan.html
---

# The EXPLAIN query plan
<a name="explain-query-plan"></a>

PostgreSQL provides the `EXPLAIN` and `EXPLAIN ANALYZE` options for returning query plans with details about how the query will be run.

## The EXPLAIN statement
<a name="explain"></a>

The `EXPLAIN` statement returns the query plan that the PostgreSQL planner generates for a given statement. The query plan shows the following:
+ How tables involved in a statement will be scanned (for example, by index scan or sequential scan)
+ How multiple tables will be joined (for example, hash join, merge join, or nested loop join)

Understanding the plan is critical when improving the performance of the query. After you understand the plan, you can focus on where the query is taking too long and take action to reduce the time.

## Using EXPLAIN ANALYZE
<a name="explain-analyze"></a>

In PostgreSQL, `EXPLAIN` will only generate a plan for the given statement. If you add the `ANALYZE` keyword, `EXPLAIN` will return the plan, run the query, and show the actual runtime and row count for each step. This is indispensable for analyzing the query performance.

|
|
| Important: When using `EXPLAIN ANALYZE`, be careful with `INSERT`, `UPDATE`, and `DELETE`. |
| --- |

## How to read the EXPLAIN query plan
<a name="read"></a>

A PostgreSQL query plan is a tree structure consisting of several nodes*.* The `EXPLAIN` query plan shows the steps that the database engine uses to run a query. The query plan provides the following information:
+ The type of operations performed, such as sequential scans, index scans, or nested loop joins.
+ A label, such as `Seq Scan`, `Index Scan`, or `Nested Loop`, to describe the operation being performed.
+ The name of the table or index being processed by the query.
+ Cost and row columns with information about the estimated cost in an arbitrary unit of computation and the number of rows processed.
+ The filter condition of any filter applied on the operation, such as the `where` condition.
+ A visual representation of the steps, with each operation shown as a node and arrows connecting the operations. The order of the operations is shown from left to right, with earlier operations feeding into later operations.

The following screenshot shows the query plan for a sequential scan.

![Query plan shown on the Data Output tab in pgAdmin.](https://docs.aws.amazon.com/prescriptive-guidance/latest/postgresql-query-tuning/images/guide-img/7b8a9711-9513-471f-b676-8df14916e186/images/30249088-2899-462f-8b65-fd26730cccdb.png)

The cost estimate `(cost=0.00..32.60 rows=2260 width=8)` means that PostgreSQL expects that the query will require 32.60 units of computation to return results.

The `0.00` value is the cost at which this node can begin working (in this case, startup time for the query). The `rows` value is the estimated number of rows that the sequential scan will return. The `width` value is the estimated size in bytes of the returned rows.

Because the example shows `EXPLAIN` with the `ANALYZE` option, the query was run, and the timing information was captured. The result `(actual time=0.120..0.121 rows=1 loops=1)` means the following:
+ The sequential scan was run one time (the `loops` value).
+ The scan returned one row.
+ The actual time was 0.12 milliseconds.
