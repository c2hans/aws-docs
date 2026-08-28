---
source_url: https://docs.aws.amazon.com/dms/latest/userguide/data-providers-postgresql.html
---

# Using a PostgreSQL database as a target in DMS Schema Conversion
<a name="data-providers-postgresql"></a>

You can use PostgreSQL databases as a migration target in DMS Schema Conversion.

For information about supported target databases, see [Target data providers for DMS Schema Conversion](CHAP_Introduction.Targets.md#CHAP_Introduction.Targets.SchemaConversion).

## Privileges for PostgreSQL as a target
<a name="data-providers-postgresql-permissions"></a>

To use PostgreSQL as a target, DMS Schema Conversion requires the following minimum privileges. The target database must exist before you connect. For each database you want to use in your migration project, grant the following privileges to the user account used for the migration:

```
GRANT CONNECT ON DATABASE {{<db_name>}} TO {{<user>}};
GRANT CREATE ON DATABASE {{<db_name>}} TO {{<user>}};
```

To use Amazon RDS for PostgreSQL as a target, DMS Schema Conversion requires the `rds_superuser` role.

To use the converted public synonyms, change the database default search path using the following command.

```
ALTER DATABASE {{<db_name>}} SET SEARCH_PATH = "$user", public_synonyms, public;
```

In this example, replace the `{{<db_name>}}` placeholder with the name of your database.

In PostgreSQL, only the schema owner or a `superuser` can drop a schema. The owner can drop a schema and all objects that this schema includes, even if the owner of the schema doesn't own some of its objects.

When you use different users to convert and apply different schemas to your target database, you may encounter an error message when DMS Schema Conversion can't drop a schema. To avoid this error message, use the `superuser` role.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
