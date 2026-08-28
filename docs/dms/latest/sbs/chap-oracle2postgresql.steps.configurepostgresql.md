---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/chap-oracle2postgresql.steps.configurepostgresql.html
---

# Step 3: Configure Your PostgreSQL Target Database
<a name="chap-oracle2postgresql.steps.configurepostgresql"></a>

1. If the schemas you are migrating do not exist on the PostgreSQL database, then create the schemas.

1. Create the AWS DMS user to connect to your target database, and grant Superuser or the necessary individual privileges (or use the master username for RDS).

   ```
   CREATE USER postgresql_dms_user WITH PASSWORD 'password';
   ALTER USER postgresql_dms_user WITH SUPERUSER;
   ```

1. Create a user for AWS SCT.

   ```
   CREATE USER postgresql_sct_user WITH PASSWORD 'password';

   GRANT CONNECT ON DATABASE database_name TO postgresql_sct_user;
   GRANT USAGE ON SCHEMA schema_name TO postgresql_sct_user;
   GRANT SELECT ON ALL TABLES IN SCHEMA schema_name TO postgresql_sct_user;
   GRANT ALL ON ALL SEQUENCES IN SCHEMA schema_name TO postgresql_sct_user;
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
