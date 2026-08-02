---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-oracle-serially-reusable-pragma-packages-into-postgresql.html
---

# Migrate Oracle SERIALLY\_REUSABLE Pragma packages into Amazon Aurora or Amazon RDS for PostgreSQL
<a name="migrate-oracle-serially-reusable-pragma-packages-into-postgresql"></a>

*Vinay Paladi, Amazon Web Services*

## Summary
<a name="migrate-oracle-serially-reusable-pragma-packages-into-postgresql-summary"></a>

This pattern provides a step-by-step approach for migrating Oracle packages that use the SERIALLY\_REUSABLE Pragma to Amazon Aurora PostgreSQL-Compatible Edition or Amazon RDS for PostgreSQL on AWS, while maintaining the original functionality.

The PRAGMA SERIALLY\_REUSABLE indicates that the package state is needed only for the duration of one call to the server (for example, a PL/SQL anonymous block or a stored procedure call through a database link). After this call, the storage for the package variables can be reused, reducing memory consumption.

PostgreSQL doesn't natively support the concept of SERIALLY\_REUSABLE Pragma. To achieve equivalent functionality, this pattern uses a wrapper function approach combined with the AWS Database Migration Service (AWS DMS) [Schema Conversion (AWS DMS SC)](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SchemaConversion.html) feature to migrate the package structure. The example script provided demonstrates how to preserve the reset-on-each-call behavior in PostgreSQL.

For more information, see [SERIALLY\_REUSABLE](https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/SERIALLY_REUSABLE-pragma.html) Pragma in the Oracle documentation.

## Prerequisites and limitations
<a name="migrate-oracle-serially-reusable-pragma-packages-into-postgresql-prereqs"></a>
+ An active AWS account
+ Access to the AWS DMS Schema Conversion service
+ An Amazon Aurora PostgreSQL-Compatible Edition database or an Amazon RDS for PostgreSQL database
+ Oracle database version 10g or later

## Architecture
<a name="migrate-oracle-serially-reusable-pragma-packages-into-postgresql-architecture"></a>

**Source technology stack**
+ On-premises Oracle database

**Target technology stack**
+ [Aurora PostgreSQL-Compatible](https://aws.amazon.com/rds/aurora/details/postgresql-details/) or Amazon RDS for PostgreSQL
+ AWS DMS Schema Conversion

**Migration architecture**

![Migrate Oracle SERIALLY_REUSABLE Pragma packages into Amazon Aurora or Amazon RDS for PostgreSQL](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/fe3c45d2-6ea4-43b5-adb1-18f068f126b9/images/955ed078-0941-4ae6-b56e-964379a29365.jpeg)

## Tools
<a name="migrate-oracle-serially-reusable-pragma-packages-into-postgresql-tools"></a>

**AWS services**
+ [AWS Database Migration Service (AWS DMS) Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SchemaConversion.html) makes database migrations between different types of databases more predictable. Use it to assess the complexity of your migration for your source data provider and to convert database schemas and code objects. You can then apply the converted code to your target database.
+ [Amazon Aurora PostgreSQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) is a fully managed, ACID-compliant relational database engine that helps you set up, operate, and scale PostgreSQL deployments.
+ [Amazon Relational Database Service (Amazon RDS) for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html) helps you set up, operate, and scale a PostgreSQL relational database in the AWS Cloud.

**Other tools**
+ [pgAdmin](https://www.pgadmin.org/) is an open-source management tool for PostgreSQL. It provides a graphical interface that helps you create, maintain, and use database objects.

## Best practices
<a name="migrate-oracle-serially-reusable-pragma-packages-into-postgresql-best-practices"></a>
+ Always use `reset_vars = 1` for top-level calls and `reset_vars = 0` for internal sub-calls.
+ Keep all default values in the `$init` function as a single source of truth.
+ Match Oracle variable names in PostgreSQL for traceability.
+ Validate by comparing Oracle `DBMS_OUTPUT` with PostgreSQL `RAISE NOTICE` output.
+ Test in separate PostgreSQL sessions to confirm variables reset between calls.

## Epics
<a name="migrate-oracle-serially-reusable-pragma-packages-into-postgresql-epics"></a>

### Migrate the Oracle package by using AWS DMS SC
<a name="migrate-the-oracle-package-by-using-dms-sc"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up AWS DMS SC. | Configure AWS DMS connectivity to the source database. For more information, see [Converting database schemas using DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/getting-started.html). | DBA, Developer |
| Convert the script. | Use AWS DMS SC to convert the Oracle package by selecting the target database as Aurora PostgreSQL-Compatible. | DBA, Developer |
| Save the .sql files. | Before you save the .sql file, modify the **Project Settings** option in AWS DMS SC to **Single file per stage**. This configures AWS DMS to separate the .sql file into multiple .sql files based on object type. | DBA, Developer |
| Change the code. | Open the `init` function generated by AWS DMS SC, and change it as shown in the example in the *Additional information* section. It will add a variable to achieve the functionality `reset_vars = 0`. | DBA, Developer |
| Test the conversion. | Deploy the `init` function to the Aurora PostgreSQL-Compatible database, and test the results. | DBA, Developer |

## Troubleshooting
<a name="migrate-oracle-serially-reusable-pragma-packages-into-postgresql-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Field does not exist error when accessing package variables. | Ensure that the `$init` function condition uses `IF v_need_init` or `reset_vars = 1` so that variables are always created on first access in a session. |
| Variables not resetting between top-level calls or resetting unexpectedly during internal sub-calls. | Use `reset_vars = 1` for direct top-level calls and pass `reset_vars = 0` for internal function-to-function calls. |

## Related resources
<a name="migrate-oracle-serially-reusable-pragma-packages-into-postgresql-resources"></a>
+ [AWS DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SchemaConversion.html)
+ [Amazon RDS](https://aws.amazon.com/rds/)
+ [Amazon Aurora features](https://aws.amazon.com/rds/aurora/postgresql-features/)
+ [SERIALLY\_REUSABLE Pragma](https://docs.oracle.com/cd/B28359_01/appdev.111/b28370/seriallyreusable_pragma.htm#LNPLS01346)

## Additional information
<a name="migrate-oracle-serially-reusable-pragma-packages-into-postgresql-additional"></a>

```
-------Source Oracle Code:
CREATE OR REPLACE PACKAGE test_pkg_var IS
  PRAGMA SERIALLY_REUSABLE;
  PROCEDURE function_1(test_id NUMBER);
  PROCEDURE function_2(test_id NUMBER);
END;
/
CREATE OR REPLACE PACKAGE BODY test_pkg_var IS
  PRAGMA SERIALLY_REUSABLE;
  v_char VARCHAR2(20) := 'DEFAULT_VALUE';
  v_num NUMBER := 123;
  PROCEDURE function_2(test_id NUMBER) IS
  BEGIN dbms_output.put_line('function_2 => v_char=' || v_char || ', v_num=' || v_num); END;
  PROCEDURE function_1(test_id NUMBER) IS
  BEGIN
    dbms_output.put_line('function_1 => v_char=' || v_char || ', v_num=' || v_num);
    v_char := 'MODIFIED_VALUE';
    dbms_output.put_line('function_1 => v_char after update=' || v_char);
    function_2(0);
  END;
END test_pkg_var;
/
SET SERVEROUTPUT ON
EXEC test_pkg_var.function_1(1);
EXEC test_pkg_var.function_2(1);
------Target PostgreSQL Code:
CREATE SCHEMA IF NOT EXISTS testoracle;
CREATE OR REPLACE FUNCTION testoracle.test_pkg_var$init(reset_vars IN INTEGER DEFAULT 0) RETURNS void AS $BODY$
DECLARE v_need_init BOOLEAN;
BEGIN
  v_need_init := aws_oracle_ext.packageinitialize(proutinename => 'testoracle.test_pkg_var');
  IF v_need_init OR reset_vars = 1 THEN
    PERFORM aws_oracle_ext.setglobalvariable(proutinename => 'testoracle.test_pkg_var', pvariable => 'v_char', pval => 'DEFAULT_VALUE'::CHARACTER VARYING(20));
    PERFORM aws_oracle_ext.setglobalvariable(proutinename => 'testoracle.test_pkg_var', pvariable => 'v_num', pval => 123);
  END IF;
END; $BODY$ LANGUAGE plpgsql;
CREATE OR REPLACE PROCEDURE testoracle.test_pkg_var$function_1(reset_vars INT DEFAULT 1) AS $BODY$
BEGIN
  PERFORM testoracle.test_pkg_var$init(reset_vars);
  RAISE NOTICE 'function_1 => v_char=%, v_num=%', aws_oracle_ext.getglobalvariable(proutinename => 'testoracle.test_pkg_var', pvariable => 'v_char', ptp => NULL::CHARACTER VARYING(20)), aws_oracle_ext.getglobalvariable(proutinename => 'testoracle.test_pkg_var', pvariable => 'v_num', ptp => NULL::DOUBLE PRECISION);
  PERFORM aws_oracle_ext.setglobalvariable(proutinename => 'testoracle.test_pkg_var', pvariable => 'v_char', pval => 'MODIFIED_VALUE'::CHARACTER VARYING(20));
  RAISE NOTICE 'function_1 => v_char after update=%', aws_oracle_ext.getglobalvariable(proutinename => 'testoracle.test_pkg_var', pvariable => 'v_char', ptp => NULL::CHARACTER VARYING(20));
  CALL testoracle.test_pkg_var$function_2(0);
END; $BODY$ LANGUAGE plpgsql;
CREATE OR REPLACE PROCEDURE testoracle.test_pkg_var$function_2(reset_vars INT DEFAULT 1) AS $BODY$
BEGIN PERFORM testoracle.test_pkg_var$init(reset_vars);
  RAISE NOTICE 'function_2 => v_char=%, v_num=%', aws_oracle_ext.getglobalvariable(proutinename => 'testoracle.test_pkg_var', pvariable => 'v_char', ptp => NULL::CHARACTER VARYING(20)), aws_oracle_ext.getglobalvariable(proutinename => 'testoracle.test_pkg_var', pvariable => 'v_num', ptp => NULL::DOUBLE PRECISION);
END; $BODY$ LANGUAGE plpgsql;
CALL testoracle.test_pkg_var$function_1(1); -- loads defaults, sets v_char='MODIFIED_VALUE', function_2 sees 'MODIFIED_VALUE'
CALL testoracle.test_pkg_var$function_2(1); -- new transcation: PRAGMA reset, sees 'DEFAULT_VALUE'
```
