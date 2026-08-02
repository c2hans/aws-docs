---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/postgresql-query-tuning/common-table-expressions.html
---

# Use case 5 – Subqueries or CTEs
<a name="common-table-expressions"></a>

Common Table Expressions (CTEs) help break down large queries into smaller queries. This makes the whole query easier to maintain.

Subquery joins are replaced by CTE joins, which are more readable because the query is named and separated inside the CTE section. This is especially helpful when the size of the query grows and the query becomes harder to maintain. In addition, the CTE results in PostgreSQL are materialized. If you call the CTE in multiple places, the actual query definition will be run only one time. The result will be stored in memory. You can use this for any complex logic that must be used in multiple places in the same query. Put that logic inside a CTE, and call the CTE any number of times.

For example, a customer was using inline application queries with many subqueries within queries. The subqueries were filtered by input parameter values sent from the applications.

```
EXPLAIN  ANALYZE
SELECT * FROM
ORDER_DETAILS A
WHERE A.ORDID IN  (SELECT ORDID FROM PAYMENT_DETAILS)
AND A.ORDID IN  (SELECT ORDID FROM   ITEM_DETAILS  )
AND  A.ORDID = 1000000;
```

```
"Nested Loop Semi Join  (cost=3000.00..194258.21 rows=5 width=74) (actual time=201.605..747.945 rows=5 loops=1)"
"  ->  Nested Loop Semi Join  (cost=2000.00..135040.47 rows=5 width=74) (actual time=146.016..666.779 rows=5 loops=1)"
"        ->  Gather  (cost=1000.00..78580.31 rows=5 width=74) (actual time=58.893..463.570 rows=5 loops=1)"
"              Workers Planned: 2"
"              Workers Launched: 2"
"              ->  Parallel Seq Scan on order_details a  (cost=0.00..77579.81 rows=2 width=74) (actual time=165.627..549.702 rows=2 loops=3)"
"                    Filter: (ordid = 1000000)"
"                    Rows Removed by Filter: 1666665"
"        ->  Materialize  (cost=1000.00..56460.07 rows=3 width=4) (actual time=17.424..40.638 rows=1 loops=5)"
"              ->  Gather  (cost=1000.00..56460.06 rows=3 width=4) (actual time=87.113..203.178 rows=1 loops=1)"
"                    Workers Planned: 2"
"                    Workers Launched: 2"
"                    ->  Parallel Seq Scan on payment_details  (cost=0.00..55459.76 rows=1 width=4) (actual time=174.431..423.792 rows=1 loops=3)"
"                          Filter: (ordid = 1000000)"
"                          Rows Removed by Filter: 1333002"
"  ->  Materialize  (cost=1000.00..59217.64 rows=4 width=4) (actual time=11.117..16.231 rows=1 loops=5)"
"        ->  Gather  (cost=1000.00..59217.62 rows=4 width=4) (actual time=55.581..81.148 rows=1 loops=1)"
"              Workers Planned: 2"
"              Workers Launched: 2"
"              ->  Parallel Seq Scan on item_details  (cost=0.00..58217.22 rows=2 width=4) (actual time=287.030..411.004 rows=1 loops=3)"
"                    Filter: (ordid = 1000000)"
"                    Rows Removed by Filter: 1333080"
"Planning Time: 0.266 ms"
"Execution Time: 747.986 ms"
```

After modifying the subqueries by using a CTE and adding filters so that only required row sets are retrieved, the query performance improves.

```
EXPLAIN  ANALYZE
WITH PAYMENT AS
 (
	 SELECT * FROM PAYMENT_DETAILS WHERE  ORDID = 1000000
 ),
ITEM AS
(SELECT * FROM ITEM_DETAILS  WHERE  ORDID = 1000000)
SELECT * FROM
ORDER_DETAILS A JOIN PAYMENT B
ON A.ORDID=B.ORDID
JOIN ITEM C ON B.ORDID=C.ORDID
```

```
"Nested Loop  (cost=3000.00..194258.91 rows=60 width=166) (actual time=586.410..732.918 rows=80 loops=1)"
"  ->  Nested Loop  (cost=2000.00..115677.83 rows=12 width=92) (actual time=456.760..457.083 rows=16 loops=1)"
"        ->  Gather  (cost=1000.00..59217.62 rows=4 width=48) (actual time=153.802..154.060 rows=4 loops=1)"
"              Workers Planned: 2"
"              Workers Launched: 2"
"              ->  Parallel Seq Scan on item_details  (cost=0.00..58217.22 rows=2 width=48) (actual time=85.417..249.045 rows=1 loops=3)"
"                    Filter: (ordid = 1000000)"
"                    Rows Removed by Filter: 1333332"
"        ->  Materialize  (cost=1000.00..56460.07 rows=3 width=44) (actual time=75.738..75.753 rows=4 loops=4)"
"              ->  Gather  (cost=1000.00..56460.06 rows=3 width=44) (actual time=302.947..303.005 rows=4 loops=1)"
"                    Workers Planned: 2"
"                    Workers Launched: 2"
"                    ->  Parallel Seq Scan on payment_details  (cost=0.00..55459.76 rows=1 width=44) (actual time=184.609..294.784 rows=1 loops=3)"
"                          Filter: (ordid = 1000000)"
"                          Rows Removed by Filter: 1333332"
"  ->  Materialize  (cost=1000.00..78580.34 rows=5 width=74) (actual time=8.103..17.238 rows=5 loops=16)"
"        ->  Gather  (cost=1000.00..78580.31 rows=5 width=74) (actual time=129.641..275.795 rows=5 loops=1)"
"              Workers Planned: 2"
"              Workers Launched: 2"
"              ->  Parallel Seq Scan on order_details a  (cost=0.00..77579.81 rows=2 width=74) (actual time=78.556..268.994 rows=2 loops=3)"
"                    Filter: (ordid = 1000000)"
"                    Rows Removed by Filter: 1666665"
"Planning Time: 0.108 ms"
"Execution Time: 732.953 ms"
```

These are the observations from the example data. When you run the query on a huge dataset, the difference in performance will be very high.
