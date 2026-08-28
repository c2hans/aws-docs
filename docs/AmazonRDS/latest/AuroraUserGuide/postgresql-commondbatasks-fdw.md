---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/postgresql-commondbatasks-fdw.html
---

# Using the postgres\_fdw extension to access external data
<a name="postgresql-commondbatasks-fdw"></a>

You can access data in a table on a remote database server with the [postgres\_fdw](https://www.postgresql.org/docs/current/static/postgres-fdw.html) extension. If you set up a remote connection from your PostgreSQL DB instance, access is also available to your read replica.

**To use postgres\_fdw to access a remote database server**

1. Install the postgres\_fdw extension.

   ```
   CREATE EXTENSION postgres_fdw;
   ```

1. Create a foreign data server using CREATE SERVER.

   ```
   CREATE SERVER foreign_server
   FOREIGN DATA WRAPPER postgres_fdw
   OPTIONS (host 'xxx.xx.xxx.xx', port '5432', dbname 'foreign_db');
   ```

1. Create a user mapping to identify the role to be used on the remote server.
**Important**
To redact the password so that it doesn't appear in the logs, set `log_statement=none` at the session level. Setting at the parameter level doesn't redact the password.

   ```
   CREATE USER MAPPING FOR local_user
   SERVER foreign_server
   OPTIONS (user 'foreign_user', password 'password');
   ```

1. Create a table that maps to the table on the remote server.

   ```
   CREATE FOREIGN TABLE foreign_table (
           id integer NOT NULL,
           data text)
   SERVER foreign_server
   OPTIONS (schema_name 'some_schema', table_name 'some_table');
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
