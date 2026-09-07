---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-optimization-for-enterpriseone/compression.html
---

# Configure data compression
<a name="compression"></a>

You can compress the tables and indexes in EnterpriseOne business data and control tables by using page or row compression. Most EnterpriseOne workloads on AWS exhibit the best performance with page compression, but extremely large workloads (multiples of uncompressed terabytes) might perform better with row compression. A detailed discussion of page versus row compression is beyond the scope of this guide. This section focuses primarily on page compression.

When you enable compression for normal EnterpriseOne workloads, there is a minimal increase in CPU usage but significant benefits to overall system performance, which can be measured in the following areas:
+ Smaller database sizes and storage requirements, because the data is stored on disk in a compressed format.
+ Higher buffer cache hit ratio, because the buffer cache can hold much more data when it's compressed.
+ Lower required Amazon EBS IOPS and throughput, because each I/O operation returns much more data, and fewer operations are required, because the buffer cache is more effective.
+ Faster backups, because data remains compressed throughout the backup process.

You can enable compression individually by table or by index alone. You can also choose the type of compression, either page or row, by table and index. It might be advantageous to not compress tables that are updated regularly, such as the F0002 (Next Number) and F0902 (Account Balances) tables. In many circumstances, enabling compression across all tables and indexes provides the easiest solution, because it provides most of the benefits without requiring an object-by-object analysis. The steps in this guide will compress all tables and indexes with page compression.

In some circumstances, compression might cause performance degradation, especially when third-party systems directly access the JD Edwards databases and perform table and index scan operations. This degradation is typically driven by poorly performing queries. In these cases, review the slow queries and use common optimization techniques to improve their performance. For example, consider rewriting the queries to use existing indexes or build new indexes.

Enabling compression is a multi-step process. Many of these steps require exclusive access to the database objects, which means that you would have to take EnterpriseOne and other systems offline. Follow these high-level steps to enable page compression on all tables and indexes in the DTA and CTL schemas:

1. Check disk space utilization before compression.

1. Run the enumeration script.

1. Run the compression script.

1. Check disk space utilization after compression.

## Check disk space utilization before compression
<a name="disk-space"></a>

To check the current disk space utilization of the database, run the following scripts.

```
USE JDE_PRIST920
SELECT DB_NAME() AS DbName,
    type_desc,
    CAST(FILEPROPERTY(name, 'SpaceUsed') AS INT)/128.0 AS SpaceUsedMB
FROM sys.database_files
WHERE type IN (0,1)
AND type_desc = 'ROWS';

SELECT SUM(CAST(FILEPROPERTY(name, 'SpaceUsed') AS INT)/128.0) AS TotalSpaceUsedMB
FROM sys.database_files
WHERE type IN (0,1)
AND type_desc = 'ROWS'
```

The output should be similar to the following:

![Disk space utilization before compression](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-optimization-for-enterpriseone/images/guide-img/1ded277e-59b3-4f6d-bcef-fa7d04f06c63/images/bd785879-8f95-40b6-b366-eb7c1c80e7e4.png)

In this example, the table rows occupy 3,407 MB of disk space.You will observe in this example that the ROWS are occupying 3407MB of diskspace.

## Run the enumeration script
<a name="enum-script"></a>

Because of the large volume of tables and indexes in the EnterpriseOne database, you can use a script to enumerate the objects to be compressed. The output of the enumeration script is the compression script that is used in the next section. Before you run the following script, update the schema owner names to reflect the owners of the tables and indexes that you want to compress.

```
declare @tblname as varchar(100)
declare @idxname as varchar(100)
declare @schemaname as varchar(100)
declare @sqlstatement as varchar(512)
declare tblcurs CURSOR for
    select t.name as tblname, s.name as schemaname
    from sys.tables t
    inner join sys.schemas s on t.schema_id = s.schema_id
    inner join sys.indexes i on i.object_id = t.object_id
    inner join sys.partitions p on i.object_id = p.object_id AND i.index_id = p.index_id
    where s.name  in ('PS920DTA', 'PS920CTL')
    and i.type_desc='CLUSTERED'
    and p.data_compression_desc <> 'PAGE'
open tblcurs
FETCH next from tblcurs into @tblname, @schemaname
while @@FETCH_STATUS = 0
begin

                FETCH next from tblcurs into @tblname, @schemaname
                set @sqlstatement = 'alter table ' + @schemaname + '.' + @tblname + ' rebuild with (DATA_COMPRESSION = PAGE)'
                print  @sqlstatement
end
close tblcurs
deallocate tblcurs
declare idxcurs CURSOR for
    select i.name as idxname, t.name as tblname, s.name as schemaname
    from sys.tables t
    inner join sys.schemas s on t.schema_id = s.schema_id
    inner join sys.indexes i on i.object_id = t.object_id
    inner jOIN sys.partitions p ON i.object_id = p.object_id AND i.index_id = p.index_id
    where s.name  in ('PS920DTA', 'PS920CTL')
    and p.data_compression_desc <> 'PAGE'
    and i.type_desc='NONCLUSTERED'
    and i.name is not null
open idxcurs
FETCH next from idxcurs into @idxname, @tblname, @schemaname
while @@FETCH_STATUS = 0
begin
                FETCH next from idxcurs into @idxname, @tblname, @schemaname
                set @sqlstatement = 'alter index ' + @idxname + ' on ' + @schemaname + '.' + @tblname + ' rebuild with (DATA_COMPRESSION = PAGE)'
                print  @sqlstatement
end
close idxcurs
deallocate idxcurs
```

## Run the compression script
<a name="compression-script"></a>

Review the output of the enumeration script that you ran in the last section. You can break this compression script up into smaller scripts and run them individually and in parallel.

|
|
| Important   Make sure that the EnterpriseOne system is offline when you run this script against your EnterpriseOne database.   |
| --- |

Here's an example of the compression script.

```
alter table PS920DTA.F07620 rebuild with (DATA_COMPRESSION = PAGE)
alter table PS920DTA.F760404A rebuild with (DATA_COMPRESSION = PAGE)
alter table PS920DTA.F31B93Z1 rebuild with (DATA_COMPRESSION = PAGE)
alter table PS920DTA.F31B65 rebuild with (DATA_COMPRESSION = PAGE)
alter table PS920DTA.F47156 rebuild with (DATA_COMPRESSION = PAGE)
alter table PS920DTA.F74F210 rebuild with (DATA_COMPRESSION = PAGE)
...
alter index F4611_16 on PS920DTA.F4611 rebuild with (DATA_COMPRESSION = PAGE)
alter index F4611_17 on PS920DTA.F4611 rebuild with (DATA_COMPRESSION = PAGE)
alter index F7000110_PK on PS920DTA.F7000110 rebuild with (DATA_COMPRESSION = PAGE)
alter index F7000110_3 on PS920DTA.F7000110 rebuild with (DATA_COMPRESSION = PAGE)
alter index F7000110_4 on PS920DTA.F7000110 rebuild with (DATA_COMPRESSION = PAGE)
alter index F76A801T_PK on PS920DTA.F76A801T rebuild with (DATA_COMPRESSION = PAGE)
...
```

## Check disk space utilization after compression
<a name="post-compression"></a>

To check the current disk space utilization of the database after compression, run the following script.

```
USE JDE_PRIST920
SELECT DB_NAME() AS DbName,
    type_desc,
    CAST(FILEPROPERTY(name, 'SpaceUsed') AS INT)/128.0 AS SpaceUsedMB
FROM sys.database_files
WHERE type IN (0,1)
AND type_desc = 'ROWS';

SELECT SUM(CAST(FILEPROPERTY(name, 'SpaceUsed') AS INT)/128.0) AS TotalSpaceUsedMB
FROM sys.database_files
WHERE type IN (0,1)
AND type_desc = 'ROWS'
```

The output should be similar to the following.

![Disk space utilization after compression](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-optimization-for-enterpriseone/images/guide-img/1ded277e-59b3-4f6d-bcef-fa7d04f06c63/images/82337489-46e7-42f8-b1ba-23042f640953.png)

In this example, you can see that space used dropped from 3,407 MB to 1,275 MB, which represents a 62 percent savings from compression. The savings for your database will vary based on how data is distributed among the tables in the database.
