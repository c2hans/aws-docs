---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/query-lifecycle-redshift/explain-redistribution.html
---

# EXPLAIN data redistribution for Amazon Redshift query plans
<a name="explain-redistribution"></a>

During join steps, a slice may need to work with data not stored locally, and network transmission (movement of data between compute nodes) is the most expensive query operation.

The `EXPLAIN` output for joins also specifies a method for how data is moved around a cluster to facilitate the join. This data movement can be either a broadcast or a redistribution.
+ In a broadcast, the data values from one side of a join are copied from each compute node to every other compute node, so that every compute node ends up with a complete copy of the data.
+ In a redistribution, participating data values are sent from their current slice to a new slice (possibly on a different node). Data is typically redistributed to match the distribution key of the other table participating in the join if that distribution key is one of the joining columns. If neither of the tables has distribution keys on one of the joining columns, either both tables are distributed or the inner table is broadcast to every node.

The `EXPLAIN` output also references inner and outer tables.
+ The inner table is scanned first and appears near the bottom of the query plan. The inner table is the table that's probed for matching rows in the build table. Usually, an inner table held in memory is the source table for hashing, and if possible, is the smaller table of the two being joined.
+ The outer table is the source of rows to match against the inner table and is usually read from disk. The query optimizer chooses the inner and outer table based on database statistics from the latest run of the `ANALYZE` command. The order of tables in the `FROM` clause of a query doesn't determine which table is inner and which is outer.

Use the following attributes in query plans to identify how data is moved to facilitate a query:
+ **DS\_BCAST\_INNER** – Indicates that a copy of the entire inner join table is being broadcast to all compute nodes.
+ **DS\_DIST\_ALL\_NONE** – No redistribution is required because the inner table has already been distributed to every node using `DISTSTYLE ALL`. The entire table is located on every compute node.
+ **DS\_DIST\_NONE** – No redistribution is required because corresponding slices are collocated on the compute nodes. This is the most efficient option because there is no network transfer.
+ **DS\_DIST\_INNER** – Indicates that the inner join table is redistributed. If the inner table is much smaller or infrequently updated, consider changing that table to `DISTSTYLE ALL`.
+ **DS\_DIST\_OUTER** – Indicates that the outer join table is redistributed. If the outer table is much smaller or infrequently updated, consider changing that table to `DISTSTYLE ALL`.
+ **DS\_DIST\_ALL\_INNER** – Indicates that the inner join table is being sent to a single node because the join table uses `DISTSTYLE ALL`. This join is executed on a single node and is likely to be slow.
+ **DS\_DIST\_BOTH** – Indicates that both tables in the join are being redistributed to all nodes. This is the worst possible option.
