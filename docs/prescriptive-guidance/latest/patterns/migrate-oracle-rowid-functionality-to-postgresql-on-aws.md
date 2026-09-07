---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-oracle-rowid-functionality-to-postgresql-on-aws.html
---

# Migrate Oracle ROWID functionality to PostgreSQL on AWS
<a name="migrate-oracle-rowid-functionality-to-postgresql-on-aws"></a>

*Rakesh Raghav and Ramesh Pathuri, Amazon Web Services*

## Summary
<a name="migrate-oracle-rowid-functionality-to-postgresql-on-aws-summary"></a>

This pattern describes options for migrating the `ROWID` pseudocolumn functionality in Oracle Database to a PostgreSQL database in Amazon Relational Database Service (Amazon RDS) for PostgreSQL, Amazon Aurora PostgreSQL-Compatible Edition, or Amazon Elastic Compute Cloud (Amazon EC2).

In an Oracle database, the `ROWID` pseudocolumn is a physical address of a row in a table. This pseudocolumn is used to uniquely identify a row even if the primary key isn’t present on a table. PostgreSQL has a similar pseudocolumn called `ctid`, but it cannot be used as a `ROWID`. As explained in the [PostgreSQL documentation](https://www.postgresql.org/docs/current/ddl-system-columns.html), `ctid` might change if it’s updated or after every `VACUUM` process.

There are three ways you can create the `ROWID` pseudocolumn functionality in PostgreSQL:
+ Use a primary key column instead of `ROWID` to identify a row in a table.
+ Use a logical primary/unique key (which might be a composite key) in the table.
+ Add a column with auto-generated values and make it a primary/unique key to mimic `ROWID`.

This pattern walks you through all three implementations and describes the advantages and disadvantages of each option.

## Prerequisites and limitations
<a name="migrate-oracle-rowid-functionality-to-postgresql-on-aws-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ Procedural Language/PostgreSQL (PL/pgSQL) coding expertise
+ Source Oracle Database
+ An Amazon RDS for PostgreSQL or Aurora PostgreSQL-Compatible cluster, or an EC2 instance to host the PostgreSQL database

**Limitations **
+ This pattern provides  workarounds for the `ROWID` functionality. PostgreSQL doesn’t provide an equivalent to `ROWID` in Oracle Database.

**Product versions**
+ PostgreSQL 11.9 or later

## Architecture
<a name="migrate-oracle-rowid-functionality-to-postgresql-on-aws-architecture"></a>

**Source technology stack  **
+ Oracle Database

**Target technology stack  **
+ Aurora PostgreSQL-Compatible, Amazon RDS for PostgreSQL, or an EC2 instance with a PostgreSQL database

![Converting an Oracle Database to PostgreSQL on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/9a2ce994-4f68-4975-aab2-796cc20a3c82/images/6e7c2ef6-f440-476a-9003-f1f166718e15.png)

**Implementation options**

There are three options to work around the lack of `ROWID` support in PostgreSQL, depending on whether your table has a primary key or unique index, a logical primary key, or an identity attribute. Your choice depends on your project timelines, your current migration phase, and dependencies on application and database code.

|
|
| Option | Description | Advantages | Disadvantages |
| --- |--- |--- |--- |
| **Primary key or unique index** | If your Oracle table has a primary key, you can use the attributes of this key to uniquely identify a row.  | + No dependency on proprietary database features.<br />+ Minimal impact on performance, because primary key fields are indexed. | + Requires changes to application and database code that relies on `ROWID` to switch to primary key fields.  |
| **Logical primary/unique key** | If your Oracle table has a logical primary key, you can use the attributes of this key to uniquely identify a row. A logical primary key consists of an attribute or a set of attributes that can uniquely identify a row, but it isn’t enforced on the database through a constraint. | + No dependency on proprietary database features. | + Requires changes to application and database code that relies on `ROWID` to switch to primary key fields.<br />+ Significant impact on performance if the attributes of the logical primary key aren’t indexed. However, you can add a unique index to prevent performance issues. |
| **Identity attribute** | if your Oracle table doesn't have a primary key, you can create an additional field as `GENERATED ALWAYS AS IDENTITY`. This attribute generates a unique value whenever data is inserted into the table, so it can be used to uniquely identify a row for Data Manipulation Language (DML) operations. | + No dependency on proprietary database features.<br />+ PostgreSQL database populates the attribute and maintains its uniqueness. | + Requires changes to application and database code that relies on `ROWID` to switch to identity attribute.<br />+ Significant impact on performance if the additional field isn’t indexed. However, you can add an index to prevent performance issues. |

## Tools
<a name="migrate-oracle-rowid-functionality-to-postgresql-on-aws-tools"></a>
+ [Amazon Relational Database Service (Amazon RDS) for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html) helps you set up, operate, and scale a PostgreSQL relational database in the AWS Cloud.
+ [Amazon Aurora PostgreSQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) is a fully managed, ACID-compliant relational database engine that helps you set up, operate, and scale PostgreSQL deployments.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell. In this pattern, you can use the AWS CLI to run SQL commands through **pgAdmin**.
+ [pgAdmin](https://www.pgadmin.org/) is an open-source management tool for PostgreSQL. It provides a graphical interface that helps you create, maintain, and use database objects.
+ [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) supports heterogeneous database migrations by automatically converting the source database schema and a majority of the custom code to a format that’s compatible with the target database.

## Epics
<a name="migrate-oracle-rowid-functionality-to-postgresql-on-aws-epics"></a>

### Identify the source tables
<a name="identify-the-source-tables"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify Oracle tables that use the `ROWID` attribute. | Use the AWS Schema Conversion Tool (AWS SCT) to identify Oracle tables that have `ROWID` functionality. For more information, see the [AWS SCT documentation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Oracle.ToPostgreSQL.html#CHAP_Source.Oracle.ToPostgreSQL.ConvertRowID).<br />—or—<br />In Oracle, use the `DBA_TAB_COLUMNS` view to identify tables that have a `ROWID` attribute. These fields might be used to store alphanumeric 10-byte characters. Determine the usage and convert these to a `VARCHAR` field if appropriate. | DBA or developer |
| Identify code that references these tables. | Use AWS SCT to generate a migration assessment report to identify procedures affected by `ROWID`. For more information, see the [AWS SCT documentation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_AssessmentReport.html).<br />—or—<br />In the source Oracle database, use the text field of the `dba_source` table to identify objects that use `ROWID` functionality. | DBA or developer |

### Determine primary key usage
<a name="determine-primary-key-usage"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify tables that don’t have primary keys. | In the source Oracle database, use `DBA_CONSTRAINTS` to identify tables that don’t have primary keys. This information will help you determine the strategy for each table. For example:<pre>select dt.*<br />from dba_tables dt<br />where not exists (select 1<br />                  from all_constraints ct<br />                  where ct.owner = Dt.owner<br />                    and ct.table_name = Dt.table_name<br />                    and ct.constraint_type = 'P'<br />                  )<br />and dt.owner = '{schema}'</pre> | DBA or developer |

### Identify and apply the solution
<a name="identify-and-apply-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Apply changes for tables that have a defined or logical primary key.  | Make the application and database code changes shown in the [Additional information](#migrate-oracle-rowid-functionality-to-postgresql-on-aws-additional) section to use a unique primary key or a logical primary key to identify a row in your table. | DBA or developer |
| Add an additional field to tables that don’t have a defined or logical primary key. | Add an attribute of type `GENERATED ALWAYS AS IDENTITY`. Make the application and database code changes shown in the [Additional information](#migrate-oracle-rowid-functionality-to-postgresql-on-aws-additional) section. | DBA or developer |
| Add an index if necessary. | Add an index to the additional field or logical primary key to improve SQL performance. | DBA or developer |

## Related resources
<a name="migrate-oracle-rowid-functionality-to-postgresql-on-aws-resources"></a>
+ [PostgreSQL CTID](https://www.postgresql.org/docs/current/ddl-system-columns.html) (PostgreSQL documentation)
+ [Generated Columns](https://www.postgresql.org/docs/current/ddl-generated-columns.html) (PostgreSQL documentation)
+ [ROWID Pseudocolumn](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/ROWID-Pseudocolumn.html#GUID-F6E0FBD2-983C-495D-9856-5E113A17FAF1) (Oracle documentation)

## Additional information
<a name="migrate-oracle-rowid-functionality-to-postgresql-on-aws-additional"></a>

The following sections provide Oracle and PostgreSQL code examples to illustrate the three approaches.

**Scenario 1: Using a primary unique key**

In the following examples, you create the table `testrowid_s1` with `emp_id` as the primary key.

*Oracle code:*

```
create table testrowid_s1 (emp_id integer, name varchar2(10), CONSTRAINT testrowid_pk PRIMARY KEY (emp_id));
INSERT INTO testrowid_s1(emp_id,name) values (1,'empname1');
INSERT INTO testrowid_s1(emp_id,name) values (2,'empname2');
INSERT INTO testrowid_s1(emp_id,name) values (3,'empname3');
INSERT INTO testrowid_s1(emp_id,name) values (4,'empname4');
commit;

SELECT rowid,emp_id,name FROM testrowid_s1;
ROWID                  EMP_ID NAME
------------------ ---------- ----------
AAAF3pAAAAAAAMOAAA          1 empname1
AAAF3pAAAAAAAMOAAB          2 empname2
AAAF3pAAAAAAAMOAAC          3 empname3
AAAF3pAAAAAAAMOAAD          4 empname4

UPDATE testrowid_s1 SET name = 'Ramesh' WHERE rowid = 'AAAF3pAAAAAAAMOAAB' ;
commit;

SELECT rowid,emp_id,name FROM testrowid_s1;
ROWID                  EMP_ID NAME
------------------ ---------- ----------
AAAF3pAAAAAAAMOAAA          1 empname1
AAAF3pAAAAAAAMOAAB          2 Ramesh
AAAF3pAAAAAAAMOAAC          3 empname3
AAAF3pAAAAAAAMOAAD          4 empname4
```

*PostgreSQL code:*

```
CREATE TABLE public.testrowid_s1
(
    emp_id integer,
    name character varying,
    primary key (emp_id)
);

insert into public.testrowid_s1 (emp_id,name) values
(1,'empname1'),(2,'empname2'),(3,'empname3'),(4,'empname4');

select emp_id,name from testrowid_s1;
 emp_id |   name
--------+----------
      1 | empname1
      2 | empname2
      3 | empname3
      4 | empname4

update testrowid_s1 set name = 'Ramesh' where emp_id = 2 ;

select emp_id,name from testrowid_s1;
 emp_id |   name
--------+----------
      1 | empname1
      3 | empname3
      4 | empname4
      2 | Ramesh
```

**Scenario 2: Using a logical primary key**

In the following examples, you create the table `testrowid_s2` with `emp_id` as the logical primary key.

*Oracle code:*

```
create table testrowid_s2 (emp_id integer, name varchar2(10) );
INSERT INTO testrowid_s2(emp_id,name) values (1,'empname1');
INSERT INTO testrowid_s2(emp_id,name) values (2,'empname2');
INSERT INTO testrowid_s2(emp_id,name) values (3,'empname3');
INSERT INTO testrowid_s2(emp_id,name) values (4,'empname4');
commit;

SELECT rowid,emp_id,name FROM testrowid_s2;
ROWID                  EMP_ID NAME
------------------ ---------- ----------
AAAF3rAAAAAAAMeAAA          1 empname1
AAAF3rAAAAAAAMeAAB          2 empname2
AAAF3rAAAAAAAMeAAC          3 empname3
AAAF3rAAAAAAAMeAAD          4 empname4

UPDATE testrowid_s2 SET name = 'Ramesh' WHERE rowid = 'AAAF3rAAAAAAAMeAAB' ;
commit;

SELECT rowid,emp_id,name FROM testrowid_s2;
ROWID                  EMP_ID NAME
------------------ ---------- ----------
AAAF3rAAAAAAAMeAAA          1 empname1
AAAF3rAAAAAAAMeAAB          2 Ramesh
AAAF3rAAAAAAAMeAAC          3 empname3
AAAF3rAAAAAAAMeAAD          4 empname4
```

*PostgreSQL code:*

```
CREATE TABLE public.testrowid_s2
(
    emp_id integer,
    name character varying
);

insert into public.testrowid_s2 (emp_id,name) values
(1,'empname1'),(2,'empname2'),(3,'empname3'),(4,'empname4');

select emp_id,name from testrowid_s2;
 emp_id |   name
--------+----------
      1 | empname1
      2 | empname2
      3 | empname3
      4 | empname4

update testrowid_s2 set name = 'Ramesh' where emp_id = 2 ;

select emp_id,name from testrowid_s2;
 emp_id |   name
--------+----------
      1 | empname1
      3 | empname3
      4 | empname4
      2 | Ramesh
```

**Scenario 3: Using an identity attribute**

In the following examples, you create the table `testrowid_s3` with no primary key and by using an identity attribute.

*Oracle code:*

```
create table testrowid_s3 (name varchar2(10));
INSERT INTO testrowid_s3(name) values ('empname1');
INSERT INTO testrowid_s3(name) values ('empname2');
INSERT INTO testrowid_s3(name) values ('empname3');
INSERT INTO testrowid_s3(name) values ('empname4');
commit;

SELECT rowid,name FROM testrowid_s3;
ROWID              NAME
------------------ ----------
AAAF3sAAAAAAAMmAAA empname1
AAAF3sAAAAAAAMmAAB empname2
AAAF3sAAAAAAAMmAAC empname3
AAAF3sAAAAAAAMmAAD empname4

UPDATE testrowid_s3 SET name = 'Ramesh' WHERE rowid = 'AAAF3sAAAAAAAMmAAB' ;
commit;

SELECT rowid,name FROM testrowid_s3;
ROWID              NAME
------------------ ----------
AAAF3sAAAAAAAMmAAA empname1
AAAF3sAAAAAAAMmAAB Ramesh
AAAF3sAAAAAAAMmAAC empname3
AAAF3sAAAAAAAMmAAD empname4
```

*PostgreSQL code:*

```
CREATE TABLE public.testrowid_s3
(
    rowid_seq bigint generated always as identity,
    name character varying
);

insert into public.testrowid_s3 (name) values
('empname1'),('empname2'),('empname3'),('empname4');

select rowid_seq,name from testrowid_s3;
 rowid_seq |   name
-----------+----------
         1 | empname1
         2 | empname2
         3 | empname3
         4 | empname4

update testrowid_s3 set name = 'Ramesh' where rowid_seq = 2 ;

select rowid_seq,name from testrowid_s3;
 rowid_seq |   name
-----------+----------
         1 | empname1
         3 | empname3
         4 | empname4
         2 | Ramesh
```
