---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/postgresql-query-tuning/in-exists.html
---

# Use case 4 – IN or EXISTS
<a name="in-exists"></a>

If the query has `IN` or `NOT IN` operators, we recommend checking the query plan to confirm that the proper index is being used. If the proper index isn't being used and query performance is taking more time than expected, try to rewrite the query using the `EXISTS` or `NOT EXISTS` conditions.

Consider the following example, which uses `NOT IN`:

```
EXPLAIN ANALYZE SELECT
  TEST_VEH.TEST_VEH_ID,
  TEST_VEH.VEHICLE_ID,
  TEST_VEH.SERVICEPROGRAM_ID,
  TEST_VEH.STARTDATE,
  TEST_VEH.ENDDATE,
  TEST_VEH.OILTYPE_ID
FROM PERF_USER.TEST_VEH TEST_VEH
JOIN  PERF_USER.OILTYPE OT ON  OT.OILTYPE_ID =TEST_VEH.OILTYPE_ID
JOIN  PERF_USER.SERVICEPROGRAM SP ON  SP.SERVICEPROGRAM_ID = TEST_VEH.SERVICEPROGRAM_ID
WHERE SP.PROGNAME  = '18FCE8FDAF365BB'
  AND OT.OILTYPE_ID  =3
  AND TEST_VEH.ENDDATE  IS NOT NULL
  AND TEST_VEH.TEST_VEH_ID NOT IN
                      (SELECT TEST_VEH_ID
                              FROM PERF_USER.VEHICLESERVICEHISTORY
                              WHERE  TEST_VEH_ID > 1
                      );
-----------------------------------------------------------------------
"Nested Loop  (cost=1009.16..1188860356305.01 rows=1 width=76) (actual time=37299.891..37347.853 rows=0 loops=1)"
"  ->  Gather  (cost=1009.16..1188860356303.88 rows=1 width=76) (actual time=37299.890..37347.849 rows=0 loops=1)"
"        Workers Planned: 2"
"        Workers Launched: 2"
"        ->  Hash Join  (cost=9.16..1188860355303.78 rows=1 width=76) (actual time=37286.742..37286.751 rows=0 loops=3)"
"              Hash Cond: ((test_veh.serviceprogram_id)::text = (sp.serviceprogram_id)::text)"
"              ->  Parallel Index Scan using test_veh_oiltype_id_ind on test_veh  (cost=0.56..1188860351273.04 rows=1072570 width=76) (actual time=37276.290..37276.292 rows=1 loops=3)"
"                    Index Cond: (oiltype_id = 3)"
"                    Filter: ((enddate IS NOT NULL) AND (NOT (SubPlan 1)))"
"                    Rows Removed by Filter: 0"
"                    SubPlan 1"
"                      ->  Materialize  (cost=0.00..1025071.31 rows=33333332 width=8) (actual time=0.418..23201.432 rows=25001498 loops=4)"
"                            ->  Seq Scan on vehicleservicehistory  (cost=0.00..728195.65 rows=33333332 width=8) (actual time=0.416..13249.975 rows=25001498 loops=4)"
"                                  Filter: (test_veh_id > 1)"
"              ->  Hash  (cost=8.58..8.58 rows=1 width=11) (actual time=9.045..9.046 rows=0 loops=3)"
"                    Buckets: 1024  Batches: 1  Memory Usage: 8kB"
"                    ->  Index Scan using progname_id_ind on serviceprogram sp  (cost=0.56..8.58 rows=1 width=11) (actual time=9.043..9.044 rows=0 loops=3)"
"                          Index Cond: ((progname)::text = '18FCE8FDAF365BB'::text)"
"  ->  Seq Scan on oiltype ot  (cost=0.00..1.12 rows=1 width=8) (never executed)"
"        Filter: (oiltype_id = 3)"
"Planning Time: 37.696 ms"
"Execution Time: 37366.335 ms"
```

The query is taking more than 37 seconds 366 milliseconds to retrieve 4 million records.

The query plan states that a sequence scan is performed on the table used in the subquery `vehicleservicehistory`. The sequence scan is producing a large number of records. For each of those records in the subquery, the query is performing a full table scan, which is causing the performance issue.

To avoid the sequence scan on the subquery, rewrite the subquery to use a correlated subquery with `NOT EXISTS`. The correlated subquery will use an index scan and a reduced number of table scans:

```
EXPLAIN ANALYZE SELECT
  TEST_VEH.TEST_VEH_ID,
  TEST_VEH.VEHICLE_ID,
  TEST_VEH.SERVICEPROGRAM_ID,
  TEST_VEH.STARTDATE,
  TEST_VEH.ENDDATE,
  TEST_VEH.OILTYPE_ID
FROM PERF_USER.TEST_VEH TEST_VEH
JOIN  PERF_USER.OILTYPE OT ON  OT.OILTYPE_ID =TEST_VEH.OILTYPE_ID
JOIN  PERF_USER.SERVICEPROGRAM SP ON  SP.SERVICEPROGRAM_ID = TEST_VEH.SERVICEPROGRAM_ID
WHERE SP.PROGNAME  = '18FCE8FDAF365BB'
       AND OT.OILTYPE_ID  =3
       AND TEST_VEH.ENDDATE  IS NOT NULL
       AND  NOT EXISTS
                    (SELECT TEST_VEH_ID
                            FROM PERF_USER.VEHICLESERVICEHISTORY
                            WHERE TEST_VEH.TEST_VEH_ID=VEHICLESERVICEHISTORY.TEST_VEH_ID
                            AND TEST_VEH_ID > 1
                    );
---------------------------------------------------------------------
"Nested Loop Anti Join  (cost=1009.03..936146.10 rows=1 width=76) (actual time=12.693..12.810 rows=0 loops=1)"
"  ->  Nested Loop  (cost=1008.59..936141.78 rows=1 width=76) (actual time=12.692..12.809 rows=0 loops=1)"
"        ->  Gather  (cost=1008.59..936140.64 rows=1 width=76) (actual time=12.691..12.807 rows=0 loops=1)"
"              Workers Planned: 2"
"              Workers Launched: 2"
"              ->  Hash Join  (cost=8.59..935140.54 rows=1 width=76) (actual time=0.773..0.774 rows=0 loops=3)"
"                    Hash Cond: ((test_veh.serviceprogram_id)::text = (sp.serviceprogram_id)::text)"
"                    ->  Parallel Seq Scan on test_veh  (cost=0.00..927087.67 rows=2145139 width=76) (actual time=0.672..0.672 rows=1 loops=3)"
"                          Filter: ((enddate IS NOT NULL) AND (oiltype_id = 3))"
"                          Rows Removed by Filter: 7"
"                    ->  Hash  (cost=8.58..8.58 rows=1 width=11) (actual time=0.040..0.040 rows=0 loops=3)"
"                          Buckets: 1024  Batches: 1  Memory Usage: 8kB"
"                          ->  Index Scan using progname_id_ind on serviceprogram sp  (cost=0.56..8.58 rows=1 width=11) (actual time=0.039..0.040 rows=0 loops=3)"
"                                Index Cond: ((progname)::text = '18FCE8FDAF365BB'::text)"
"        ->  Seq Scan on oiltype ot  (cost=0.00..1.12 rows=1 width=8) (never executed)"
"              Filter: (oiltype_id = 3)"
"  ->  Index Only Scan using veh_ser_ind on vehicleservicehistory  (cost=0.44..4.32 rows=1 width=8) (never executed)"
"        Index Cond: ((test_veh_id = test_veh.test_veh_id) AND (test_veh_id > 1))"
"        Heap Fetches: 0"
"Planning Time: 11.115 ms"
"Execution Time: 12.871 ms"
```

After the modification, the query is taking less than 13 ms to process 4 million records

According to the query plan of the modified query, the table `vehicleservicehistory` can have an index scan. Using an index scan reduces the cost and the number of affected rows. This way, you can reduce the runtime of a query and increase its performance.
