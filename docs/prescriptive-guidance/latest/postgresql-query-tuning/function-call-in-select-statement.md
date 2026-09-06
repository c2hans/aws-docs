---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/postgresql-query-tuning/function-call-in-select-statement.html
---

# Use case 3 – Function call in the SELECT statement
<a name="function-call-in-select-statement"></a>

Calling a function in a `where` clause can reduce query performance when the function is `VOLATILE` and you don't use the `select` keyword while calling the function:

```
Select * from tab_name where FieldName = FunctionName(parameters);
```

An index scan runs if the `select` statement is used while calling the function:

```
Select * from tab_name where FieldName = ( select FunctionName(parameters) );
```

The `pnr_number` field has an index in the `rnr_expiry_date` table. The index is used when comparing the value in the `where` clause.

```
explain analyze select * from perf_user.rnr_expiry_date where pnr_number= 'EE9F41';

"Index Scan using rnr_expiry_date_idx3 on rnr_expiry_date  (cost=0.29..8.31 rows=1 width=72) (actual time=0.020..0.021 rows=1 loops=1)"
"  Index Cond: ((pnr_number)::text = 'EE9F41'::text)"
"Planning Time: 0.063 ms"
"Execution Time: 0.038 ms"
```

A sequential scan is performed when a function is called without the `select` keyword even when an index is available on the field.

```
explain analyze select * from perf_user.rnr_expiry_date where pnr_number= perf_user.return_data();

"Seq Scan on rnr_expiry_date  (cost=0.00..27084.00 rows=1 width=72) (actual time=0.112..135.917 rows=1 loops=1)"
"  Filter: ((pnr_number)::text = (perf_user.return_data())::text)"
"  Rows Removed by Filter: 99999"
"Planning Time: 0.053 ms"
"Execution Time: 136.803 ms"
```

An index scan is performed when the function is called with the `select` keyword.

```
explain analyze select * from perf_user.rnr_expiry_date where pnr_number= (select perf_user.return_data() );

"Index Scan using rnr_expiry_date_idx3 on rnr_expiry_date  (cost=0.55..8.57 rows=1 width=72) (actual time=0.058..0.061 rows=1 loops=1)"
"  Index Cond: ((pnr_number)::text = ($0)::text)"
"  InitPlan 1 (returns $0)"
"    ->  Result  (cost=0.00..0.26 rows=1 width=32) (actual time=0.021..0.022 rows=1 loops=1)"
"Planning Time: 0.147 ms"
"Execution Time: 0.111 ms"
```
