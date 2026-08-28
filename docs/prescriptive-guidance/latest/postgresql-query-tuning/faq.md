---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/postgresql-query-tuning/faq.html
---

# FAQ
<a name="faq"></a>

Find answers to frequently raise questions about tuning query performance.

## What is EXPLAIN?
<a name="q-1"></a>

`EXPLAIN` is a keyword that you prepend to a PostgreSQL query (`SELECT`, `UPDATE`, `INSERT`, `DELETE`) to generate a query plan. The PostgreSQL query plan details how the database intends to run the query. This plan includes information about the order of a table scan, index usage, and joins.

Use the query plan to identify potential bottlenecks, optimize queries, and improve overall performance. When reviewing the query plan, consider the following factors:
+ Table access approaches
+ Join approaches
+ Filter conditions
+ Sort operations
+ Index usage
+ Parallelism
+ Statistics
+ Cost estimations
+ Rows retrieved from each step
+ Data distribution

For more information about [EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html), see the PostgreSQL documentation.

## What is EXPLAIN ANALYZE?
<a name="q-2"></a>

When you prepend `EXPLAIN ANALYZE` to a query and run the query, PostgreSQL runs the query and returns both the query plan and runtime statistics. The actual runtime, rows processed from each step, and other relevant information are displayed along with the query plan. Using `EXPLAIN ANALYZE` on a production database should be done with caution, because running the query could impact database performance during the analysis.

For more information about [EXPLAIN ANALYZE](https://www.postgresql.org/docs/current/sql-explain.html#:~:text=The%20ANALYZE%20option%20causes%20the,of%20rows%20it%20actually%20returned.), see the PostgreSQL documentation.

## What is collation in PostgreSQL?
<a name="q-3"></a>

In PostgreSQL, a collation is a set of rules for determining how strings are compared and sorted. The collation defines the order in which characters are considered in comparisons, considering language-specific rules and conversions.

For more information about [collation](https://www.postgresql.org/docs/current/collation.html#:~:text=The%20collation%20feature%20allows%20specifying,be%20changed%20after%20its%20creation.), see the PostgreSQL documentation.

## What is a CTE?
<a name="q-4"></a>

In a PostgreSQL database, a Common Table Expression (CTE) is a named temporary result set that you can reference. CTEs provide a way to create more readable and modular SQL queries by breaking down complex logic into smaller, named units.

For more information about [CTEs](https://www.postgresql.org/docs/current/queries-with.html), see the PostgreSQL documentation.

## What are the categories of functions in PostgreSQL?
<a name="1-5"></a>

Every PostgreSQL function has a volatility classification, with the possibilities being `VOLATILE`, `STABLE`, or `IMMUTABLE`:
+ **VOLATILE **– A `VOLATILE` function can do anything, including modify the database. It can return different results on successive calls with the same arguments. The optimizer makes no assumptions about the behavior of such functions. A query using a volatile function will re-evaluate the function at every row where its value is needed.
+ **STABLE **– A `STABLE` function can't modify the database. It's guaranteed to return the same results given the same arguments for all rows within a single statement. When you use this classification, the optimizer can optimize multiple calls of the function to a single call. In particular, it's safe to use an expression that contains such a function in an index scan condition. (Because an index scan will evaluate the comparison value only one time, not one time at each row, it isn't valid to use a `VOLATILE` function in an index scan condition.)
+ **IMMUTABLE** – An `IMMUTABLE` function can't modify the database and is guaranteed to return the same results given the same arguments forever. When you use this classification, the optimizer can pre-evaluate the function when a query calls it with constant arguments. For example, a query such as `SELECT ... WHERE x = 2 + 2` can be simplified on sight to `SELECT ... WHERE x = 4`, because the function underlying the integer addition operator is marked `IMMUTABLE`.

`VOLATILE` is the default if the `CREATE FUNCTION` command doesn't specify a category. For more information about [function types](https://www.postgresql.org/docs/16/sql-createfunction.html), see the PostgreSQL documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
