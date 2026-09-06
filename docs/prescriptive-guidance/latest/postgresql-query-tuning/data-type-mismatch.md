---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/postgresql-query-tuning/data-type-mismatch.html
---

# Use case 2 – Data type mismatch
<a name="data-type-mismatch"></a>

Choosing the proper data type based on the data helps to provide the optimum balance between storage size and performance.

The following example query uses the `pnr_number` column to join two tables. The `pnr_number` column has different data types in different tables.

|
|
| Table name | Column name and data type |
| --- |--- |
| `perf_user.rnr_segment_pax` | `pnr_number character varying(6)` |
| `perf_user.rnr_expiry_date` | `pnr_number character(2)` |

```
EXPLAIN ANALYZE UPDATE perf_user.RNR_SEGMENT_PAX x SET ARC_EXPIRY_DATE = y.ARC_EXPIRY_DATE
       FROM (SELECT AIRLINE_IATA_CODE, PNR_NUMBER, ARC_EXPIRY_DATE, 0+row_num ROW_NUM
               FROM perf_user.RNR_EXPIRY_DATE
              WHERE airline_iata_code = 'XX'
                AND row_num BETWEEN (1*5000)+0 AND (1+1)*5000) y
         WHERE  x.airline_iata_code = y.airline_iata_code
             AND  x.PNR_NUMBER =y.PNR_NUMBER;

-----------------------------------------------------------------------------------------------

Update on rnr_segment_pax x  (cost=290.97..1104986.32 rows=15515 width=460) (actual time=14574.118..14574.120 rows=0 loops=1)
  ->  Hash Join  (cost=290.97..1104986.32 rows=15515 width=460) (actual time=16.967..14101.983 rows=11953 loops=1)
       Hash Cond: ((x.pnr_number)::text = (rnr_expiry_date.pnr_number)::text)
        ->  Seq Scan on rnr_segment_pax x  (cost=0.00..954539.00 rows=40000320 width=446) (actual time=0.011..9702.989 rows=40000000 loops=1)
              Filter: ((airline_iata_code)::bpchar = 'XX'::bpchar)
        ->  Hash  (cost=225.37..225.37 rows=5248 width=24) (actual time=16.540..16.541 rows=5001 loops=1)
              Buckets: 8192  Batches: 1  Memory Usage: 338kB
              ->  Index Scan using rnr_expiry_date_idx1 on rnr_expiry_date  (cost=0.29..225.37 rows=5248 width=24) (actual time=3.102..15.331 rows=5001 loops=1)
                    Index Cond: ((row_num >= 5000) AND (row_num <= 10000))
                    Filter: (airline_iata_code = 'XX'::bpchar)
Planning Time: 4.445 ms
Execution Time: 14574.322 ms
```

When you run `EXPLAIN ANALYZE`, the planner uses a sequence scan on `rnr_segment_pax` instead of an index scan even though the columns used in the join have indexes. The planner isn't using an index scan because the columns used in the join are different lengths.

Alter the table columns to keep the data type the same for both tables involved in the join condition, and then analyze the table:

```
alter table perf_user.rnr_expiry_date alter column airline_iata_code type character varying(6) ;

analyze perf_user.rnr_expiry_date;
```

Now the tables have the same length on both of the columns that are used in the join condition.

Run `EXPLAIN ANALYZE` again. The planner performs an index scan, which improves the query performance significantly.

```
Update on rnr_segment_pax x  (cost=0.86..59733.09 rows=14637 width=460) (actual time=416.653..416.654 rows=0 loops=1)
  ->  Nested Loop  (cost=0.86..59733.09 rows=14637 width=460) (actual time=0.103..91.106 rows=11953 loops=1)
        ->  Index Scan using rnr_expiry_date_idx1 on rnr_expiry_date  (cost=0.29..212.69 rows=4951 width=24) (actual time=0.025..3.023 rows=5001 loops=1)
              Index Cond: ((row_num >= 5000) AND (row_num <= 10000))
              Filter: ((airline_iata_code)::text = 'XX'::text)
        ->  Index Scan using rnr_segment_pax_pk on rnr_segment_pax x  (cost=0.56..11.99 rows=3 width=446) (actual time=0.014..0.016 rows=2 loops=5001)
              Index Cond: (((airline_iata_code)::text = 'XX'::text) AND ((pnr_number)::text = (rnr_expiry_date.pnr_number)::text))
Planning Time: 0.310 ms
Execution Time: 416.696 ms
```
