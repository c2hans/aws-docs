---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/postgresql-maintenance-rds-aurora/reindex.html
---

# Rebuilding indexes
<a name="reindex"></a>

The PostgreSQL `REINDEX` command rebuilds an index by using the data that's stored in the index's table and replacing the old copy of the index. We recommend that you use `REINDEX` in the following scenarios:
+ When an index becomes corrupted and no longer contains valid data. This can happen as a result of software or hardware failures.
+ When queries that previously used the index stop using it.
+ When the index becomes bloated with a large number of empty or nearly empty pages. You should run `REINDEX` when the bloat percentage (`bloat_pct`) is greater than 20.

The following query helps you find `bloat_pct`.

```
SELECT current_database(), nspname AS schemaname, tblname, idxname, bs*(relpages)::bigint AS real_size,
  bs*(relpages-est_pages)::bigint AS extra_size,
  100 * (relpages-est_pages)::float / relpages AS extra_pct,
  fillfactor,
  CASE WHEN relpages > est_pages_ff
    THEN bs*(relpages-est_pages_ff)
    ELSE 0
  END AS bloat_size,
  100 * (relpages-est_pages_ff)::float / relpages AS bloat_pct,
  is_na
  -- , 100-(pst).avg_leaf_density AS pst_avg_bloat, est_pages, index_tuple_hdr_bm, maxalign, pagehdr, nulldatawidth, nulldatahdrwidth, reltuples, relpages -- (DEBUG INFO)
FROM (
  SELECT coalesce(1 +
         ceil(reltuples/floor((bs-pageopqdata-pagehdr)/(4+nulldatahdrwidth)::float)), 0 -- ItemIdData size + computed avg size of a tuple (nulldatahdrwidth)
      ) AS est_pages,
      coalesce(1 +
         ceil(reltuples/floor((bs-pageopqdata-pagehdr)*fillfactor/(100*(4+nulldatahdrwidth)::float))), 0
      ) AS est_pages_ff,
      bs, nspname, tblname, idxname, relpages, fillfactor, is_na
      -- , pgstatindex(idxoid) AS pst, index_tuple_hdr_bm, maxalign, pagehdr, nulldatawidth, nulldatahdrwidth, reltuples -- (DEBUG INFO)
  FROM (
      SELECT maxalign, bs, nspname, tblname, idxname, reltuples, relpages, idxoid, fillfactor,
            ( index_tuple_hdr_bm +
                maxalign - CASE -- Add padding to the index tuple header to align on MAXALIGN
                  WHEN index_tuple_hdr_bm%maxalign = 0 THEN maxalign
                  ELSE index_tuple_hdr_bm%maxalign
                END
              + nulldatawidth + maxalign - CASE -- Add padding to the data to align on MAXALIGN
                  WHEN nulldatawidth = 0 THEN 0
                  WHEN nulldatawidth::integer%maxalign = 0 THEN maxalign
                  ELSE nulldatawidth::integer%maxalign
                END
            )::numeric AS nulldatahdrwidth, pagehdr, pageopqdata, is_na
            -- , index_tuple_hdr_bm, nulldatawidth -- (DEBUG INFO)
      FROM (
          SELECT n.nspname, i.tblname, i.idxname, i.reltuples, i.relpages,
              i.idxoid, i.fillfactor, current_setting('block_size')::numeric AS bs,
              CASE -- MAXALIGN: 4 on 32bits, 8 on 64bits (and mingw32 ?)
                WHEN version() ~ 'mingw32' OR version() ~ '64-bit|x86_64|ppc64|ia64|amd64' THEN 8
                ELSE 4
              END AS maxalign,
              /* per page header, fixed size: 20 for 7.X, 24 for others */
              24 AS pagehdr,
              /* per page btree opaque data */
              16 AS pageopqdata,
              /* per tuple header: add IndexAttributeBitMapData if some cols are null-able */
              CASE WHEN max(coalesce(s.null_frac,0)) = 0
                  THEN 8 -- IndexTupleData size
                  ELSE 8 + (( 32 + 8 - 1 ) / 8) -- IndexTupleData size + IndexAttributeBitMapData size ( max num filed per index + 8 - 1 /8)
              END AS index_tuple_hdr_bm,
              /* data len: we remove null values save space using it fractionnal part from stats */
              sum( (1-coalesce(s.null_frac, 0)) * coalesce(s.avg_width, 1024)) AS nulldatawidth,
              max( CASE WHEN i.atttypid = 'pg_catalog.name'::regtype THEN 1 ELSE 0 END ) > 0 AS is_na
          FROM (
              SELECT ct.relname AS tblname, ct.relnamespace, ic.idxname, ic.attpos, ic.indkey, ic.indkey[ic.attpos], ic.reltuples, ic.relpages, ic.tbloid, ic.idxoid, ic.fillfactor,
                  coalesce(a1.attnum, a2.attnum) AS attnum, coalesce(a1.attname, a2.attname) AS attname, coalesce(a1.atttypid, a2.atttypid) AS atttypid,
                  CASE WHEN a1.attnum IS NULL
                  THEN ic.idxname
                  ELSE ct.relname
                  END AS attrelname
              FROM (
                  SELECT idxname, reltuples, relpages, tbloid, idxoid, fillfactor, indkey,
                      pg_catalog.generate_series(1,indnatts) AS attpos
                  FROM (
                      SELECT ci.relname AS idxname, ci.reltuples, ci.relpages, i.indrelid AS tbloid,
                          i.indexrelid AS idxoid,
                          coalesce(substring(
                              array_to_string(ci.reloptions, ' ')
                              from 'fillfactor=([0-9]+)')::smallint, 90) AS fillfactor,
                          i.indnatts,
                          pg_catalog.string_to_array(pg_catalog.textin(
                              pg_catalog.int2vectorout(i.indkey)),' ')::int[] AS indkey
                      FROM pg_catalog.pg_index i
                      JOIN pg_catalog.pg_class ci ON ci.oid = i.indexrelid
                      WHERE ci.relam=(SELECT oid FROM pg_am WHERE amname = 'btree')
                      AND ci.relpages > 0
                  ) AS idx_data
              ) AS ic
              JOIN pg_catalog.pg_class ct ON ct.oid = ic.tbloid
              LEFT JOIN pg_catalog.pg_attribute a1 ON
                  ic.indkey[ic.attpos] <> 0
                  AND a1.attrelid = ic.tbloid
                  AND a1.attnum = ic.indkey[ic.attpos]
              LEFT JOIN pg_catalog.pg_attribute a2 ON
                  ic.indkey[ic.attpos] = 0
                  AND a2.attrelid = ic.idxoid
                  AND a2.attnum = ic.attpos
            ) i
            JOIN pg_catalog.pg_namespace n ON n.oid = i.relnamespace
            JOIN pg_catalog.pg_stats s ON s.schemaname = n.nspname
                                      AND s.tablename = i.attrelname
                                      AND s.attname = i.attname
            GROUP BY 1,2,3,4,5,6,7,8,9,10,11
      ) AS rows_data_stats
  ) AS rows_hdr_pdg_stats
) AS relation_stats
ORDER BY nspname, tblname, idxname;
```

Index pages that are completely empty are reclaimed for reuse. However, we recommend periodic reindexing if the index keys on a page have been deleted but space remains allocated.

Recreating the index helps provide better query performance. You can recreate an index in three ways, as described in the following table.

|
|
| Method | Description | Limitations |
| --- |--- |--- |
| `CREATE INDEX`** **`DROP INDEX`** with **`CONCURRENTLY` **option** | Builds a new index and removes the old index. The optimizer generates plans by using the newly created index instead of the old index. During low peak hours, you can drop the old index. | Index creation take more time when you use the `CONCURRENTLY` option, because it has to track all incoming changes. When changes are frozen, the process is marked as complete. |
| `REINDEX`** with the **`CONCURRENTLY`** option** | Locks write operations during the rebuild process. PostgreSQL version 12** **and later versions provide the `CONCURRENTLY` option, which avoids these locks.  | Using `CONCURRENTLY` requires a longer time to rebuild the index. |
| `pg_repack`** extension** | Cleans the bloat from a table and rebuilds the index. | You must run this extension from an EC2 instance or your local computer that is connected to the database. |

## Creating a new index
<a name="reindex-create"></a>

The `DROP INDEX` and `CREATE INDEX` commands, when used together, rebuild an index:

```
DROP INDEX <index_name>
CREATE INDEX <index_name> ON TABLE <table_name> (<column1>[,<column2>])
```

The disadvantage of this approach is its exclusive lock on the table, which impacts performance during this activity. The `DROP INDEX` command acquires an exclusive lock, which blocks both read and write operations on the table. The `CREATE INDEX` command blocks the write operations on the table. It allows read operations, but these are expensive during index creation.

## Rebuilding an index
<a name="reindex-rebuild"></a>

The `REINDEX` command helps you maintain consistent database performance. When you perform a large number of DML operations on a table, these result in both table and index bloat. Indexes are used to speed lookup on tables to improve query performance. Index bloating affects lookups and query performance. Therefore, we recommend that you perform reindexing on tables that have a high volume of DML operations to maintain consistency in the performance of queries.

The `REINDEX` command rebuilds the index from scratch by locking the write operations on the underlying table, but it allows read operations on the table. However, it does block the read operations on the index. Queries that use the corresponding index are blocked, but other queries aren't.

PostgreSQL version 12 introduced a new optional parameter, `CONCURRENTLY`, which rebuilds the index from scratch but doesn't lock the write or read operations on the table or on queries that use the index. However, it takes a longer time to complete the process when you use this option.

## Examples
<a name="reindex-examples"></a>

### Creating and dropping an index
<a name="creating-and-dropping-an-index.354cc544-b0b3-5c62-ad8d-50f655b0b695"></a>

Create a new index with the `CONCURRENTLY `option:

```
create index CONCURRENTLY on table(columns) ;
```

Drop the old index with the `CONCURRENTLY `option:

```
drop index CONCURRENTLY <index name> ;
```

### Rebuilding an index
<a name="rebuilding-an-index.e99c75c9-d884-5722-bdd9-52badcac082d"></a>

To rebuild a single index:

```
reindex index <index name> ;
```

To rebuild all indexes in a table:

```
reindex table <table name> ;
```

 To rebuild all indexes in a schema:

```
reindex schema <schema name> ;
```

### Rebuilding an index concurrently
<a name="rebuilding-an-index-concurrently.a13a2a57-c988-57c6-8bab-dc86813e65ba"></a>

To rebuild a single index:

```
reindex index CONCURRENTLY  <indexname> ;
```

To rebuild all indexes in a table:

```
reindex table CONCURRENTLY  <tablename> ;
```

To rebuild all indexes in a schema:

```
reindex schema CONCURRENTLY  <schemaname> ;
```

### Rebuilding or relocating indexes only
<a name="rebuilding-or-relocating-indexes-only.5d684b78-d2bc-5f20-82e8-8cfd95088ff7"></a>

To rebuild a single index:

```
pg_repack -h <hostname> -d <dbname> -i <indexname> -k
```

To rebuild all indexes:

```
pg_repack -h <hostname> -d <dbname> -x <indexname> -t <tablename> -k
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
