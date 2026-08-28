---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ExportSnapshot.postgres-permissions.html
---

# Troubleshooting RDS for PostgreSQL permissions errors
<a name="USER_ExportSnapshot.postgres-permissions"></a>

When exporting PostgreSQL databases to Amazon S3, you might see a `PERMISSIONS_DO_NOT_EXIST` error stating that certain tables were skipped. This error usually occurs when the superuser, which you specified when creating the database, doesn't have permissions to access those tables.

To fix this error, run the following command:

```
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA {{schema_name}} TO {{superuser_name}}
```

For more information on superuser privileges, see [Master user account privileges](UsingWithRDS.MasterAccounts.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
