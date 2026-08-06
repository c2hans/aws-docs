---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-oracle-database-error-codes-to-an-amazon-aurora-postgresql-compatible-database.html
---

# Migrate Oracle Database error codes to an Amazon Aurora PostgreSQL-Compatible database
<a name="migrate-oracle-database-error-codes-to-an-amazon-aurora-postgresql-compatible-database"></a>

*Sai Parthasaradhi and Veeranjaneyulu Grandhi, Amazon Web Services*

## Summary
<a name="migrate-oracle-database-error-codes-to-an-amazon-aurora-postgresql-compatible-database-summary"></a>

This pattern shows how to migrate Oracle Database error codes to an [Amazon Aurora PostgreSQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) database by using a predefined metadata table.

Oracle Database error codes don’t always have a corresponding PostgreSQL error code. This difference in error codes can make it difficult to configure the processing logic of the procedures or functions in the target PostgreSQL architecture.

You can simplify the process by storing the source and target database error codes that are meaningful to your PL/pgSQL program in a metadata table. Then, configure the table to flag valid Oracle Database error codes and map them to their PostgreSQL equivalents before continuing with the remaining process logic. If the Oracle Database error code isn’t in the metadata table, the process exits with the exception. Then, you can manually review the error details and add the new error code to the table if your program requires it.

By using this configuration, your Amazon Aurora PostgreSQL-Compatible database can handle errors in the same way that your source Oracle database does.

**Note**
Configuring a PostgreSQL database to handle Oracle Database error codes correctly usually requires changes to the database and application code.

## Prerequisites and limitations
<a name="migrate-oracle-database-error-codes-to-an-amazon-aurora-postgresql-compatible-database-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A source Oracle Database with instance and listener services up and running
+ An Amazon Aurora PostgreSQL-Compatible cluster that’s up and running
+ Familiarity with Oracle Database
+ Familiarity with PostgreSQL databases

## Architecture
<a name="migrate-oracle-database-error-codes-to-an-amazon-aurora-postgresql-compatible-database-architecture"></a>

The following diagram shows an example Amazon Aurora PostgreSQL-Compatible database workflow for data error code validation and handling:

![Data error code validation and handling for an Aurora PostgreSQL-Compatible database.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/82751f40-2fd9-4ce7-ab61-0874552d857b/images/b7ab627e-8f34-4635-8660-93c5c80ce38d.png)

The diagram shows the following workflow:

1. A table holds Oracle Database error codes and classifications and their equivalent PostgreSQL error codes and classifications. The table includes a **valid\_error** column that classifies if specific, predefined error codes are valid or not.

1. When a PL/pgSQL function (**func\_processdata**) throws an exception, it invokes a second PL/pgSQL function (**error\_validation**).

1. The **error\_validation** function accepts the Oracle Database error code as an input argument. Then, the function checks the incoming error code against the table to see if the error is included in the table.

1. If the Oracle Database error code is included in the table, then the **error\_validation** function returns a **TRUE** value and the process logic continues. If the error code isn’t included in the table, then the function returns a **FALSE **value, and the process logic exits with an exception.

1. When the function returns a **FALSE** value, then the error details are manually reviewed by the application’s functional lead to determine its validity.

1. The new error code is then either manually added to the table or not. If the error code is valid and added to the table, then the **error\_validation** function returns a **TRUE** value the next time the exception occurs. If the error code isn’t valid, and the process must fail when the exception occurs, then the error code isn’t added to the table.

**Technology stack**
+ Amazon Aurora PostgreSQL
+ pgAdmin
+ Oracle SQL Developer

## Tools
<a name="migrate-oracle-database-error-codes-to-an-amazon-aurora-postgresql-compatible-database-tools"></a>
+ [Amazon Aurora PostgreSQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) is a fully managed, ACID-compliant relational database engine that helps you set up, operate, and scale PostgreSQL deployments.
+ [pgAdmin](https://www.pgadmin.org/) is an open-source administration and development tool for PostgreSQL. It provides a graphical interface that simplifies the creation, maintenance, and use of database objects.
+ [Oracle SQL Developer](https://www.oracle.com/in/database/technologies/appdev/sqldeveloper-landing.html) is a free, integrated development environment that simplifies the development and management of Oracle Database in both traditional and cloud deployments.

## Epics
<a name="migrate-oracle-database-error-codes-to-an-amazon-aurora-postgresql-compatible-database-epics"></a>

### Migrate Oracle Database error codes to your Amazon Aurora PostgreSQL-Compatible database
<a name="migrate-oracle-database-error-codes-to-your-amazon-aurora-postgresql-compatible-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a table in the Amazon Aurora PostgreSQL-Compatible database. | Run the following PostgreSQL [CREATE TABLE](https://www.postgresql.org/docs/current/sql-createtable.html) command:<pre>(<br /><br />    source_error_code numeric NOT NULL,<br /><br />    target_error_code character varying NOT NULL,<br /><br />    valid_error character varying(1) NOT NULL<br /><br />); </pre> | PostgreSQL Developer, Oracle, RDS/Aurora for PostgreSQL |
| Add PostgreSQL error codes and their corresponding Oracle Database error codes to the table. | Run the PostgreSQL [INSERT](https://www.postgresql.org/docs/current/sql-insert.html) command to add the required error code values to the **error\_codes** table.<br />The PostgreSQL error codes must use the character varying data type (**SQLSTATE **value). The Oracle error codes must use the numeric data type (**SQLCODE** value).<br />**Example Insert statements:**<pre>insert into error_codes values (-1817,'22007','Y');<br />insert into error_codes values (-1816,'22007','Y');<br />insert into error_codes values (-3114,'08006','N');</pre>If you’re catching Oracle-specific Java database connectivity (JDBC) exceptions, you must replace those exceptions with either generic cross-database exceptions or switch to PostgreSQL-specific exceptions. | PostgreSQL Developer, Oracle, RDS/Aurora for PostgreSQL |
| Create a PL/pgSQL function to validate error codes. | Create a PL/pgSQL function by running the PostgreSQL [CREATE FUNCTION](https://www.postgresql.org/docs/current/sql-createfunction.html) command. Make sure that the function does the following:+ Accepts the Oracle error codes thrown by a program.<br />+ Checks if error codes are present in the **error\_codes** table.<br />+ Returns **TRUE** or **FALSE** value, based on if the error code is present in the metadata table or not. | PostgreSQL Developer, Oracle, RDS/Aurora for PostgreSQL |
| Manually review new error codes as they’re recorded by the PL/pgSQL function. | Manually review the new error codes.<br />If a new error code is valid for your use case, add it to the **error\_codes** table by running the PostgreSQL **INSERT** command.<br />-or-<br />If a new error code isn’t valid for your use case, don’t add it to the table. The process logic will continue to fail and exit with exception when the error occurs. | PostgreSQL Developer, Oracle, RDS/Aurora for PostgreSQL |

## Related resources
<a name="migrate-oracle-database-error-codes-to-an-amazon-aurora-postgresql-compatible-database-resources"></a>

[Appendix A. PostgreSQL Error Codes](https://www.postgresql.org/docs/11/errcodes-appendix.html) (PostgreSQL documentation)

[Database error messages](https://docs.oracle.com/cd/E11882_01/server.112/e17766/toc.htm) (Oracle Database documentation)
