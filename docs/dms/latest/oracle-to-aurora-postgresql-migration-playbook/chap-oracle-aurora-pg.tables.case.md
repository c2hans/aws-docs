---
source_url: https://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/chap-oracle-aurora-pg.tables.case.html
---

# Case sensitivity differences for Oracle and PostgreSQL
<a name="chap-oracle-aurora-pg.tables.case"></a>

Object name case sensitivity is different for Oracle and PostgreSQL. Oracle names aren’t case sensitive. PostgreSQL names are case sensitive.

By default, AWS SCT uses object name in lower-case for PostgreSQL. In most cases, you’ll want to use AWS DMS transformations to change schema, table, and column names to lower case.

To have an upper-case name, you must place the objects names within doubles quotes.

For example, to create a table named `EMPLOYEES` (upper-case) in PostgreSQL, you should use the following

```
CREATE TABLE "EMPLOYEES" (
  EMP_ID NUMERIC PRIMARY KEY,
  EMP_FULL_NAME VARCHAR(60) NOT NULL,
  AVG_SALARY NUMERIC NOT NULL);
```

The following command creates a table named employees (lower-case).

```
CREATE TABLE EMPLOYEES (
  EMP_ID NUMERIC PRIMARY KEY,
  EMP_FULL_NAME VARCHAR(60) NOT NULL,
  AVG_SALARY NUMERIC NOT NULL);
```

If you don’t use doubles quotes, PostgreSQL looks for object names in their lower-case form. For `CREATE` commands where you don’t use doubles quotes, PostgreSQL creates objects with lower-case names. Therefore, to create, query, or manipulate an upper-cased (or mixed) object names, use doubles quotes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
