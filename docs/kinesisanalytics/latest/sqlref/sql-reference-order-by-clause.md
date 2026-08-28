---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-order-by-clause.html
---

# ORDER BY clause
<a name="sql-reference-order-by-clause"></a>

A streaming query can use ORDER BY if its leading expression is time-based and monotonic. For example, a streaming query whose leading expression is based on the ROWTIME column can use ORDER BY to do the following operations:
+ Sort the results of a streaming GROUP BY.
+ Sort a batch of rows arriving within a fixed time window of a stream.
+ Perform streaming ORDER BY on windowed-joins.

The "time-based and monotonic" requirement on the leading expression means that the query

```
CREATE OR REPLACE PUMP "STREAM_PUMP" AS INSERT INTO "DESTINATION_SQL_STREAM"
SELECT STREAM DISTINCT ticker FROM trades ORDER BY ticker
```

will fail, but the query

```
CREATE OR REPLACE PUMP "STREAM_PUMP" AS INSERT INTO "DESTINATION_SQL_STREAM"
SELECT STREAM DISTINCT rowtime, ticker FROM trades ORDER BY ROWTIME, ticker
```

will succeed.

**Note**
The preceding examples use the `DISTINCT` clause to remove duplicate instances of the same ticker symbol from the result set, so that the results will be monotonic.

Streaming ORDER BY sorts rows using SQL-2008 compliant syntax for the ORDER BY clause. It can be combined with a UNION ALL statement, and can sort on expressions, such as:

```
CREATE OR REPLACE PUMP "STREAM_PUMP" AS INSERT INTO "DESTINATION_SQL_STREAM"
SELECT STREAM x, y FROM t1
UNION ALL
SELECT STREAM a, b FROM t2 ORDER BY ROWTIME, MOD(x, 5)
```

The ORDER BY clause can specify ascending or descending sort order, and can use column ordinals, as well as ordinals specifying (referring to) the position of items in the select list.

**Note**
The `UNION` statement in the preceding query collects records from two separate streams for ordering.
<a name="TOC32"></a>
**Streaming ORDER BY SQL Declarations**
The streaming ORDER BY clause includes the following functional attributes:
+ Gathers rows until the monotonic expression in streaming ORDER BY clause does not change.
+ Does not require streaming GROUP BY clause in the same statement.
+ Can use any column with a basic SQL data type of TIMESTAMP, DATE, DECIMAL, INTEGER, FLOAT, CHAR, VARCHAR.
+ Does not require that columns/expressions in the ORDER BY clause be present in the SELECT list of the statement.
+ Applies all the standard SQL validation rules for ORDER BY clause.

The following query is an example of streaming ORDER BY:

```
CREATE OR REPLACE PUMP "STREAM_PUMP" AS INSERT INTO "DESTINATION_SQL_STREAM"
SELECT STREAM state, city, SUM(amount)
FROM orders
GROUP BY FLOOR(ROWTIME TO HOUR), state, city
ORDER BY FLOOR(ROWTIME TO HOUR), state, SUM(amount)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
