---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-oracle-edition/assess-environment.html
---

# Assessing your environment
<a name="assess-environment"></a>

To assess your Oracle database and find out whether Enterprise Edition features are being used, you can use one of the following approaches:
+ SQL commands
+ The license-evaluation feature of AWS SCT

## Assessing Oracle Database Enterprise Edition by using SQL commands
<a name="sql-commands"></a>

Oracle tracks the usage of Oracle Database options, Oracle management packs, and their corresponding features in a view called [DBA\_FEATURE\_USAGE\_STATISTICS](https://docs.oracle.com/database/121/REFRN/GUID-B8A38B9B-3AAA-4341-AA05-4309870CE73B.htm#REFRN23396). The view is updated once a week by default, so it might take 7 days to show recent usage data. To get the latest information, manually refresh the view using the `DBMS_FEATURE_USAGE_INTERNAL` package. Your database user requires `EXECUTE` privilege on `DBMS_FEATURE_USAGE_INTERNAL` to refresh the view, and `SELECT ANY DICTIONARY` privilege to query the view.

Oracle provides the `script options_packs_usage_statistics.sql` in [Support document 1317265.1](https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1317265.1). You can use that script to check which options, features, and management packs have been used in the database. Alternatively, you can run the following query to list previously used options and features.

```
-- To view the last refresh date of DBA_FEATURE_USAGE_STATISTICS
 select max(last_sample_date) from dba_feature_usage_statistics order by 1;

 -- To manually refresh DBA_FEATURE_USAGE_STATISTICS view
 exec sys.dbms_feature_usage_internal.exec_db_usage_sampling(sysdate);

 -- To list features and options in use
 select dbafus1.name, dbafus1.detected_usages, dbafus1.currently_used, dbafus1.first_usage_date, dbafus1.last_usage_date, dbafus1.version
 from dba_feature_usage_statistics dbafus1
 where  dbafus1.version = (select max(dbafus2.version)
                      from dba_feature_usage_statistics dbafus2
                      where dbafus2.name = dbafus1.name)
 and dbafus1.detected_usages > 0
 and dbafus1.dbid = (select dbid from v$database)
 and dbafus1.currently_used='TRUE'
 order by dbafus1.name;

 -- To check use of parallelism for activities like DMLs, DDLs, index builds, statistics gathering, Data Pump
 select name, value
 from gv$sysstat
 where
    upper(NAME) like '%PARALLEL OPERATIONS%'
 OR
    upper(NAME) like '%PARALLELIZED%'
 OR
    upper(NAME) like '%PX%';

 -- To identify use of Materialized Views Query Rewrite
 select owner, mview_name from dba_mviews
 where owner not like '%SYS%'
 and rewrite_enabled='Y';

 -- To identify bitmap indexes
 select * from dba_indexes
 where index_type='BITMAP'
 and owner not like '%SYS%';

 -- To identify non-system use of Partitioning
 select * from dba_tab_partitions where table_owner not like '%SYS%';
```

Review the result of the previous query and compare it with [Oracle documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/dblic/Licensing-Information.html#GUID-B6113390-9586-46D7-9008-DCC9EDA45AB4). Investigate each Enterprise Edition feature or option listed in the output to understand their use case and determine appropriate alternatives in Oracle Database Standard Edition 2 where possible.

## Assessing Oracle Database Enterprise Edition by using AWS SCT
<a name="aws-sct"></a>

AWS Schema Conversion Tool (AWS SCT) provides a project-based user interface for assessing, converting, and copying the database schema of your source Oracle database into a format that is compatible with Amazon RDS for Oracle. Using AWS SCT, you can analyze potential cost savings that can be achieved by changing your Oracle Database license type from Enterprise Edition to Standard Edition 2.

The *License evaluation and cloud support* section of the AWS SCT report provides detailed information about Oracle database features in use. This information can help you make informed decisions while migrating to Amazon RDS for Oracle. For example, the report might say that your Enterprise Edition server uses the Compression feature, and that you must remove dependencies on ColumnStoreIndex and Partitioning. It also lists features, such as InMemoryOLTP, that can't be moved to Amazon RDS for Oracle.

### Scaling the Oracle assessment
<a name="scaling-the-oracle-assessment.54254dd9-662a-5faa-8b55-23b060eef8c5"></a>

To evaluate multiple servers, you can run batch assessments with AWS SCT by using the [multiserver assessor](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_AssessmentReport.Multiserver.html#CHAP_AssessmentReport.Multiserver.Agreggated) option. After assessing each schema, the assessor produces a server-level report that includes the *License evaluation and cloud support* section.
