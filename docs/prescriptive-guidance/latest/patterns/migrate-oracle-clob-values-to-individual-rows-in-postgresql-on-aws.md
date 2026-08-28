---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-oracle-clob-values-to-individual-rows-in-postgresql-on-aws.html
---

# Migrate Oracle CLOB values to individual rows in PostgreSQL on AWS
<a name="migrate-oracle-clob-values-to-individual-rows-in-postgresql-on-aws"></a>

*Sai Krishna Namburu and Sindhusha Paturu, Amazon Web Services*

## Summary
<a name="migrate-oracle-clob-values-to-individual-rows-in-postgresql-on-aws-summary"></a>

This pattern describes how to split Oracle character large object (CLOB) values into individual rows in Amazon Aurora PostgreSQL-Compatible Edition and Amazon Relational Database Service (Amazon RDS) for PostgreSQL. PostgreSQL doesn’t support the CLOB data type.

Tables with interval partitions are identified in the source Oracle database, and the table name, the type of partition, the interval of the partition, and other metadata are captured and loaded into the target database. You can load CLOB data that is less than 1 GB in size into target tables as text by using AWS Database Migration Service (AWS DMS), or you can export the data in CSV format, load it into an Amazon Simple Storage Service (Amazon S3) bucket, and migrate it to your target PostgreSQL database.

After migration, you can use the custom PostgreSQL code that is provided with this pattern to split the CLOB data into individual rows based on the new line character identifier (`CHR(10)`) and populate the target** **table.

## Prerequisites and limitations
<a name="migrate-oracle-clob-values-to-individual-rows-in-postgresql-on-aws-prereqs"></a>

**Prerequisites **
+ An Oracle database table that has interval partitions and records with a CLOB data type.
+ An Aurora PostgreSQL-Compatible or Amazon RDS for PostgreSQL database that has a table structure that’s similar to the source table (same columns and data types).

**Limitations **
+ The CLOB value cannot exceed 1 GB.
+ Each row in the target table must have a new line character identifier.

**Product versions**
+ Oracle 12c
+ Aurora Postgres 11.6

## Architecture
<a name="migrate-oracle-clob-values-to-individual-rows-in-postgresql-on-aws-architecture"></a>

The following diagram shows a source Oracle table with CLOB data, and the equivalent PostgreSQL table in Aurora PostgreSQL-Compatible version 11.6.

![Source CLOB table and equivalent target PostgreSQL table.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/55806ee7-6a9f-4058-9a47-a07de68223ca/images/79b9d4b9-6f20-4db5-8ca8-2a599769a498.png)

## Tools
<a name="migrate-oracle-clob-values-to-individual-rows-in-postgresql-on-aws-tools"></a>

**AWS services**
+ [Amazon Aurora PostgreSQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) is a fully managed, ACID-compliant relational database engine that helps you set up, operate, and scale PostgreSQL deployments.
+ [Amazon Relational Database Service (Amazon RDS) for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html) helps you set up, operate, and scale a PostgreSQL relational database in the AWS Cloud.
+ [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) helps you migrate data stores into the AWS Cloud or between combinations of cloud and on-premises setups.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Other tools**

You can use the following client tools to connect to, access, and manage your Aurora PostgreSQL-Compatible and Amazon RDS for PostgreSQL databases. (These tools aren’t used within this pattern.)
+ [pgAdmin](https://www.pgadmin.org/) is an open-source management tool for PostgreSQL. It provides a graphical interface that helps you create, maintain, and use database objects.
+ [DBeaver](https://dbeaver.io/) is an open-source database tool for developers and database administrators. You can use the tool to manipulate, monitor, analyze, administer, and migrate your data.

## Best practices
<a name="migrate-oracle-clob-values-to-individual-rows-in-postgresql-on-aws-best-practices"></a>

For best practices for migrating your database from Oracle to PostgreSQL, see the AWS blog post [Best practices for migrating an Oracle database to Amazon RDS PostgreSQL or Amazon Aurora PostgreSQL: Migration process and infrastructure considerations](https://aws.amazon.com/blogs/database/best-practices-for-migrating-an-oracle-database-to-amazon-rds-postgresql-or-amazon-aurora-postgresql-migration-process-and-infrastructure-considerations/).

For best practices for configuring the AWS DMS task for migrating large binary objects, see [Migrating large binary objects (LOBs)](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_BestPractices.html#CHAP_BestPractices.LOBS) in the AWS DMS documentation.

## Epics
<a name="migrate-oracle-clob-values-to-individual-rows-in-postgresql-on-aws-epics"></a>

### Identify the CLOB data
<a name="identify-the-clob-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Analyze the CLOB data. | In the source Oracle database, analyze the CLOB data to see whether it contains column headers, so you can determine the method for loading the data into the target table. <br />To analyze the input data, use the following query.<br />`SELECT * FROM clobdata_or;  ` | Developer |
| Load the CLOB data to the target database. | Migrate the table that has CLOB data to an interim (staging) table in the Aurora or Amazon RDS target database. You can use AWS DMS or upload the data as a CSV file to an Amazon S3 bucket.<br />For information about using AWS DMS for this task, see [Using an Oracle database as a source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html) and [Using a PostgreSQL database as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html) in the AWS DMS documentation.<br />For information about using Amazon S3 for this task, see [Using Amazon S3 as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html) in the AWS DMS documentation. | Migration engineer, DBA |
| Validate the target PostgreSQL table. | Validate the target data, including headers, against the source data by using the following queries in the target database.<pre>SELECT * FROM clobdata_pg;<br />SELECT * FROM clobdatatarget;</pre><br />Compare the results against the query results from the source database (from the first step). | Developer |
| Split the CLOB data into separate rows. | Run the custom PostgreSQL code provided in the [Additional information](#migrate-oracle-clob-values-to-individual-rows-in-postgresql-on-aws-additional) section to split the CLOB data and insert it into separate rows in the target PostgreSQL table. | Developer |

### Validate the data.
<a name="validate-the-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the data in the target table. | Validate the data inserted into the target table by using the following queries.<pre>SELECT * FROM clobdata_pg;<br />SELECT * FROM clobdatatarget;</pre> | Developer |

## Related resources
<a name="migrate-oracle-clob-values-to-individual-rows-in-postgresql-on-aws-resources"></a>
+ [CLOB data type](https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm#SQLRF0021) (Oracle documentation)
+ [Data types](https://www.postgresql.org/docs/11/datatype.html) (PostgreSQL documentation)

## Additional information
<a name="migrate-oracle-clob-values-to-individual-rows-in-postgresql-on-aws-additional"></a>

**PostgreSQL function for splitting CLOB data**

```
do
$$
declare
totalstr varchar;
str1 varchar;
str2 varchar;
pos1 integer := 1;
pos2 integer ;
len integer;

begin
        select rawdata||chr(10) into totalstr from clobdata_pg;
        len :=  length(totalstr) ;
        raise notice 'Total length : %',len;
        raise notice 'totalstr : %',totalstr;
        raise notice 'Before while loop';

        while pos1 < len  loop

                  select position (chr(10) in totalstr) into pos2;
                 raise notice '1st position of new line : %',pos2;

                str1 := substring (totalstr,pos1,pos2-1);
                raise notice 'str1 : %',str1;

                   insert into clobdatatarget(data) values (str1);
                   totalstr := substring(totalstr,pos2+1,len);
                   raise notice 'new totalstr :%',totalstr;
                len :=  length(totalstr) ;

        end loop;
end
$$
LANGUAGE 'plpgsql' ;
```

**Input and output examples**

You can use the following examples to try out the PostgreSQL code before you migrate your data.

Create an Oracle database with three input lines.

```
CREATE TABLE clobdata_or (
id INTEGER GENERATED ALWAYS AS IDENTITY,
rawdata clob  );

insert into clobdata_or(rawdata) values (to_clob('test line 1') || chr(10) || to_clob('test line 2') || chr(10) || to_clob('test line 3') || chr(10));
COMMIT;

SELECT * FROM clobdata_or;
```

This displays the following output.

|  |  |
| --- |--- |
| id | rawdata |
| 1 | test line 1 test line 2 test line 3 |

Load the source data into a PostgreSQL staging table (`clobdata_pg`) for processing.

```
SELECT * FROM clobdata_pg;

CREATE TEMP TABLE clobdatatarget (id1 SERIAL,data VARCHAR );

<Run the code in the additional information section.>

SELECT * FROM clobdatatarget;
```

This displays the following output.

|  |  |
| --- |--- |
| id1 | data |
| 1 | test line 1 |
| 2 | test line 2 |
| 3 | test line 3 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
