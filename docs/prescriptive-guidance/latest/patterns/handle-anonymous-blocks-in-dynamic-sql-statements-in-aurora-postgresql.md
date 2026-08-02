---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/handle-anonymous-blocks-in-dynamic-sql-statements-in-aurora-postgresql.html
---

# Handle anonymous blocks in Dynamic SQL statements in Aurora PostgreSQL
<a name="handle-anonymous-blocks-in-dynamic-sql-statements-in-aurora-postgresql"></a>

*anuradha chintha, Amazon Web Services*

## Summary
<a name="handle-anonymous-blocks-in-dynamic-sql-statements-in-aurora-postgresql-summary"></a>

Note: Amazon Cloud Directory is no longer open to new customers. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

This pattern shows you how to avoid the error that you get when handling anonymous blocks in Dynamic SQL statements. You receive an error message when you use the AWS Schema Conversion Tool to convert an Oracle database to an Aurora PostgreSQL-Compatible Edition database. To avoid the error, you must know the value of an `OUT` bind variable, but you can’t know the value of an `OUT` bind variable until after you run the SQL statement. The error results from the AWS Schema Conversion Tool (AWS SCT) not understanding the logic inside the Dynamic SQL statement. AWS SCT can’t convert the dynamic SQL statement in PL/SQL code (that is, functions, procedures, and packages).

## Prerequisites and limitations
<a name="handle-anonymous-blocks-in-dynamic-sql-statements-in-aurora-postgresql-prereqs"></a>

**Prerequisites**
+ Active AWS account
+ [Aurora PostgreSQL database (DB) instance](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.html)
+ [Amazon Relational Database Service (Amazon RDS) for Oracle DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html)
+ [PostgreSQL interactive terminal (psql)](https://www.postgresql.org/docs/current/app-psql.html)
+ [SQL \*Plus](https://docs.oracle.com/cd/B14117_01/server.101/b12170/qstart.htm)
+ `AWS_ORACLE_EXT` schema (part of the [AWS SCT extension pack](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_ExtensionPack.html)) in your target database
+ Latest version of [AWS Schema Conversion Tool (AWS SCT)](https://aws.amazon.com/dms/schema-conversion-tool/) and its required drivers

## Architecture
<a name="handle-anonymous-blocks-in-dynamic-sql-statements-in-aurora-postgresql-architecture"></a>

**Source technology stack**
+ On-premises Oracle Database 10g and later version

**Target technology stack**
+ Amazon Aurora PostgreSQL
+ Amazon RDS for PostgreSQL
+ AWS Schema Conversion Tool (AWS SCT)

**Migration architecture**

The following diagram shows how to use AWS SCT and Oracle `OUT` bind variables to scan your application code for embedded SQL statements and convert the code to a compatible format that an Aurora database can use.

![Architecture diagram for using AWS SCT and Oracle OUT bind variables](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/ada89410-b866-4d39-af9c-021be6cc6ae5/images/7c004981-2ed0-4b67-989f-54d8691712ca.png)

The diagram shows the following workflow:

1. Generate an AWS SCT report for the source database by using Aurora PostgreSQL as the target database.

1. Identify the anonymous block in the Dynamic SQL code block (for which AWS SCT raised the error).

1. Convert the code block manually and deploy the code on a target database.

## Tools
<a name="handle-anonymous-blocks-in-dynamic-sql-statements-in-aurora-postgresql-tools"></a>

**AWS services**
+ [Amazon Aurora PostgreSQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) is a fully managed, ACID-compliant relational database engine that helps you set up, operate, and scale PostgreSQL deployments.
+ [Amazon Relational Database Service (Amazon RDS) for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale an Oracle relational database in the AWS Cloud.
+ [AWS Schema Conversion Tool (AWS SCT)](https://aws.amazon.com/dms/schema-conversion-tool/) helps you make heterogeneous database migrations predictable by automatically converting the source database schema and a majority of the database code objects to a format compatible with the target database.

**Other tools**
+ [pgAdmin](https://www.pgadmin.org/) enables you to connect to and interact with your database server.
+ [Oracle SQL Developer](https://www.oracle.com/database/sqldeveloper/) is an integrated development environment that you can use to develop and manage databases in Oracle Database. You can use either [SQL \*Plus](https://docs.oracle.com/cd/B19306_01/server.102/b14357/qstart.htm) or Oracle SQL Developer for this pattern.

## Epics
<a name="handle-anonymous-blocks-in-dynamic-sql-statements-in-aurora-postgresql-epics"></a>

### Configure the Oracle source database
<a name="configure-the-oracle-source-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Oracle instance on Amazon RDS or Amazon EC2. | To create an Oracle DB instance on Amazon RDS, see [Creating an Oracle DB instance and connecting to a database on an Oracle DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.Oracle.html) in the Amazon RDS documentation.<br />To create an Oracle DB instance on Amazon Elastic Compute Cloud (Amazon EC2), see [Amazon EC2 for Oracle](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/ec2-oracle.html) in the AWS Prescriptive Guidance documentation. | DBA |
| Create a database schema and objects for migration. | You can use Amazon Cloud Directory to create a database schema. For more information, see [Create a Schema](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/getting_started_create_schema.html) in the Cloud Directory documentation. | DBA |
| Configure inbound and outbound security groups. | To create and configure security groups, see [Controlling access with security groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html) in the Amazon RDS documentation. | DBA |
| Confirm that the database is running. | To check the status of your database, see [Viewing Amazon RDS events](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ListEvents.html) in the Amazon RDS documentation. | DBA |

### Configure the target Aurora PostgreSQL database
<a name="configure-the-target-aurora-postgresql-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Aurora PostgreSQL instance in Amazon RDS. | To create an Aurora PostgreSQL instance, see [Creating a DB cluster and connecting to a database on an Aurora PostgreSQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.AuroraPostgreSQL.html) in the Amazon RDS documentation. | DBA |
| Configure an inbound and outbound security group. | To create and configure security groups, see [Provide access to the DB cluster in the VPC by creating a security group](https://docs.amazonaws.cn/en_us/AmazonRDS/latest/AuroraUserGuide/CHAP_SettingUp_Aurora.html#CHAP_SettingUp_Aurora.SecurityGroup) in the Aurora documentation. | DBA |
| Confirm that the Aurora PostgreSQL database is running. | To check the status of your database, see [Viewing Amazon RDS events](https://docs.amazonaws.cn/en_us/AmazonRDS/latest/AuroraUserGuide/USER_ListEvents.html) in the Aurora documentation. | DBA |

### Set up AWS SCT
<a name="set-up-aws-sct"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Connect AWS SCT to the source database. | To connect AWS SCT to your source database, see [Connecting to PostgreSQL as a source](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.Connecting) in the AWS SCT documentation. | DBA |
| Connect AWS SCT to the target database. | To connect AWS SCT to your target database, see the [What is the AWS Schema Conversion Tool?](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) in the AWS Schema Conversion Tool User Guide. | DBA |
| Convert the database schema in AWS SCT and save the automated converted code as a SQL file. | To save AWS SCT converted files, see [Saving and applying your converted schema in AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Converting.html#CHAP_Converting.SaveAndApply) in the AWS Schema Conversion Tool User Guide. | DBA |

### Migrate the code
<a name="migrate-the-code"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Get the SQL file for manual conversion. | In the AWS SCT converted file, pull the SQL file that requires manual conversion. | DBA |
| Update the script. | Manually update the SQL file. | DBA |

## Related resources
<a name="handle-anonymous-blocks-in-dynamic-sql-statements-in-aurora-postgresql-resources"></a>
+ [Amazon RDS](https://aws.amazon.com/rds/)
+ [Amazon Aurora Features](https://aws.amazon.com/rds/aurora/postgresql-features/)

## Additional information
<a name="handle-anonymous-blocks-in-dynamic-sql-statements-in-aurora-postgresql-additional"></a>

The following example code shows how to configure the Oracle source database:

```
CREATE or replace PROCEDURE calc_stats_new1 (
  a NUMBER,
  b NUMBER,
  result out NUMBER)
IS
BEGIN
result:=a+b;
END;
/
```

```
set serveroutput on ;

DECLARE
  a NUMBER := 4;
  b NUMBER := 7;
  plsql_block VARCHAR2(100);
  output number;
BEGIN
  plsql_block := 'BEGIN calc_stats_new1(:a, :b,:output); END;';
  EXECUTE IMMEDIATE plsql_block USING a, b,out output;
  DBMS_OUTPUT.PUT_LINE('output:'||output);

END;
```

The following example code shows how to configure the target Aurora PostgreSQL database:

```
 w integer,
 x integer)
RETURNS integer
AS
$BODY$
DECLARE
begin
return w + x ;
end;
$BODY$
LANGUAGE  plpgsql;

CREATE OR REPLACE FUNCTION test_pg.init()
RETURNS void
AS
$BODY$
BEGIN
if aws_oracle_ext.is_package_initialized
      ('test_pg' ) then
      return;
    end if;
    perform aws_oracle_ext.set_package_initialized
      ('test_pg' );

PERFORM aws_oracle_ext.set_package_variable('test_pg', 'v_output', NULL::INTEGER);
PERFORM aws_oracle_ext.set_package_variable('test_pg', 'v_status', NULL::text);
END;
$BODY$
LANGUAGE  plpgsql;

DO $$
declare
v_sql text;
v_output_loc int;
a integer :=1;
b integer :=2;
BEGIN
perform  test_pg.init();
--raise notice 'v_sql %',v_sql;
execute 'do $a$ declare v_output_l int; begin select * from test_pg.calc_stats_new1('||a||','||b||') into v_output_l;
PERFORM aws_oracle_ext.set_package_variable(''test_pg'', ''v_output'', v_output_l) ; end; $a$'  ;
v_output_loc := aws_oracle_ext.get_package_variable('test_pg', 'v_output');
raise notice 'v_output_loc %',v_output_loc;
END ;
$$
```
