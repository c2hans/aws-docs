---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-oracle-functions-and-procedures-that-have-more-than-100-arguments-to-postgresql.html
---

# Migrate Oracle functions and procedures that have more than 100 arguments to PostgreSQL
<a name="migrate-oracle-functions-and-procedures-that-have-more-than-100-arguments-to-postgresql"></a>

*Srinivas Potlachervoo, Amazon Web Services*

## Summary
<a name="migrate-oracle-functions-and-procedures-that-have-more-than-100-arguments-to-postgresql-summary"></a>

This pattern shows how to migrate Oracle Database functions and procedures that have more than 100 arguments to PostgreSQL. For example, you can use this pattern to migrate Oracle functions and procedures to one of the following PostgreSQL-compatible AWS database services:
+ Amazon Relational Database Service (Amazon RDS) for PostgreSQL
+ Amazon Aurora PostgreSQL-Compatible Edition

PostgreSQL doesn’t support functions or procedures that have more than 100 arguments. As a workaround, you can define a new data type that has type fields that match the source function’s arguments. Then, you can create and run a PL/pgSQL function that uses the custom data type as an argument.

## Prerequisites and limitations
<a name="migrate-oracle-functions-and-procedures-that-have-more-than-100-arguments-to-postgresql-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ An [Amazon RDS Oracle database (DB) instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html)
+ An [Amazon RDS for PostgreSQL DB instance](https://aws.amazon.com/getting-started/hands-on/create-connect-postgresql-db/) or an [Aurora PostgreSQL-Compatible DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.AuroraPostgreSQL.html)

**Product versions**
+ Amazon RDS Oracle DB instance versions 10.2 and later
+ Amazon RDS PostgreSQL DB instance versions 9.4 and later, or Aurora PostgreSQL-Compatible DB instance versions 9.4 and later
+ Oracle SQL Developer version 18 and later
+ pgAdmin version 4 and later

## Architecture
<a name="migrate-oracle-functions-and-procedures-that-have-more-than-100-arguments-to-postgresql-architecture"></a>

**Source technology stack  **
+ Amazon RDS Oracle DB instance versions 10.2 and later

**Target technology stack  **
+ Amazon RDS PostgreSQL DB instance versions 9.4 and later, or Aurora PostgreSQL-Compatible DB instance versions 9.4 and later

## Tools
<a name="migrate-oracle-functions-and-procedures-that-have-more-than-100-arguments-to-postgresql-tools"></a>

**AWS services**
+ [Amazon Relational Database Service (Amazon RDS) for PostgreSQL ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html)helps you set up, operate, and scale a PostgreSQL relational database in the AWS Cloud.
+ [Amazon Aurora PostgreSQL-Compatible Edition ](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html)is a fully managed, ACID-compliant relational database engine that helps you set up, operate, and scale PostgreSQL deployments.

**Other services**
+ [Oracle SQL Developer](https://www.oracle.com/database/technologies/appdev/sqldeveloper-landing.html) is an integrated development environment that simplifies the development and management of Oracle databases in both traditional and cloud-based deployments.
+ [pgAdmin](https://www.pgadmin.org/) is an open-source management tool for PostgreSQL. It provides a graphical interface that helps you create, maintain, and use database objects.

## Best practices
<a name="migrate-oracle-functions-and-procedures-that-have-more-than-100-arguments-to-postgresql-best-practices"></a>

Make sure that the data type that you create matches the type fields that are included in the source Oracle function or procedure.

## Epics
<a name="migrate-oracle-functions-and-procedures-that-have-more-than-100-arguments-to-postgresql-epics"></a>

### Run an Oracle function or procedure that has more than 100 arguments
<a name="run-an-oracle-function-or-procedure-that-has-more-than-100-arguments"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create or identify an existing Oracle/PLSQL function or procedure that has more than 100 arguments. | Create an Oracle/PLSQL function or procedure that has more than 100 arguments.<br />-or-<br />Identify an existing Oracle/PLSQL function or procedure that has more than 100 arguments.<br />For more information, see sections [14.7 CREATE FUNCTION Statement](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/lnpls/CREATE-FUNCTION-statement.html#GUID-B71BC5BD-B87C-4054-AAA5-213E856651F2) and [14.11 CREATE PROCEDURE Statement](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/lnpls/CREATE-PROCEDURE-statement.html#GUID-5F84DB47-B5BE-4292-848F-756BF365EC54) in the Oracle Database documentation. | Oracle/PLSQL knowledge |
| Compile the Oracle/PLSQL function or procedure. | Compile the Oracle/PLSQL function or procedure.<br />For more information, see [Compiling a function](https://docs.oracle.com/cd/E37097_01/doc.42/e35128/GUID-6B7B6F82-616D-4915-82BE-D4AE7F59CF37.htm#AEUTL165) in the Oracle Database documentation. | Oracle/PLSQL knowledge |
| Run the Oracle/PLSQL function. | Run the Oracle/PLSQL function or procedure. Then, save the output. | Oracle/PLSQL knowledge |

### Define a new data type that matches the source function's or procedure's arguments
<a name="define-a-new-data-type-that-matches-the-source-functionapos-s-or-procedureapos-s-arguments"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Define a new data type in PostgreSQL. | Define a new data type in PostgreSQL that includes all of the same fields that appear in the source Oracle function’s or procedure’s arguments.<br />For more information, see [CREATE TYPE](https://www.postgresql.org/docs/current/sql-createtype.html) in the PostgreSQL documentation. | PostgreSQL PL/pgSQL knowledge |

### Create a PostgreSQL function that includes the new TYPE argument
<a name="create-a-postgresql-function-that-includes-the-new-type-argument"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a PostgreSQL function that includes the new data type. | Create a PostgreSQL function that includes the new `TYPE` argument.<br />To review an example function, see the **Additional information** section of this pattern. | PostgreSQL PL/pgSQL knowledge |
| Compile the PostgreSQL function. | Compile the function in PostgreSQL. If the new data type fields match the source function’s or procedure’s arguments, then the function successfully compiles. | PostgreSQL PL/pgSQL knowledge |
| Run the PostgreSQL function. | Run the PostgreSQL function. | PostgreSQL PL/pgSQL knowledge |

## Troubleshooting
<a name="migrate-oracle-functions-and-procedures-that-have-more-than-100-arguments-to-postgresql-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| The function returns the following error:<br />**ERROR: syntax error near "<statement>"** | Make sure that all of the function’s statements end with a semicolon (`;`). |
| The function returns the following error:<br />**ERROR: "<variable>" is not a known variable** | Make sure that the variable that’s used in the function body is listed within the function’s `DECLARE` section. |

## Related resources
<a name="migrate-oracle-functions-and-procedures-that-have-more-than-100-arguments-to-postgresql-resources"></a>
+ [Working with Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) (*Amazon Aurora User Guide for Aurora*)
+ [CREATE TYPE](https://www.postgresql.org/docs/11/sql-createtype.html) (PostgreSQL documentation)

## Additional information
<a name="migrate-oracle-functions-and-procedures-that-have-more-than-100-arguments-to-postgresql-additional"></a>

**Example PostgreSQL function that includes a TYPE argument**

```
CREATE OR REPLACE FUNCTION test_proc_new
(
    IN p_rec type_test_proc_args
)
RETURNS void
AS
$BODY$
BEGIN

    /*
    **************
    The body would contain code to process the input values.
    For our testing, we will display couple of values.
    ***************
    */
    RAISE NOTICE USING MESSAGE = CONCAT_WS('', 'p_acct_id: ', p_rec.p_acct_id);
    RAISE NOTICE USING MESSAGE = CONCAT_WS('', 'p_ord_id: ', p_rec.p_ord_id);
    RAISE NOTICE USING MESSAGE = CONCAT_WS('', 'p_ord_date: ', p_rec.p_ord_date);

END;
$BODY$
LANGUAGE plpgsql
COST 100;
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
