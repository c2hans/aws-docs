---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_TABLES_SPACE_USAGE.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# SVV\_TABLES\_SPACE\_USAGE

SVV\_TABLES\_SPACE\_USAGE shows the storage capacity used by different table types on each compute node: local permanent tables, local temporary tables, and remote tables that this cluster accesses from other clusters through datashares. Each data block uses 1 MB.

Use SVV\_TABLES\_SPACE\_USAGE to see how much storage on each node your own tables use and how much data from remote tables on other clusters uses through data sharing. For the space used by individual tables, see [SVV\_TABLE\_INFO](r_SVV_TABLE_INFO.md). For the space used per block, see [SVV\_DISKUSAGE](r_SVV_DISKUSAGE.md) or [STV\_BLOCKLIST](r_STV_BLOCKLIST.md).

The SVV\_TABLES\_SPACE\_USAGE view summarizes information from the following system tables:
+  [STV\_NODE\_STORAGE\_CAPACITY](r_STV_NODE_STORAGE_CAPACITY.md)
+  [STV\_SLICES](r_STV_SLICES.md)
+  [STV\_TBL\_PERM](r_STV_TBL_PERM.md)

SVV\_TABLES\_SPACE\_USAGE is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="r_SVV_TABLES_SPACE_USAGE-table-columns"></a>

| Column name | Data type | Description |
| --- | --- | --- |
| node | integer | Node number. |
| capacity | bigint | The maximum number of 1 MB blocks the node can hold. This is the total storage capacity provisioned for the node, as in the capacity column of STV\_NODE\_STORAGE\_CAPACITY. For RA3 node types, this is the same as the total managed storage quota for the cluster. |
| local\_perm\_tables\_space\_used | bigint | Space used on the node by user-created permanent tables in all databases, in 1 MB blocks. This doesn't include system tables or tables that hold data shared from other clusters. |
| local\_temp\_tables\_space\_used | bigint | Space used on the node by temporary tables, in 1 MB blocks. |
| datasharing\_tables\_space\_used | bigint | Space used on the node by remote tables that this cluster accesses from other clusters through datashares, in 1 MB blocks. This is 0 on a cluster that doesn't consume any datashares. |

## Sample queries
<a name="r_SVV_TABLES_SPACE_USAGE-sample-queries"></a>

The following example returns the space usage of each node. These examples ran on a two-node RA3 cluster that consumes a datashare.

```
select * from svv_tables_space_usage order by node;

node | capacity  | local_perm_tables_space_used | local_temp_tables_space_used | datasharing_tables_space_used
-----+-----------+------------------------------+------------------------------+-------------------------------
   0 | 128000000 |                     39415933 |                            0 |                       3813397
   1 | 128000000 |                     36033602 |                            0 |                       3685379
(2 rows)
```

The following example returns the percentage of each node's capacity used by each kind of table.

```
select node,
       capacity,
       round(100.0 * local_perm_tables_space_used / capacity, 2) as pct_perm,
       round(100.0 * local_temp_tables_space_used / capacity, 2) as pct_temp,
       round(100.0 * datasharing_tables_space_used / capacity, 2) as pct_datasharing
from svv_tables_space_usage
order by node;

node | capacity  | pct_perm | pct_temp | pct_datasharing
-----+-----------+----------+----------+-----------------
   0 | 128000000 |    30.79 |     0.00 |            2.98
   1 | 128000000 |    28.15 |     0.00 |            2.88
(2 rows)
```

The following example returns the totals for the whole cluster.

```
select sum(capacity) as capacity,
       sum(local_perm_tables_space_used) as local_perm,
       sum(local_temp_tables_space_used) as local_temp,
       sum(datasharing_tables_space_used) as datasharing
from svv_tables_space_usage;

capacity  | local_perm | local_temp | datasharing
----------+------------+------------+-------------
256000000 |   75449535 |          0 |     7498776
(1 row)
```

The following example returns the free space and the percentage of free space on each node.

```
with node_usage as (
    select node,
           capacity,
           local_perm_tables_space_used + local_temp_tables_space_used
               + datasharing_tables_space_used as used
    from svv_tables_space_usage
)
select node,
       capacity,
       capacity - used as free_space,
       round(100.0 * (capacity - used) / capacity, 2) as pct_free
from node_usage
order by node;

node | capacity  | free_space | pct_free
-----+-----------+------------+----------
   0 | 128000000 |   84770670 |    66.23
   1 | 128000000 |   88281019 |    68.97
(2 rows)
```

## Usage notes
<a name="r_SVV_TABLES_SPACE_USAGE-usage-notes"></a>

Keep the following in mind when you use SVV\_TABLES\_SPACE\_USAGE:
+ On clusters with many tables, the query can take longer than most system view queries. Avoid running it at high frequency.
+ The view doesn't count a table that ALTER TABLE is rewriting until the ALTER finishes.
+ The view counts only space used by tables. For a node's actual free space, use STV\_NODE\_STORAGE\_CAPACITY.
