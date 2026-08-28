---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/database-refactor-prioritization/appendix.html
---

# Appendix: Sample queries for PL/SQL object counts
<a name="appendix"></a>

Use the sample queries in this section to get PL/SQL object counts for your Oracle and SQL Server databases. You can wrap these queries in a script to collect the necessary data. To optimize, create a common user across all databases.

## Oracle databases
<a name="oracle"></a>

```
SELECT *
FROM
    (
      select
         host_name as SERVERNAME,
         instance_name as DATABASENAME,
         'ORACLE' as DATABASEENGINE,
         (
            select
               case
                  when
                     (
                        select
                           substr(value, - 7, 5)
                        from
                           v $ listener_network
                        where
                           type = 'LOCAL LISTENER'
                     )
                     like '%=%'
                  then
(
                     select
                        substr(value, - 6, 4)
                     from
                        v $ listener_network
                     where
                        type = 'LOCAL LISTENER')
                     else
(
                        select
                           substr(value, - 7, 5)
                        from
                           v $ listener_network
                        where
                           type = 'LOCAL LISTENER')
               end
                        from
                           dual
         )
         as DATABASEPORT,
         version as DATABASEVERSION,
         edition
      from
         v $ instance
    )
    q,
    (
      select
         obj.owner "APPSCHEMA",
          obj_cnt "TOTALOBJECTS",
         decode(seg_size, NULL, 0, seg_size) "SIZEINGB"
      from
         (
            select
               owner,
               count(*) obj_cnt
            from
               dba_objects
            where
               owner not in
               (
                  'RDSADMIN',
                  'SYS',
                  'SYSTEM',
                  'XS$NULL',
                  'OJVMSYS',
                  'LBACSYS',
                  'OUTLN',
                  'SYS$UMF',
                  'DBSNMP',
                  'SI_INFORMTN_SCHEMA',
                  'DVF',
                  'DVSYS',
                  'ORDPLUGINS',
                  'MDSYS',
                  'OLAPSYS',
                  'ORDDATA',
                  'XDB',
                  'WMSYS',
                  'ORDSYS',
                  'GSMCATUSER',
                  'MDDATA',
                  'REMOTE_SCHEDULER_AGENT',
                  'SYSBACKUP',
                  'ORACLE_OCM',
                  'SPATIAL_CSW_ADMIN_USR',
                  'PUBLIC',
                  'SYSBACKUP',
                  'SYSRAC',
                  'SYSKM',
                  'OUTLN',
                  'SYS$UMF',
                  'SYSDG',
                  'SYS',
                  'APPQOSSYS',
                  'DBSFWUSER',
                  'GGSYS',
                  'ANONYMOUS',
                  'CTXSYS',
                  'GSMADMIN_INTERNAL',
                  'XDB',
                   'DBSNMP',
                  'GSMCATUSER',
                  'REMOTE_SCHEDULER_AGENT',
                  'AUDSYS',
                  'DIP',
                  'GSMUSER',
                  'SVCSAMLMSRO',
                  'REMOTE_SCHEDULER_AGENT',
                  'PERFSTAT'
               )
            group by
               owner
         )
         obj,
         (
            select
               owner,
               ceil(sum(bytes) / 1024 / 1024 / 1024) seg_size
            from
               dba_segments
            where
               owner not in
               (
                  'RDSADMIN',
                  'SYS',
                  'SYSTEM',
                  'XS$NULL',
                  'OJVMSYS',
                  'LBACSYS',
                  'OUTLN',
                  'SYS$UMF',
                  'DBSNMP',
                  'SI_INFORMTN_SCHEMA',
                  'DVF',
                  'DVSYS',
                  'ORDPLUGINS',
                  'MDSYS',
                  'OLAPSYS',
                  'ORDDATA',
                  'XDB',
                  'WMSYS',
                  'ORDSYS',
                  'GSMCATUSER',
                  'MDDATA',
                  'REMOTE_SCHEDULER_AGENT',
                  'SYSBACKUP',
                  'ORACLE_OCM',
                  'SPATIAL_CSW_ADMIN_USR',
                  'PUBLIC',
                  'SYSBACKUP',
                  'SYSRAC',
                  'SYSKM',
                  'OUTLN',
                  'SYS$UMF',
                  'SYSDG',
                  'SYS',
                  'APPQOSSYS',
                  'DBSFWUSER',
                  'GGSYS',
                  'ANONYMOUS',
                  'CTXSYS',
                  'GSMADMIN_INTERNAL',
                  'XDB',
                  'DBSNMP',
                  'GSMCATUSER',
                  'REMOTE_SCHEDULER_AGENT',
                  'AUDSYS',
                  'DIP',
                  'GSMUSER',
                  'SVCSAMLMSRO',
                  'REMOTE_SCHEDULER_AGENT',
                  'PERFSTAT'
               )
            group by
               owner
         )
         seg
      where
         obj.owner = seg.owner( + )
      order by
         3 desc,
         2 desc,
         1
    )
    b;
```

## SQL Server databases
<a name="sql"></a>

```
SELECT (SELECT
         @@ServerName)
       AS SERVERNAME,
       DB_NAME() AS DATABASENAME,
       'MSSQL' AS DATABASEENGINE,
       SERVERPROPERTY('PRODUCTVERSION') AS DATABASEVERSION,
       (SELECT
         -- '$($db.DatabasePort)'
         '1433')
       AS DATABASEPORT,
       SERVERPROPERTY('edition') AS EDITION,
       SCHEMA_NAME(so.schema_id) AS APPSCHEMA,
       (SELECT
         COUNT(*) cnt
       FROM sys.objects oo
       WHERE oo.schema_id = so.schema_id
       AND oo.[is_ms_shipped] = 0
       GROUP BY SCHEMA_NAME(schema_id))
       AS TOTALOBJECTS,
       CAST((SUM(ps.reserved_page_count) * 8.0 / 1024 / 1024) AS decimal(10, 2)) AS SIZEINGB
FROM sys.dm_db_partition_stats ps
JOIN sys.indexes i
  ON i.object_id = ps.object_id
  AND i.index_id = ps.index_id
JOIN sys.objects so
  ON i.object_id = so.object_id
WHERE so.type = 'U'
GROUP BY so.schema_id
ORDER BY OBJECT_SCHEMA_NAME(so.schema_id),
SIZEINGB DESC;
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
