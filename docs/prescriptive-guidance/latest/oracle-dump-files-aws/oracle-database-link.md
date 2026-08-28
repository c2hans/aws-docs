---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/oracle-dump-files-aws/oracle-database-link.html
---

# Using an Oracle database link to transfer dump files
<a name="oracle-database-link"></a>

An Oracle database link is a schema object in one database that enables you to access objects on another database. To use the database link to move the Oracle Database dump files from source to target, you must create the DB link in the source system and confirm connectivity between the source and the target. For more information on how to create an Oracle database link and make sure that it's working as expected, see the [Oracle documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-DATABASE-LINK.html#GUID-D966642A-B19E-449D-9968-1121AF06D793).

The process for copying the Oracle database dump files is the same for the Amazon RDS for Oracle and Amazon EC2 targets. To copy the dump files to the target, run the following code.

```
BEGIN
DBMS_FILE_TRANSFER.PUT_FILE(
source_directory_object => 'DATA_PUMP_DIR', --Source dump file directory name
source_file_name => 'hotels.dmp',
destination_directory_object => 'DATA_PUMP_DIR', --For RDS you can chose default directory DATA_PUMP_DIR for EC2 provide the directory path
destination_file_name => 'hotels_copied.dmp',
destination_database => 'DB_Link_Name'  --DB Link name
);
END;
/
```

In a separate query window, check the progress and files in the `DATA_PUMP_DIR` in the RDS for Oracle instance by running the following code.

```
SELECT SID, SERIAL#, CONTEXT, SOFAR, TOTALWORK,opname,
       ROUND(SOFAR/TOTALWORK*100,2) "%_COMPLETE",units
FROM   V$SESSION_LONGOPS
where  OPNAME NOT LIKE '%aggregate%'
AND    TOTALWORK != 0
AND    SOFAR <> TOTALWORK;
```

To check the files on Amazon EC2, navigate to the directory path that you have provided to copy the files.

To check the files on Amazon RDS for Oracle, run the following code.

```
select * from table (RDSADMIN.RDS_FILE_UTIL.LISTDIR('DATA_PUMP_DIR')) order by filename;
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
