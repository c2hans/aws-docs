---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/query-lifecycle-redshift/explain-operators.html
---

# EXPLAIN operators for Amazon Redshift query plans
<a name="explain-operators"></a>

This section briefly describes the operators that you see most often in the `EXPLAIN` output.

## Sequential scan
<a name="sequential-scan"></a>

The sequential scan operator (Seq Scan) indicates a table scan. Seq Scan scans each column in the table sequentially from beginning to end and evaluates query constraints (in the `WHERE` clause) for every row.

## Join operators
<a name="join-operators"></a>

Amazon Redshift selects join operators based on the physical design of the tables being joined, the location of the data required for the join, and the specific requirements of the query itself.

### Nested loop
<a name="nested-loop.70e17c9a-e81d-58fe-8637-9db5d04611c6"></a>

A nested loop is used mainly for cross-joins. Cross-joins are joins without a join condition that result in the Cartesian product of two tables. Nested loops are typically run as nested loop joins, which are the slowest of the possible join types. If a nested loop is present, you could see a nested loop alert event in the [STL\_ALERT\_EVENT\_LOG](https://docs.aws.amazon.com/redshift/latest/dg/r_STL_ALERT_EVENT_LOG.html) view. You can run the following query to identify the queries that have nested loops:

```
select q.query,
       trim(q.querytxt) as sql_query,
       q.starttime
from stl_query q
join stl_alert_event_log l
    on l.query = q.query
    and l.event like 'Nested Loop Join in the query plan%'
order by q.starttime desc;
```

### Hash join and hash
<a name="hash-join-and-hash.74144fc8-df0d-573b-8bc0-a810f7ca26dc"></a>

Hash join and hash operators are typically faster than a nested loop join. These operators are used for inner joins and left and right outer joins. You can use hash join and hash operators when joining tables where the join columns are not both distribution keys and sort keys. The hash operator creates the hash table for the inner table in the join. The hash join operator reads the outer table, hashes the joining column, and finds matches in the inner hash table.

### Merge join
<a name="merge-join.cfadd240-d49c-551c-b003-f3bdafca0eb0"></a>

The merge join operator is typically the fastest join and is used for inner joins and outer joins. The merge join isn't used for full joins. You can use a merge join when joining tables where the join columns are both distribution keys and sort keys, and when less than 20 percent of the joining tables are unsorted. The merge join operator reads two sorted tables in order and finds the matching rows. To view the percent of unsorted rows, query the [SVV\_TABLE\_INFO](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_TABLE_INFO.html) system table.

## Aggregate operators
<a name="aggregate-operators"></a>

The query plan uses the following operators in queries that involve aggregate functions and `GROUP BY` operations:
+ **Aggregate** – Operator for scalar aggregate functions such as `AVG` and `SUM`
+ **HashAggregate** – Operator for unsorted grouped aggregate functions
+ **GroupAggregate** – Operator for sorted grouped aggregate functions

### Sort operators
<a name="sort-operators.9b0add5c-49f4-5f2c-825a-1ad471102085"></a>

The query plan uses the following operators when queries have to sort or merge result sets:
+ **Sort** – Evaluates the `ORDER BY` clause and other sort operations, such as sorts required by `UNION` queries and joins, `SELECT DISTINCT` queries, and window functions
+ **Merge** – Produces final sorted results according to intermediate sorted results that derive from parallel operations

### UNION, INTERSECT, and EXCEPT operators
<a name="union--intersect--and-except-operators.8814e9b8-6245-5132-bdfd-4f1d8c73b439"></a>

The query plan uses the following operators for queries that involve set operations with `UNION`, `INTERSECT`, and `EXCEPT`:
+ **Subquery** – Used to run `UNION` queries
+ **Hash Intersect Distinct** – Used to run `INTERSECT` queries
+ **SetOp Except** – Used to run `EXCEPT` (or `MINUS`) queries

### Other operators
<a name="other-operators.f098d5d6-e152-5f6d-9db2-c47c92ede93d"></a>

The following operators also appear frequently in `EXPLAIN` output for routine queries:
+ **Unique** – Removes duplicates for `SELECT DISTINCT` queries and `UNION` queries
+ **Limit** – Processes the `LIMIT` clause
+ **Window** – Runs window functions
+ **Result** – Runs scalar functions that don't involve any table access
+ **Subplan** – Used for certain subqueries
+ **Network** – Sends intermediate results to the leader node for further processing
+ **Materialize** – Saves rows for input to nested loop joins and some merge joins
