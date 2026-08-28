---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/emulate-oracle-plsql-associative-arrays-in-aurora-and-rds-postgresql.html
---

# Emulate Oracle PL/SQL associative arrays in Amazon Aurora PostgreSQL and Amazon RDS for PostgreSQL
<a name="emulate-oracle-plsql-associative-arrays-in-aurora-and-rds-postgresql"></a>

*Rajkumar Raghuwanshi, Bhanu Ganesh Gudivada, and Sachin Khanna, Amazon Web Services*

## Summary
<a name="emulate-oracle-plsql-associative-arrays-in-aurora-and-rds-postgresql-summary"></a>

This pattern describes how to emulate Oracle PL/SQL associative arrays with empty index positions in [Amazon Aurora PostgreSQL](https://aws.amazon.com/rds/aurora/) and [Amazon RDS for PostgreSQL](https://aws.amazon.com/rds/postgresql/) environments. It also describes some of the differences between Oracle PL/SQL associative arrays and PostgreSQL arrays with regard to how each handles empty index positions during migrations.

We provide a PostgreSQL alternative to using `aws_oracle_ext` functions for handling empty index positions when migrating an Oracle database. This pattern uses an additional column to store index positions, and it maintains Oracle's handling of sparse arrays while incorporating native PostgreSQL capabilities.

*Oracle*

In Oracle, collections can be initialized as empty and populated using the `EXTEND` collection method, which appends `NULL` elements to the array. When working with PL/SQL associative arrays indexed by `PLS_INTEGER`, the `EXTEND` method adds `NULL` elements sequentially, but elements can also be initialized at nonsequential index positions. Any index position that isn't explicitly initialized remains empty.

This flexibility allows for sparse array structures where elements can be populated at arbitrary positions. When iterating through collections using a `FOR LOOP` with `FIRST` and `LAST` bounds, only the initialized elements (whether `NULL` or with a defined value) are processed, while empty positions are skipped.

*PostgreSQL (Amazon Aurora and Amazon RDS)*

PostgreSQL handles empty values differently from `NULL` values. It stores empty values as distinct entities that use one byte of storage. When an array has empty values, PostgreSQL assigns sequential index positions just like non-empty values. But sequential indexing requires additional processing because the system must iterate through all indexed positions, including the empty ones. This makes traditional array creation inefficient for sparse datasets.

*AWS Schema Conversion Tool*

The [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/) typically handles Oracle-to-PostgreSQL migrations using `aws_oracle_ext` functions. In this pattern, we propose an alternative approach that uses native PostgreSQL capabilities, which combines PostgreSQL array types with an additional column for storing index positions. The system can then iterate through arrays using just the index column.

## Prerequisites and limitations
<a name="emulate-oracle-plsql-associative-arrays-in-aurora-and-rds-postgresql-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ Administrator permissions in AWS Identity and Access Management (IAM)
+ An instance that’s compatible with Amazon RDS or Aurora PostgreSQL
+ Database architect or developer skills with Oracle and PostgreSQL

**Limitations**
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

**Product versions**

This pattern was tested with the following versions:
+ Amazon Aurora PostgreSQL 13.3
+ Amazon RDS for PostgreSQL 13.3
+ AWS SCT 1.0.674
+ Oracle 19c EE

## Architecture
<a name="emulate-oracle-plsql-associative-arrays-in-aurora-and-rds-postgresql-architecture"></a>

**Source technology stack**
+ On-premises Oracle database

**Target technology stack**
+ Amazon Aurora PostgreSQL
+ Amazon RDS for PostgreSQL

**Target architecture**

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/a62d038c-ca3c-41e1-aa7e-74282d2e54f4/images/13aacf00-655a-4149-a4e7-42b66dbea4e1.png)

The diagram shows the following:
+ A source Amazon RDS for Oracle database instance
+ An Amazon EC2 instance with AWS SCT for converting Oracle functions to the PostgreSQL equivalent
+ A target database that’s compatible with Amazon Aurora PostgreSQL

## Tools
<a name="emulate-oracle-plsql-associative-arrays-in-aurora-and-rds-postgresql-tools"></a>

**AWS services**
+ [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) is a fully managed relational database engine that's built for the cloud and compatible with MySQL and PostgreSQL.
+ [Amazon Aurora PostgreSQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) is a fully managed, ACID-compliant relational database engine that helps you set up, operate, and scale PostgreSQL deployments.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database in the AWS Cloud.
+ [Amazon Relational Database Service (Amazon RDS) for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html) helps you set up, operate, and scale an Oracle relational database in the AWS Cloud.
+ [Amazon Relational Database Service (Amazon RDS) for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html) helps you set up, operate, and scale a PostgreSQL relational database in the AWS Cloud.
+ [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) supports heterogeneous database migrations by automatically converting the source database schema and a majority of the custom code to a format that’s compatible with the target database.

**Other tools**
+ [Oracle SQL Developer](https://www.oracle.com/database/technologies/appdev/sqldeveloper-landing.html) is an integrated development environment that simplifies the development and management of Oracle databases in both traditional and cloud-based deployments.
+ [pgAdmin](https://www.pgadmin.org/) is an open source management tool for PostgreSQL. It provides a graphical interface that helps you create, maintain, and use database objects. In this pattern, pgAdmin connects to the RDS for PostgreSQL database instance and queries the data. Alternatively, you can use the psql command line client.

## Best practices
<a name="emulate-oracle-plsql-associative-arrays-in-aurora-and-rds-postgresql-best-practices"></a>
+ Test data set boundaries and edge scenarios.
+ Consider implementing error handling for out-of-bounds index conditions.
+ Optimize queries to avoid scanning sparse data sets.

## Epics
<a name="emulate-oracle-plsql-associative-arrays-in-aurora-and-rds-postgresql-epics"></a>

### Oracle associative array behavior (source)
<a name="oracle-associative-array-behavior-source"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a source PL/SQL block in Oracle. | Create a source PL/SQL block in Oracle that uses the following associative array:<pre>DECLARE<br />    TYPE country_codes IS TABLE OF VARCHAR2(100) INDEX BY pls_integer;<br />    cc country_codes;<br />    cc_idx NUMBER := NULL;<br />BEGIN<br />    cc(7) := 'India';<br />    cc(3) := 'UK';<br />    cc(5) := 'USA';<br />    cc(0) := 'China';<br />    cc(-2) := 'Invalid';<br />    dbms_output.put_line('cc_length:' || cc.COUNT);<br />    IF (cc.COUNT > 0) THEN<br />        cc_idx := cc.FIRST;<br />        FOR i IN 1..cc.COUNT LOOP<br />            dbms_output.put_line('cc_idx:' || cc_idx || ' country:' || cc(cc_idx));<br />            cc_idx := cc.next(cc_idx);<br />        END LOOP;<br />    END IF;<br />END;</pre> | DBA |
| Run the PL/SQL block. | Run the source PL/SQL block in Oracle. If there are gaps between the index values of an associative array, no data is stored in those gaps. This allows the Oracle loop to iterate only through the index positions. | DBA |
| Review the output. | Five elements were inserted into the array (`cc`) at nonconsecutive intervals. The array count is shown in the following output:<pre>cc_length:5<br />cc_idx:-2 country:Invalid<br />cc_idx:0 country:China<br />cc_idx:3 country:UK<br />cc_idx:5 country:USA<br />cc_idx:7 country:India</pre> | DBA |

### PostgreSQL associative array behavior (target)
<a name="postgresql-associative-array-behavior-target"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a target PL/pgSQL block in PostgreSQL. | Create a target PL/pgSQL block in PostgreSQL that uses the following associative array:<pre>DO $$<br />DECLARE<br />    cc character varying(100)[];<br />    cc_idx integer := NULL;<br />BEGIN<br />    cc[7] := 'India';<br />    cc[3] := 'UK';<br />    cc[5] := 'USA';<br />    cc[0] := 'China';<br />    cc[-2] := 'Invalid';<br />    RAISE NOTICE 'cc_length: %', ARRAY_LENGTH(cc, 1);<br />    IF (ARRAY_LENGTH(cc, 1) > 0) THEN<br />        FOR i IN ARRAY_LOWER(cc, 1)..ARRAY_UPPER(cc, 1)<br />        LOOP<br />            RAISE NOTICE 'cc_idx:% country:%', i, cc[i];<br />        END LOOP;<br />    END IF;<br />END;<br />$$;</pre> | DBA |
| Run the PL/pgSQL block. | Run the target PL/pgSQL block in PostgreSQL. If there are gaps between the index values of an associative array, no data is stored in those gaps. This allows the PostgreSQL loop to iterate only through the index positions. | DBA |
| Review the output. | The array length is greater than 5 because `NULL` is stored in the gaps between index positions. As shown in the following output, the loop completes 10 iterations to retrieve 5 values in the array.<pre>cc_length:10<br />cc_idx:-2 country:Invalid<br />cc_idx:-1 country:<NULL><br />cc_idx:0 country:China<br />cc_idx:1 country:<NULL><br />cc_idx:2 country:<NULL><br />cc_idx:3 country:UK<br />cc_idx:4 country:<NULL><br />cc_idx:5 country:USA<br />cc_idx:6 country:<NULL><br />cc_idx:7 country:India</pre> | DBA |

### Emulate Oracle associative array behavior
<a name="emulate-oracle-associative-array-behavior"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a target PL/pgSQL block with an array and user-defined type. | To optimize performance and match Oracle's functionality, we can create a user-defined type that stores both index positions and their corresponding data. This approach reduces unnecessary iterations by maintaining direct associations between indices and values.<pre>DO $$<br />DECLARE<br />    cc country_codes[];<br />    cc_append country_codes := NULL;<br />    i record;<br />BEGIN<br />    cc_append.idx = 7;<br />    cc_append.val = 'India';<br />    cc := array_append(cc, cc_append);<br />    cc_append.idx = 3;<br />    cc_append.val = 'UK';<br />    cc := array_append(cc, cc_append);<br />    cc_append.idx = 5;<br />    cc_append.val = 'USA';<br />    cc := array_append(cc, cc_append);<br />    cc_append.idx = 0;<br />    cc_append.val = 'China';<br />    cc := array_append(cc, cc_append);<br />    cc_append.idx = - 2;<br />    cc_append.val = 'Invalid';<br />    cc := array_append(cc, cc_append);<br />    RAISE NOTICE 'cc_length: %', ARRAY_LENGTH(cc, 1);<br />    IF (ARRAY_LENGTH(cc, 1) > 0) THEN<br />        FOR i IN (<br />            SELECT<br />                *<br />            FROM<br />                unnest(cc)<br />            ORDER BY<br />                idx)<br />                LOOP<br />                    RAISE NOTICE 'cc_idx:% country:%', i.idx, i.val;<br />                END LOOP;<br />    END IF;<br />END;<br />$$;</pre> | DBA |
| Run the PL/pgSQL block. | Run the target PL/pgSQL block. If there are gaps between the index values of an associative array, no data is stored in those gaps. This allows the PostgreSQL loop to iterate only through the index positions. | DBA |
| Review the output. | As shown in the following output, the user-defined type stores only populated data elements, which means that the array length matches the number of values. As a result, `LOOP` iterations are optimized to process only existing data, eliminating the need to track empty positions.<pre>cc_length:5<br />cc_idx:-2 country:Invalid<br />cc_idx:0 country:China<br />cc_idx:3 country:UK<br />cc_idx:5 country:USA<br />cc_idx:7 country:India</pre> | DBA |

## Troubleshooting
<a name="emulate-oracle-plsql-associative-arrays-in-aurora-and-rds-postgresql-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| **Index out of bounds error**+ **Issue**: `ERROR: array subscript out of bounds` when accessing array elements<br />+ **Cause**: Attempting to access an index position that doesn't exist in the user-defined type array | You can validate index existence before access by using a `WHERE` clause filter on the `idx` column when unnesting the array, or you can implement boundary checks in your PL/pgSQL code. |
| **NULL value handling**+ **Issue**: Unexpected NULL values appearing in query results when iterating through the array<br />+ **Cause**: Array elements not properly initialized with both `idx` and `val` fields before appending | Make sure that both fields of the user-defined type are populated before using `array_append()`. Add explicit NULL checks as follows: `IF cc_append.val IS NOT NULL THEN cc := array_append(cc, cc_append); END IF;` |

## Related resources
<a name="emulate-oracle-plsql-associative-arrays-in-aurora-and-rds-postgresql-resources"></a>

**AWS documentation**
+ [AWS database blog](https://aws.amazon.com/blogs/database/)
+ [Oracle to Aurora PostgreSQL migration playbook](https://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/chap-oracle-aurora-pg.html)

**Other documentation**
+ [Oracle associative arrays](https://docs.oracle.com/en/database/oracle/oracle-database/23/lnpls/associative-arrays.html#GUID-8060F01F-B53B-48D4-9239-7EA8461C2170)
+ [PostgreSQL array functions and operators](https://www.postgresql.org/docs/current/functions-array.html)
+ [PostgreSQL user-defined types](https://www.postgresql.org/docs/current/sql-createtype.html)

## Additional information
<a name="emulate-oracle-plsql-associative-arrays-in-aurora-and-rds-postgresql-additional"></a>

*Performance considerations*
+ This approach reduces iteration overhead by 50% or more for sparse arrays compared to native PostgreSQL arrays with NULL placeholders.
+ Storage efficiency improves because only actual data is stored, not empty index positions.

*Compatibility notes*
+ This pattern maintains Oracle's sparse array semantics while using PostgreSQL's native array capabilities.
+ The solution is compatible with all PostgreSQL versions that support user-defined composite types.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
