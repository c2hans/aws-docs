---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/postgresql-query-tuning/collations.html
---

# Use case 1 – Collations
<a name="collations"></a>

In a database, a collation is a set of rules for determining how data is sorted and compared. A collation is usually applied to how text data is sorted in different languages for indexing for making comparisons between text values. Different languages have different character sets and ordering. With a collation, you can sort character data for a given language by using rules that define the correct character sequence. You can also specify the following:
+ Case-sensitivity
+ Accent marks
+ Kana character types
+ Use of symbols or punctuation
+ Character width
+ Word sorting

There might be a performance impact if the join column uses a different collation. The following example query uses three tables, with a different collation for the join column.

|
|
| Table name | Column name |
| --- |--- |
| `rnr_segment` | `pnr_number character varying(15) COLLATE pg_catalog."C" NOT NULL` |
| `rnr_segment_pax` | `pnr_number character varying(15) COLLATE pg_catalog."default" NOT NULL` |
| `rnr_seat_numbers` | `pnr_number character varying(15) COLLATE pg_catalog."default" NOT NULL` |

```
EXPLAIN ANALYZE SELECT
A.PNR_NUMBER,
A.PAX_ID,
A.SEGMENT_ID,
B.OANDD_ID,
C.SEAT_ID,
C.BD_AIRPORT_CODE,
C.OFF_AIRPORT_CODE,
C.SEAT_NUMBER ,
B.CABIN_CLASS ,
A.SEGMENT_PAX_ID,
C.SEAT_ALLOC_ID,
C.SSR_ID,
C.SEAT_ATTRIBUTE_CODE
from
RNR_SEGMENT_PAX A,
RNR_SEGMENT B,
RNR_SEAT_NUMBERS C
where
B.AIRLINE_IATA_CODE = 'XX'
and B.FLIGHT_CARRIER = 'XX'
and B.FLIGHT_NUMBER = 140
and B.FLIGHT_SUFFIX ='*'
and B.FLIGHT_DATE_LTC = TO_DATE('01-JAN-2023', 'DD-MON-YYYY')
and A.AIRLINE_IATA_CODE = B.AIRLINE_IATA_CODE
and A.PNR_NUMBER = B.PNR_NUMBER
and A.SEGMENT_ID = B.SEGMENT_ID
and C.AIRLINE_IATA_CODE = B.AIRLINE_IATA_CODE
and C.PNR_NUMBER = B.PNR_NUMBER
and C.SEGMENT_ID = B.SEGMENT_ID
and A.PAX_ID = C.PAX_ID
and B.PNR_NUMBER in ('9F1588','E37DE0','04E82B','813D11','BFF10F');
```

The query plan for the previous query uses a sequence scan on the `rnr_seat_numbers` table even though that table has a proper index on the joined columns. The planner isn't using an index scan because these joined columns are using different collations:

```
Nested Loop  (cost=1112.14..927363.51 rows=1 width=833) (actual time=5395.367..5397.253 rows=0 loops=1)
  Join Filter: (((b.pnr_number)::text = (a.pnr_number)::text) AND (b.segment_id = a.segment_id))
  ->  Gather  (cost=1111.58..670766.48 rows=1 width=843) (actual time=5395.367..5397.251 rows=0 loops=1)
        Workers Planned: 2
        Workers Launched: 2
        ->  Hash Join  (cost=111.58..669766.38 rows=1 width=843) (actual time=5388.992..5388.993 rows=0 loops=3)
              Hash Cond: (((c.pnr_number)::text = (b.pnr_number)::text) AND (c.segment_id = b.segment_id))
              ->  Parallel Seq Scan on rnr_seat_numbers c  (cost=0.00..582154.96 rows=16666637 width=760) (actual time=0.008..2963.019 rows=13333333 loops=3)
                    Filter: ((airline_iata_code)::text = 'XX'::text)
              ->  Hash  (cost=111.52..111.52 rows=4 width=86) (actual time=0.121..0.121 rows=2 loops=3)
                    Buckets: 1024  Batches: 1  Memory Usage: 9kB
                    ->  Index Scan using rnr_segment_pk on rnr_segment b  (cost=0.56..111.52 rows=4 width=86) (actual time=0.082..0.116 rows=2 loops=3)
                          Index Cond: (((pnr_number)::text = ANY ('{9F1588,E37DE0,04E82B,813D11,BFF10F}'::text[])) AND ((airline_iata_code)::text = 'XX'::text))
                          Filter: (((flight_carrier)::text = 'XX'::text) AND (flight_number = 140) AND ((flight_suffix)::text = '*'::text) AND (flight_date_ltc = to_date('01-JAN-2023'::text, 'DD-MON-YYYY'::text)))
                          Rows Removed by Filter: 20
  ->  Index Scan using rnr_segment_pax_pk on rnr_segment_pax a  (cost=0.56..256597.02 rows=1 width=28) (never executed)
        Index Cond: (((airline_iata_code)::text = 'XX'::text) AND (segment_id = c.segment_id) AND (pax_id = c.pax_id))
        Filter: ((c.pnr_number)::text = (pnr_number)::text)
Planning Time: 0.982 ms
Execution Time: 5397.314 ms
```

To change the table column collation from the `"C"` language to the default collation provided by PostgreSQL, run the following `alter` statement, and then analyze the table:

```
alter table rnr_segment alter column pnr_number type character varying(15) COLLATE pg_catalog."default";

Analyze rnr_segment;
```

The query plan now uses an index scan, and the runtime is reduced.

```
Nested Loop  (cost=1.69..146.63 rows=1 width=833) (actual time=0.155..0.155 rows=0 loops=1)
  ->  Nested Loop  (cost=1.13..145.89 rows=1 width=111) (actual time=0.154..0.155 rows=0 loops=1)
        ->  Index Scan using rnr_segment_pk on rnr_segment b  (cost=0.56..111.51 rows=4 width=86) (actual time=0.048..0.097 rows=2 loops=1)
              Index Cond: (((pnr_number)::text = ANY ('{9F1588,E37DE0,04E82B,813D11,BFF10F}'::text[])) AND ((airline_iata_code)::text = 'XX'::text))
              Filter: (((flight_carrier)::text = 'XX'::text) AND (flight_number = 140) AND ((flight_suffix)::text = '*'::text) AND (flight_date_ltc = to_date('01-JAN-2023'::text, 'DD-MON-YYYY'::text)))
              Rows Removed by Filter: 20
        ->  Index Scan using rnr_segment_pax_pk on rnr_segment_pax a  (cost=0.56..8.58 rows=1 width=28) (actual time=0.027..0.027 rows=0 loops=2)
              Index Cond: (((airline_iata_code)::text = 'XX'::text) AND ((pnr_number)::text = (b.pnr_number)::text) AND (segment_id = b.segment_id))
  ->  Index Scan using rnr_seat_numbers_pk on rnr_seat_numbers c  (cost=0.56..0.72 rows=1 width=760) (never executed)
        Index Cond: (((pnr_number)::text = (a.pnr_number)::text) AND (segment_id = a.segment_id) AND (pax_id = a.pax_id) AND ((airline_iata_code)::text = 'XX'::text))
Planning Time: 1.432 ms
Execution Time: 0.207 ms
```
