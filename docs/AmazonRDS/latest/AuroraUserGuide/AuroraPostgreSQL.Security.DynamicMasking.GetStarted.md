---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Security.DynamicMasking.GetStarted.html
---

# Getting started with dynamic masking
<a name="AuroraPostgreSQL.Security.DynamicMasking.GetStarted"></a>

To dynamically mask data, you install the `pg_columnmask` extension in your database and create masking policies for your tables. The setup process involves prerequisite verification, extension installation, role configuration, policy creation, and validation testing.

## Extension installation and configuration
<a name="AuroraPostgreSQL.Security.DynamicMasking.GetStarted.Installation"></a>

Connect to your Aurora PostgreSQL cluster using the RDS Console Query Editor or a PostgreSQL client such as psql with rds\_superuser (master user) credentials.

Execute the extension creation command to enable `pg_columnmask` functionality:

```
CREATE EXTENSION pg_columnmask;
```

This command installs the `pg_columnmask` extension, creates the necessary catalog tables, and registers the built-in masking functions. The extension installation is database-specific, meaning you must install it separately in each database where the functionality is required.

**Note**
Connections made before installing this extension will still show unmasked data. Close and reconnect to fix this.

Verify the extension installation by checking the available masking functions:

```
SELECT proname FROM pg_proc
    WHERE pronamespace = 'pgcolumnmask'::regnamespace AND proname LIKE 'mask_%';
    proname
--------Output --------
 mask_email
 mask_text
 mask_timestamp
(3 rows)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
