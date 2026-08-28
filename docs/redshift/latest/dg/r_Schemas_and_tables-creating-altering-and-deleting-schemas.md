---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_Schemas_and_tables-creating-altering-and-deleting-schemas.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Creating, altering, and deleting schemas
<a name="r_Schemas_and_tables-creating-altering-and-deleting-schemas"></a>

Any user can create schemas and alter or drop schemas they own.

You can perform the following actions:
+ To create a schema, use the [CREATE SCHEMA](r_CREATE_SCHEMA.md) command.
+ To change the owner of a schema, use the [ALTER SCHEMA](r_ALTER_SCHEMA.md) command.
+ To delete a schema and its objects, use the [DROP SCHEMA](r_DROP_SCHEMA.md) command.
+ To create a table within a schema, create the table with the format *schema\_name.table\_name*.

To view a list of all schemas, query the PG\_NAMESPACE system catalog table:

```
select * from pg_namespace;
```

To view a list of tables that belong to a schema, query the PG\_TABLE\_DEF system catalog table. For example, the following query returns a list of tables in the PG\_CATALOG schema.

```
select distinct(tablename) from pg_table_def
where schemaname = 'pg_catalog';
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
